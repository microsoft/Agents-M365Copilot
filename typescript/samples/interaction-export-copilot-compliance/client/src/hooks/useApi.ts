import { useState, useEffect, useCallback } from 'react';
import { useAuth } from '../auth/AuthProvider';

const API_BASE = '/api';

export function useApi<T>(path: string, deps: unknown[] = []) {
    const [data, setData] = useState<T | null>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);
    const { getToken } = useAuth();

    const fetchData = useCallback(async () => {
        setLoading(true);
        setError(null);
        try {
            const token = await getToken();
            const res = await fetch(`${API_BASE}${path}`, {
                headers: { Authorization: `Bearer ${token}` },
            });
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

export async function triggerExport(getToken: () => Promise<string>, userId?: string, appClass?: string) {
    const token = await getToken();
    const res = await fetch(`${API_BASE}/export`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${token}` },
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
    targetUserId?: string;
    appClass?: string;
    startDate?: string;
    endDate?: string;
}): string {
    const qs = new URLSearchParams();
    qs.set('format', params.format);
    if (params.targetUserId) qs.set('targetUserId', params.targetUserId);
    if (params.appClass) qs.set('appClass', params.appClass);
    if (params.startDate) qs.set('startDate', params.startDate);
    if (params.endDate) qs.set('endDate', params.endDate);
    return `${API_BASE}/export/download?${qs.toString()}`;
}
