import { useState, useEffect, useCallback } from 'react';

const API_BASE = '/api';

export function useApi<T>(path: string, deps: unknown[] = []) {
    const [data, setData] = useState<T | null>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    const fetchData = useCallback(async () => {
        setLoading(true);
        setError(null);
        try {
            const res = await fetch(`${API_BASE}${path}`);
            if (!res.ok) throw new Error(`HTTP ${res.status}`);
            const json = await res.json();
            setData(json);
        } catch (err) {
            setError((err as Error).message);
        } finally {
            setLoading(false);
        }
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [path, ...deps]);

    useEffect(() => {
        fetchData();
    }, [fetchData]);

    return { data, loading, error, refetch: fetchData };
}

export async function triggerExport(userId?: string, appClass?: string) {
    const res = await fetch(`${API_BASE}/export`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ userId, appClass }),
    });
    if (!res.ok) {
        const body = await res.json().catch(() => ({}));
        throw new Error(body.error ?? `HTTP ${res.status}`);
    }
    return res.json() as Promise<{ success: boolean; count: number }>;
}

export function buildDownloadUrl(params: {
    format: 'json' | 'csv';
    appClass?: string;
    startDate?: string;
    endDate?: string;
}): string {
    const qs = new URLSearchParams();
    qs.set('format', params.format);
    if (params.appClass) qs.set('appClass', params.appClass);
    if (params.startDate) qs.set('startDate', params.startDate);
    if (params.endDate) qs.set('endDate', params.endDate);
    return `${API_BASE}/export/download?${qs.toString()}`;
}
