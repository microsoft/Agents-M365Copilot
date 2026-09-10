// ─── Auth context: exposes user info, roles, and token acquisition ───

import { createContext, useContext, useCallback, useState, useEffect, type ReactNode } from 'react';
import { useMsal, useIsAuthenticated } from '@azure/msal-react';
import { InteractionRequiredAuthError } from '@azure/msal-browser';
import { loginRequest } from './msalConfig';

interface AuthUser {
    oid: string;
    name: string;
    email: string;
    roles: string[];
}

interface AuthContextValue {
    user: AuthUser | null;
    isAdmin: boolean;
    isViewer: boolean;
    loading: boolean;
    getToken: () => Promise<string>;
    login: () => void;
    logout: () => void;
}

const AuthContext = createContext<AuthContextValue>({
    user: null,
    isAdmin: false,
    isViewer: false,
    loading: true,
    getToken: async () => '',
    login: () => { },
    logout: () => { },
});

export function useAuth() {
    return useContext(AuthContext);
}

export function AuthProvider({ children }: { children: ReactNode }) {
    const { instance, accounts } = useMsal();
    const isAuthenticated = useIsAuthenticated();
    const [user, setUser] = useState<AuthUser | null>(null);
    const [loading, setLoading] = useState(true);

    const getToken = useCallback(async (): Promise<string> => {
        if (!accounts[0]) throw new Error('Not authenticated');
        try {
            const response = await instance.acquireTokenSilent({
                ...loginRequest,
                account: accounts[0],
            });
            return response.idToken;
        } catch (err) {
            if (err instanceof InteractionRequiredAuthError) {
                await instance.acquireTokenRedirect(loginRequest);
                return ''; // won't reach here — page will redirect
            }
            throw err;
        }
    }, [instance, accounts]);

    const login = useCallback(() => {
        instance.loginRedirect(loginRequest).catch(console.error);
    }, [instance]);

    const logout = useCallback(() => {
        instance.logoutRedirect().catch(console.error);
    }, [instance]);

    useEffect(() => {
        if (!isAuthenticated || !accounts[0]) {
            setUser(null);
            setLoading(false);
            return;
        }

        (async () => {
            try {
                const token = await getToken();
                const res = await fetch('/api/auth/me', {
                    headers: { Authorization: `Bearer ${token}` },
                });
                if (res.ok) {
                    setUser(await res.json());
                }
            } catch (err) {
                console.error('Failed to fetch user info:', err);
            } finally {
                setLoading(false);
            }
        })();
    }, [isAuthenticated, accounts, getToken]);

    const isAdmin = user?.roles.includes('ComplianceAdmin') ?? false;
    const isViewer = user?.roles.includes('ComplianceViewer') ?? false;

    return (
        <AuthContext.Provider value={{ user, isAdmin, isViewer, loading, getToken, login, logout }}>
            {children}
        </AuthContext.Provider>
    );
}
