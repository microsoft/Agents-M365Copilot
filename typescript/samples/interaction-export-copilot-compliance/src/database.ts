// ─── SQLite persistence layer ───

import Database from 'better-sqlite3';
import path from 'path';
import { createLogger } from './logger';
import type { InteractionRow, DashboardStats, InteractionListParams, PaginatedResult, TargetUserSummary } from './types';

const log = createLogger('Database');

const DB_PATH = path.resolve(process.env.DB_PATH ?? 'interactions.db');

let db: Database.Database;

export function initDatabase(): void {
    db = new Database(DB_PATH);
    db.pragma('journal_mode = WAL');

    db.exec(`
    CREATE TABLE IF NOT EXISTS interactions (
      id                TEXT PRIMARY KEY,
      session_id        TEXT,
      request_id        TEXT,
    target_user_id    TEXT,
      app_class         TEXT NOT NULL,
      interaction_type  TEXT NOT NULL,
      conversation_type TEXT,
      created_at        TEXT NOT NULL,
      locale            TEXT,
      body_content_type TEXT,
      body_content      TEXT,
      from_user_id      TEXT,
      from_user_name    TEXT,
      from_app_id       TEXT,
      from_app_name     TEXT,
      contexts_json     TEXT,
      attachments_json  TEXT,
      links_json        TEXT,
      mentions_json     TEXT,
      exported_at       TEXT NOT NULL DEFAULT (datetime('now'))
    );

    CREATE INDEX IF NOT EXISTS idx_interactions_session    ON interactions(session_id);
    CREATE INDEX IF NOT EXISTS idx_interactions_request    ON interactions(request_id);
    CREATE INDEX IF NOT EXISTS idx_interactions_app_class  ON interactions(app_class);
    CREATE INDEX IF NOT EXISTS idx_interactions_type       ON interactions(interaction_type);
    CREATE INDEX IF NOT EXISTS idx_interactions_created_at ON interactions(created_at);
  `);

    // Backward-compatible migration for databases created before target_user_id existed.
    const columns = db.prepare('PRAGMA table_info(interactions)').all() as { name: string }[];
    const hasTargetUserId = columns.some((c) => c.name === 'target_user_id');
    if (!hasTargetUserId) {
        db.exec('ALTER TABLE interactions ADD COLUMN target_user_id TEXT');
    }
    db.exec('CREATE INDEX IF NOT EXISTS idx_interactions_target_user ON interactions(target_user_id)');

    log.info(`Database initialised at ${DB_PATH}`);
}

// ─── Upsert interactions ───

const upsertStmt = () => db.prepare(`
  INSERT INTO interactions (
        id, session_id, request_id, target_user_id, app_class, interaction_type, conversation_type,
    created_at, locale, body_content_type, body_content,
    from_user_id, from_user_name, from_app_id, from_app_name,
    contexts_json, attachments_json, links_json, mentions_json, exported_at
  ) VALUES (
    @id, @session_id, @request_id, @target_user_id, @app_class, @interaction_type, @conversation_type,
    @created_at, @locale, @body_content_type, @body_content,
    @from_user_id, @from_user_name, @from_app_id, @from_app_name,
    @contexts_json, @attachments_json, @links_json, @mentions_json, datetime('now')
  ) ON CONFLICT(id) DO UPDATE SET
    body_content      = excluded.body_content,
        target_user_id    = excluded.target_user_id,
    exported_at       = datetime('now')
`);

export function upsertInteractions(rows: InteractionRow[]): number {
    const stmt = upsertStmt();
    const tx = db.transaction((items: InteractionRow[]) => {
        let count = 0;
        for (const item of items) {
            stmt.run(item);
            count++;
        }
        return count;
    });
    const inserted = tx(rows);
    log.info(`Upserted ${inserted} interactions`);
    return inserted;
}

// ─── Query helpers ───

