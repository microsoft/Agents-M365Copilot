# Copilot AI Interaction — Change Notifications (TypeScript)

A TypeScript sample that subscribes to [Get change notifications for Copilot AI interactions using Microsoft Graph](https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/api/ai-services/change-notifications/aiinteraction-changenotifications) for **Microsoft 365 Copilot AI interactions** and decrypts the encrypted resource data in real time using a local webhook server with [Dev Tunnels](https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/overview).




## Key documentation

| Topic | Link |
|---|---|
| Create subscription (POST) | <https://learn.microsoft.com/en-us/graph/api/subscription-post-subscriptions> |
| Notifications with resource data | <https://learn.microsoft.com/en-us/graph/change-notifications-with-resource-data> |
| Decrypt resource data | <https://learn.microsoft.com/en-us/graph/change-notifications-with-resource-data#decrypting-resource-data-from-change-notifications> |
| Lifecycle notifications | <https://learn.microsoft.com/en-us/graph/change-notifications-lifecycle-events> |
| `aiInteraction` resource type | <https://learn.microsoft.com/en-us/graph/api/resources/aiinteraction> |
| Copilot APIs overview | <https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/copilot-apis-overview> |
| Dev Tunnels quickstart | <https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/get-started> |
| Register an Entra app | <https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app> |
| Graph SDKs — Auth providers | <https://learn.microsoft.com/en-us/graph/sdks/choose-authentication-providers> |

---

## Prerequisites

