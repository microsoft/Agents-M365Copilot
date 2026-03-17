// ============================================================
// server.ts
// Webhook server to receive Microsoft Graph change notifications
// for Copilot AI interactions
// Docs: https://learn.microsoft.com/en-us/graph/change-notifications-overview
// ============================================================

import express, { Request, Response, NextFunction } from "express";
import crypto from "crypto";
import forge from "node-forge";
import fs from "fs";
import path from "path";
import dotenv from "dotenv";
import { createLogger } from "./logger";
import type { Server } from "http";

dotenv.config();

// ============================================================
// Loggers — one per logical area for easy filtering
// ============================================================
const log = createLogger("Server");
const notifLog = createLogger("Notification");
const cryptoLog = createLogger("Crypto");

// ============================================================
// Types & Interfaces
// ============================================================

/** Encrypted content payload from Microsoft Graph */
interface EncryptedContent {
    data: string;
    dataKey: string;
    dataSignature: string;
    encryptionCertificateId: string;
    encryptionCertificateThumbprint: string;
}

/** Resource data within a change notification */
interface ResourceData {
    id?: string;
    "@odata.type"?: string;
    [key: string]: unknown;
}

/** A single change notification from Microsoft Graph */
interface ChangeNotification {
    subscriptionId: string;
    changeType: string;
    resource: string;
    resourceData?: ResourceData;
    tenantId?: string;
    clientState?: string;
    encryptedContent?: EncryptedContent;
}

/** The notification payload wrapper */
interface NotificationPayload {
    value: ChangeNotification[];
}

/** Sender identity (user or application) */
interface IdentityInfo {
    id?: string;
    displayName?: string;
}

/** AI Interaction "from" field */
interface InteractionFrom {
    user?: IdentityInfo;
    application?: IdentityInfo;
}

/** Attachment within an AI interaction */
interface InteractionAttachment {
    name?: string;
    contentType: string;
    content?: string | Record<string, unknown>;
    contentUrl?: string;
}

/** Context reference in an AI interaction */
interface InteractionContext {
    displayName: string;
    contextType: string;
}

/** Body of an AI interaction */
interface InteractionBody {
    contentType: string;
    content?: string;
}

/** Decrypted AI Interaction resource
 *  @see https://learn.microsoft.com/en-us/graph/api/resources/aiinteraction
 */
interface AiInteraction {
    id: string;
    sessionId: string;
    interactionType: string;
    appClass: string;
    conversationType: string;
    createdDateTime: string;
    locale: string;
    from?: InteractionFrom;
    body?: InteractionBody;
    contexts?: InteractionContext[];
    attachments?: InteractionAttachment[];
}

/** Adaptive Card element (simplified) */
interface AdaptiveCardElement {
    type?: string;
    text?: string;
    altText?: string;
    title?: string;
    inlines?: Array<{ type?: string; text?: string }>;
    facts?: Array<{ title: string; value: string }>;
    body?: AdaptiveCardElement[];
    items?: AdaptiveCardElement[];
    columns?: Array<{ items?: AdaptiveCardElement[] }>;
    actions?: Array<{
        title?: string;
        card?: { body?: AdaptiveCardElement[] };
    }>;
    content?: string | Record<string, unknown>;
}

/** Adaptive Card structure */
interface AdaptiveCard {
    body?: AdaptiveCardElement[];
    actions?: Array<{ title?: string }>;
}

// ============================================================
// App Setup
// ============================================================

const app = express();
const PORT: number = parseInt(process.env.PORT || "3000", 10);

// Validate critical config early
if (isNaN(PORT) || PORT < 1 || PORT > 65535) {
    log.error("Invalid PORT value", { PORT: process.env.PORT });
    process.exit(1);
}

// Parse JSON bodies with a size limit and error handling
app.use(
    express.json({
        limit: "1mb",
        strict: true,
    })
);

// Handle JSON parse errors gracefully
app.use((err: Error & { type?: string; status?: number }, _req: Request, res: Response, next: NextFunction) => {
    if (err.type === "entity.parse.failed" || err.message?.includes("JSON")) {
        log.error("Malformed JSON in request body", { error: err.message });
        res.status(400).json({ error: "Invalid JSON in request body" });
        return;
    }
    next(err);
});

