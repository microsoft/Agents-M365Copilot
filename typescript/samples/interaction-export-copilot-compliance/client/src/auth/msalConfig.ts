// ─── MSAL configuration for frontend auth ───

import { PublicClientApplication, type Configuration, LogLevel } from '@azure/msal-browser';

let msalInstance: PublicClientApplication | null = null;
let authConfig: { clientId: string; tenantId: string; redirectUri: string } | null = null;

export async function getAuthConfig() {
    if (authConfig) return authConfig;
    const res = await fetch('/api/auth/config');
    authConfig = await res.json();
    return authConfig!;
}

export async function getMsalInstance(): Promise<PublicClientApplication> {
    if (msalInstance) return msalInstance;

    const config = await getAuthConfig();

    const msalConfig: Configuration = {
        auth: {
            clientId: config.clientId,
            authority: `https://login.microsoftonline.com/${config.tenantId}`,
            redirectUri: config.redirectUri,
        },
        cache: {
            cacheLocation: 'sessionStorage',
        },
        system: {
            loggerOptions: {
                logLevel: LogLevel.Verbose,
                loggerCallback: (level, message) => {
                    console.log(`[MSAL ${LogLevel[level]}] ${message}`);
                },
            },
        },
    };

    msalInstance = new PublicClientApplication(msalConfig);
    await msalInstance.initialize();
    return msalInstance;
}

export const loginRequest = {
    scopes: ['openid', 'profile', 'email'],
};
