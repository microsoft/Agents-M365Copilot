import { useState } from 'react';
import { ChevronLeft, ChevronRight, MessageCircle, ExternalLink } from 'lucide-react';
import { useApi } from '../hooks/useApi';
import type { InteractionRow, PaginatedResult, SessionSummary } from '../types';
import { getAppLabel } from '../types';

interface SessionViewProps {
    focusedSessionId?: string | null;
    onClearFocus?: () => void;
}

export default function SessionView({ focusedSessionId, onClearFocus }: SessionViewProps) {
    const [page, setPage] = useState(1);
    const [selectedSession, setSelectedSession] = useState<string | null>(focusedSessionId ?? null);

    const { data: sessionsData, loading: sessionsLoading } = useApi<PaginatedResult<SessionSummary>>(
        `/sessions?page=${page}&pageSize=20`,
        [page],
    );

    const activeSession = focusedSessionId ?? selectedSession;

    const { data: sessionInteractions, loading: sessionLoading } = useApi<InteractionRow[]>(
        activeSession ? `/sessions/${encodeURIComponent(activeSession)}` : '/sessions/__none__',
        [activeSession],
    );

    if (activeSession && (focusedSessionId || selectedSession)) {
        return (
            <div className="space-y-4">
                <button
                    onClick={() => {
                        setSelectedSession(null);
                        onClearFocus?.();
                    }}
                    className="text-sm text-brand-600 hover:text-brand-800 flex items-center gap-1"
                >
                    <ChevronLeft size={16} /> Back to sessions
                </button>

                <div className="bg-white rounded-xl border border-gray-200 p-6 shadow-sm">
                    <h3 className="text-sm font-semibold text-gray-700 mb-1">Session Timeline</h3>
                    <p className="text-xs text-gray-400 mb-6 font-mono break-all">{activeSession}</p>

                    {sessionLoading && <p className="text-gray-400 text-sm">Loading…</p>}

                    {sessionInteractions && (
                        <div className="relative">
                            {/* Timeline line */}
                            <div className="absolute left-5 top-0 bottom-0 w-0.5 bg-gray-200" />

                            <div className="space-y-6">
                                {sessionInteractions.map((row, idx) => {
                                    const isPrompt = row.interaction_type === 'userPrompt';
                                    return (
                                        <div key={row.id} className="relative flex gap-4">
                                            {/* Timeline dot */}
                                            <div
                                                className={`relative z-10 flex items-center justify-center w-10 h-10 rounded-full border-2 ${isPrompt
                                                        ? 'bg-emerald-50 border-emerald-400'
                                                        : 'bg-purple-50 border-purple-400'
                                                    }`}
                                            >
                                                <MessageCircle
                                                    size={16}
                                                    className={isPrompt ? 'text-emerald-600' : 'text-purple-600'}
                                                />
                                            </div>

                                            {/* Content card */}
                                            <div className="flex-1 bg-gray-50 rounded-lg border border-gray-200 p-4">
                                                <div className="flex items-center justify-between mb-2">
                                                    <div className="flex items-center gap-2">
                                                        <span
                                                            className={`text-xs font-semibold px-2 py-0.5 rounded-full ${isPrompt
                                                                    ? 'bg-emerald-100 text-emerald-700'
                                                                    : 'bg-purple-100 text-purple-700'
                                                                }`}
                                                        >
                                                            {isPrompt ? 'User Prompt' : 'AI Response'}
                                                        </span>
                                                        <span className="text-xs text-gray-400 bg-gray-100 px-2 py-0.5 rounded">
                                                            {getAppLabel(row.app_class)}
                                                        </span>
                                                        <span className="text-xs text-gray-400">
                                                            #{idx + 1}
                                                        </span>
                                                    </div>
                                                    <span className="text-xs text-gray-400">
                                                        {new Date(row.created_at).toLocaleString()}
                                                    </span>
                                                </div>

                                                <p className="text-sm text-gray-800 whitespace-pre-wrap">
                                                    {row.body_content || '(empty)'}
                                                </p>

                                                {row.from_user_name && (
                                                    <p className="mt-2 text-xs text-gray-400">
                                                        From: {row.from_user_name}
                                                    </p>
                                                )}
                                                {row.from_app_name && (
                                                    <p className="mt-1 text-xs text-gray-400">
                                                        App: {row.from_app_name}
                                                    </p>
                                                )}
                                            </div>
                                        </div>
                                    );
                                })}
                            </div>
                        </div>
                    )}
                </div>
            </div>
        );
    }

    // Session list view
    return (
        <div className="bg-white rounded-xl border border-gray-200 shadow-sm">
            <div className="p-4 border-b border-gray-200">
                <h3 className="text-sm font-semibold text-gray-700">Copilot Sessions</h3>
                <p className="text-xs text-gray-400 mt-0.5">
                    Each session groups a user's conversation with Copilot
                </p>
            </div>

            <div className="divide-y divide-gray-100">
                {sessionsLoading && (
                    <div className="px-4 py-12 text-center text-gray-400 text-sm">Loading…</div>
                )}
                {!sessionsLoading && (!sessionsData || sessionsData.data.length === 0) && (
                    <div className="px-4 py-12 text-center text-gray-400 text-sm">No sessions found</div>
                )}
                {sessionsData?.data.map((s) => (
                    <div
                        key={s.sessionId}
                        className="px-4 py-4 flex items-center justify-between hover:bg-gray-50 transition-colors cursor-pointer"
                        onClick={() => setSelectedSession(s.sessionId)}
                    >
                        <div>
                            <p className="text-sm font-medium text-gray-800 font-mono break-all">
                                {s.sessionId.substring(0, 40)}…
                            </p>
                            <div className="flex items-center gap-3 mt-1 text-xs text-gray-400">
                                <span>{s.interactionCount} interactions</span>
                                <span>·</span>
                                <span>{new Date(s.firstAt).toLocaleDateString()} — {new Date(s.lastAt).toLocaleDateString()}</span>
                                <span>·</span>
                                <span>
                                    {s.apps
                                        .split(',')
                                        .map((a: string) => getAppLabel(a.trim()))
                                        .join(', ')}
                                </span>
                            </div>
                        </div>
                        <ExternalLink size={16} className="text-gray-300" />
                    </div>
                ))}
            </div>

            {sessionsData && sessionsData.totalPages > 1 && (
                <div className="flex items-center justify-between px-4 py-3 border-t border-gray-200 text-sm text-gray-600">
                    <span>Page {sessionsData.page} / {sessionsData.totalPages}</span>
                    <div className="flex items-center gap-2">
                        <button
                            disabled={page <= 1}
                            onClick={() => setPage(page - 1)}
                            className="p-1.5 rounded hover:bg-gray-100 disabled:opacity-30"
                        >
                            <ChevronLeft size={18} />
                        </button>
                        <button
                            disabled={page >= sessionsData.totalPages}
                            onClick={() => setPage(page + 1)}
                            className="p-1.5 rounded hover:bg-gray-100 disabled:opacity-30"
                        >
                            <ChevronRight size={18} />
                        </button>
                    </div>
                </div>
            )}
        </div>
    );
}