// Load private key for decrypting notification payloads
let privateKey: string | null = null;
const privateKeyPath: string = path.join(__dirname, "..", "certs", "private-key.pem");
try {
    if (fs.existsSync(privateKeyPath)) {
        privateKey = fs.readFileSync(privateKeyPath, "utf8");
        // Quick sanity check that the file looks like a PEM key
        if (!privateKey.includes("-----BEGIN")) {
            log.warn("Private key file does not appear to be in PEM format", { path: privateKeyPath });
            privateKey = null;
        } else {
            cryptoLog.info("Private key loaded for payload decryption", { path: privateKeyPath });
        }
    } else {
        cryptoLog.warn("No private key found — run 'npm run generate-cert' first", { expected: privateKeyPath });
    }
} catch (err) {
    const error = err as NodeJS.ErrnoException;
    cryptoLog.error("Failed to read private key file", {
        path: privateKeyPath,
        code: error.code,
        error: error.message,
    });
}

// ============================================================
// Health check endpoint
// ============================================================
app.get("/", (_req: Request, res: Response) => {
    res.json({
        status: "running",
        service: "Copilot AI Interaction Change Notifications Webhook",
        privateKeyLoaded: privateKey !== null,
        timestamp: new Date().toISOString(),
    });
});

// ============================================================
// Notification endpoint — receives change notifications
// @see https://learn.microsoft.com/en-us/graph/change-notifications-delivery-webhooks
// ============================================================
app.post("/api/notifications", (req: Request, res: Response) => {
    // ----------------------------------------------------------
    // Step 1: Handle validation request from Microsoft Graph
    // When you first create a subscription, Graph sends a
    // validation token that must be returned as plain text.
    // ----------------------------------------------------------
    const validationToken = req.query.validationToken as string | undefined;
    if (validationToken) {
        notifLog.info("Subscription validation request received", {
            tokenPreview: validationToken.substring(0, 50) + "...",
        });
        res.set("Content-Type", "text/plain");
        res.status(200).send(validationToken);
        return;
    }

    // ----------------------------------------------------------
    // Step 1b: Validate request body structure
    // ----------------------------------------------------------
    if (!req.body || !Array.isArray(req.body.value)) {
        notifLog.warn("Invalid notification payload — missing 'value' array", {
            bodyKeys: req.body ? Object.keys(req.body) : "(empty)",
        });
        res.status(400).json({ error: "Expected { value: [...] } payload" });
        return;
    }

    // ----------------------------------------------------------
    // Step 2: Process incoming notifications
    // ----------------------------------------------------------
    notifLog.separator();
    notifLog.info("CHANGE NOTIFICATION RECEIVED");

    const body = req.body as NotificationPayload;
    const notifications: ChangeNotification[] = body.value;

    if (!notifications || notifications.length === 0) {
        notifLog.warn("No notifications in payload");
        res.status(202).send();
        return;
    }

    notifications.forEach((notification: ChangeNotification, index: number) => {
        notifLog.info(`Processing notification ${index + 1} of ${notifications.length}`);

        // Validate required fields
        if (!notification.subscriptionId || !notification.changeType || !notification.resource) {
            notifLog.warn("Notification missing required fields — skipping", {
                hasSubscriptionId: !!notification.subscriptionId,
                hasChangeType: !!notification.changeType,
                hasResource: !!notification.resource,
            });
            return; // skip this notification, continue processing others
        }

        notifLog.details({
            "Subscription ID": notification.subscriptionId,
            "Change Type": notification.changeType,
            "Resource": notification.resource,
            "Resource ID": notification.resourceData?.id || "N/A",
            "OData Type": notification.resourceData?.["@odata.type"] || "N/A",
            "Tenant ID": notification.tenantId || "N/A",
        });

        // Verify client state for security
        if (notification.clientState) {
            const expectedPrefix = "copilot-ai-notifications-";
            if (!notification.clientState.startsWith(expectedPrefix)) {
                notifLog.warn("Unexpected client state value — notification may not be from our subscription", {
                    clientState: notification.clientState,
                });
            } else {
                notifLog.debug("Client state verified", { clientState: notification.clientState });
            }
        } else {
            notifLog.warn("No client state in notification — cannot verify origin");
        }

        // ----------------------------------------------------------
        // Step 3: Decrypt resource data if present
        // @see https://learn.microsoft.com/en-us/graph/change-notifications-with-resource-data
        // ----------------------------------------------------------
        if (notification.encryptedContent) {
            if (!privateKey) {
                cryptoLog.error("Cannot decrypt — private key not loaded. Run 'npm run generate-cert' and restart.");
                return;
            }

            // Validate encrypted content has required fields
            if (!notification.encryptedContent.data || !notification.encryptedContent.dataKey) {
                cryptoLog.error("Encrypted content missing required fields", {
                    hasData: !!notification.encryptedContent.data,
                    hasDataKey: !!notification.encryptedContent.dataKey,
                });
                return;
            }

            cryptoLog.info("Decrypting resource data...");
            try {
                const decrypted = decryptNotificationPayload(notification.encryptedContent);

                let aiInteraction: AiInteraction;
                try {
                    aiInteraction = JSON.parse(decrypted);
                } catch (parseErr) {
                    const pe = parseErr as Error;
                    cryptoLog.error("Decrypted payload is not valid JSON", {
                        error: pe.message,
                        preview: decrypted.substring(0, 100),
                    });
                    return;
                }

                if (!aiInteraction.id) {
                    notifLog.warn("Decrypted AI interaction is missing an ID — payload may be malformed");
                }

                notifLog.info("Decrypted AI Interaction");
                notifLog.details({
                    "ID": aiInteraction.id,
                    "Session ID": aiInteraction.sessionId,
                    "Interaction Type": aiInteraction.interactionType,
                    "App Class": aiInteraction.appClass,
                    "Conversation Type": aiInteraction.conversationType,
                    "Created": aiInteraction.createdDateTime,
                    "Locale": aiInteraction.locale,
                });

                // Log who sent it
                if (aiInteraction.from) {
                    if (aiInteraction.from.user) {
                        notifLog.info("From (User)", {
                            displayName: aiInteraction.from.user.displayName ?? undefined,
                            id: aiInteraction.from.user.id ?? undefined,
                        });
                    }
                    if (aiInteraction.from.application) {
                        notifLog.info("From (App)", {
                            displayName: aiInteraction.from.application.displayName ?? undefined,
                            id: aiInteraction.from.application.id ?? undefined,
                        });
                    }
                }

                // Log the content
                if (aiInteraction.body) {
                    const contentPreview = aiInteraction.body.content?.substring(0, 200) || "N/A";
                    notifLog.info("Interaction body", {
                        contentType: aiInteraction.body.contentType,
                        preview: contentPreview + ((aiInteraction.body.content?.length ?? 0) > 200 ? "..." : ""),
                    });
                }

                // Log contexts
                if (aiInteraction.contexts && aiInteraction.contexts.length > 0) {
                    notifLog.info(`Contexts (${aiInteraction.contexts.length})`);
                    aiInteraction.contexts.forEach((ctx: InteractionContext) => {
                        notifLog.debug("Context", { displayName: ctx.displayName, type: ctx.contextType });
                    });
                }

                // Log attachments & extract Adaptive Card content
                if (aiInteraction.attachments && aiInteraction.attachments.length > 0) {
                    notifLog.info(`Attachments (${aiInteraction.attachments.length})`);
                    aiInteraction.attachments.forEach(
                        (att: InteractionAttachment, attIdx: number) => {
                            notifLog.debug(`Attachment #${attIdx + 1}`, {
                                name: att.name || "(unnamed)",
                                contentType: att.contentType,
                            });

                            // Extract text from Adaptive Cards
                            if (
                                att.contentType === "application/vnd.microsoft.card.adaptive" &&
                                att.content
                            ) {
                                try {
                                    const card: AdaptiveCard =
                                        typeof att.content === "string"
                                            ? JSON.parse(att.content)
                                            : (att.content as unknown as AdaptiveCard);
                                    const extractedText = extractAdaptiveCardText(card);
                                    if (extractedText) {
                                        notifLog.info("Adaptive Card content:");
                                        notifLog.separator();
                                        extractedText.split("\n").forEach((line: string) => {
                                            if (line.trim()) {
                                                notifLog.info(`  ${line}`);
                                            }
                                        });
                                        notifLog.separator();
                                    } else {
                                        notifLog.warn("Adaptive Card parsed but no text content found");
                                    }
                                } catch (e) {
                                    const error = e as Error;
                                    notifLog.warn(`Could not parse Adaptive Card: ${error.message}`);
                                }
                            }

                            // Log reference/URL attachments
                            if (att.contentUrl) {
                                notifLog.debug("Attachment URL", { url: att.contentUrl });
                            }
                        }
                    );
                }
            } catch (err) {
                const error = err as Error;
                cryptoLog.error("Decryption failed", { error: error.message });
            }
        }
    });

    notifLog.separator();
    notifLog.blank();

    // Must return 202 Accepted to acknowledge receipt
    res.status(202).send();
});

