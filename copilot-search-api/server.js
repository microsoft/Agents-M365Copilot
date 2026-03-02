const express = require('express');
const {
  performSearch,
  searchWithPathFilter,
  buildPathFilter,
} = require('./search');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(express.json());

// CORS middleware (adjust origins as needed)
app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Headers', 'Content-Type, Authorization');
  res.header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  if (req.method === 'OPTIONS') {
    return res.sendStatus(200);
  }
  next();
});

// Health check endpoint
app.get('/health', (req, res) => {
  res.json({ status: 'ok', service: 'Microsoft 365 Copilot Search API' });
});

/**
 * POST /api/search
 * Perform a semantic search
 * 
 * Request body:
 * {
 *   "query": "natural language search query",
 *   "pageSize": 10,
 *   "skipToken": "optional pagination token",
 *   "filterExpression": "optional KQL filter"
 * }
 */
app.post('/api/search', async (req, res) => {
  try {
    const { query, pageSize, skipToken, filterExpression } = req.body;

    if (!query) {
      return res.status(400).json({ error: 'Query parameter is required' });
    }

    if (query.length > 1500) {
      return res.status(400).json({
        error: 'Query exceeds maximum length of 1,500 characters',
      });
    }

    const options = {};
    if (pageSize) options.pageSize = pageSize;
    if (skipToken) options.skipToken = skipToken;
    if (filterExpression) options.filterExpression = filterExpression;

    const results = await performSearch(query, options);

    res.json({
      success: true,
      query: query,
      resultCount: results.searchHits?.length || 0,
      data: results,
    });
  } catch (error) {
    console.error('Search error:', error);
    res.status(error.statusCode || 500).json({
      success: false,
      error: error.message,
      details: error.body || null,
    });
  }
});

/**
 * POST /api/search/path
 * Perform a semantic search with path filtering
 * 
 * Request body:
 * {
 *   "query": "natural language search query",
 *   "path": "https://contoso-my.sharepoint.com/personal/.../Documents/Folder",
 *   "pageSize": 10
 * }
 */
app.post('/api/search/path', async (req, res) => {
  try {
    const { query, path, pageSize } = req.body;

    if (!query) {
      return res.status(400).json({ error: 'Query parameter is required' });
    }

    if (!path) {
      return res.status(400).json({ error: 'Path parameter is required' });
    }

    const filterExpression = buildPathFilter(path);
    const options = { filterExpression };
    if (pageSize) options.pageSize = pageSize;

    const results = await performSearch(query, options);

    res.json({
      success: true,
      query: query,
      path: path,
      resultCount: results.searchHits?.length || 0,
      data: results,
    });
  } catch (error) {
    console.error('Search error:', error);
    res.status(error.statusCode || 500).json({
      success: false,
      error: error.message,
      details: error.body || null,
    });
  }
});

/**
 * GET /api/search/examples
 * Get example queries and best practices
 */
app.get('/api/search/examples', (req, res) => {
  res.json({
    bestPractices: [
      'Use descriptive and natural language-based queries',
      'Provide as much context as possible',
      'Avoid overly generic queries',
      'Avoid spelling errors in important keywords',
      'Use full OneDrive path for path filtering',
    ],
    exampleQueries: [
      'quarterly financial reports from last year',
      'project documentation related to cloud migration',
      'presentations about product roadmap',
      'meeting notes from marketing team',
      'budget spreadsheets for 2024',
    ],
    restrictions: {
      maxQueryLength: 1500,
      maxPageSize: 100,
      rateLimit: '200 requests per user per hour',
      supportedSources: ['OneDrive for work or school'],
      supportedFileExtensions: [
        '.aspx', '.docx', '.pptx', '.pdf', '.onepart',
        '.doc', '.html', '.eml', '.mp4', '.loop',
        '.one', '.fluid', '.png', '.jpg', '.json',
        '.csv', '.xml', '.ppt'
      ],
    },
  });
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error('Unhandled error:', err);
  res.status(500).json({
    success: false,
    error: 'Internal server error',
  });
});

// Start server
app.listen(PORT, () => {
  console.log(`\n🚀 Microsoft 365 Copilot Search API Server`);
  console.log(`📍 Server running on http://localhost:${PORT}`);
  console.log(`\nAvailable endpoints:`);
  console.log(`  GET  /health - Health check`);
  console.log(`  POST /api/search - Perform semantic search`);
  console.log(`  POST /api/search/path - Search with path filter`);
  console.log(`  GET  /api/search/examples - Get examples and best practices`);
  console.log(`\nPress Ctrl+C to stop\n`);
});

module.exports = app;
