import { useState } from 'react';
import { Search, ChevronLeft, ChevronRight, User, Bot, ExternalLink } from 'lucide-react';
import { useApi } from '../hooks/useApi';
import type { InteractionRow, PaginatedResult } from '../types';
import { getAppLabel, APP_CLASS_LABELS } from '../types';

interface InteractionsTableProps {
    targetUserId?: string;
    onViewSession?: (sessionId: string) => void;
}

export default function InteractionsTable({ targetUserId, onViewSession }: InteractionsTableProps) {
    const [page, setPage] = useState(1);
    const [pageSize] = useState(25);
    const [search, setSearch] = useState('');
    const [appFilter, setAppFilter] = useState('');
    const [typeFilter, setTypeFilter] = useState('');
    const [startDate, setStartDate] = useState('');
    const [endDate, setEndDate] = useState('');
    const [expandedId, setExpandedId] = useState<string | null>(null);

    const queryParams = new URLSearchParams({
        page: String(page),
        pageSize: String(pageSize),
    });
    if (targetUserId) queryParams.set('targetUserId', targetUserId);
    if (search) queryParams.set('search', search);
    if (appFilter) queryParams.set('appClass', appFilter);
    if (typeFilter) queryParams.set('interactionType', typeFilter);
    if (startDate) queryParams.set('startDate', startDate);
    if (endDate) queryParams.set('endDate', endDate);

    const { data, loading } = useApi<PaginatedResult<InteractionRow>>(
        `/interactions?${queryParams.toString()}`,
        [page, pageSize, search, appFilter, typeFilter, startDate, endDate],
    );

    return (
        <div className="bg-white rounded-xl border border-gray-200 shadow-sm">
            {/* Toolbar */}
            <div className="p-4 border-b border-gray-200 flex flex-wrap gap-3 items-center">
                <div className="relative flex-1 min-w-[200px]">
                    <Search size={16} className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400" />
                    <input
                        type="text"
                        placeholder="Search interactions…"
                        value={search}
                        onChange={(e) => { setSearch(e.target.value); setPage(1); }}
                        className="w-full pl-9 pr-3 py-2 text-sm border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-brand-500"
                    />
                </div>

                <select
                    value={appFilter}
                    onChange={(e) => { setAppFilter(e.target.value); setPage(1); }}
                    className="text-sm border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:ring-2 focus:ring-brand-500"
                >
                    <option value="">All Apps</option>
                    {Object.entries(APP_CLASS_LABELS).map(([key, label]) => (
                        <option key={key} value={key}>{label}</option>
                    ))}
                </select>

                <select
                    value={typeFilter}
                    onChange={(e) => { setTypeFilter(e.target.value); setPage(1); }}
                    className="text-sm border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:ring-2 focus:ring-brand-500"
                >
                    <option value="">All Types</option>
                    <option value="userPrompt">User Prompt</option>
                    <option value="aiResponse">AI Response</option>
                </select>

                <input
                    type="date"
                    value={startDate}
                    onChange={(e) => { setStartDate(e.target.value); setPage(1); }}
                    className="text-sm border border-gray-300 rounded-md px-2 py-2 focus:outline-none focus:ring-2 focus:ring-brand-500"
                />
                <span className="text-gray-400 text-sm">to</span>
                <input
                    type="date"
                    value={endDate}
                    onChange={(e) => { setEndDate(e.target.value); setPage(1); }}
                    className="text-sm border border-gray-300 rounded-md px-2 py-2 focus:outline-none focus:ring-2 focus:ring-brand-500"
                />
            </div>

            {/* Table */}
            <div className="overflow-x-auto">
                <table className="w-full text-sm">
                    <thead>
                        <tr className="bg-gray-50 text-left text-gray-600 text-xs uppercase tracking-wider">
                            <th className="px-4 py-3 font-semibold">Type</th>
                            <th className="px-4 py-3 font-semibold">App</th>
                            <th className="px-4 py-3 font-semibold">From</th>
                            <th className="px-4 py-3 font-semibold">Content</th>
                            <th className="px-4 py-3 font-semibold">Timestamp</th>
                            <th className="px-4 py-3 font-semibold">Session</th>
                        </tr>
                    </thead>
                    <tbody className="divide-y divide-gray-100">
                        {loading && (
                            <tr>
                                <td colSpan={6} className="px-4 py-12 text-center text-gray-400">
                                    Loading…
                                </td>
                            </tr>
                        )}
                        {!loading && (!data || data.data.length === 0) && (
                            <tr>
                                <td colSpan={6} className="px-4 py-12 text-center text-gray-400">
                                    No interactions found
                                </td>
                            </tr>
                        )}
                        {data?.data.map((row) => (
                            <>
                                <tr
                                    key={row.id}
                                    className="hover:bg-gray-50 cursor-pointer transition-colors"
                                    onClick={() => setExpandedId(expandedId === row.id ? null : row.id)}
                                >
                                    <td className="px-4 py-3">
                                        {row.interaction_type === 'userPrompt' ? (
                                            <span className="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-xs font-medium bg-emerald-100 text-emerald-700">
                                                <User size={12} /> Prompt
                                            </span>
                                        ) : (
                                            <span className="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-xs font-medium bg-purple-100 text-purple-700">
                                                <Bot size={12} /> Response
                                            </span>
                                        )}
                                    </td>
                                    <td className="px-4 py-3">
                                        <span className="inline-flex px-2 py-0.5 rounded text-xs font-medium bg-gray-100 text-gray-700">
                                            {getAppLabel(row.app_class)}
                                        </span>
                                    </td>
                                    <td className="px-4 py-3 text-gray-700">
                                        {row.from_user_name ?? row.from_app_name ?? '—'}
                                    </td>
                                    <td className="px-4 py-3 text-gray-600 max-w-md truncate">
                                        {row.body_content?.substring(0, 120) ?? '—'}
                                    </td>
                                    <td className="px-4 py-3 text-gray-500 whitespace-nowrap">
                                        {new Date(row.created_at).toLocaleString()}
                                    </td>
                                    <td className="px-4 py-3">
                                        {onViewSession && (
                                            <button
                                                onClick={(e) => {
                                                    e.stopPropagation();
                                                    if (!row.session_id) return;
                                                    onViewSession(row.session_id);
                                                }}
                                                className="text-brand-600 hover:text-brand-800 inline-flex items-center gap-1 text-xs"
                                                title="View session"
                                            >
                                                <ExternalLink size={12} /> View
                                            </button>
                                        )}
                                    </td>
                                </tr>
                                {expandedId === row.id && (
                                    <tr key={`${row.id}-expanded`}>
                                        <td colSpan={6} className="px-6 py-4 bg-gray-50">
                                            <div className="space-y-2 text-sm">
                                                <div>
                                                    <span className="font-semibold text-gray-600">Full Content:</span>
                                                    <p className="mt-1 whitespace-pre-wrap text-gray-800 bg-white p-3 rounded border border-gray-200 max-h-60 overflow-y-auto">
                                                        {row.body_content || '(empty)'}
                                                    </p>
                                                </div>
                                                <div className="grid grid-cols-2 gap-4 text-xs text-gray-500">
                                                    <div><span className="font-medium">ID:</span> {row.id}</div>
                                                    <div><span className="font-medium">Request ID:</span> {row.request_id}</div>
                                                    <div><span className="font-medium">Session ID:</span> {row.session_id}</div>
                                                    <div><span className="font-medium">Locale:</span> {row.locale}</div>
                                                    <div><span className="font-medium">Conversation Type:</span> {row.conversation_type}</div>
                                                    <div><span className="font-medium">Exported At:</span> {new Date(row.exported_at).toLocaleString()}</div>
                                                </div>
                                            </div>
                                        </td>
                                    </tr>
                                )}
                            </>
                        ))}
                    </tbody>
                </table>
            </div>

            {/* Pagination */}
            {data && data.totalPages > 1 && (
                <div className="flex items-center justify-between px-4 py-3 border-t border-gray-200 text-sm text-gray-600">
                    <span>
                        Showing {(data.page - 1) * data.pageSize + 1}–
                        {Math.min(data.page * data.pageSize, data.total)} of {data.total}
                    </span>
                    <div className="flex items-center gap-2">
                        <button
                            disabled={page <= 1}
                            onClick={() => setPage(page - 1)}
                            className="p-1.5 rounded hover:bg-gray-100 disabled:opacity-30 disabled:cursor-not-allowed"
                        >
                            <ChevronLeft size={18} />
                        </button>
                        <span className="px-2">
                            Page {data.page} / {data.totalPages}
                        </span>
                        <button
                            disabled={page >= data.totalPages}
                            onClick={() => setPage(page + 1)}
                            className="p-1.5 rounded hover:bg-gray-100 disabled:opacity-30 disabled:cursor-not-allowed"
                        >
                            <ChevronRight size={18} />
                        </button>
                    </div>
                </div>
            )}
        </div>
    );
}
