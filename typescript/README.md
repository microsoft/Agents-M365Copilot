# Microsoft Copilot APIs TypeScript Client Library

Integrate the Microsoft Copilot APIs into your Python application!

## Installation

The Copilot APIs TypeScript client libraries will soon be available in npm.

```Shell
npm install @microsoft/agents-m365copilot-beta –save
```

## Create a Copilot APIs client and make an API call

The following code example shows how to create an instance of a Microsoft 365 Copilot APIs client with an authentication provider in the supported languages. The authentication provider handles acquiring access tokens for the application. Many different authentication providers are available for each language and platform. The different authentication providers support different client scenarios. For details about which provider and options are appropriate for your scenario, see [Choose an Authentication Provider](/graph/sdks/choose-authentication-providers). 

The example also shows how to make a call to the Retrieval API. To call this API, you first need to create a request object and then run the POST method on the request.

The client ID is the app registration ID that is generated when you [register your app in the Azure portal](/graph/auth-register-app-v2).

import { createBaseAgentsM365CopilotBetaServiceClient, RetrievalDataSourceObject } from '@microsoft/agents-m365copilot-beta';
import { DeviceCodeCredential } from '@azure/identity';
import { FetchRequestAdapter } from '@microsoft/kiota-http-fetchlibrary';

async function main() {
    // Initialize authentication with Device Code flow
    const credential = new DeviceCodeCredential({
        tenantId: process.env.TENANT_ID,
        clientId: process.env.CLIENT_ID,
        userPromptCallback: (info) => {
            console.log(`\nTo sign in, use a web browser to open the page ${info.verificationUri}`);
            console.log(`Enter the code ${info.userCode} to authenticate.`);
            console.log(`The code will expire at ${info.expiresOn}`);
        }
    });

    // Create request adapter with auth
    const adapter = new FetchRequestAdapter(credential, {
        scopes: ['https://graph.microsoft.com/.default']
    });
    adapter.baseUrl = "https://graph.microsoft.com/beta";

    // Create client instance
    const client = createBaseAgentsM365CopilotBetaServiceClient(adapter);

    try {
        console.log(`Using API base URL: ${adapter.baseUrl}\n`);

        // Create the retrieval request body
        const retrievalBody = {
            dataSource: RetrievalDataSourceObject.SharePoint,
            queryString: "What is the latest in my organization"
        };

        // Make the API call
        console.log("Making retrieval API request...");
        const retrieval = await client.copilot.retrieval.post(retrievalBody);

        // Process the results
        if (retrieval?.retrievalHits) {
            console.log(`\nReceived ${retrieval.retrievalHits.length} hits`);
            for (const hit of retrieval.retrievalHits) {
                console.log(`\nWeb URL: ${hit.webUrl}`);
                for (const extract of hit.extracts || []) {
                    console.log(`Text:\n${extract.text}\n`);
                }
            }
        }
    } catch (error) {
        console.error('Error:', error);
        throw error;
    }
}
