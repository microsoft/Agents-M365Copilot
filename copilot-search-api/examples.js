// Example usage file demonstrating the Copilot Search API

const {
  performSearch,
  searchWithPathFilter,
  performPaginatedSearch,
  displayResults,
} = require('./search');

/**
 * Example 1: Simple semantic search
 */
async function example1_SimpleSearch() {
  console.log('\n=== Example 1: Simple Semantic Search ===\n');
  
  const query = 'quarterly financial reports from last year';
  console.log(`Query: "${query}"\n`);
  
  const results = await performSearch(query, { pageSize: 5 });
  displayResults(results);
}

/**
 * Example 2: Search with larger page size
 */
async function example2_LargerPageSize() {
  console.log('\n=== Example 2: Search with Larger Page Size ===\n');
  
  const query = 'project documentation about cloud migration';
  console.log(`Query: "${query}"\n`);
  
  const results = await performSearch(query, { pageSize: 20 });
  displayResults(results);
}

/**
 * Example 3: Search with path filter
 * Note: Replace the path with an actual path from your OneDrive
 */
async function example3_PathFiltering() {
  console.log('\n=== Example 3: Search with Path Filter ===\n');
  
  const query = 'budget spreadsheets';
  // Replace with your actual OneDrive path
  const path = 'https://contoso-my.sharepoint.com/personal/username_domain_com/Documents/Finance';
  
  console.log(`Query: "${query}"`);
  console.log(`Path: "${path}"\n`);
  
  try {
    const results = await searchWithPathFilter(query, path);
    displayResults(results);
  } catch (error) {
    console.log('Note: Update the path variable with your actual OneDrive path to use this example.');
    console.error('Error:', error.message);
  }
}

/**
 * Example 4: Paginated search (retrieve all results)
 */
async function example4_PaginatedSearch() {
  console.log('\n=== Example 4: Paginated Search ===\n');
  
  const query = 'meeting notes from marketing team';
  console.log(`Query: "${query}"\n`);
  
  const allResults = await performPaginatedSearch(query, 10);
  
  console.log(`\n=== All Results (${allResults.length}) ===\n`);
  allResults.forEach((hit, index) => {
    console.log(`${index + 1}. ${hit.resource.name}`);
    if (hit.resource.webUrl) {
      console.log(`   ${hit.resource.webUrl}`);
    }
  });
}

/**
 * Example 5: Multiple natural language queries
 */
async function example5_MultipleQueries() {
  console.log('\n=== Example 5: Multiple Natural Language Queries ===\n');
  
  const queries = [
    'presentations about product roadmap',
    'customer feedback surveys',
    'technical specifications for new features',
  ];
  
  for (const query of queries) {
    console.log(`\nQuery: "${query}"`);
    const results = await performSearch(query, { pageSize: 3 });
    
    if (results.searchHits && results.searchHits.length > 0) {
      console.log(`Found ${results.searchHits.length} results:`);
      results.searchHits.forEach((hit, index) => {
        console.log(`  ${index + 1}. ${hit.resource.name}`);
      });
    } else {
      console.log('No results found.');
    }
  }
}

/**
 * Example 6: Handling empty results
 */
async function example6_EmptyResults() {
  console.log('\n=== Example 6: Handling Empty Results ===\n');
  
  const query = 'xyzabc123nonexistentdocument'; // Intentionally obscure query
  console.log(`Query: "${query}"\n`);
  
  const results = await performSearch(query, { pageSize: 10 });
  
  if (!results.searchHits || results.searchHits.length === 0) {
    console.log('✓ Correctly handled empty results');
    console.log('Tips for better results:');
    console.log('- Make queries more descriptive');
    console.log('- Add more context');
    console.log('- Avoid overly generic terms');
    console.log('- Check spelling of important keywords');
  }
}

// Main execution
(async () => {
  try {
    console.log('\n🔍 Microsoft 365 Copilot Search API - Examples\n');
    console.log('Note: These examples require proper authentication setup.');
    console.log('See README.md for configuration instructions.\n');
    
    // Run examples (uncomment the ones you want to try)
    await example1_SimpleSearch();
    
    // await example2_LargerPageSize();
    // await example3_PathFiltering();
    // await example4_PaginatedSearch();
    // await example5_MultipleQueries();
    // await example6_EmptyResults();
    
  } catch (error) {
    console.error('\n❌ Error running examples:', error.message);
    
    if (error.code === 'ENOENT' && error.path?.includes('.env')) {
      console.error('\n⚠️  Configuration file not found!');
      console.error('Please create a .env file based on .env.example');
      console.error('See README.md for setup instructions.');
    } else if (error.message?.includes('TENANT_ID')) {
      console.error('\n⚠️  Missing environment variables!');
      console.error('Please configure TENANT_ID and CLIENT_ID in your .env file');
    } else if (error.statusCode === 401) {
      console.error('\n⚠️  Authentication failed!');
      console.error('Please check your Azure AD app registration and credentials');
    } else if (error.statusCode === 403) {
      console.error('\n⚠️  Access denied!');
      console.error('Please ensure:');
      console.error('1. Your app has the correct API permissions');
      console.error('2. Admin consent has been granted');
      console.error('3. The user has a Microsoft 365 Copilot license');
    }
    
    if (error.body) {
      console.error('\nAPI Response:', JSON.stringify(error.body, null, 2));
    }
  }
})();
