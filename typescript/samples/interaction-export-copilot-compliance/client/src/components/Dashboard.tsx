import { useState, useEffect, useRef } from 'react';
import { useAuth } from '../auth/AuthProvider';
import StatsCards from './StatsCards';
import AppUsageChart from './AppUsageChart';
import type { DashboardStats } from '../types';
import { RefreshCw, CheckCircle, Download } from 'lucide-react';

interface SyncResponse {
    synced: boolean;
    exported: number;
    freshness: { exists: boolean; stale: boolean; lastExportAt: string | null; interactionCount: number };
    stats: DashboardStats;
}

interface DashboardProps {
    refreshKey: number;
    targetUserId?: string;
}

export default function Dashboard({ refreshKey, targetUserId }: DashboardProps) {
    const { getToken } = useAuth();
    const [stats, setStats] = useState<DashboardStats | null>(null);
    const [syncing, setSyncing] = useState(false);
    const [syncMessage, setSyncMessage] = useState<string | null>(null);
    const [error, setError] = useState<string | null>(null);
    const lastSyncedUser = useRef<string>('');

    // Auto-sync when targetUserId changes or on mount
    useEffect(() => {
        if (!targetUserId) return;

        // Skip if already synced for this user in this session
        if (lastSyncedUser.current === targetUserId && stats) return;

        const sync = async () => {
            setSyncing(true);
            setError(null);
            setSyncMessage(null);
            try {
                const token = await getToken();
                const res = await fetch('/api/sync', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${token}` },
                    body: JSON.stringify({ userId: targetUserId }),
                });
                if (!res.ok) throw new Error(`HTTP ${res.status}`);
                const data: SyncResponse = await res.json();
                setStats(data.stats);
                lastSyncedUser.current = targetUserId;

                if (data.synced) {
                    setSyncMessage(`Synced ${data.exported.toLocaleString()} interactions from Microsoft Graph`);
                } else {
                    setSyncMessage('Data is up to date');
                }
            } catch (err) {
                setError((err as Error).message);
            } finally {
                setSyncing(false);
            }
        };

        sync();
    }, [targetUserId, refreshKey, getToken]);

    // Manual refresh
    const handleRefresh = async () => {
        lastSyncedUser.current = ''; // force re-sync
        setSyncing(true);
        setError(null);
        setSyncMessage(null);
        try {
            const token = await getToken();
            const res = await fetch('/api/sync', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${token}` },
                body: JSON.stringify({ userId: targetUserId }),
            });
            if (!res.ok) throw new Error(`HTTP ${res.status}`);
            const data: SyncResponse = await res.json();
            setStats(data.stats);
            lastSyncedUser.current = targetUserId ?? '';
            setSyncMessage(data.synced
                ? `Refreshed — ${data.exported.toLocaleString()} interactions synced`
                : 'Already up to date');
        } catch (err) {
            setError((err as Error).message);
        } finally {
            setSyncing(false);
        }
    };

    if (syncing && !stats) {
        return (
            <div className="flex flex-col items-center justify-center h-64 text-gray-500 gap-3">
                <RefreshCw size={24} className="animate-spin text-brand-500" />
                <p className="text-sm">Syncing interactions from Microsoft Graph…</p>
                <p className="text-xs text-gray-400">This may take a moment for first-time users</p>
            </div>
        );
    }

    if (error && !stats) {
        return (
            <div className="bg-red-50 border border-red-200 rounded-xl p-6 text-center">
                <p className="text-sm text-red-700 font-medium">Failed to sync data</p>
                <p className="text-xs text-red-500 mt-1">{error}</p>
                <button
                    onClick={handleRefresh}
                    className="mt-4 inline-flex items-center gap-2 bg-red-600 text-white px-4 py-2 rounded-lg text-sm font-medium hover:bg-red-700 transition-colors"
                >
                    <RefreshCw size={14} /> Retry
                </button>
            </div>
        );
    }

    if (!stats) return null;

    return (
        <div className="space-y-6">
            {/* Sync status bar */}
            <div className="flex items-center justify-between">
                <div className="flex items-center gap-2">
                    {syncMessage && (
                        <span className="inline-flex items-center gap-1.5 text-xs text-emerald-600 bg-emerald-50 px-3 py-1 rounded-full">
                            <CheckCircle size={12} /> {syncMessage}
                        </span>
                    )}
                    {syncing && (
                        <span className="inline-flex items-center gap-1.5 text-xs text-brand-600">
                            <RefreshCw size={12} className="animate-spin" /> Syncing…
                        </span>
                    )}
                </div>
                <button
                    onClick={handleRefresh}
                    disabled={syncing}
                    className="inline-flex items-center gap-1.5 text-xs text-brand-600 hover:text-brand-800 disabled:opacity-50 transition-colors"
                >
                    <RefreshCw size={12} /> Refresh
                </button>
            </div>

            {error && (
                <div className="bg-red-50 border border-red-200 rounded-lg p-3 text-sm text-red-700">
                    Sync error: {error}
                </div>
            )}

            <StatsCards stats={stats} />
            <AppUsageChart stats={stats} />

            {stats.recentExportAt && (
                <div className="text-xs text-gray-400 text-right">
                    Last synced: {new Date(stats.recentExportAt).toLocaleString()}
                </div>
            )}
        </div>
    );
}
