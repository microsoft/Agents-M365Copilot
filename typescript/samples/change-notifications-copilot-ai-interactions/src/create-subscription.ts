// ============================================================
// create-subscription.ts
// Creates a Microsoft Graph subscription for Copilot AI
// interaction change notifications
//
// Docs:
//   Subscription API  : https://learn.microsoft.com/en-us/graph/api/subscription-post-subscriptions
//   AI Interaction     : https://learn.microsoft.com/en-us/graph/api/resources/aiinteraction
//   Encrypted content  : https://learn.microsoft.com/en-us/graph/change-notifications-with-resource-data
// ============================================================

import dotenv from "dotenv";
import { ClientSecretCredential } from "@azure/identity";
import { Client } from "@microsoft/microsoft-graph-client";
import {
    TokenCredentialAuthenticationProvider,
} from "@microsoft/microsoft-graph-client/authProviders/azureTokenCredentials";
import fs from "fs";
import path from "path";
import { createLogger } from "./logger";

dotenv.config();

const log = createLogger("Subscription");

// ============================================================
// Types
// ============================================================

/** Shape of the subscription request body sent to Microsoft Graph */
interface SubscriptionRequest {
    changeType: string;
    notificationUrl: string;
    resource: string;
    includeResourceData: boolean;
    encryptionCertificate: string;
    encryptionCertificateId: string;
    expirationDateTime: string;
    clientState: string;
}

/** Shape of the subscription response from Microsoft Graph */
interface SubscriptionResponse {
    id: string;
    resource: string;
    changeType: string;
    expirationDateTime: string;
    notificationUrl: string;
    clientState: string;
}

/** Graph API error shape */
interface GraphError extends Error {
    statusCode?: number;
    body?: string | { error?: { code?: string; message?: string } };
}

// ============================================================
// Main
// ============================================================

