// ─── MSAL client-credentials authentication ───

import { ConfidentialClientApplication } from '@azure/msal-node';
import { createLogger } from './logger';

const log = createLogger('Auth');

let msalClient: ConfidentialClientApplication | null = null;

function getClient(): ConfidentialClientApplication {
    if (msalClient) return msalClient;

    const tenantId = process.env.TENANT_ID;
    const clientId = process.env.CLIENT_ID;
    const clientSecret = process.env.CLIENT_SECRET;

    if (!tenantId || !clientId || !clientSecret) {
        throw new Error('Missing TENANT_ID, CLIENT_ID, or CLIENT_SECRET in environment');
    }

    msalClient = new ConfidentialClientApplication({
        auth: {
            clientId,
            clientSecret,
            authority: `https://login.microsoftonline.com/${tenantId}`,
        },
    });

    log.info('MSAL confidential client initialised');
    return msalClient;
}

export async function getAccessToken(): Promise<string> {
    const client = getClient();
    const result = await client.acquireTokenByClientCredential({
        scopes: ['https://graph.microsoft.com/.default'],
    });

    if (!result?.accessToken) {
        throw new Error('Failed to acquire access token');
    }

    log.debug('Access token acquired');
    return result.accessToken;
}
