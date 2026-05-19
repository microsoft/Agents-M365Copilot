import { useState } from 'react';
import { Download, Upload, RefreshCw, CheckCircle, AlertCircle } from 'lucide-react';
import { triggerExport, buildDownloadUrl } from '../hooks/useApi';
import { APP_CLASS_LABELS } from '../types';
import DateRangePicker from './DateRangePicker';

interface ExportPanelProps {
    onExportComplete?: () => void;
}

export default function ExportPanel({ onExportComplete }: ExportPanelProps) {
    const [exporting, setExporting] = useState(false);
    const [exportResult, setExportResult] = useState<{ success: boolean; count?: number; error?: string } | null>(null);
    const [userId, setUserId] = useState('');
    const [appFilter, setAppFilter] = useState('');
    const [downloadAppFilter, setDownloadAppFilter] = useState('');
    const [startDate, setStartDate] = useState('');
    const [endDate, setEndDate] = useState('');

    const handleExport = async () => {
        setExporting(true);
        setExportResult(null);
        try {
            const result = await triggerExport(userId || undefined, appFilter || undefined);
            setExportResult({ success: true, count: result.count });
            onExportComplete?.();
        } catch (err) {
            setExportResult({ success: false, error: (err as Error).message });
        } finally {
            setExporting(false);
        }
    };

    return (
        <div className="space-y-6">
            {/* Fetch from Graph */}
            <div className="bg-white rounded-xl border border-gray-200 p-6 shadow-sm">
                <div className="flex items-center gap-2 mb-4">
                    <Upload size={18} className="text-brand-600" />
                    <h3 className="text-sm font-semibold text-gray-700">
                        Export from Microsoft Graph
                    </h3>
                </div>
                <p className="text-xs text-gray-500 mb-4">
                    Pull Copilot AI interactions from the Graph API and store them in the local database for compliance archival.
                </p>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
                    <div>
                        <label className="block text-xs font-medium text-gray-600 mb-1">
                            User ID (or uses USER_ID from .env)
                        </label>
                        <input
                            type="text"
                            value={userId}
                            onChange={(e) => setUserId(e.target.value)}
                            placeholder="e.g. 886cb6c8-eb73-…"
                            className="w-full border border-gray-300 rounded-md px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-brand-500"
                        />
                    </div>
                    <div>
                        <label className="block text-xs font-medium text-gray-600 mb-1">
                            App Filter (optional)
                        </label>
                        <select
                            value={appFilter}
                            onChange={(e) => setAppFilter(e.target.value)}
                            className="w-full border border-gray-300 rounded-md px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-brand-500"
                        >
                            <option value="">All Apps</option>
                            {Object.entries(APP_CLASS_LABELS).map(([key, label]) => (
                                <option key={key} value={key}>{label}</option>
                            ))}
                        </select>
                    </div>
                </div>

                <button
                    onClick={handleExport}
                    disabled={exporting}
                    className="inline-flex items-center gap-2 bg-brand-600 text-white px-5 py-2.5 rounded-lg text-sm font-medium hover:bg-brand-700 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
                >
                    {exporting ? <RefreshCw size={16} className="animate-spin" /> : <Upload size={16} />}
                    {exporting ? 'Exporting…' : 'Run Export'}
                </button>

                {exportResult && (
                    <div
                        className={`mt-4 flex items-center gap-2 text-sm px-4 py-3 rounded-lg ${exportResult.success
                                ? 'bg-emerald-50 text-emerald-700 border border-emerald-200'
                                : 'bg-red-50 text-red-700 border border-red-200'
                            }`}
                    >
                        {exportResult.success ? (
                            <>
                                <CheckCircle size={16} />
                                Export complete — {exportResult.count} interactions archived
                            </>
                        ) : (
                            <>
                                <AlertCircle size={16} />
                                Export failed: {exportResult.error}
                            </>
                        )}
                    </div>
                )}
            </div>

            {/* Download archive */}
            <div className="bg-white rounded-xl border border-gray-200 p-6 shadow-sm">
                <div className="flex items-center gap-2 mb-4">
                    <Download size={18} className="text-brand-600" />
                    <h3 className="text-sm font-semibold text-gray-700">
                        Download Compliance Archive
                    </h3>
                </div>
                <p className="text-xs text-gray-500 mb-4">
                    Download all stored interactions as JSON or CSV for regulatory review and archival.
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

                <div className="flex gap-3">
                    <a
                        href={buildDownloadUrl({ format: 'json', appClass: downloadAppFilter, startDate, endDate })}
                        className="inline-flex items-center gap-2 bg-gray-100 text-gray-700 px-4 py-2.5 rounded-lg text-sm font-medium hover:bg-gray-200 transition-colors border border-gray-200"
                    >
                        <Download size={16} /> Download JSON
                    </a>
                    <a
                        href={buildDownloadUrl({ format: 'csv', appClass: downloadAppFilter, startDate, endDate })}
                        className="inline-flex items-center gap-2 bg-gray-100 text-gray-700 px-4 py-2.5 rounded-lg text-sm font-medium hover:bg-gray-200 transition-colors border border-gray-200"
                    >
                        <Download size={16} /> Download CSV
                    </a>
                </div>
            </div>
        </div>
    );
}
