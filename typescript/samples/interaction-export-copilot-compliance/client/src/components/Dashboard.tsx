import { useApi } from '../hooks/useApi';
import StatsCards from './StatsCards';
import AppUsageChart from './AppUsageChart';
import type { DashboardStats } from '../types';

interface DashboardProps {
    refreshKey: number;
}

export default function Dashboard({ refreshKey }: DashboardProps) {
    const { data: stats, loading } = useApi<DashboardStats>('/stats', [refreshKey]);

    if (loading || !stats) {
        return (
            <div className="flex items-center justify-center h-64 text-gray-400 text-sm">
                Loading dashboard…
            </div>
        );
    }

    return (
        <div className="space-y-6">
            <StatsCards stats={stats} />
            <AppUsageChart stats={stats} />

            {stats.recentExportAt && (
                <div className="text-xs text-gray-400 text-right">
                    Last export: {new Date(stats.recentExportAt).toLocaleString()}
                </div>
            )}
        </div>
    );
}
