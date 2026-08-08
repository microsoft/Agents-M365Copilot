# Copilot Interaction Export API — Compliance Dashboard (TypeScript)

A TypeScript sample that uses the [Copilot Activity Export API](https://learn.microsoft.com/en-us/microsoftteams/export-teams-content-copilot) (`getAllEnterpriseInteractions`) to pull, archive, and visualise Microsoft 365 Copilot AI interactions for compliance and audit purposes.

Unlike the [`change-notifications-copilot-ai-interactions`](https://github.com/microsoft/Agents-M365Copilot/tree/main/typescript/samples/change-notifications-copilot-ai-interactions) sample (real-time push via Graph change notifications), this sample uses an **on-demand pull model** — exporting interactions via the Microsoft Graph REST API, storing them in a local SQLite database, and surfacing them through a React compliance dashboard.

> 💡 **Companion sample**: For a push-based, near real-time approach using webhooks, see [change-notifications-copilot-ai-interactions](https://github.com/microsoft/Agents-M365Copilot/tree/main/typescript/samples/change-notifications-copilot-ai-interactions).

## Key documentation

| Topic | Link |
|-------|------|
| Copilot Interaction Export overview | https://learn.microsoft.com/en-us/microsoftteams/export-teams-content-copilot |
| `aiInteractionHistory: getAllEnterpriseInteractions` | https://learn.microsoft.com/en-us/graph/api/aiinteractionhistory-getallenterpriseinteractions |
| `aiInteraction` resource type | https://learn.microsoft.com/en-us/graph/api/resources/aiinteraction |
| Copilot APIs overview | https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/copilot-apis-overview |
| Register an Entra app | https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app |

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│    Compliance Dashboard (React + Vite + Tailwind + MSAL)        │
│  ┌──────────┐  ┌──────────────┐  ┌────────────┐  ┌──────────┐  │
│  │ Overview │  │ Interactions │  │  Sessions  │  │ Download │
│  │  Stats   │  │    Table     │  │  Timeline  │  │   CSV    │
│  └──────────┘  └──────────────┘  └────────────┘  └──────────┘  │
│  ┌──────────────────────────────────────────────────────────┐    │
│  │  User Selector (Archive search + Graph tenant search)   │    │
│  └──────────────────────────────────────────────────────────┘    │
└──────────────────────────┬──────────────────────────────────────┘
                           │ REST API (JWT-protected)
┌──────────────────────────┴──────────────────────────────────────┐
│              Backend (Express + TypeScript + SQLite)             │
│  ┌────────────────┐  ┌──────────────┐  ┌─────────────────────┐  │
│  │  Graph Export   │  │  Auto-Sync   │  │   SQLite Storage    │
│  │  Service        │  │  (freshness  │  │  (upsert, no       │
│  │  (pagination,   │  │   check +    │  │   duplicates)       │
│  │   user-scoped)  │  │   scheduler) │  │                     │
│  └────────────────┘  └──────────────┘  └─────────────────────┘  │
│  ┌────────────────┐  ┌──────────────┐                           │
│  │  JWT Auth       │  │  Graph User  │                           │
│  │  Middleware     │  │  Search      │                           │
│  └────────────────┘  └──────────────┘                           │
└──────────────────────────┬──────────────────────────────────────┘
                           │ Microsoft Graph API v1.0
                           ▼
    GET /copilot/users/{id}/interactionHistory/getAllEnterpriseInteractions
```

## Key Features

### Authentication & Role-Based Access
- **Entra ID login** — users sign in via MSAL (redirect flow) with their Microsoft account
- **Two app roles**: `ComplianceAdmin` (full access) and `ComplianceViewer` (read-only)
- **JWT validation** on all API endpoints using Entra ID JWKS

### Auto-Sync Flow
1. User logs in → dashboard defaults to their own Copilot interaction data
2. Backend checks if data exists and is fresh (< 1 hour old)
3. If missing or stale → auto-exports from Graph, stores in SQLite
4. If fresh → serves from local DB instantly
5. Hourly cron scheduler keeps data updated automatically

### User Switching
- **Archive search** — search users already in the local database
- **Graph search** — search any tenant user by display name via Microsoft Graph
- Inline autocomplete dropdown with click-to-select
- Dashboard re-syncs automatically when user is switched

### Dashboard Tabs
| Tab | Description |
|-----|-------------|
| **Overview** | Stats cards (total interactions, prompts, responses, sessions) + pie/bar charts by app |
| **Interactions** | Searchable, filterable, paginated table with expandable detail rows |
| **Sessions** | Session list grouped by `sessionId` with a timeline view showing prompt ↔ response pairs |
| **Download** | Download stored interactions as CSV with app filter and date range |

### Data Integrity
- SQLite `ON CONFLICT(id) DO UPDATE` upsert — **no duplicate records** across repeated exports
- Each interaction tagged with `target_user_id` for per-user scoping
- WAL mode for concurrent read/write safety

## Prerequisites

- [Node.js](https://nodejs.org/) v18 or later
- A [Microsoft Entra app registration](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app) with:
  - **Application permissions**: `AiEnterpriseInteraction.Read.All`, `User.Read.All` (both with admin consent)
  - **SPA redirect URI**: `http://localhost:3000`
  - **App roles** defined: `ComplianceAdmin`, `ComplianceViewer`
- Target users with a **Microsoft 365 Copilot** license

## Project structure

```
├── src/
│   ├── server.ts           # Express API server + static file serving
│   ├── auth.ts             # MSAL client-credentials authentication (Graph calls)
│   ├── auth-middleware.ts   # JWT validation middleware + role guards
│   ├── graph-export.ts     # Graph Export service (pagination, live stats)
│   ├── database.ts         # SQLite persistence (upsert, freshness check, user scoping)
│   ├── scheduler.ts        # Cron-based automatic export
│   ├── run-export.ts       # One-shot CLI export runner
│   ├── logger.ts           # Structured logger utility
│   └── types.ts            # Shared TypeScript types
├── client/
│   ├── src/
│   │   ├── App.tsx                      # Root app with tab navigation + user selector
│   │   ├── main.tsx                     # React entry point with MSAL provider
│   │   ├── types.ts                     # Frontend types + constants
│   │   ├── auth/
│   │   │   ├── msalConfig.ts            # MSAL browser configuration
│   │   │   └── AuthProvider.tsx         # Auth context (login, token, roles)
│   │   ├── hooks/useApi.ts              # Auth-aware data fetching hooks
│   │   └── components/
│   │       ├── Navbar.tsx               # Top navigation + user info + role badge
│   │       ├── Dashboard.tsx            # Overview tab (auto-sync + stats)
│   │       ├── StatsCards.tsx           # Metric cards
│   │       ├── AppUsageChart.tsx        # Pie + bar charts (Recharts)
│   │       ├── InteractionsTable.tsx    # Filterable interactions table
│   │       ├── SessionView.tsx          # Session list + timeline
│   │       ├── ExportPanel.tsx          # CSV download controls
│   │       └── DateRangePicker.tsx      # Date range input
│   ├── index.html
│   ├── package.json
│   ├── vite.config.ts
│   ├── tsconfig.json
│   ├── tailwind.config.js
│   └── postcss.config.js
├── .env.example
├── .gitignore
├── package.json
├── tsconfig.json
└── README.md
```

## Getting started

### 1. Install dependencies

```bash
npm install
cd client && npm install && cd ..
```

### 2. Register an app in Microsoft Entra

1. Open the [Microsoft Entra admin center](https://entra.microsoft.com/).
2. Go to **App registrations** → **New registration**.
3. Name: e.g. `Copilot Interaction Export` / Single tenant.
4. Click **Register**.

#### Add API permissions

1. **API permissions** → **Add a permission** → **Microsoft Graph** → **Application permissions**.
2. Add **`AiEnterpriseInteraction.Read.All`** and **`User.Read.All`**.
3. **Grant admin consent**.

#### Add SPA redirect URI

1. **Authentication** → **Add a platform** → **Single-page application (SPA)**.
2. Set redirect URI to `http://localhost:3000`.
3. Click **Configure**.

#### Define app roles

1. **App roles** → **Create app role**:
   - Display name: `Compliance Admin`, Value: `ComplianceAdmin`, Allowed member types: Users/Groups
   - Display name: `Compliance Viewer`, Value: `ComplianceViewer`, Allowed member types: Users/Groups

#### Assign roles to users

1. Go to **Enterprise applications** → your app → **Users and groups**.
2. **Add user/group** → select users → assign `ComplianceAdmin` or `ComplianceViewer` role.

#### Create a client secret

1. **Certificates & secrets** → **New client secret**.
2. Copy the **Value** — you will need it for `.env`.

### 3. Configure environment variables

```bash
cp .env.example .env
```

Fill in your values:

```env
TENANT_ID=<your-tenant-id>
CLIENT_ID=<your-client-id>
CLIENT_SECRET=<your-client-secret>
USER_ID=<fallback-user-object-id>
PORT=3000
REDIRECT_URI=http://localhost:3000
```

### 4. Build the frontend

```bash
cd client
npm run build
cd ..
```

### 5. Start the server

```bash
npm run dev
```

Open **http://localhost:3000** in your browser. Sign in with a user that has the `ComplianceAdmin` or `ComplianceViewer` role assigned.

## API endpoints

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| `GET` | `/api/auth/config` | Public | MSAL configuration for frontend |
| `GET` | `/api/auth/me` | Bearer | Current user info + roles |
| `POST` | `/api/sync` | Bearer | Auto-sync: check freshness + export if needed |
| `GET` | `/api/stats` | Bearer | Dashboard statistics (scoped by `?targetUserId`) |
| `GET` | `/api/interactions` | Bearer | Paginated interactions (`?page`, `pageSize`, `targetUserId`, `appClass`, `interactionType`, `search`, `startDate`, `endDate`, `sessionId`) |
| `GET` | `/api/sessions` | Bearer | Paginated session list |
| `GET` | `/api/sessions/:sessionId` | Bearer | All interactions in a session (timeline) |
| `POST` | `/api/export` | Bearer (Admin) | Trigger manual Graph export |
| `GET` | `/api/export/download` | Public | Download archive as CSV (`?format=csv&targetUserId=&appClass=&startDate=&endDate=`) |
| `GET` | `/api/users` | Bearer | Search archived users in local DB |
| `GET` | `/api/graph/users` | Bearer | Search tenant users by display name via Graph |
| `GET` | `/api/graph/stats` | Bearer | Live stats from Graph (no storage) |

## How it works

1. **User login** — Frontend authenticates via MSAL redirect flow. Backend validates JWT on every API call.
2. **Auto-sync** — On login (or user switch), `POST /api/sync` checks if data is fresh. If stale/missing, exports from Graph automatically.
3. **Export** — The Graph Export service calls `GET /copilot/users/{id}/interactionHistory/getAllEnterpriseInteractions` with full `@odata.nextLink` pagination.
4. **Storage** — Each `aiInteraction` is upserted into SQLite with `target_user_id` tagging. `ON CONFLICT` prevents duplicates.
5. **Scheduler** — A cron job (default: every hour) automatically re-exports for the configured `USER_ID`.
6. **Dashboard** — The React frontend queries the Express REST API to display per-user stats, tables, timelines, and CSV download.

## Important notes

- **Two auth layers**: MSAL client credentials (backend → Graph) + JWT validation (frontend → backend).
- Delta queries are **not supported** by this API — each export pulls the full set (upsert prevents duplicates).
- The recommended `$top` value is **100** for optimal performance.
- This API can retrieve interactions from **deleted users** and **deleted interactions**.
- If a user prompt is edited, it is treated as a new interaction.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `AADSTS500113: No reply address` | Add `http://localhost:3000` as SPA redirect URI in Authentication |
| `Access Denied` after login | Assign `ComplianceAdmin` or `ComplianceViewer` role in Enterprise apps → Users and groups |
| `403 Forbidden` on Graph call | Ensure `AiEnterpriseInteraction.Read.All` + `User.Read.All` are granted with admin consent |
| No interactions returned | Ensure the target user has a Copilot license and has been using Copilot |
| Empty dashboard | The auto-sync runs on login — check server logs for export errors |
| Frontend not loading | Ensure you've run `cd client && npm run build` first |
| CSV download fails with auth error | Should not happen — download endpoint is public. Check the URL format. |

## Related resources

- [Microsoft 365 Copilot APIs Client Libraries (Agents-M365Copilot)](https://github.com/microsoft/Agents-M365Copilot)
- [Companion sample — `change-notifications-copilot-ai-interactions`](https://github.com/microsoft/Agents-M365Copilot/tree/main/typescript/samples/change-notifications-copilot-ai-interactions) (push-based / real-time)
- [Microsoft Graph API documentation](https://learn.microsoft.com/en-us/graph/)
