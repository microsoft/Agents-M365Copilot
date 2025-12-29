# On-Behalf-Of (OBO) Flow – Complete Setup Guide

This README documents the complete **On-Behalf-Of (OBO) authentication flow** used to call Microsoft 365 Copilot / Microsoft Graph APIs from a backend service on behalf of a signed-in user.

---

## Overview

The OBO flow enables:

1. **Frontend app** authenticates the user
2. **Frontend** obtains a token for the Backend API (Token A)
3. **Backend API** exchanges Token A for a Graph token using OBO (Token B)
4. **Backend** calls Copilot / Graph APIs
5. Results flow back to the frontend

```
User → Frontend App → Backend API → Copilot / Graph API
                                ← Results
```

---

## Prerequisites

- Azure subscription (Admin access)
- Azure AD / Entra ID tenant
- Python 3.9+
- Virtual environment enabled
- VS Code / Terminal
- Admin rights to manage Conditional Access policies

---

## Architecture

### Tokens

| Token | Audience | Used For |
|------|--------|---------|
| Token A | Backend API | Frontend → Backend authentication |
| Token B | Microsoft Graph | Backend → Copilot / Graph APIs |

### App Registrations

1. **Frontend App** (Public client)
   - Handles user sign-in
   - Requests token for Backend API

2. **Backend App** (Confidential client)
   - Has client secret
   - Performs OBO token exchange
   - Calls Microsoft Graph / Copilot APIs

---

## Part 1 – Azure Portal Configuration

### Step 1: Register Backend API App

- Azure Portal → Azure AD → App registrations → New registration
- Name: `m365copilot-backend-api`
- Accounts: Single tenant
- Redirect URI: None

Save:
- Tenant ID
- Backend Client ID

---

### Step 2: Expose Backend API

- Expose an API → Set Application ID URI

```
api://<BACKEND_CLIENT_ID>
```

Add Scope:

| Setting | Value |
|------|------|
| Scope name | access_as_user |
| Consent | Admin & User |
| State | Enabled |

---

### Step 3: Create Backend Client Secret

- Certificates & secrets → New client secret
- Copy secret immediately

Save as:

```
BACKEND_CLIENT_SECRET
```

---

### Step 4: Add Graph Permissions (Delegated)

Add Microsoft Graph permissions:

- Files.Read.All
- Sites.Read.All
- User.Read

Grant **Admin Consent**

---

### Step 5: Configure Known Client Applications

Edit **Manifest** of backend app:

```json
"knownClientApplications": [
  "00000000000000000000"
]
```

Save changes

---

### Step 6: Configure Frontend App Redirect URI

- App registrations → Frontend app
- Authentication → Add platform
- Mobile & desktop applications

Add:

```
http://localhost
```

---

### Step 7: Add Backend API Permission to Frontend

- API permissions → Add a permission → My APIs
- Select backend API
- Delegated permission: `access_as_user`

Grant **Admin Consent**

---

## Part 2 – Local Configuration

### Step 8: `.env` File

```env
TENANT_ID=xxxx

# Frontend App
FRONTEND_CLIENT_ID=048d1f20-xxxx

# Backend App
BACKEND_CLIENT_ID=xxxx
BACKEND_CLIENT_SECRET=xxxx

BACKEND_API_URL=http://localhost:5000

# Legacy (optional)
CLIENT_ID=048d1f20
CLIENT_SECRET=xxxx
```

---

### Step 9: Install Dependencies

```bash
pip install msal flask requests
```

---

## Conditional Access Warning

If testing on **unmanaged devices**, temporarily disable or set to report-only:

```
[SharePoint admin center] Block access from apps on unmanaged devices
```

Azure Portal → Azure AD → Security → Conditional Access → Policies

---

## Part 3 – Run the Application

### Step 10: Start Backend API

```bash
python backend_api.py
```

Expected output:

```
Starting Backend API Server...
Running at http://localhost:5000
```

---

### Step 11: Run Frontend Client

```bash
python frontend_client.py
```

---

### Step 12: Authenticate User

- Browser opens
- Sign in with Azure AD credentials
- Consent permissions
- Browser may redirect to localhost (error page is OK)

---

## Verification

Success output:

```
SUCCESS! OBO Flow Completed
Total hits: X
```

---

## Common Errors & Fixes

### AADSTS65001 – User not consented
- Re-run Step 7
- Grant admin consent

### AADSTS50013 – Assertion audience mismatch
- Verify Application ID URI

### 401 Unauthorized
- Validate BACKEND_CLIENT_SECRET
- Ensure Graph permissions are granted

### Connection refused
- Ensure backend API is running

### Browser not opening
- Ensure redirect URI is configured

---

## Verification Checklist

✅ Backend app exposed API
✅ access_as_user scope exists
✅ Known client applications configured
✅ Frontend redirect URI added
✅ Admin consents granted
✅ Backend API running
✅ Frontend client successful

---


---

## Ports

| Service | Port |
|------|----|
| Backend API | 5000 |

---

## Key Takeaway

OBO enables **secure user-delegated access** from backend services without re-prompting users, following Zero Trust principles.

---