async function createSubscription(): Promise<void> {
    log.separator();
    log.info("Creating Copilot AI Interaction Subscription");
    log.separator();

    // ----------------------------------------------------------
    // Validate environment variables
    // ----------------------------------------------------------
    const requiredVars: string[] = [
        "TENANT_ID",
        "CLIENT_ID",
        "CLIENT_SECRET",
        "NOTIFICATION_URL",
        "USER_ID",
    ];
    const missing: string[] = requiredVars.filter(
        (v) => !process.env[v] || process.env[v]!.startsWith("your-")
    );

    if (missing.length > 0) {
        log.error("Missing or placeholder environment variables", {
            missing: missing.join(", "),
        });
        log.info("Please update your .env file with actual values.");
        process.exit(1);
    }

    // ----------------------------------------------------------
    // Load encryption certificate
    // ----------------------------------------------------------
    const certPath: string = path.join(__dirname, "..", "certs", "certificate-base64.txt");
    if (!fs.existsSync(certPath)) {
        log.error("Encryption certificate not found — run 'npm run generate-cert' first", {
            expected: certPath,
        });
        process.exit(1);
    }

    let base64Certificate: string;
    try {
        base64Certificate = fs.readFileSync(certPath, "utf8").trim();
    } catch (readErr) {
        const e = readErr as NodeJS.ErrnoException;
        log.error("Failed to read encryption certificate", {
            path: certPath,
            code: e.code,
            error: e.message,
        });
        process.exit(1);
    }

    if (!base64Certificate || base64Certificate.length < 100) {
        log.error("Encryption certificate appears empty or invalid", {
            path: certPath,
            sizeChars: base64Certificate.length,
        });
        process.exit(1);
    }

    log.info("Encryption certificate loaded", { path: certPath });

    // ----------------------------------------------------------
    // Create Graph client with application credentials
    // @see https://learn.microsoft.com/en-us/graph/sdks/choose-authentication-providers#client-credentials-provider
    // ----------------------------------------------------------
    let graphClient: Client;
    try {
        const credential = new ClientSecretCredential(
            process.env.TENANT_ID!,
            process.env.CLIENT_ID!,
            process.env.CLIENT_SECRET!
        );

        const authProvider = new TokenCredentialAuthenticationProvider(credential, {
            scopes: ["https://graph.microsoft.com/.default"],
        });

        graphClient = Client.initWithMiddleware({ authProvider });
        log.info("Graph client initialized");
    } catch (authErr) {
        const e = authErr as Error;
        log.error("Failed to initialise Graph client or authentication credentials", {
            error: e.message,
        });
        log.warn("Verify TENANT_ID, CLIENT_ID, and CLIENT_SECRET in your .env file");
        process.exit(1);
    }

    // ----------------------------------------------------------
    // Build subscription request
    // @see https://learn.microsoft.com/en-us/graph/api/subscription-post-subscriptions
    // ----------------------------------------------------------
    const userId: string = process.env.USER_ID!;
    const notificationUrl: string = process.env.NOTIFICATION_URL!;
    const certId: string =
        process.env.ENCRYPTION_CERTIFICATE_ID || "copilot-change-notifications-cert";

    // Expiration: 1 hour from now (max without lifecycleNotificationUrl)
    const expirationDateTime = new Date();
    expirationDateTime.setHours(expirationDateTime.getHours() + 1);

    const subscription: SubscriptionRequest = {
        changeType: "created,updated,deleted",
        notificationUrl,
        resource: `/copilot/users/${userId}/interactionHistory/getAllEnterpriseInteractions`,
        includeResourceData: true,
        encryptionCertificate: base64Certificate,
        encryptionCertificateId: certId,
        expirationDateTime: expirationDateTime.toISOString(),
        clientState: "copilot-ai-notifications-" + Date.now(),
    };

    log.info("Subscription request");
    log.details({
        "User ID": userId,
        "Resource": subscription.resource,
        "Change Types": subscription.changeType,
        "Notification URL": notificationUrl,
        "Include Data": String(subscription.includeResourceData),
        "Expires": subscription.expirationDateTime,
    });

    // ----------------------------------------------------------
    // Create the subscription via Microsoft Graph
    // ----------------------------------------------------------
    try {
        log.info("Creating subscription via Microsoft Graph...");
        const result: SubscriptionResponse = await graphClient
            .api("/subscriptions")
            .post(subscription);

        log.info("Subscription created successfully");
        log.details({
            "ID": result.id,
            "Resource": result.resource,
            "Change Type": result.changeType,
            "Expiration": result.expirationDateTime,
            "Notification URL": result.notificationUrl,
            "Client State": result.clientState,
        });

        // Save subscription ID for later reference
        const infoPath = path.join(__dirname, "..", "subscription-info.json");
        try {
            fs.writeFileSync(infoPath, JSON.stringify(result, null, 2));
            log.info("Subscription details saved", { file: "subscription-info.json" });
        } catch (writeErr) {
            const we = writeErr as NodeJS.ErrnoException;
            log.warn("Subscription created but failed to save info file", {
                path: infoPath,
                code: we.code,
                error: we.message,
            });
        }
    } catch (err) {
        const error = err as GraphError;
        log.error("Failed to create subscription", {
            status: error.statusCode || "Unknown",
            message: error.message,
        });

        if (error.body) {
            try {
                const errorBody =
                    typeof error.body === "string" ? JSON.parse(error.body) : error.body;
                log.error("Graph API error details", {
                    code: errorBody.error?.code || "Unknown",
                    detail: errorBody.error?.message || "No details",
                });
            } catch {
                log.error("Raw error body", { body: String(error.body) });
            }
        }

        log.warn("Common issues:");
        log.details({
            "Permission": "Ensure app has 'AiEnterpriseInteraction.Read.User' or '.Read.All'",
            "Admin consent": "Ensure admin consent has been granted",
            "Notification URL": "Ensure the URL is publicly accessible (dev tunnel running)",
            "Copilot license": "Ensure the target user has a Microsoft 365 Copilot Chat license",
        });

        process.exit(1);
    }
}

createSubscription().catch((err: Error) => {
    log.error("Unexpected error during subscription creation", {
        error: err.message,
        stack: err.stack?.split("\n").slice(0, 3).join(" | "),
    });
    process.exit(1);
});