export function getStats(targetUserId?: string): DashboardStats {
    const where = targetUserId ? 'WHERE target_user_id = @targetUserId' : '';
    const bindings = targetUserId ? { targetUserId } : {};

    const total = db.prepare(`SELECT COUNT(*) as c FROM interactions ${where}`).get(bindings) as { c: number };
    const prompts = db.prepare(`SELECT COUNT(*) as c FROM interactions ${where ? `${where} AND` : 'WHERE'} interaction_type = 'userPrompt'`).get(bindings) as { c: number };
    const responses = db.prepare(`SELECT COUNT(*) as c FROM interactions ${where ? `${where} AND` : 'WHERE'} interaction_type = 'aiResponse'`).get(bindings) as { c: number };
    const sessions = db.prepare(`SELECT COUNT(DISTINCT session_id) as c FROM interactions ${where}`).get(bindings) as { c: number };
    const appBreakdown = db.prepare(`SELECT app_class as appClass, COUNT(*) as count FROM interactions ${where} GROUP BY app_class ORDER BY count DESC`).all(bindings) as { appClass: string; count: number }[];
    const recentExport = db.prepare(`SELECT MAX(exported_at) as m FROM interactions ${where}`).get(bindings) as { m: string | null };

    return {
        totalInteractions: total.c,
        totalUserPrompts: prompts.c,
        totalAiResponses: responses.c,
        totalSessions: sessions.c,
        appBreakdown,
        recentExportAt: recentExport.m,
    };
}

export function getInteractions(params: InteractionListParams): PaginatedResult<InteractionRow> {
    const page = params.page ?? 1;
    const pageSize = Math.min(params.pageSize ?? 25, 100);
    const offset = (page - 1) * pageSize;

    const conditions: string[] = [];
    const bindings: Record<string, string> = {};

    if (params.targetUserId) {
        conditions.push('target_user_id = @targetUserId');
        bindings.targetUserId = params.targetUserId;
    }

    if (params.appClass) {
        conditions.push('app_class = @appClass');
        bindings.appClass = params.appClass;
    }
    if (params.interactionType) {
        conditions.push('interaction_type = @interactionType');
        bindings.interactionType = params.interactionType;
    }
    if (params.sessionId) {
        conditions.push('session_id = @sessionId');
        bindings.sessionId = params.sessionId;
    }
    if (params.startDate) {
        conditions.push('created_at >= @startDate');
        bindings.startDate = params.startDate;
    }
    if (params.endDate) {
        conditions.push('created_at <= @endDate');
        bindings.endDate = params.endDate;
    }
    if (params.search) {
        conditions.push('body_content LIKE @search');
        bindings.search = `%${params.search}%`;
    }

    const where = conditions.length ? `WHERE ${conditions.join(' AND ')}` : '';

    const countRow = db.prepare(`SELECT COUNT(*) as c FROM interactions ${where}`).get(bindings) as { c: number };
    const rows = db.prepare(`SELECT * FROM interactions ${where} ORDER BY created_at DESC LIMIT @limit OFFSET @offset`).all({
        ...bindings,
        limit: pageSize,
        offset,
    }) as InteractionRow[];

    return {
        data: rows,
        total: countRow.c,
        page,
        pageSize,
        totalPages: Math.ceil(countRow.c / pageSize),
    };
}

export function getSessionInteractions(sessionId: string, targetUserId?: string): InteractionRow[] {
    const where = targetUserId
        ? 'WHERE session_id = @sessionId AND target_user_id = @targetUserId'
        : 'WHERE session_id = @sessionId';
    return db.prepare(`SELECT * FROM interactions ${where} ORDER BY created_at ASC`).all(
        targetUserId ? { sessionId, targetUserId } : { sessionId },
    ) as InteractionRow[];
}

