import { useState } from 'react';
import { Download } from 'lucide-react';
import { buildDownloadUrl } from '../hooks/useApi';
import { APP_CLASS_LABELS } from '../types';
import DateRangePicker from './DateRangePicker';

interface ExportPanelProps {
    selectedUserId?: string;
    onExportComplete?: () => void;
}

export default function ExportPanel({ selectedUserId }: ExportPanelProps) {
    const [downloadAppFilter, setDownloadAppFilter] = useState('');
    const [startDate, setStartDate] = useState('');
    const [endDate, setEndDate] = useState('');

    return (
        <div className="space-y-6">
            {/* Info banner */}
            <div className="bg-blue-50 border border-blue-200 rounded-xl p-4">
                <p className="text-sm text-blue-800 font-medium">Data is synced automatically</p>
                <p className="text-xs text-blue-600 mt-0.5">
                    Interactions are exported from Microsoft Graph automatically when you view a user's dashboard.
                    Data refreshes hourly via the scheduler and on-demand when you switch users.
                </p>
            </div>

            {/* Download archive — CSV only */}
            <div className="bg-white rounded-xl border border-gray-200 p-6 shadow-sm">
                <div className="flex items-center gap-2 mb-4">
                    <Download size={18} className="text-brand-600" />
                    <h3 className="text-sm font-semibold text-gray-700">
                        Download Compliance Archive
                    </h3>
                </div>
                <p className="text-xs text-gray-500 mb-4">
                    Download stored interactions as CSV for regulatory review, legal hold, and eDiscovery workflows.
                </p>

                <div className="flex flex-wrap items-end gap-4 mb-4">
                    <div>
                        <label className="block text-xs font-medium text-gray-600 mb-1">App Filter</label>
                        <select
                            value={downloadAppFilter}
                            onChange={(e) => setDownloadAppFilter(e.target.value)}
                            className="border border-gray-300 rounded-md px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-brand-500"
                        >
                            <option value="">All Apps</option>
                            {Object.entries(APP_CLASS_LABELS).map(([key, label]) => (
                                <option key={key} value={key}>{label}</option>
                            ))}
                        </select>
                    </div>

                    <DateRangePicker
                        startDate={startDate}
                        endDate={endDate}
                        onStartChange={setStartDate}
                        onEndChange={setEndDate}
                    />
                </div>

                <a
                    href={buildDownloadUrl({
                        format: 'csv',
                        targetUserId: selectedUserId,
                        appClass: downloadAppFilter,
                        startDate,
                        endDate,
                    })}
                    className="inline-flex items-center gap-2 bg-brand-600 text-white px-5 py-2.5 rounded-lg text-sm font-medium hover:bg-brand-700 transition-colors"
                >
                    <Download size={16} /> Download CSV
                </a>
            </div>
        </div>
    );
}
