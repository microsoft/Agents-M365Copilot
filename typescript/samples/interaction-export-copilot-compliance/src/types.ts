// ─── Types for Microsoft Graph aiInteraction resource ───

export interface AiInteraction {
    id: string;
    sessionId: string;
    requestId: string;
    appClass: string;
    interactionType: 'userPrompt' | 'aiResponse' | 'unknownFutureValue';
    conversationType: string;
    etag: string;
    createdDateTime: string;
    locale: string;
    contexts: AiInteractionContext[];
    from: IdentitySet;
    body: ItemBody;
    attachments: AiInteractionAttachment[];
    links: AiInteractionLink[];
    mentions: AiInteractionMention[];
}

export interface AiInteractionContext {
    contextReference: string;
    displayName: string;
    contextType: string;
}

export interface IdentitySet {
    application?: {
        id: string;
        displayName: string;
        applicationIdentityType: string;
    } | null;
    device?: unknown | null;
    user?: {
        id: string;
        displayName: string;
        userIdentityType: string;
        tenantId?: string;
    } | null;
}

export interface ItemBody {
    contentType: string;
    content: string;
}

export interface AiInteractionAttachment {
    attachmentId: string;
    contentType: string;
    contentUrl: string;
    content: string | null;
    name: string;
}

export interface AiInteractionLink {
    linkUrl: string;
    displayName: string;
    linkType: string;
}

export interface AiInteractionMention {
    mentionId: number;
    mentionText: string;
    mentioned: IdentitySet;
}

export interface GraphPagedResponse<T> {
    '@odata.context'?: string;
    '@odata.count'?: number;
    '@odata.nextLink'?: string;
    value: T[];
}

// ─── Database row shapes ───

export interface InteractionRow {
    id: string;
    session_id: string | null;
    request_id: string | null;
    target_user_id: string;
    app_class: string;
    interaction_type: string;
    conversation_type: string;
    created_at: string;
    locale: string;
    body_content_type: string;
    body_content: string;
    from_user_id: string | null;
    from_user_name: string | null;
    from_app_id: string | null;
    from_app_name: string | null;
    contexts_json: string;
    attachments_json: string;
    links_json: string;
    mentions_json: string;
    exported_at: string;
}

// ─── API response shapes ───

export interface DashboardStats {
    totalInteractions: number;
    totalUserPrompts: number;
    totalAiResponses: number;
    totalSessions: number;
    appBreakdown: { appClass: string; count: number }[];
    recentExportAt: string | null;
}

export interface InteractionListParams {
    page?: number;
    pageSize?: number;
    targetUserId?: string;
    appClass?: string;
    interactionType?: string;
    search?: string;
    startDate?: string;
    endDate?: string;
    sessionId?: string;
}

export interface PaginatedResult<T> {
    data: T[];
    total: number;
    page: number;
    pageSize: number;
    totalPages: number;
}

export interface TargetUserSummary {
    userId: string;
    displayName: string;
    interactionCount: number;
    lastExportAt: string;
}

export const APP_CLASS_LABELS: Record<string, string> = {
    'IPM.SkypeTeams.Message.Copilot.Word': 'Word',
    'IPM.SkypeTeams.Message.Copilot.Excel': 'Excel',
    'IPM.SkypeTeams.Message.Copilot.Teams': 'Teams',
    'IPM.SkypeTeams.Message.Copilot.BizChat': 'Business Chat',
    'IPM.SkypeTeams.Message.Copilot.WebChat': 'Web Chat',
    'IPM.SkypeTeams.Message.Copilot.Outlook': 'Outlook',
    'IPM.SkypeTeams.Message.Copilot.SharePoint': 'SharePoint',
    'IPM.SkypeTeams.Message.Copilot.Forms': 'Forms',
    'IPM.SkypeTeams.Message.Copilot.M365AdminCenter': 'M365 Admin Center',
    'IPM.SkypeTeams.Message.Copilot.OfficeCopilotSearchAnswer': 'Office Search',
    'IPM.SkypeTeams.Message.Copilot.ThirdPartyCopilot': 'Third-Party Agent',
    'IPM.SkypeTeams.Message.Copilot.PowerPoint': 'PowerPoint',
    'IPM.SkypeTeams.Message.Copilot.OneNote': 'OneNote',
    'IPM.SkypeTeams.Message.Copilot.Loop': 'Loop',
    'IPM.SkypeTeams.Message.Copilot.Whiteboard': 'Whiteboard',
};
