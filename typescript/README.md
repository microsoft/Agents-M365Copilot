# Microsoft 365 Copilot APIs TypeScript Client Library

Integrate the Microsoft 365 Copilot APIs into your TypeScript application!

> **Note:**
>
>Because the Microsoft 365 Copilot APIs in the beta endpoint are subject to breaking changes, don't use this preview release of the client libraries in production apps.

## Installation

The Microsoft 365 Copilot APIs client libraries will be available in the following packages in Node Package Manager (npm):

- [microsoft/agents-m365copilot-beta](https://github.com/microsoft/Agents-M365Copilot/tree/main/typescript/packages/agents-m365copilot-beta): Contains the models and request builders for accessing the beta endpoint. microsoft/agents-m365copilot-beta has a dependency on microsoft/agents-m365copilot-core.
- [microsoft/agents-m365copilot-core](https://github.com/microsoft/Agents-M365Copilot/tree/main/typescript/packages/agents-m365copilot-core): The core library for making calls to the Copilot APIs.

To install the client libraries via npm.

```Shell
npm install @microsoft/agents-m365copilot-beta –save
```

## Create a Copilot APIs client and make an API call

The following code example shows how to create an instance of a Microsoft 365 Copilot APIs client with an authentication provider in the supported languages. The authentication provider handles acquiring access tokens for the application. Many different authentication providers are available for each language and platform. The different authentication providers support different client scenarios. For details about which provider and options are appropriate for your scenario, see [Choose an Authentication Provider](https://learn.microsoft.com/graph/sdks/choose-authentication-providers). 

The example also shows how to make a call to the Microsoft 365 Copilot Retrieval API. To call this API, you first need to create a request object and then run the POST method on the request.

The client ID is the app registration ID that is generated when you [register your app in the Azure portal](https://learn.microsoft.com/graph/auth-register-app-v2).

>**Note:**
>    
>Your tenant must have a Microsoft 365 Copilot license.

```TypeScript

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

```

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