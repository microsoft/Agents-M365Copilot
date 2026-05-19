// ─── Express API server ───

import 'dotenv/config';
import express from 'express';
import cors from 'cors';
import { initDatabase, getStats, getInteractions, getSessionInteractions, getSessions, exportAll } from './database';
import { exportInteractions } from './graph-export';
import { startScheduler } from './scheduler';
import { createLogger } from './logger';
import path from 'path';

const log = createLogger('Server');

const app = express();
app.use(cors());
app.use(express.json());

// ─── Serve the frontend build ───
const clientDist = path.resolve(__dirname, '..', 'client', 'dist');
app.use(express.static(clientDist));

// ─── REST API routes ───

// Dashboard statistics
app.get('/api/stats', (_req, res) => {
    try {
        const stats = getStats();
        res.json(stats);
    } catch (err) {
        log.error(`GET /api/stats failed: ${(err as Error).message}`);
        res.status(500).json({ error: 'Failed to fetch stats' });
    }
});

// Paginated interactions list
app.get('/api/interactions', (req, res) => {
    try {
        const result = getInteractions({
            page: Number(req.query.page) || 1,
            pageSize: Number(req.query.pageSize) || 25,
            appClass: req.query.appClass as string | undefined,
            interactionType: req.query.interactionType as string | undefined,
            search: req.query.search as string | undefined,
            startDate: req.query.startDate as string | undefined,
            endDate: req.query.endDate as string | undefined,
            sessionId: req.query.sessionId as string | undefined,
        });
        res.json(result);
    } catch (err) {
        log.error(`GET /api/interactions failed: ${(err as Error).message}`);
        res.status(500).json({ error: 'Failed to fetch interactions' });
    }
});

// Session list
app.get('/api/sessions', (req, res) => {
    try {
        const result = getSessions({
            page: Number(req.query.page) || 1,
            pageSize: Number(req.query.pageSize) || 25,
            startDate: req.query.startDate as string | undefined,
            endDate: req.query.endDate as string | undefined,
        });
        res.json(result);
    } catch (err) {
        log.error(`GET /api/sessions failed: ${(err as Error).message}`);
        res.status(500).json({ error: 'Failed to fetch sessions' });
    }
});

// Single session's interactions (timeline view)
app.get('/api/sessions/:sessionId', (req, res) => {
    try {
        const interactions = getSessionInteractions(req.params.sessionId);
        res.json(interactions);
    } catch (err) {
        log.error(`GET /api/sessions/:id failed: ${(err as Error).message}`);
        res.status(500).json({ error: 'Failed to fetch session' });
    }
});

// Trigger a manual export from Graph
app.post('/api/export', async (req, res) => {
    const userId = req.body.userId || process.env.USER_ID;
    if (!userId) {
        res.status(400).json({ error: 'userId is required (body or USER_ID env)' });
        return;
    }
    try {
        const count = await exportInteractions({
            userId,
            appClass: req.body.appClass,
        });
        res.json({ success: true, count });
    } catch (err) {
        log.error(`POST /api/export failed: ${(err as Error).message}`);
        res.status(500).json({ error: (err as Error).message });
    }
});

// Download interactions as JSON for compliance archival
app.get('/api/export/download', (req, res) => {
    try {
        const data = exportAll({
            appClass: req.query.appClass as string | undefined,
            startDate: req.query.startDate as string | undefined,
            endDate: req.query.endDate as string | undefined,
        });

        const format = req.query.format ?? 'json';

        if (format === 'csv') {
            res.setHeader('Content-Type', 'text/csv');
            res.setHeader('Content-Disposition', 'attachment; filename=copilot-interactions-export.csv');
            const headers = [
                'id', 'session_id', 'request_id', 'app_class', 'interaction_type',
                'conversation_type', 'created_at', 'locale', 'body_content',
                'from_user_id', 'from_user_name', 'from_app_id', 'from_app_name', 'exported_at',
            ];
            res.write(headers.join(',') + '\n');
            for (const row of data) {
                const values = headers.map((h) => {
                    const val = (row as unknown as Record<string, unknown>)[h];
                    const str = String(val ?? '');
                    return `"${str.replace(/"/g, '""')}"`;
                });
                res.write(values.join(',') + '\n');
            }
            res.end();
        } else {
            res.setHeader('Content-Type', 'application/json');
            res.setHeader('Content-Disposition', 'attachment; filename=copilot-interactions-export.json');
            res.json(data);
        }
    } catch (err) {
        log.error(`GET /api/export/download failed: ${(err as Error).message}`);
        res.status(500).json({ error: 'Export failed' });
    }
});

// SPA fallback
app.get('*', (_req, res) => {
    res.sendFile(path.join(clientDist, 'index.html'));
});

// ─── Bootstrap ───

const PORT = Number(process.env.PORT) || 3000;

initDatabase();
startScheduler();

app.listen(PORT, () => {
    log.info(`🚀 Server running on http://localhost:${PORT}`);
    log.info(`📊 Dashboard: http://localhost:${PORT}`);
    log.info(`📡 API base:  http://localhost:${PORT}/api`);
});
