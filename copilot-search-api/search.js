require('isomorphic-fetch');
const { Client } = require('@microsoft/microsoft-graph-client');
const { ClientSecretCredential, DeviceCodeCredential } = require('@azure/identity');
require('dotenv').config();

/**
 * Creates and returns an authenticated Microsoft Graph client
 */
function getAuthenticatedClient() {
  let credential;

  if (process.env.CLIENT_SECRET) {
    // App-only authentication
    credential = new ClientSecretCredential(
      process.env.TENANT_ID,
      process.env.CLIENT_ID,
      process.env.CLIENT_SECRET
    );
  } else {
    // Device code flow (user authentication)
    credential = new DeviceCodeCredential({
      tenantId: process.env.TENANT_ID,
      clientId: process.env.CLIENT_ID,
      userPromptCallback: (info) => {
        console.log(info.message);
      },
    });
  }

  return Client.initWithMiddleware({
    authProvider: {
      getAccessToken: async () => {
        const token = await credential.getToken(
          'https://graph.microsoft.com/.default'
        );
        return token.token;
      },
    },
  });
}

/**
 * Performs search using Microsoft 365 Copilot Search API
 */
async function performSearch(query, options = {}) {
  try {
    if (!query) {
      throw new Error('Query parameter is required');
    }

    if (query.length > 1500) {
      throw new Error('Query exceeds maximum length of 1,500 characters');
    }

    const pageSize = options.pageSize || 10;
    if (pageSize > 100) {
      throw new Error('pageSize cannot exceed 100');
    }

    const client = getAuthenticatedClient();

    const requestPayload = {
      requests: [
        {
          entityTypes: ['driveItem'],
          query: {
            queryString: query,
          },
          from: 0,
          size: pageSize,
        },
      ],
    };

    // Add path filter if provided
    if (options.filterExpression) {
      requestPayload.requests[0].query.queryString +=
        ` AND ${options.filterExpression}`;
    }

    console.log('Sending request to Graph /beta/search/query');

    const response = await client
      .api('/search/query')
      .version('beta')
      .post(requestPayload);

    // Extract hits safely
    const hits =
      response?.value?.[0]?.hitsContainers?.[0]?.hits || [];

    return {
      success: true,
      searchHits: hits,
      skipToken:
        response?.value?.[0]?.hitsContainers?.[0]?.moreResultsAvailable
          ? 'more-results-available'
          : null,
    };
  } catch (error) {
    console.error('Search API Error:', error.message);

    return {
      success: false,
      error: error.message,
      details: error.body ? JSON.stringify(error.body) : null,
    };
  }
}

/**
 * Builds a path filter expression (KQL style)
 */
function buildPathFilter(path) {
  return `path:"${path}"`;
}

/**
 * Search with path filter
 */
async function searchWithPathFilter(query, oneDrivePath) {
  const filterExpression = buildPathFilter(oneDrivePath);
  return await performSearch(query, {
    filterExpression,
    pageSize: 20,
  });
}

/**
 * Paginated search (basic loop)
 */
async function performPaginatedSearch(query, pageSize = 10) {
  const results = [];

  const response = await performSearch(query, { pageSize });

  if (response.searchHits) {
    results.push(...response.searchHits);
  }

  return results;
}

/**
 * Display results in readable format
 */
function displayResults(response) {
  if (!response.searchHits || response.searchHits.length === 0) {
    console.log('\nNo relevant results found.');
    return;
  }

  console.log(`\n=== Search Results (${response.searchHits.length}) ===\n`);

  response.searchHits.forEach((hit, index) => {
    const resource = hit.resource;

    console.log(`${index + 1}. ${resource.name}`);
    console.log(`   Type: ${resource['@odata.type']}`);
    console.log(`   ID: ${resource.id}`);

    if (resource.webUrl) {
      console.log(`   URL: ${resource.webUrl}`);
    }

    if (resource.lastModifiedDateTime) {
      console.log(`   Last Modified: ${resource.lastModifiedDateTime}`);
    }

    if (hit.summary) {
      console.log(`   Summary: ${hit.summary}`);
    }

    console.log('');
  });
}

// Export functions
module.exports = {
  performSearch,
  searchWithPathFilter,
  performPaginatedSearch,
  buildPathFilter,
  displayResults,
};

// Run example if executed directly
if (require.main === module) {
  (async () => {
    console.log('\n=== Microsoft 365 Copilot Search API Example ===\n');

    const results = await performSearch(
      'quarterly financial reports from last year',
      { pageSize: 5 }
    );

    displayResults(results);
  })();
}