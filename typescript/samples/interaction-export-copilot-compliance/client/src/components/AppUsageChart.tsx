import { PieChart, Pie, Cell, ResponsiveContainer, BarChart, Bar, XAxis, YAxis, Tooltip, Legend } from 'recharts';
import type { DashboardStats } from '../types';
import { getAppLabel, getAppColor } from '../types';

interface AppUsageChartProps {
    stats: DashboardStats;
}

export default function AppUsageChart({ stats }: AppUsageChartProps) {
    const data = stats.appBreakdown.map((item) => ({
        name: getAppLabel(item.appClass),
        value: item.count,
        fill: getAppColor(item.appClass),
    }));

    if (!data.length) {
        return (
            <div className="bg-white rounded-xl border border-gray-200 p-6 flex items-center justify-center h-64 text-gray-400">
                No interaction data yet
            </div>
        );
    }

    const total = data.reduce((sum, d) => sum + d.value, 0);
    // Only label slices that are >= 5% of total to avoid overlap on long-tail slices
    const LABEL_THRESHOLD = 0.05;

    return (
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
            {/* Pie Chart */}
            <div className="bg-white rounded-xl border border-gray-200 p-6 shadow-sm">
                <h3 className="text-sm font-semibold text-gray-700 mb-4">
                    Interactions by App
                </h3>
                <div className="flex items-center gap-2">
                    <ResponsiveContainer width="60%" height={260}>
                        <PieChart>
                            <Pie
                                data={data}
                                cx="50%"
                                cy="50%"
                                innerRadius={55}
                                outerRadius={95}
                                paddingAngle={2}
                                dataKey="value"
                                minAngle={2}
                                label={({ percent }) =>
                                    percent >= LABEL_THRESHOLD
                                        ? `${(percent * 100).toFixed(0)}%`
                                        : ''
                                }
                                labelLine={false}
                            >
                                {data.map((entry, idx) => (
                                    <Cell key={idx} fill={entry.fill} />
                                ))}
                            </Pie>
                            <Tooltip
                                formatter={(value: number) => [
                                    `${value.toLocaleString()} (${((value / total) * 100).toFixed(1)}%)`,
                                    'Interactions',
                                ]}
                            />
                        </PieChart>
                    </ResponsiveContainer>
                    <ul className="flex-1 space-y-1.5 text-xs max-h-[260px] overflow-y-auto pr-1">
                        {data.map((entry) => {
                            const pct = ((entry.value / total) * 100).toFixed(1);
                            return (
                                <li
                                    key={entry.name}
                                    className="flex items-center gap-2 text-gray-700"
                                >
                                    <span
                                        className="inline-block w-2.5 h-2.5 rounded-sm flex-shrink-0"
                                        style={{ backgroundColor: entry.fill }}
                                    />
                                    <span className="truncate flex-1" title={entry.name}>
                                        {entry.name}
                                    </span>
                                    <span className="text-gray-500 tabular-nums">{pct}%</span>
                                </li>
                            );
                        })}
                    </ul>
                </div>
            </div>

            {/* Bar Chart */}
            <div className="bg-white rounded-xl border border-gray-200 p-6 shadow-sm">
                <h3 className="text-sm font-semibold text-gray-700 mb-4">
                    Interaction Volume by App
                </h3>
                <ResponsiveContainer width="100%" height={260}>
                    <BarChart data={data} layout="vertical" margin={{ left: 30 }}>
                        <XAxis type="number" />
                        <YAxis type="category" dataKey="name" width={100} tick={{ fontSize: 12 }} />
                        <Tooltip />
                        <Legend />
                        <Bar dataKey="value" name="Interactions" radius={[0, 6, 6, 0]}>
                            {data.map((entry, idx) => (
                                <Cell key={idx} fill={entry.fill} />
                            ))}
                        </Bar>
                    </BarChart>
                </ResponsiveContainer>
            </div>
        </div>
    );
}
