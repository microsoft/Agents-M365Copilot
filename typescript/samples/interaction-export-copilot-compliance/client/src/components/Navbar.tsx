import { Shield } from 'lucide-react';

type Tab = 'overview' | 'interactions' | 'sessions' | 'export';

interface NavbarProps {
    activeTab: Tab;
    onTabChange: (tab: Tab) => void;
}

const tabs: { id: Tab; label: string }[] = [
    { id: 'overview', label: 'Overview' },
    { id: 'interactions', label: 'Interactions' },
    { id: 'sessions', label: 'Sessions' },
    { id: 'export', label: 'Export & Archive' },
];

export default function Navbar({ activeTab, onTabChange }: NavbarProps) {
    return (
        <header className="bg-white border-b border-gray-200 shadow-sm">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="flex items-center justify-between h-16">
                    <div className="flex items-center gap-3">
                        <div className="flex items-center justify-center w-9 h-9 rounded-lg bg-brand-600 text-white">
                            <Shield size={20} />
                        </div>
                        <div>
                            <h1 className="text-lg font-semibold text-gray-900 leading-tight">
                                Copilot Compliance Dashboard
                            </h1>
                            <p className="text-xs text-gray-500 leading-tight">
                                Interaction Export API
                            </p>
                        </div>
                    </div>

                    <nav className="flex space-x-1">
                        {tabs.map((t) => (
                            <button
                                key={t.id}
                                onClick={() => onTabChange(t.id)}
                                className={`px-4 py-2 text-sm font-medium rounded-md transition-colors ${activeTab === t.id
                                        ? 'bg-brand-50 text-brand-700'
                                        : 'text-gray-600 hover:text-gray-900 hover:bg-gray-100'
                                    }`}
                            >
                                {t.label}
                            </button>
                        ))}
                    </nav>
                </div>
            </div>
        </header>
    );
}
