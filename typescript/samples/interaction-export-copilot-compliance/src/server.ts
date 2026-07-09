// ─── Express API server ───

import 'dotenv/config';
import express from 'express';
import cors from 'cors';
import { initDatabase, getStats, getInteractions, getSessionInteractions, getSessions, exportAll, listTargetUsers, checkUserFreshness } from './database';
import { exportInteractions, fetchLiveStats } from './graph-export';
import { getAccessToken } from './auth';
import { requireAuth, requireRole, ROLES, type AuthenticatedRequest } from './auth-middleware';
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

// ─── Auth config endpoint (public — frontend needs this before login) ───
app.get('/api/auth/config', (_req, res) => {
    res.json({
        clientId: process.env.CLIENT_ID,
        tenantId: process.env.TENANT_ID,
        redirectUri: process.env.REDIRECT_URI || `http://localhost:${process.env.PORT || 3000}`,
    });
});

// ─── Auth info endpoint (returns current user details after login) ───
app.get('/api/auth/me', requireAuth, (req: AuthenticatedRequest, res) => {
    res.json({
        oid: req.user?.oid,
        name: req.user?.name,
        email: req.user?.email,
        roles: req.user?.roles,
    });
});

// ─── Protected API routes ───
// All /api/* routes below require authentication.
// Read-only routes require ComplianceAdmin OR ComplianceViewer.
// Write routes (export) require ComplianceAdmin only.

const readAccess = [requireAuth, requireRole(ROLES.ADMIN, ROLES.VIEWER)];
const writeAccess = [requireAuth, requireRole(ROLES.ADMIN)];

// Dashboard statistics
app.get('/api/stats', ...readAccess, (_req: AuthenticatedRequest, res) => {
    try {
        const targetUserId = _req.query.targetUserId as string | undefined;
        const stats = getStats(targetUserId);
        res.json(stats);
    } catch (err) {
        log.error(`GET /api/stats failed: ${(err as Error).message}`);
        res.status(500).json({ error: 'Failed to fetch stats' });
    }
});

// Auto-sync: check freshness and export if needed, then return stats
app.post('/api/sync', ...readAccess, async (req: AuthenticatedRequest, res) => {
    const userId = (req.body.userId as string) || req.user?.oid;
    if (!userId) {
        res.status(400).json({ error: 'userId is required' });
        return;
    }
    try {
        const freshness = checkUserFreshness(userId);
        let exported = 0;

        if (!freshness.exists || freshness.stale) {
            log.info(`[Sync] Data for ${userId} is ${freshness.exists ? 'stale' : 'missing'} — auto-exporting…`);
            exported = await exportInteractions({ userId });
            log.info(`[Sync] Auto-export complete — ${exported} interactions`);
        } else {
            log.info(`[Sync] Data for ${userId} is fresh (last export: ${freshness.lastExportAt})`);
        }

        const stats = getStats(userId);
        res.json({
            synced: !freshness.exists || freshness.stale,
            exported,
            freshness,
            stats,
        });
    } catch (err) {
        log.error(`POST /api/sync failed: ${(err as Error).message}`);
        res.status(500).json({ error: (err as Error).message });
    }
});

// Paginated interactions list
app.get('/api/interactions', ...readAccess, (req: AuthenticatedRequest, res) => {
    try {
        const result = getInteractions({
            page: Number(req.query.page) || 1,
            pageSize: Number(req.query.pageSize) || 25,
            targetUserId: req.query.targetUserId as string | undefined,
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
app.get('/api/sessions', ...readAccess, (req: AuthenticatedRequest, res) => {
    try {
        const result = getSessions({
            page: Number(req.query.page) || 1,
            pageSize: Number(req.query.pageSize) || 25,
            targetUserId: req.query.targetUserId as string | undefined,
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
app.get('/api/sessions/:sessionId', ...readAccess, (req: AuthenticatedRequest, res) => {
    try {
        const targetUserId = req.query.targetUserId as string | undefined;
        const interactions = getSessionInteractions(req.params.sessionId as string, targetUserId);
        res.json(interactions);
    } catch (err) {
        log.error(`GET /api/sessions/:id failed: ${(err as Error).message}`);
        res.status(500).json({ error: 'Failed to fetch session' });
    }
});

// Trigger a manual export from Graph (Admin only)
app.post('/api/export', ...writeAccess, async (req: AuthenticatedRequest, res) => {
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

// Download interactions as CSV (no auth required — serves local DB data only)
app.get('/api/export/download', (req, res) => {
    try {
        const data = exportAll({
            targetUserId: req.query.targetUserId as string | undefined,
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

// Searchable list of target users present in the archive
app.get('/api/users', ...readAccess, (req: AuthenticatedRequest, res) => {
    try {
        const users = listTargetUsers(req.query.search as string | undefined);
        res.json(users);
    } catch (err) {
        log.error(`GET /api/users failed: ${(err as Error).message}`);
        res.status(500).json({ error: 'Failed to fetch users' });
    }
});

// Live stats from Graph API (count-only, no local storage)
app.get('/api/graph/stats', ...readAccess, async (req: AuthenticatedRequest, res) => {
    const userId = (req.query.userId as string) || req.user?.oid;
    if (!userId) {
        res.status(400).json({ error: 'userId is required' });
        return;
    }
    try {
        const stats = await fetchLiveStats(userId);
        res.json(stats);
    } catch (err) {
        log.error(`GET /api/graph/stats failed: ${(err as Error).message}`);
        res.status(500).json({ error: (err as Error).message });
    }
});

// Search Microsoft Graph for users by display name (for admin to find user IDs)
app.get('/api/graph/users', ...readAccess, async (req: AuthenticatedRequest, res) => {
    const search = (req.query.search as string ?? '').trim();
    if (!search || search.length < 2) {
        res.json([]);
        return;
    }
    try {
        const token = await getAccessToken();
        const safeSearch = search.replace(/'/g, "''");
        const graphUrl = `https://graph.microsoft.com/v1.0/users?$filter=startsWith(displayName,'${safeSearch}')&$select=id,displayName,mail,userPrincipalName&$top=20&$count=true`;
        log.info(`Graph user search: ${graphUrl}`);
        const graphRes = await fetch(
            graphUrl,
            {
                headers: {
                    Authorization: `Bearer ${token}`,
                    'Content-Type': 'application/json',
                    ConsistencyLevel: 'eventual',
                },
            },
        );
        if (!graphRes.ok) {
            const body = await graphRes.text();
            log.error(`Graph user search error ${graphRes.status}: ${body}`);
            res.status(graphRes.status).json({ error: 'Graph user search failed' });
            return;
        }
        const json = await graphRes.json() as { value: { id: string; displayName: string; mail: string; userPrincipalName: string }[] };
        res.json(json.value.map((u) => ({
            userId: u.id,
            displayName: u.displayName,
            email: u.mail || u.userPrincipalName,
        })));
    } catch (err) {
        log.error(`GET /api/graph/users failed: ${(err as Error).message}`);
        res.status(500).json({ error: 'Graph user search failed' });
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