// ============================================================
// 404 handler — catch requests to unknown routes
// ============================================================
app.use((_req: Request, res: Response) => {
    log.warn("Route not found", { method: _req.method, path: _req.path });
    res.status(404).json({ error: "Not found" });
});

// ============================================================
// Global Express error handler (must have 4 params)
// ============================================================
app.use((err: Error, _req: Request, res: Response, _next: NextFunction) => {
    log.error("Unhandled Express error", {
        error: err.message,
        stack: err.stack?.split("\n").slice(0, 3).join(" | "),
    });
    res.status(500).json({ error: "Internal server error" });
});

// ============================================================
// Extract readable text from Adaptive Card JSON
// Recursively walks the card body/actions to pull out all
// TextBlock, RichTextBlock, FactSet, and other text elements
// ============================================================
function extractAdaptiveCardText(card: AdaptiveCard): string {
    const lines: string[] = [];

    function walk(elements: AdaptiveCardElement[]): void {
        if (!Array.isArray(elements)) return;

        for (const el of elements) {
            if (!el || typeof el !== "object") continue;

            // TextBlock — most common text element
            if (el.type === "TextBlock" && el.text) {
                lines.push(el.text);
            }

            // RichTextBlock with inline text
            if (el.type === "RichTextBlock" && Array.isArray(el.inlines)) {
                for (const inline of el.inlines) {
                    if (inline.type === "TextRun" && inline.text) {
                        lines.push(inline.text);
                    }
                }
            }

            // FactSet — key/value pairs
            if (el.type === "FactSet" && Array.isArray(el.facts)) {
                for (const fact of el.facts) {
                    lines.push(`${fact.title}: ${fact.value}`);
                }
            }

            // Image with alt text
            if (el.type === "Image" && el.altText) {
                lines.push(`[Image: ${el.altText}]`);
            }

            // Recurse into containers, columns, etc.
            if (Array.isArray(el.body)) walk(el.body);
            if (Array.isArray(el.items)) walk(el.items);
            if (Array.isArray(el.columns)) {
                for (const col of el.columns) {
                    if (Array.isArray(col.items)) walk(col.items);
                }
            }
            if (Array.isArray(el.actions)) {
                for (const action of el.actions) {
                    if (action.title) lines.push(`[Action: ${action.title}]`);
                    if (action.card && Array.isArray(action.card.body)) {
                        walk(action.card.body);
                    }
                }
            }
        }
    }

    // Start walking from body, then top-level actions
    if (Array.isArray(card.body)) walk(card.body);
    if (Array.isArray(card.actions)) {
        for (const action of card.actions) {
            if (action.title) lines.push(`[Action: ${action.title}]`);
        }
    }

    return lines.join("\n");
}

