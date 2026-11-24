// ─── Microsoft Graph Export Service ───
// Calls GET /copilot/users/{id}/interactionHistory/getAllEnterpriseInteractions
// with full pagination and optional appClass / date filtering.

import { getAccessToken } from './auth';
import { upsertInteractions } from './database';
import { createLogger } from './logger';
import type { AiInteraction, GraphPagedResponse, InteractionRow } from './types';

const log = createLogger('GraphExport');

const GRAPH_BASE = 'https://graph.microsoft.com/v1.0';

interface ExportOptions {
    userId: string;
    appClass?: string;
    startDate?: string;
    endDate?: string;
    top?: number;
}

export async function exportInteractions(opts: ExportOptions): Promise<number> {
    const { userId, appClass, top = 100 } = opts;

    let url = `${GRAPH_BASE}/copilot/users/${encodeURIComponent(userId)}/interactionHistory/getAllEnterpriseInteractions?$top=${top}`;

    // Build $filter
    const filters: string[] = [];
    if (appClass) {
        filters.push(`appClass eq '${appClass}'`);
    }
    if (filters.length) {
        url += `&$filter=${encodeURIComponent(filters.join(' and '))}`;
    }

    const token = await getAccessToken();
    let totalExported = 0;
    let pageNum = 0;

    while (url) {
        pageNum++;
        log.info(`Fetching page ${pageNum} …`);

        const res = await fetch(url, {
            headers: { Authorization: `Bearer ${token}`, 'Content-Type': 'application/json' },
        });

        if (!res.ok) {
            const body = await res.text();
            log.error(`Graph API error ${res.status}: ${body}`);
            throw new Error(`Graph API returned ${res.status}`);
        }

        const json = (await res.json()) as GraphPagedResponse<AiInteraction>;

        if (json.value.length) {
            const rows = json.value.map((interaction) => mapToRow(interaction, userId));
            const count = upsertInteractions(rows);
            totalExported += count;
            log.info(`Page ${pageNum}: stored ${count} interactions`);
        } else {
            log.info(`Page ${pageNum}: no interactions`);
        }

        url = json['@odata.nextLink'] ?? '';
    }

    log.info(`Export complete — ${totalExported} interactions stored`);
    return totalExported;
}

// ─── Live stats from Graph (count-only, no storage) ───

export interface LiveStats {
    totalInteractions: number;
    totalUserPrompts: number;
    totalAiResponses: number;
    totalSessions: number;
    appBreakdown: { appClass: string; count: number }[];
    source: 'graph';
}

export async function fetchLiveStats(userId: string): Promise<LiveStats> {
    let url: string = `${GRAPH_BASE}/copilot/users/${encodeURIComponent(userId)}/interactionHistory/getAllEnterpriseInteractions?$top=100`;
    const token = await getAccessToken();

    let totalInteractions = 0;
    let totalUserPrompts = 0;
    let totalAiResponses = 0;
    const sessionIds = new Set<string>();
    const appCounts = new Map<string, number>();
    let pageNum = 0;

    while (url) {
        pageNum++;
        log.info(`[LiveStats] Fetching page ${pageNum} …`);

        const res = await fetch(url, {
            headers: { Authorization: `Bearer ${token}`, 'Content-Type': 'application/json' },
        });

        if (!res.ok) {
            const body = await res.text();
            log.error(`[LiveStats] Graph API error ${res.status}: ${body}`);
            throw new Error(`Graph API returned ${res.status}`);
        }

        const json = (await res.json()) as GraphPagedResponse<AiInteraction>;

        for (const interaction of json.value) {
            totalInteractions++;
            if (interaction.interactionType === 'userPrompt') totalUserPrompts++;
            if (interaction.interactionType === 'aiResponse') totalAiResponses++;
            if (interaction.sessionId) sessionIds.add(interaction.sessionId);
            appCounts.set(interaction.appClass, (appCounts.get(interaction.appClass) ?? 0) + 1);
        }

        url = json['@odata.nextLink'] ?? '';
    }

    const appBreakdown = [...appCounts.entries()]
        .map(([appClass, count]) => ({ appClass, count }))
        .sort((a, b) => b.count - a.count);

    log.info(`[LiveStats] Done — ${totalInteractions} interactions, ${sessionIds.size} sessions`);

    return {
        totalInteractions,
        totalUserPrompts,
        totalAiResponses,
        totalSessions: sessionIds.size,
        appBreakdown,
        source: 'graph',
    };
}

// ─── Map Graph resource to database row ───

function mapToRow(i: AiInteraction, targetUserId: string): InteractionRow {
    return {
        id: i.id,
        session_id: i.sessionId ?? null,
        request_id: i.requestId ?? null,
        target_user_id: targetUserId,
        app_class: i.appClass,
        interaction_type: i.interactionType,
        conversation_type: i.conversationType ?? '',
        created_at: i.createdDateTime,
        locale: i.locale ?? '',
        body_content_type: i.body?.contentType ?? '',
        body_content: i.body?.content ?? '',
        from_user_id: i.from?.user?.id ?? null,
        from_user_name: i.from?.user?.displayName ?? null,
        from_app_id: i.from?.application?.id ?? null,
        from_app_name: i.from?.application?.displayName ?? null,
        contexts_json: JSON.stringify(i.contexts ?? []),
        attachments_json: JSON.stringify(i.attachments ?? []),
        links_json: JSON.stringify(i.links ?? []),
        mentions_json: JSON.stringify(i.mentions ?? []),
        exported_at: new Date().toISOString(),
    };
}
