// ─── Shared types matching the backend API ───

export interface DashboardStats {
    totalInteractions: number;
    totalUserPrompts: number;
    totalAiResponses: number;
    totalSessions: number;
    appBreakdown: { appClass: string; count: number }[];
    recentExportAt: string | null;
}

export interface InteractionRow {
    id: string;
    session_id: string;
    request_id: string;
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

export interface PaginatedResult<T> {
    data: T[];
    total: number;
    page: number;
    pageSize: number;
    totalPages: number;
}

export interface SessionSummary {
    sessionId: string;
    interactionCount: number;
    firstAt: string;
    lastAt: string;
    apps: string;
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

export const APP_CLASS_COLORS: Record<string, string> = {
    'IPM.SkypeTeams.Message.Copilot.Word': '#2B579A',
    'IPM.SkypeTeams.Message.Copilot.Excel': '#217346',
    'IPM.SkypeTeams.Message.Copilot.Teams': '#6264A7',
    'IPM.SkypeTeams.Message.Copilot.BizChat': '#0078D4',
    'IPM.SkypeTeams.Message.Copilot.WebChat': '#9B59B6',
    'IPM.SkypeTeams.Message.Copilot.Outlook': '#0078D4',
    'IPM.SkypeTeams.Message.Copilot.SharePoint': '#038387',
    'IPM.SkypeTeams.Message.Copilot.Forms': '#008272',
    'IPM.SkypeTeams.Message.Copilot.M365AdminCenter': '#5C2D91',
    'IPM.SkypeTeams.Message.Copilot.OfficeCopilotSearchAnswer': '#F59E0B',
    'IPM.SkypeTeams.Message.Copilot.ThirdPartyCopilot': '#EC4899',
    'IPM.SkypeTeams.Message.Copilot.PowerPoint': '#B7472A',
    'IPM.SkypeTeams.Message.Copilot.OneNote': '#7719AA',
    'IPM.SkypeTeams.Message.Copilot.Loop': '#3B5BDB',
    'IPM.SkypeTeams.Message.Copilot.Whiteboard': '#E81123',
};

export function getAppLabel(appClass: string): string {
    return APP_CLASS_LABELS[appClass] ?? appClass.split('.').pop() ?? appClass;
}

export function getAppColor(appClass: string): string {
    return APP_CLASS_COLORS[appClass] ?? '#6B7280';
}