// ============================================================
// Decrypt the encrypted notification payload
// Per Microsoft docs:
//   1. Decrypt dataKey with RSA-OAEP → symmetric key
//   2. Validate HMAC-SHA256(data) == dataSignature
//   3. Decrypt data with AES-256-CBC
//      - Key = decrypted symmetric key
//      - IV  = first 16 bytes of the symmetric key
//      - Padding = PKCS7
// @see https://learn.microsoft.com/en-us/graph/change-notifications-with-resource-data#decrypting-resource-data-from-change-notifications
// ============================================================
function decryptNotificationPayload(encryptedContent: EncryptedContent): string {
    if (!privateKey) {
        throw new Error("Private key not loaded. Run 'npm run generate-cert' first.");
    }

    // Step 1: Decrypt the symmetric key using RSA-OAEP with the private key
    let forgePrivateKey: forge.pki.rsa.PrivateKey;
    try {
        forgePrivateKey = forge.pki.privateKeyFromPem(privateKey);
    } catch (err) {
        const e = err as Error;
        throw new Error(`Failed to parse private key PEM: ${e.message}`);
    }

    let decryptedSymmetricKeyRaw: string;
    try {
        decryptedSymmetricKeyRaw = forgePrivateKey.decrypt(
            forge.util.decode64(encryptedContent.dataKey),
            "RSA-OAEP",
            {
                md: forge.md.sha1.create(),
                mgf1: { md: forge.md.sha1.create() },
            }
        );
    } catch (err) {
        const e = err as Error;
        throw new Error(
            `RSA-OAEP decryption of symmetric key failed. This usually means the certificate ` +
            `used for the subscription does not match the current private key. ` +
            `Re-generate the cert and re-create the subscription. Detail: ${e.message}`
        );
    }

    // Convert the decrypted symmetric key to a Buffer
    const symmetricKeyBytes: Buffer = Buffer.from(decryptedSymmetricKeyRaw, "binary");
    cryptoLog.debug("Symmetric key decrypted", { lengthBytes: symmetricKeyBytes.length });

    // Step 2: Validate HMAC-SHA256 signature (if dataSignature is present)
    if (encryptedContent.dataSignature) {
        const hmac = crypto.createHmac("sha256", symmetricKeyBytes);
        hmac.update(Buffer.from(encryptedContent.data, "base64"));
        const computedSignature: string = hmac.digest("base64");

        if (computedSignature !== encryptedContent.dataSignature) {
            throw new Error(
                "HMAC-SHA256 signature mismatch — the notification payload may have been tampered with. " +
                "This could also indicate a key mismatch. Re-generate the certificate and re-create the subscription."
            );
        } else {
            cryptoLog.info("HMAC signature verified");
        }
    } else {
        cryptoLog.warn("No dataSignature in encrypted content — cannot verify integrity");
    }

    // Step 3: Decrypt the data using AES-256-CBC
    // IV = first 16 bytes of the decrypted symmetric key (per Microsoft docs)
    const iv: Buffer = symmetricKeyBytes.slice(0, 16);
    const encryptedData: Buffer = Buffer.from(encryptedContent.data, "base64");

    try {
        const decipher = crypto.createDecipheriv("aes-256-cbc", symmetricKeyBytes, iv);
        decipher.setAutoPadding(true); // PKCS7 padding
        let decrypted: string = decipher.update(encryptedData, undefined, "utf8");
        decrypted += decipher.final("utf8");
        return decrypted;
    } catch (err) {
        const e = err as Error;
        throw new Error(
            `AES-256-CBC decryption failed. The symmetric key length is ${symmetricKeyBytes.length} bytes ` +
            `(expected 32). Detail: ${e.message}`
        );
    }
}