export function getSessions(params: { page?: number; pageSize?: number; startDate?: string; endDate?: string; targetUserId?: string }): PaginatedResult<{
    sessionId: string;
    interactionCount: number;
    firstAt: string;
    lastAt: string;
    apps: string;
}> {
    const page = params.page ?? 1;
    const pageSize = Math.min(params.pageSize ?? 25, 100);
    const offset = (page - 1) * pageSize;

    const conditions: string[] = [];
    const bindings: Record<string, string> = {};

    if (params.targetUserId) {
        conditions.push('target_user_id = @targetUserId');
        bindings.targetUserId = params.targetUserId;
    }
    if (params.startDate) {
        conditions.push('created_at >= @startDate');
        bindings.startDate = params.startDate;
    }
    if (params.endDate) {
        conditions.push('created_at <= @endDate');
        bindings.endDate = params.endDate;
    }

    const where = conditions.length ? `WHERE ${conditions.join(' AND ')}` : '';

    const countRow = db.prepare(`SELECT COUNT(DISTINCT session_id) as c FROM interactions ${where}`).get(bindings) as { c: number };

    const rows = db.prepare(`
    SELECT
      session_id as sessionId,
      COUNT(*) as interactionCount,
      MIN(created_at) as firstAt,
      MAX(created_at) as lastAt,
      GROUP_CONCAT(DISTINCT app_class) as apps
    FROM interactions ${where}
    GROUP BY session_id
    ORDER BY MAX(created_at) DESC
    LIMIT @limit OFFSET @offset
  `).all({ ...bindings, limit: pageSize, offset }) as {
        sessionId: string;
        interactionCount: number;
        firstAt: string;
        lastAt: string;
        apps: string;
    }[];

    return {
        data: rows,
        total: countRow.c,
        page,
        pageSize,
        totalPages: Math.ceil(countRow.c / pageSize),
    };
}

export function exportAll(params: { targetUserId?: string; appClass?: string; startDate?: string; endDate?: string }): InteractionRow[] {
    const conditions: string[] = [];
    const bindings: Record<string, string> = {};

    if (params.targetUserId) {
        conditions.push('target_user_id = @targetUserId');
        bindings.targetUserId = params.targetUserId;
    }

    if (params.appClass) {
        conditions.push('app_class = @appClass');
        bindings.appClass = params.appClass;
    }
    if (params.startDate) {
        conditions.push('created_at >= @startDate');
        bindings.startDate = params.startDate;
    }
    if (params.endDate) {
        conditions.push('created_at <= @endDate');
        bindings.endDate = params.endDate;
    }

    const where = conditions.length ? `WHERE ${conditions.join(' AND ')}` : '';
    return db.prepare(`SELECT * FROM interactions ${where} ORDER BY created_at ASC`).all(bindings) as InteractionRow[];
}

export function listTargetUsers(search?: string): TargetUserSummary[] {
    const term = (search ?? '').trim();
    const where = term
        ? `WHERE target_user_id IS NOT NULL AND (
                         target_user_id LIKE @like OR
                         target_user_id IN (
                             SELECT DISTINCT target_user_id
                             FROM interactions
                             WHERE from_user_name LIKE @like
                         )
                     )`
        : 'WHERE target_user_id IS NOT NULL';

    return db.prepare(`
            SELECT
                target_user_id as userId,
                COALESCE(
                    MAX(CASE WHEN from_user_id = target_user_id THEN from_user_name END),
                    'Unknown user'
                ) as displayName,
                COUNT(*) as interactionCount,
                MAX(exported_at) as lastExportAt
            FROM interactions
            ${where}
            GROUP BY target_user_id
            ORDER BY lastExportAt DESC
            LIMIT 50
        `).all(term ? { like: `%${term}%` } : {}) as TargetUserSummary[];
}

/**
 * Check if a target user's data is fresh enough (exported within the last hour).
 * Returns { exists, stale, lastExportAt, interactionCount }.
 */
export function checkUserFreshness(targetUserId: string): {
    exists: boolean;
    stale: boolean;
    lastExportAt: string | null;
    interactionCount: number;
} {
    const row = db.prepare(`
        SELECT COUNT(*) as c, MAX(exported_at) as lastExport
        FROM interactions
        WHERE target_user_id = @targetUserId
    `).get({ targetUserId }) as { c: number; lastExport: string | null };

    const exists = row.c > 0;
    let stale = !exists;

    if (row.lastExport) {
        const lastMs = new Date(row.lastExport).getTime();
        const ageMs = Date.now() - lastMs;
        stale = ageMs > 60 * 60 * 1000; // older than 1 hour
    }

    return {
        exists,
        stale,
        lastExportAt: row.lastExport,
        interactionCount: row.c,
    };
}
