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
            const rows = json.value.map(mapToRow);
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

// ─── Map Graph resource to database row ───

function mapToRow(i: AiInteraction): InteractionRow {
    return {
        id: i.id,
        session_id: i.sessionId ?? null,
        request_id: i.requestId ?? null,
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
