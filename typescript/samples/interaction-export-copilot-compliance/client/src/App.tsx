import { useState, useCallback } from 'react';
import Navbar from './components/Navbar';
import Dashboard from './components/Dashboard';
import InteractionsTable from './components/InteractionsTable';
import SessionView from './components/SessionView';
import ExportPanel from './components/ExportPanel';

type Tab = 'overview' | 'interactions' | 'sessions' | 'export';

export default function App() {
    const [activeTab, setActiveTab] = useState<Tab>('overview');
    const [refreshKey, setRefreshKey] = useState(0);
    const [focusedSession, setFocusedSession] = useState<string | null>(null);

    const handleViewSession = useCallback((sessionId: string) => {
        setFocusedSession(sessionId);
        setActiveTab('sessions');
    }, []);

    const handleExportComplete = useCallback(() => {
        setRefreshKey((k) => k + 1);
    }, []);

    return (
        <div className="min-h-screen bg-gray-50">
            <Navbar activeTab={activeTab} onTabChange={(t) => { setActiveTab(t); setFocusedSession(null); }} />

            <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
                {activeTab === 'overview' && <Dashboard refreshKey={refreshKey} />}
                {activeTab === 'interactions' && (
                    <InteractionsTable onViewSession={handleViewSession} />
                )}
                {activeTab === 'sessions' && (
                    <SessionView
                        focusedSessionId={focusedSession}
                        onClearFocus={() => setFocusedSession(null)}
                    />
                )}
                {activeTab === 'export' && (
                    <ExportPanel onExportComplete={handleExportComplete} />
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
