// ─── JWT validation middleware for Entra ID tokens ───

import type { Request, Response, NextFunction } from 'express';
import jwt from 'jsonwebtoken';
import jwksClient from 'jwks-rsa';
import { createLogger } from './logger';

const log = createLogger('AuthMiddleware');

const tenantId = process.env.TENANT_ID!;
const clientId = process.env.CLIENT_ID!;

const jwks = jwksClient({
    jwksUri: `https://login.microsoftonline.com/${tenantId}/discovery/v2.0/keys`,
    cache: true,
    rateLimit: true,
});

function getSigningKey(header: jwt.JwtHeader, callback: jwt.SigningKeyCallback): void {
    jwks.getSigningKey(header.kid, (err, key) => {
        if (err) return callback(err);
        callback(null, key?.getPublicKey());
    });
}

export interface AuthenticatedRequest extends Request {
    user?: {
        oid: string;
        name: string;
        email: string;
        roles: string[];
    };
}

export const ROLES = {
    ADMIN: 'ComplianceAdmin',
    VIEWER: 'ComplianceViewer',
} as const;

/**
 * Validates the Bearer token from Entra ID.
 * Extracts user info and app roles from the JWT claims.
 */
export function requireAuth(req: AuthenticatedRequest, res: Response, next: NextFunction): void {
    const authHeader = req.headers.authorization;
    if (!authHeader?.startsWith('Bearer ')) {
        res.status(401).json({ error: 'Missing or invalid Authorization header' });
        return;
    }

    const token = authHeader.substring(7);

    jwt.verify(
        token,
        getSigningKey,
        {
            audience: clientId,
            issuer: [
                `https://login.microsoftonline.com/${tenantId}/v2.0`,
                `https://sts.windows.net/${tenantId}/`,
            ],
            algorithms: ['RS256'],
        },
        (err, decoded) => {
            if (err) {
                log.warn(`Token validation failed: ${err.message}`);
                res.status(401).json({ error: 'Invalid or expired token' });
                return;
            }

            const claims = decoded as Record<string, unknown>;
            req.user = {
                oid: (claims.oid as string) ?? '',
                name: (claims.name as string) ?? '',
                email: (claims.preferred_username as string) ?? (claims.upn as string) ?? '',
                roles: (claims.roles as string[]) ?? [],
            };

            log.debug(`Authenticated: ${req.user.name} (${req.user.email}), roles: [${req.user.roles.join(', ')}]`);
            next();
        },
    );
}

/**
 * Requires the user to have at least one of the specified roles.
 */
export function requireRole(...allowedRoles: string[]) {
    return (req: AuthenticatedRequest, res: Response, next: NextFunction): void => {
        const userRoles = req.user?.roles ?? [];
        const hasRole = allowedRoles.some((r) => userRoles.includes(r));
        if (!hasRole) {
            log.warn(`Access denied for ${req.user?.email}: needs [${allowedRoles.join(', ')}], has [${userRoles.join(', ')}]`);
            res.status(403).json({ error: 'Insufficient permissions' });
            return;
        }
        next();
    };
}
