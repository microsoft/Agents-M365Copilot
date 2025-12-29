# Microsoft 365 Copilot APIs Python Client Library

Integrate the Microsoft 365 Copilot APIs into your Python application!

> **Note:**
>
>Because the Copilot APIs in the beta endpoint are subject to breaking changes, don't use this preview release of the client libraries in production apps.

## Installation

The Microsoft 365 Copilot APIs client libraries are available in the following packages in the Python Package Index (PyPi):

- [microsoft-agents-m365copilot-beta](https://github.com/microsoft/Agents-M365Copilot/tree/main/python/packages/microsoft_agents_m365copilot_beta): Contains the models and request builders for accessing the beta endpoint. microsoft-agents-m365copilot-beta has a dependency on microsoft-agents-m365copilot-core.
- [microsoft-agents-m365copilot-core](https://github.com/microsoft/Agents-M365Copilot/tree/main/python/packages/microsoft_agents_m365copilot_core): The core library for making calls to the Copilot APIs.

To install the client libraries via PyPi:

```py
pip install microsoft-agents-m365copilot-beta
```

## Create a Copilot APIs client and make an API call

The following code example shows how to create an instance of a Microsoft 365 Copilot APIs client with an authentication provider in the supported languages. The authentication provider handles acquiring access tokens for the application. Many different authentication providers are available for each language and platform. The different authentication providers support different client scenarios. For details about which provider and options are appropriate for your scenario, see [Choose an Authentication Provider](https://learn.microsoft.com/graph/sdks/choose-authentication-providers). 

The example also shows how to make a call to the Microsoft 365 Copilot Retrieval API. 

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



## Issues

To view or log issues, see [issues](https://github.com/microsoft/Agents-M365Copilot/issues).

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft 
trademarks or logos is subject to and must follow 
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.