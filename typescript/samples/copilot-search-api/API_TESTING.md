# API Testing with cURL

This file contains example cURL commands for testing the Microsoft 365 Copilot Search API endpoints.

## Prerequisites

1. Start the server:
   ```bash
   npm start
   ```

2. Server should be running on `http://localhost:3000`

---

## 1. Health Check

```bash
curl http://localhost:3000/health
```

Expected response:
```json
{
  "status": "ok",
  "service": "Microsoft 365 Copilot Search API"
}
```

---

## 2. Simple Search

```bash
curl -X POST http://localhost:3000/api/search \
  -H "Content-Type: application/json" \
  -d '{
    "query": "quarterly financial reports from last year",
    "pageSize": 10
  }'
```

---

## 3. Search with Larger Page Size

```bash
curl -X POST http://localhost:3000/api/search \
  -H "Content-Type: application/json" \
  -d '{
    "query": "project documentation about cloud migration",
    "pageSize": 20
  }'
```

---

## 4. Search with Path Filter

**Note:** Replace the path with your actual OneDrive path

```bash
curl -X POST http://localhost:3000/api/search/path \
  -H "Content-Type: application/json" \
  -d '{
    "query": "budget spreadsheets",
    "path": "https://contoso-my.sharepoint.com/personal/username_domain_com/Documents/Finance",
    "pageSize": 10
  }'
```

To get the correct path:
1. Open OneDrive in browser
2. Navigate to a folder
3. Right-click on a file → "Details"
4. Copy the path from the details pane

---

## 5. Search with Custom Filter Expression

```bash
curl -X POST http://localhost:3000/api/search \
  -H "Content-Type: application/json" \
  -d '{
    "query": "meeting notes",
    "filterExpression": "path:\"https://contoso-my.sharepoint.com/personal/user_domain_com/Documents/Meetings\"",
    "pageSize": 15
  }'
```

---

## 6. Paginated Search

First request:
```bash
curl -X POST http://localhost:3000/api/search \
  -H "Content-Type: application/json" \
  -d '{
    "query": "presentations about product roadmap",
    "pageSize": 10
  }'
```

If the response contains a `skipToken`, use it for the next page:
```bash
curl -X POST http://localhost:3000/api/search \
  -H "Content-Type: application/json" \
  -d '{
    "query": "presentations about product roadmap",
    "pageSize": 10,
    "skipToken": "YOUR_SKIP_TOKEN_HERE"
  }'
```

---

## 7. Get Examples and Best Practices

```bash
curl http://localhost:3000/api/search/examples
```

---

## Example Queries

Here are some effective natural language queries to try:

```bash
# Financial documents
curl -X POST http://localhost:3000/api/search \
  -H "Content-Type: application/json" \
  -d '{"query": "quarterly financial reports from Q4 2024", "pageSize": 10}'

# Project documentation
curl -X POST http://localhost:3000/api/search \
  -H "Content-Type: application/json" \
  -d '{"query": "technical specifications for the new mobile app", "pageSize": 10}'

# Meeting notes
curl -X POST http://localhost:3000/api/search \
  -H "Content-Type: application/json" \
  -d '{"query": "meeting notes from marketing team about brand strategy", "pageSize": 10}'

# Presentations
curl -X POST http://localhost:3000/api/search \
  -H "Content-Type: application/json" \
  -d '{"query": "presentations about product roadmap for 2025", "pageSize": 10}'

# Spreadsheets
curl -X POST http://localhost:3000/api/search \
  -H "Content-Type: application/json" \
  -d '{"query": "budget spreadsheets for engineering department", "pageSize": 10}'
```

---

## Response Format

Successful response:
```json
{
  "success": true,
  "query": "your search query",
  "resultCount": 5,
  "data": {
    "searchHits": [
      {
        "resource": {
          "@odata.type": "#microsoft.graph.driveItem",
          "id": "file-id",
          "name": "Document.docx",
          "webUrl": "https://...",
          "lastModifiedDateTime": "2025-01-15T10:30:00Z"
        },
        "summary": "Preview text..."
      }
    ],
    "skipToken": "token-for-next-page"
  }
}
```

Error response:
```json
{
  "success": false,
  "error": "Error message",
  "details": {}
}
```

---

## PowerShell Examples

If you prefer PowerShell:

```powershell
# Simple search
$body = @{
    query = "quarterly financial reports from last year"
    pageSize = 10
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:3000/api/search" `
    -Method Post `
    -ContentType "application/json" `
    -Body $body

# Search with path filter
$body = @{
    query = "budget spreadsheets"
    path = "https://contoso-my.sharepoint.com/personal/user_domain_com/Documents/Finance"
    pageSize = 10
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:3000/api/search/path" `
    -Method Post `
    -ContentType "application/json" `
    -Body $body
```

---

## Troubleshooting

### 401 Unauthorized
- Check your Azure AD app registration
- Verify API permissions are granted
- Ensure credentials in `.env` are correct

### 403 Forbidden
- Verify admin consent has been granted for API permissions
- Check that the user has a Microsoft 365 Copilot license
- Ensure the user has access to OneDrive content

### Empty results
- Make queries more descriptive and specific
- Add more context to your search query
- Avoid overly generic terms
- Check spelling of important keywords

### Rate limit errors
- The API allows 200 requests per user per hour
- Implement delays between requests
- Consider caching results
