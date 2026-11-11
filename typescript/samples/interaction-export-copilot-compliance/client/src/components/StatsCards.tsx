import { MessageSquare, Bot, LayoutGrid, Clock } from 'lucide-react';
import type { DashboardStats } from '../types';

interface StatsCardsProps {
    stats: DashboardStats;
}

export default function StatsCards({ stats }: StatsCardsProps) {
    const cards = [
        {
            label: 'Total Interactions',
            value: stats.totalInteractions.toLocaleString(),
            icon: <LayoutGrid size={22} />,
            color: 'bg-blue-500',
        },
        {
            label: 'User Prompts',
            value: stats.totalUserPrompts.toLocaleString(),
            icon: <MessageSquare size={22} />,
            color: 'bg-emerald-500',
        },
        {
            label: 'AI Responses',
            value: stats.totalAiResponses.toLocaleString(),
            icon: <Bot size={22} />,
            color: 'bg-purple-500',
        },
        {
            label: 'Unique Sessions',
            value: stats.totalSessions.toLocaleString(),
            icon: <Clock size={22} />,
            color: 'bg-amber-500',
        },
    ];

    return (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
            {cards.map((c) => (
                <div
                    key={c.label}
                    className="bg-white rounded-xl border border-gray-200 p-5 flex items-center gap-4 shadow-sm hover:shadow-md transition-shadow"
                >
                    <div
                        className={`flex items-center justify-center w-11 h-11 rounded-lg text-white ${c.color}`}
                    >
                        {c.icon}
                    </div>
                    <div>
                        <p className="text-2xl font-bold text-gray-900">{c.value}</p>
                        <p className="text-sm text-gray-500">{c.label}</p>
                    </div>
                </div>
            ))}
        </div>
    );
}