- [Node.js](https://nodejs.org/) v18 or later
- [VS Code Dev Tunnels CLI](https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/get-started) (or the VS Code Dev Tunnels extension)
- A [Microsoft Entra app registration](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app) with:
  - **Application permission**: `AiEnterpriseInteraction.Read.User` _or_ `AiEnterpriseInteraction.Read.All`
  - Admin consent granted
- A target user with a **Microsoft 365 Copilot Chat license**

---

## Project structure

```
├── src/
│   ├── server.ts                  # Express webhook server
│   ├── create-subscription.ts     # Creates Graph subscription
│   ├── generate-certificate.ts    # Generates self-signed cert for encryption
│   └── logger.ts                  # Structured logger utility (levels, timestamps, component tags)
├── certs/                         # Generated certificates (git-ignored)
├── .env.example                   # Template for environment variables
├── .gitignore
├── package.json
├── tsconfig.json
└── README.md
```

---

## Getting started

### 1. Install dependencies

```bash
npm install
```

### 2. Install Dev Tunnels CLI

```bash
# Windows (winget)
winget install Microsoft.devtunnel

# Or download manually:
# https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/get-started
```

### 3. Log in to Dev Tunnels

```bash
devtunnel user login
```

### 4. Generate the encryption certificate

Because notifications include encrypted resource data, a certificate is required:

```bash
npm run generate-cert
```

This creates three files under `certs/`:

| File | Purpose |
|---|---|
| `certificate.pem` | PEM certificate |
| `private-key.pem` | Private key used to decrypt payloads |
| `certificate-base64.txt` | Base64 DER certificate sent in the subscription request |

### 5. Register an app in Microsoft Entra

1. Open the [Microsoft Entra admin center](https://entra.microsoft.com).
2. Go to **App registrations** → **New registration**.
3. Name: e.g. `Copilot Change Notifications` / Single tenant.
4. Click **Register**.

#### Add API permissions

1. **API permissions** → **Add a permission** → **Microsoft Graph** → **Application permissions**.
2. Search for `AiEnterpriseInteraction.Read.User` or `AiEnterpriseInteraction.Read.All`.
3. **Add permissions** → **Grant admin consent**.

> See [Register an application](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app) for full instructions.

#### Create a client secret

1. **Certificates & secrets** → **New client secret**.
2. Copy the **Value** — you will need it for `.env`.

### 6. Configure environment variables

Copy `.env.example` to `.env` and fill in your values:

```bash
cp .env.example .env
```

```env
TENANT_ID=<your-tenant-id>
CLIENT_ID=<your-client-id>
CLIENT_SECRET=<your-client-secret>
USER_ID=<target-user-object-id>
PORT=3000
NOTIFICATION_URL=https://<your-tunnel>.devtunnels.ms/api/notifications
ENCRYPTION_CERTIFICATE_ID=copilot-change-notifications-cert
```

### 7. Start the webhook server

```bash
npm start
```

Expected output:

```
🚀 Server running on http://localhost:3000
📡 Notification endpoint: http://localhost:3000/api/notifications
```

### 8. Create a Dev Tunnel

In a **new terminal**:

```bash
devtunnel host -p 3000 --allow-anonymous
```

Copy the tunnel URL (e.g. `https://abc123xyz-3000.devtunnels.ms`).

### 9. Update `.env` with the tunnel URL

```env
NOTIFICATION_URL=https://abc123xyz-3000.devtunnels.ms/api/notifications
```

Restart the server after updating.

### 10. Create the Graph subscription

```bash
npm run create-subscription
```

On success you will see:

```
✅ Subscription created successfully!
   ID: <subscription-id>
   Expiration: <1 hour from now>
```

---

## How it works

```
┌──────────────┐       ┌─────────────────┐       ┌─────────────────┐
│   Target     │       │   Microsoft 365  │       │  Microsoft      │
│   User       │──────▶│   Copilot        │──────▶│  Graph          │
│              │ asks  │   (AI)           │ logs  │  (Subscription) │
└──────────────┘       └─────────────────┘       └────────┬────────┘
                                                          │
                                                          │ POST notification
                                                          ▼
                       ┌─────────────────┐       ┌─────────────────┐
                       │  Your Local     │◀──────│   Dev Tunnel    │
                       │  Webhook Server │       │   (public URL)  │
                       │  (localhost:3000)│       │                 │
                       └─────────────────┘       └─────────────────┘
```

1. **User prompt** → Copilot receives the query → a `created` notification is sent.
2. **Copilot response** → another `created` notification is sent.
3. Each notification contains the full **encrypted** [`aiInteraction`](https://learn.microsoft.com/en-us/graph/api/resources/aiinteraction) payload.
4. The server decrypts it using the private key and logs the interaction details.

---

## Subscription details

| Property | Value |
|---|---|
| **Resource** | `/copilot/users/{userId}/interactionHistory/getAllEnterpriseInteractions` |
| **Change Types** | `created`, `updated`, `deleted` |
| **Include Resource Data** | `true` (encrypted) |
| **Max Expiration** | 1 hour (without `lifecycleNotificationUrl`) |
| **Required Permission** | `AiEnterpriseInteraction.Read.User` or `.Read.All` |

---

## Important notes

- **Subscriptions expire in 1 hour.** Re-run `npm run create-subscription` to renew.
- **Dev Tunnel must be running** when creating the subscription — Graph validates the URL on creation.
- **Keep the server running** — if Graph cannot reach the webhook, notifications are dropped.
- The `clientState` property is used to verify that incoming notifications belong to your subscription.

---

## Troubleshooting

| Issue | Solution |
|---|---|
| Subscription creation fails with **403** | Ensure `AiEnterpriseInteraction.Read.User` permission is granted with admin consent |
| Validation error on creation | Ensure the dev tunnel is running and the URL is correct |
| `lifecycleNotificationUrl required` | Your expiration is >1 hour; reduce it or add a lifecycle URL |
| No notifications received | Ensure the target user has a Copilot Chat license and is actively using Copilot |
| Decryption fails | Re-generate the certificate (`npm run generate-cert`) and re-create the subscription |

---

## Related resources

- [Microsoft 365 Copilot APIs Client Libraries (Agents-M365Copilot)](https://github.com/microsoft/Agents-M365Copilot)
- [Microsoft Graph change notifications documentation](https://learn.microsoft.com/en-us/graph/change-notifications-overview)
