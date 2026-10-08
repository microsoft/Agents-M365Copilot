# Microsoft 365 Copilot Search API Sample

A Node.js sample demonstrating how to use the Microsoft 365 Copilot Search API to perform hybrid semantic and lexical search across OneDrive for work or school content.

## Overview

This sample showcases the **Microsoft 365 Copilot Search API (preview)**, which enables:
- **Hybrid search** (semantic + lexical) using natural language queries
- **Context-aware** document discovery in OneDrive for work or school
- **Path-based filtering** using Keyword Query Language (KQL)
- **Secure, compliant** search that respects permissions and access controls

## Prerequisites

1. **Microsoft 365 Copilot License**: The Search API requires a Microsoft 365 Copilot license add-on
2. **Node.js**: Version 14.x or higher
3. **Azure AD App Registration**: Required for authentication

## Setup Instructions

### Step 1: Create an Azure AD App Registration

1. Go to the [Azure Portal](https://portal.azure.com/#view/Microsoft_AAD_RegisteredApps/ApplicationsListBlade)
2. Click **New registration**
3. Enter a name (e.g., "Copilot Search API Sample")
4. Select **Accounts in this organizational directory only**
5. Click **Register**

### Step 2: Configure API Permissions

1. In your app registration, go to **API permissions**
2. Click **Add a permission** → **Microsoft Graph** → **Delegated permissions**
3. Add the following permission:
   - `Files.Read.All` (for accessing OneDrive content)
4. Click **Add permissions**
5. Click **Grant admin consent** (requires admin privileges)

### Step 3: Create Client Secret (Optional)

For app-only authentication (service principal):
1. Go to **Certificates & secrets**
2. Click **New client secret**
3. Add a description and select expiration
4. Copy the **Value** (you won't be able to see it again)

### Step 4: Configure Environment Variables

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and fill in your values:
   ```env
   TENANT_ID=your-tenant-id-here
   CLIENT_ID=your-client-id-here
   CLIENT_SECRET=your-client-secret-here  # Optional
   PORT=3000
   ```

### Step 5: Install Dependencies

```bash
npm install
```

To add Express (needed for the server):
```bash
npm install express
```

## Usage

### Option 1: Run as CLI Tool

Execute search directly from command line:

```bash
node search.js
```

Edit the examples in `search.js` to customize your queries.

### Option 2: Run as REST API Server

Start the Express server:

```bash
npm start
```

The server will start on `http://localhost:3000` with the following endpoints:

#### Endpoints

**1. Health Check**
```bash
GET /health
```

**2. Perform Semantic Search**
```bash
POST /api/search
Content-Type: application/json

{
  "query": "quarterly financial reports from last year",
  "pageSize": 10,
  "skipToken": "optional-pagination-token",
  "filterExpression": "optional-kql-filter"
}
```

Example with curl:
```bash
curl -X POST http://localhost:3000/api/search \
  -H "Content-Type: application/json" \
  -d '{
    "query": "project documentation about cloud migration",
    "pageSize": 20
  }'
```

**3. Search with Path Filter**
```bash
POST /api/search/path
Content-Type: application/json

{
  "query": "budget spreadsheets",
  "path": "https://contoso-my.sharepoint.com/personal/username_domain_com/Documents/Finance",
  "pageSize": 10
}
```

**4. Get Examples and Best Practices**
```bash
GET /api/search/examples
```

## Code Examples

### Basic Search

```javascript
const { performSearch, displayResults } = require('./search');

async function search() {
  const query = 'quarterly financial reports from last year';
  const results = await performSearch(query, { pageSize: 10 });
  displayResults(results);
}

search();
```

### Search with Path Filter

```javascript
const { searchWithPathFilter, displayResults } = require('./search');

async function searchInFolder() {
  const query = 'project documentation';
  const path = 'https://contoso-my.sharepoint.com/personal/user_contoso_com/Documents/Projects';
  
  const results = await searchWithPathFilter(query, path);
  displayResults(results);
}

searchInFolder();
```

### Paginated Search

```javascript
const { performPaginatedSearch } = require('./search');

async function searchAll() {
  const query = 'meeting notes from marketing team';
  const allResults = await performPaginatedSearch(query, 20);
  
  console.log(`Total results: ${allResults.length}`);
  allResults.forEach((hit, index) => {
    console.log(`${index + 1}. ${hit.resource.name}`);
  });
}

searchAll();
```

## Best Practices

Based on the official documentation:

1. **Craft Descriptive Queries**
   - ✅ "quarterly financial reports from last year"
   - ❌ "reports"

2. **Provide Context**
   - ✅ "project documentation about cloud migration for Azure"
   - ❌ "documents"

3. **Use Natural Language**
   - The API understands context and intent
   - Write queries as you would ask a person

4. **Avoid Spelling Errors**
   - Spelling errors in important keywords can affect relevance

5. **Use Full OneDrive Paths**
   - Use paths from file details pane, not sharing links
   - Format: `https://contoso-my.sharepoint.com/personal/username_domain_com/Documents/Folder`

6. **Use All Results**
   - Results are ordered by relevance
   - Don't discard lower-ranked results without review

## API Restrictions

- **Query length**: Maximum 1,500 characters
- **Page size**: Maximum 100 results per page
- **Rate limit**: 200 requests per user per hour
- **Data source**: OneDrive for work or school only (SharePoint coming soon)
- **File size limits**:
  - .docx, .pptx, .pdf: Maximum 512 MB
  - Other extensions: Maximum 150 MB
- **Supported file extensions**: .aspx, .docx, .pptx, .pdf, .onepart, .doc, .html, .eml, .mp4, .loop, .one, .fluid, .png, .jpg, .json, .csv, .xml, .ppt

## Authentication Methods

### Method 1: Device Code Flow (User Authentication)

Set only `TENANT_ID` and `CLIENT_ID` in `.env`. The app will prompt you to authenticate via device code.

### Method 2: Client Credentials (App-Only)

Set `TENANT_ID`, `CLIENT_ID`, and `CLIENT_SECRET` in `.env`. The app will authenticate as a service principal.

## Response Structure

```json
{
  "searchHits": [
    {
      "resource": {
        "@odata.type": "#microsoft.graph.driveItem",
        "id": "file-id",
        "name": "Q4 Financial Report.docx",
        "webUrl": "https://...",
        "lastModifiedDateTime": "2025-01-15T10:30:00Z"
      },
      "summary": "Summary or preview text..."
    }
  ],
  "skipToken": "token-for-next-page"
}
```

## Troubleshooting

### Error: "Unauthorized" or "401"
- Verify your app registration has the correct API permissions
- Ensure admin consent has been granted
- Check that your credentials in `.env` are correct

### Error: "No relevant results found"
- The query might be too generic
- Try adding more context to your query
- Verify the user has access to OneDrive content
- Check if the content exists in the user's working set

### Error: "Rate limit exceeded"
- The API allows 200 requests per user per hour
- Implement caching or reduce request frequency

## Resources

- [Official Documentation](https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/api/ai-services/search/overview)
- [Try in Graph Explorer](https://developer.microsoft.com/graph/graph-explorer)
- [Microsoft Graph SDK](https://docs.microsoft.com/graph/sdks/sdks-overview)
- [Terms of Use](https://learn.microsoft.com/microsoft-365-copilot/extensibility/api-terms-of-use)

## License

This sample is provided as-is under the MIT License.

## Support

For issues or questions:
- Create an issue in this repository
- Refer to the [official documentation](https://learn.microsoft.com/microsoft-365-copilot/extensibility/api/ai-services/search/overview)
- Check [Microsoft 365 Copilot FAQ](https://learn.microsoft.com/microsoft-365-copilot/extensibility/faq)
