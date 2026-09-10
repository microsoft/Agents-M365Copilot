interface DateRangePickerProps {
    startDate: string;
    endDate: string;
    onStartChange: (v: string) => void;
    onEndChange: (v: string) => void;
}

export default function DateRangePicker({
    startDate,
    endDate,
    onStartChange,
    onEndChange,
}: DateRangePickerProps) {
    return (
        <div className="flex items-center gap-2 text-sm">
            <label className="text-gray-500 font-medium">From</label>
            <input
                type="date"
                value={startDate}
                onChange={(e) => onStartChange(e.target.value)}
                className="border border-gray-300 rounded-md px-2 py-1.5 text-sm focus:outline-none focus:ring-2 focus:ring-brand-500 focus:border-brand-500"
            />
            <label className="text-gray-500 font-medium">To</label>
            <input
                type="date"
                value={endDate}
                onChange={(e) => onEndChange(e.target.value)}
                className="border border-gray-300 rounded-md px-2 py-1.5 text-sm focus:outline-none focus:ring-2 focus:ring-brand-500 focus:border-brand-500"
            />
        </div>
    );
}
