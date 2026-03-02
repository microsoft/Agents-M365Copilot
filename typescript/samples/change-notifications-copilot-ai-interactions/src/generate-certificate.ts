// ============================================================
// generate-certificate.ts
// Generates a self-signed certificate for encrypting
// change notification resource data from Microsoft Graph
//
// Docs: https://learn.microsoft.com/en-us/graph/change-notifications-with-resource-data#setting-up-certificate-and-decryption-keys
// ============================================================

import forge from "node-forge";
import fs from "fs";
import path from "path";
import { createLogger } from "./logger";

const log = createLogger("Certificate");

function generateCertificate(): void {
    log.info("Generating self-signed certificate for change notification encryption...");

    // ----------------------------------------------------------
    // Step 1: Generate RSA key pair
    // ----------------------------------------------------------
    let keys: forge.pki.rsa.KeyPair;
    try {
        keys = forge.pki.rsa.generateKeyPair(2048);
    } catch (err) {
        const e = err as Error;
        log.error("Failed to generate RSA key pair", { error: e.message });
        process.exit(1);
    }

    // ----------------------------------------------------------
    // Step 2: Create a self-signed certificate
    // ----------------------------------------------------------
    let cert: forge.pki.Certificate;
    try {
        cert = forge.pki.createCertificate();
        cert.publicKey = keys.publicKey;
        cert.serialNumber = "01";
        cert.validity.notBefore = new Date();
        cert.validity.notAfter = new Date();
        cert.validity.notAfter.setFullYear(cert.validity.notAfter.getFullYear() + 1);

        const attrs: forge.pki.CertificateField[] = [
            { name: "commonName", value: "Copilot Change Notifications" },
            { name: "organizationName", value: "Development" },
            { name: "countryName", value: "US" },
        ];

        cert.setSubject(attrs);
        cert.setIssuer(attrs);
        cert.sign(keys.privateKey, forge.md.sha256.create());
    } catch (err) {
        const e = err as Error;
        log.error("Failed to create self-signed certificate", { error: e.message });
        process.exit(1);
    }

    // Convert to PEM format
    const certPem: string = forge.pki.certificateToPem(cert);
    const privateKeyPem: string = forge.pki.privateKeyToPem(keys.privateKey);

    // ----------------------------------------------------------
    // Step 3: Save certificate and private key to disk
    // ----------------------------------------------------------
    const certsDir: string = path.join(__dirname, "..", "certs");
    try {
        if (!fs.existsSync(certsDir)) {
            fs.mkdirSync(certsDir, { recursive: true });
        }
    } catch (err) {
        const e = err as NodeJS.ErrnoException;
        log.error("Failed to create certs directory", {
            path: certsDir,
            code: e.code,
            error: e.message,
        });
        process.exit(1);
    }

    const filesToWrite: Array<{ name: string; content: string }> = [
        { name: "certificate.pem", content: certPem },
        { name: "private-key.pem", content: privateKeyPem },
    ];

    // Get base64-encoded certificate (without PEM headers) for the subscription request
    let base64Cert: string;
    try {
        base64Cert = forge.util.encode64(
            forge.asn1.toDer(forge.pki.certificateToAsn1(cert)).getBytes()
        );
        filesToWrite.push({ name: "certificate-base64.txt", content: base64Cert });
    } catch (err) {
        const e = err as Error;
        log.error("Failed to encode certificate to base64 DER", { error: e.message });
        process.exit(1);
    }

    for (const file of filesToWrite) {
        const filePath = path.join(certsDir, file.name);
        try {
            fs.writeFileSync(filePath, file.content);
        } catch (err) {
            const e = err as NodeJS.ErrnoException;
            log.error(`Failed to write ${file.name}`, {
                path: filePath,
                code: e.code,
                error: e.message,
            });
            process.exit(1);
        }
    }

    // ----------------------------------------------------------
    // Step 4: Compute thumbprint and report success
    // ----------------------------------------------------------
    let thumbprint: string;
    try {
        const md = forge.md.sha1.create();
        md.update(forge.asn1.toDer(forge.pki.certificateToAsn1(cert)).getBytes());
        thumbprint = md.digest().toHex();
    } catch (err) {
        const e = err as Error;
        log.warn("Certificate saved but failed to compute thumbprint", { error: e.message });
        thumbprint = "(unavailable)";
    }

    log.info("Certificate generated successfully");
    log.info("Files created in ./certs/ directory");
    log.details({
        "certificate.pem": "PEM certificate",
        "private-key.pem": "Private key for decryption",
        "certificate-base64.txt": "Base64 cert for subscription request",
    });
    log.info("Certificate metadata");
    log.details({
        "Thumbprint": thumbprint,
        "Certificate ID": "copilot-change-notifications-cert",
    });
}

try {
    generateCertificate();
} catch (err) {
    const e = err as Error;
    log.error("Unexpected error during certificate generation", {
        error: e.message,
        stack: e.stack?.split("\n").slice(0, 3).join(" | "),
    });
    process.exit(1);
}
