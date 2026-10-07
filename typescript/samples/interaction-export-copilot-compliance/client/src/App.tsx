import { useState, useCallback, useMemo, useEffect } from 'react';
import { Shield, LogIn, LogOut, Search, Users } from 'lucide-react';
import Navbar from './components/Navbar';
import Dashboard from './components/Dashboard';
import InteractionsTable from './components/InteractionsTable';
import SessionView from './components/SessionView';
import ExportPanel from './components/ExportPanel';
import { useApi } from './hooks/useApi';
import { useAuth } from './auth/AuthProvider';
import type { TargetUserSummary } from './types';

type Tab = 'overview' | 'interactions' | 'sessions' | 'export';

interface GraphUser {
    userId: string;
    displayName: string;
    email: string;
}

export default function App() {
    const { user, isAdmin, isViewer, loading: authLoading, login, logout, getToken } = useAuth();
    const [activeTab, setActiveTab] = useState<Tab>('overview');
    const [refreshKey, setRefreshKey] = useState(0);
    const [focusedSession, setFocusedSession] = useState<string | null>(null);

    // ─── User search state ───
    const [userSearch, setUserSearch] = useState('');
    const [selectedUserId, setSelectedUserId] = useState('');
    const [graphUsers, setGraphUsers] = useState<GraphUser[]>([]);
    const [searchMode, setSearchMode] = useState<'local' | 'graph'>('local');

    // Local archived users
    const usersPath = useMemo(
        () => `/users?search=${encodeURIComponent(userSearch.trim())}`,
        [userSearch],
    );
    const { data: localUsers } = useApi<TargetUserSummary[]>(usersPath, [usersPath, refreshKey]);

    // Auto-select logged-in user by default
    useEffect(() => {
        if (!selectedUserId && user?.oid) {
            setSelectedUserId(user.oid);
        }
    }, [selectedUserId, user]);

    // Graph user search (debounced)
    useEffect(() => {
        if (searchMode !== 'graph' || userSearch.trim().length < 2) {
            setGraphUsers([]);
            return;
        }
        const timer = setTimeout(async () => {
            try {
                const token = await getToken();
                const res = await fetch(`/api/graph/users?search=${encodeURIComponent(userSearch.trim())}`, {
                    headers: { Authorization: `Bearer ${token}` },
                });
                if (res.ok) {
                    const data = await res.json();
                    console.log('Graph user search results:', data);
                    setGraphUsers(data);
                } else {
                    console.error('Graph search failed:', res.status, await res.text());
                }
            } catch (err) { console.error('Graph search error:', err); }
        }, 400);
        return () => clearTimeout(timer);
    }, [userSearch, searchMode, getToken]);

    const handleViewSession = useCallback((sessionId: string) => {
        setFocusedSession(sessionId);
        setActiveTab('sessions');
    }, []);

    const handleExportComplete = useCallback(() => {
        setRefreshKey((k) => k + 1);
    }, []);

    // ─── Loading state ───
    if (authLoading) {
        return (
            <div className="min-h-screen bg-gray-50 flex items-center justify-center">
                <div className="text-gray-400 text-sm">Loading…</div>
            </div>
        );
    }

    // ─── Login screen ───
    if (!user) {
        return (
            <div className="min-h-screen bg-gray-50 flex items-center justify-center">
                <div className="bg-white rounded-2xl border border-gray-200 shadow-lg p-10 text-center max-w-md">
                    <div className="flex items-center justify-center w-14 h-14 rounded-xl bg-brand-600 text-white mx-auto mb-4">
                        <Shield size={28} />
                    </div>
                    <h1 className="text-xl font-semibold text-gray-900 mb-2">Copilot Compliance Dashboard</h1>
                    <p className="text-sm text-gray-500 mb-6">
                        Sign in with your Microsoft Entra account to access the compliance dashboard.
                        Requires <strong>ComplianceAdmin</strong> or <strong>ComplianceViewer</strong> role.
                    </p>
                    <button
                        onClick={login}
                        className="inline-flex items-center gap-2 bg-brand-600 text-white px-6 py-3 rounded-lg text-sm font-medium hover:bg-brand-700 transition-colors"
                    >
                        <LogIn size={18} /> Sign in with Microsoft
                    </button>
                </div>
            </div>
        );
    }

    // ─── Access denied ───
    if (!isAdmin && !isViewer) {
        return (
            <div className="min-h-screen bg-gray-50 flex items-center justify-center">
                <div className="bg-white rounded-2xl border border-gray-200 shadow-lg p-10 text-center max-w-md">
                    <div className="flex items-center justify-center w-14 h-14 rounded-xl bg-red-100 text-red-600 mx-auto mb-4">
                        <Shield size={28} />
                    </div>
                    <h1 className="text-xl font-semibold text-gray-900 mb-2">Access Denied</h1>
                    <p className="text-sm text-gray-500 mb-4">
                        Your account <strong>{user.email}</strong> does not have the required role.
                        Contact your admin to assign <strong>ComplianceAdmin</strong> or <strong>ComplianceViewer</strong>.
                    </p>
                    <button
                        onClick={logout}
                        className="inline-flex items-center gap-2 bg-gray-100 text-gray-700 px-5 py-2.5 rounded-lg text-sm font-medium hover:bg-gray-200 transition-colors border border-gray-200"
                    >
                        <LogOut size={16} /> Sign out
                    </button>
                </div>
            </div>
        );
    }

    // ─── Dropdown items: either local archived users or Graph search results ───
    const dropdownItems = searchMode === 'graph'
        ? graphUsers.map((u) => ({ id: u.userId, label: `${u.displayName} (${u.email})` }))
        : (localUsers ?? []).map((u) => ({ id: u.userId, label: `${u.displayName} (${u.userId})` }));

    return (
        <div className="min-h-screen bg-gray-50">
            <Navbar
                activeTab={activeTab}
                onTabChange={(t) => { setActiveTab(t); setFocusedSession(null); }}
                user={user}
                isAdmin={isAdmin}
                onLogout={logout}
            />

            <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
                {/* ─── User Selector ─── */}
                <div className="mb-4 bg-white border border-gray-200 rounded-xl p-4 shadow-sm">
                    <div className="flex flex-col md:flex-row md:items-end gap-3">
                        {/* Search mode toggle */}
                        <div className="flex gap-1 self-start md:self-end">
                            <button
                                onClick={() => setSearchMode('local')}
                                className={`px-3 py-2 text-xs rounded-md font-medium transition-colors ${searchMode === 'local' ? 'bg-brand-50 text-brand-700' : 'bg-gray-100 text-gray-600 hover:bg-gray-200'}`}
                                title="Search users already in the local archive"
                            >
                                <Users size={14} className="inline mr-1" />Archive
                            </button>
                            <button
                                onClick={() => setSearchMode('graph')}
                                className={`px-3 py-2 text-xs rounded-md font-medium transition-colors ${searchMode === 'graph' ? 'bg-brand-50 text-brand-700' : 'bg-gray-100 text-gray-600 hover:bg-gray-200'}`}
                                title="Search all users in your tenant via Microsoft Graph"
                            >
                                <Search size={14} className="inline mr-1" />Graph
                            </button>
                        </div>

                        {/* Search input + inline results */}
                        <div className="flex-1 relative">
                            <label className="block text-xs font-medium text-gray-600 mb-1">
                                {searchMode === 'graph' ? 'Search tenant by display name' : 'Search archived users'}
                            </label>
                            <input
                                type="text"
                                value={userSearch}
                                onChange={(e) => setUserSearch(e.target.value)}
                                placeholder={searchMode === 'graph' ? 'Type a name (min 2 chars)…' : 'Search by user ID or name…'}
                                className="w-full border border-gray-300 rounded-md px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-brand-500"
                            />

                            {/* Autocomplete dropdown */}
                            {dropdownItems.length > 0 && userSearch.trim().length >= 1 && (
                                <ul className="absolute z-50 left-0 right-0 mt-1 bg-white border border-gray-200 rounded-lg shadow-lg max-h-60 overflow-y-auto">
                                    {dropdownItems.map((item) => (
                                        <li
                                            key={item.id}
                                            onClick={() => {
                                                setSelectedUserId(item.id);
                                                setUserSearch('');
                                            }}
                                            className={`px-4 py-2.5 text-sm cursor-pointer hover:bg-brand-50 transition-colors border-b border-gray-50 last:border-b-0 ${selectedUserId === item.id ? 'bg-brand-50 text-brand-700 font-medium' : 'text-gray-700'
                                                }`}
                                        >
                                            {item.label}
                                        </li>
                                    ))}
                                </ul>
                            )}
                        </div>
                    </div>

                    {selectedUserId && (
                        <div className="mt-2 flex items-center gap-2">
                            <span className="text-xs text-gray-500">Dashboard scope:</span>
                            <span className="text-xs font-mono bg-gray-100 px-2 py-0.5 rounded text-gray-700">{selectedUserId}</span>
                            {selectedUserId === user?.oid && (
                                <span className="text-[10px] font-semibold bg-brand-100 text-brand-700 px-1.5 py-0.5 rounded">You</span>
                            )}
                            {selectedUserId !== user?.oid && (
                                <button
                                    onClick={() => setSelectedUserId(user?.oid ?? '')}
                                    className="text-[10px] text-brand-600 hover:underline"
                                >
                                    Reset to me
                                </button>
                            )}
                        </div>
                    )}
                </div>

                {activeTab === 'overview' && <Dashboard refreshKey={refreshKey} targetUserId={selectedUserId} />}
                {activeTab === 'interactions' && (
                    <InteractionsTable targetUserId={selectedUserId} onViewSession={handleViewSession} />
                )}
                {activeTab === 'sessions' && (
                    <SessionView
                        targetUserId={selectedUserId}
                        focusedSessionId={focusedSession}
                        onClearFocus={() => setFocusedSession(null)}
                    />
                )}
                {activeTab === 'export' && (
                    <ExportPanel selectedUserId={selectedUserId} />
                )}
            </main>

            <footer className="text-center text-xs text-gray-400 py-6 border-t border-gray-200 mt-8">
                Copilot Interaction Export API — Compliance Dashboard
                &nbsp;·&nbsp;
                <a
                    href="https://learn.microsoft.com/en-us/graph/api/aiinteractionhistory-getallenterpriseinteractions"
                    target="_blank"
                    rel="noreferrer"
                    className="text-brand-500 hover:underline"
                >
                    API Docs
                </a>
            </footer>
        </div>
    );
}
