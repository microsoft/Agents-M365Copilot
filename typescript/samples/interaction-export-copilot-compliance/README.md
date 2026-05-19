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
│              Compliance Dashboard (React + Vite + Tailwind)     │
│  ┌──────────┐  ┌──────────────┐  ┌────────────┐  ┌──────────┐  │
│  │ Overview │  │ Interactions │  │  Sessions  │  │  Export   │
│  │  Stats   │  │    Table     │  │  Timeline  │  │  Archive  │
│  └──────────┘  └──────────────┘  └────────────┘  └──────────┘  │
└──────────────────────────┬──────────────────────────────────────┘
                           │ REST API
┌──────────────────────────┴──────────────────────────────────────┐
│              Backend (Express + TypeScript + SQLite)             │
│  ┌────────────────┐  ┌──────────────┐  ┌─────────────────────┐  │
│  │  Graph Export   │  │   Scheduler  │  │   SQLite Storage    │
│  │  Service        │  │  (cron-based │  │  (persistent store) │
│  │  (pagination,   │  │   polling)   │  │                     │
│  │   filtering)    │  │              │  │                     │
│  └────────────────┘  └──────────────┘  └─────────────────────┘  │
└──────────────────────────┬──────────────────────────────────────┘
                           │ Microsoft Graph API v1.0
                           ▼
    GET /copilot/users/{id}/interactionHistory/getAllEnterpriseInteractions
```

## Dashboard Features

| Tab | Description |
|-----|-------------|
| **Overview** | Stats cards (total interactions, prompts, responses, sessions) + pie/bar charts by app |
| **Interactions** | Searchable, filterable, paginated table with expandable detail rows |
| **Sessions** | Session list grouped by `sessionId` with a timeline view showing prompt ↔ response pairs |
| **Export & Archive** | Trigger Graph export on-demand, download stored interactions as JSON or CSV |

## Prerequisites

- [Node.js](https://nodejs.org/) v18 or later
- A [Microsoft Entra app registration](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app) with:
  - Application permission: **`AiEnterpriseInteraction.Read.All`**
  - Admin consent granted
- A target user with a **Microsoft 365 Copilot** license

## Project structure

```
├── src/
│   ├── server.ts           # Express API server + static file serving
│   ├── auth.ts             # MSAL client-credentials authentication
│   ├── graph-export.ts     # Graph Export service (pagination, filtering)
│   ├── database.ts         # SQLite persistence layer
│   ├── scheduler.ts        # Cron-based automatic export
│   ├── run-export.ts       # One-shot CLI export runner
│   ├── logger.ts           # Structured logger utility
│   └── types.ts            # Shared TypeScript types
├── client/
│   ├── src/
│   │   ├── App.tsx                      # Root app with tab navigation
│   │   ├── main.tsx                     # React entry point
│   │   ├── types.ts                     # Frontend types + constants
│   │   ├── hooks/useApi.ts              # Data fetching hooks
│   │   └── components/
│   │       ├── Navbar.tsx               # Top navigation bar
│   │       ├── Dashboard.tsx            # Overview tab
│   │       ├── StatsCards.tsx           # Metric cards
│   │       ├── AppUsageChart.tsx        # Pie + bar charts (Recharts)
│   │       ├── InteractionsTable.tsx    # Filterable interactions table
│   │       ├── SessionView.tsx          # Session list + timeline
│   │       ├── ExportPanel.tsx          # Export/download controls
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
2. Search for **`AiEnterpriseInteraction.Read.All`**.
3. **Add permissions** → **Grant admin consent**.

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
USER_ID=<target-user-object-id>
PORT=3000
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

Open **http://localhost:3000** in your browser to see the compliance dashboard.

### 6. Run a manual export

Either use the **Export & Archive** tab in the dashboard, or run the CLI:

```bash
npm run export
```

## API endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/api/stats` | Dashboard statistics |
| `GET` | `/api/interactions` | Paginated interactions (supports `?page`, `pageSize`, `appClass`, `interactionType`, `search`, `startDate`, `endDate`, `sessionId`) |
| `GET` | `/api/sessions` | Paginated session list |
| `GET` | `/api/sessions/:sessionId` | All interactions in a session (timeline) |
| `POST` | `/api/export` | Trigger Graph export (`{ userId, appClass }`) |
| `GET` | `/api/export/download` | Download archive as JSON or CSV (`?format=json|csv&appClass=&startDate=&endDate=`) |

## Supported appClass filters

| Filter Value | App |
|-------------|-----|
| `IPM.SkypeTeams.Message.Copilot.Word` | Word |
| `IPM.SkypeTeams.Message.Copilot.Excel` | Excel |
| `IPM.SkypeTeams.Message.Copilot.Teams` | Teams |
| `IPM.SkypeTeams.Message.Copilot.BizChat` | Business Chat |
| `IPM.SkypeTeams.Message.Copilot.WebChat` | Web Chat |

## How it works

1. **Authentication** — MSAL acquires a token using client credentials (`AiEnterpriseInteraction.Read.All`).
2. **Export** — The Graph Export service calls `GET /copilot/users/{id}/interactionHistory/getAllEnterpriseInteractions` with full `@odata.nextLink` pagination.
3. **Storage** — Each `aiInteraction` is upserted into a local SQLite database with all properties preserved.
4. **Scheduler** — A cron job (default: every hour) automatically re-exports new interactions.
5. **Dashboard** — The React frontend queries the Express REST API to display stats, tables, timelines, and export controls.

## Important notes

- The API requires **application permissions** (not delegated) — the app runs without a signed-in user.
- Delta queries are **not supported** by this API — each export pulls the full set (the SQLite upsert prevents duplicates).
- The recommended `$top` value is **100** for optimal performance.
- This API can retrieve interactions from **deleted users** and **deleted interactions**.
- If a user prompt is edited, it is treated as a new interaction.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `403 Forbidden` on Graph call | Ensure `AiEnterpriseInteraction.Read.All` is granted with admin consent |
| No interactions returned | Ensure the target user has a Copilot license and has been using Copilot |
| Empty dashboard | Run an export first — via the Export tab or `npm run export` |
| Frontend not loading | Ensure you've run `cd client && npm run build` first |

## Related resources

- [Microsoft 365 Copilot APIs Client Libraries (Agents-M365Copilot)](https://github.com/microsoft/Agents-M365Copilot)
- [Companion sample — `change-notifications-copilot-ai-interactions`](https://github.com/microsoft/Agents-M365Copilot/tree/main/typescript/samples/change-notifications-copilot-ai-interactions) (push-based / real-time)
- [Microsoft Graph API documentation](https://learn.microsoft.com/en-us/graph/)
