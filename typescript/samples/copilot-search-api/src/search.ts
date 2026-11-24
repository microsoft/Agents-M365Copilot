import 'isomorphic-fetch';
import { Client } from '@microsoft/microsoft-graph-client';
import {
  ClientSecretCredential,
  DeviceCodeCredential,
} from '@azure/identity';
import dotenv from 'dotenv';

dotenv.config();

function getAuthenticatedClient() {
  let credential: any;

  if (process.env.CLIENT_SECRET) {
    credential = new ClientSecretCredential(
      process.env.TENANT_ID as string,
      process.env.CLIENT_ID as string,
      process.env.CLIENT_SECRET as string
    );
  } else {
    credential = new DeviceCodeCredential({
      tenantId: process.env.TENANT_ID,
      clientId: process.env.CLIENT_ID,
      userPromptCallback: (info: any) => {
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
        return token?.token;
      },
    },
  });
}

async function performSearch(query: any, options: any = {}) {
  try {
    if (!query) {
      throw new Error('Query parameter is required');
    }

    const pageSize = options.pageSize || 10;

    const client = getAuthenticatedClient();

    const requestPayload: any = {
      requests: [
        {
          entityTypes: ['driveItem'],
          query: { queryString: query },
          from: 0,
          size: pageSize,
        },
      ],
    };

    if (options.filterExpression) {
      requestPayload.requests[0].query.queryString +=
        ` AND ${options.filterExpression}`;
    }

    const response: any = await client
      .api('/search/query')
      .version('beta')
      .post(requestPayload);

    const hits =
      response?.value?.[0]?.hitsContainers?.[0]?.hits || [];

    return {
      success: true,
      searchHits: hits,
      skipToken:
        response?.value?.[0]?.hitsContainers?.[0]
          ?.moreResultsAvailable
          ? 'more-results-available'
          : null,
    };
  } catch (error: any) {
    return {
      success: false,
      error: error?.message,
      details: error?.body
        ? JSON.stringify(error.body)
        : null,
    };
  }
}

function buildPathFilter(path: any) {
  return `path:"${path}"`;
}

async function searchWithPathFilter(
  query: any,
  oneDrivePath: any
) {
  const filterExpression = buildPathFilter(oneDrivePath);
  return performSearch(query, {
    filterExpression,
    pageSize: 20,
  });
}

export {
  performSearch,
  searchWithPathFilter,
  buildPathFilter,
};