// ============================================================
// Lifecycle notification endpoint (for subscriptions > 1 hour)
// @see https://learn.microsoft.com/en-us/graph/change-notifications-lifecycle-events
// ============================================================
app.post("/api/lifecycle", (req: Request, res: Response) => {
    const validationToken = req.query.validationToken as string | undefined;
    if (validationToken) {
        notifLog.info("Lifecycle validation request received");
        res.set("Content-Type", "text/plain");
        res.status(200).send(validationToken);
        return;
    }

    notifLog.info("LIFECYCLE NOTIFICATION RECEIVED", req.body as Record<string, unknown>);

    res.status(202).send();
});

// ============================================================
// Start the server
// ============================================================
let server: Server;

try {
    server = app.listen(PORT, () => {
        log.separator();
        log.info("Copilot AI Interaction — Change Notifications Webhook");
        log.separator();
        log.blank();
        log.info(`Server running on http://localhost:${PORT}`);
        log.details({
            "Notification endpoint": `http://localhost:${PORT}/api/notifications`,
            "Health check": `http://localhost:${PORT}/`,
        });
        log.blank();
        log.info("Next steps:");
        log.details({
            "1": `Start a dev tunnel: devtunnel host -p ${PORT} --allow-anonymous`,
            "2": "Update NOTIFICATION_URL in .env with the tunnel URL",
            "3": "Run: npm run create-subscription",
        });
        log.separator();
        log.blank();
    });

    server.on("error", (err: NodeJS.ErrnoException) => {
        if (err.code === "EADDRINUSE") {
            log.error(`Port ${PORT} is already in use. Stop the other process or use a different PORT in .env.`);
        } else if (err.code === "EACCES") {
            log.error(`Permission denied for port ${PORT}. Try a port > 1024 or run with elevated privileges.`);
        } else {
            log.error("Server error", { code: err.code, error: err.message });
        }
        process.exit(1);
    });
} catch (err) {
    const error = err as Error;
    log.error("Failed to start server", { error: error.message });
    process.exit(1);
}

// ============================================================
// Graceful shutdown — clean up on SIGINT / SIGTERM
// ============================================================
function shutdown(signal: string): void {
    log.info(`Received ${signal} — shutting down gracefully...`);
    server?.close(() => {
        log.info("Server closed. Goodbye.");
        process.exit(0);
    });
    // Force exit if close takes too long
    setTimeout(() => {
        log.warn("Graceful shutdown timed out — forcing exit");
        process.exit(1);
    }, 5000);
}

process.on("SIGINT", () => shutdown("SIGINT"));
process.on("SIGTERM", () => shutdown("SIGTERM"));

// ============================================================
// Catch-all handlers for truly unexpected errors
// ============================================================
process.on("unhandledRejection", (reason: unknown) => {
    log.error("Unhandled promise rejection", {
        reason: reason instanceof Error ? reason.message : String(reason),
        stack: reason instanceof Error ? reason.stack?.split("\n").slice(0, 3).join(" | ") : undefined,
    });
});

process.on("uncaughtException", (err: Error) => {
    log.error("Uncaught exception — process will exit", {
        error: err.message,
        stack: err.stack?.split("\n").slice(0, 3).join(" | "),
    });
    process.exit(1);
});
