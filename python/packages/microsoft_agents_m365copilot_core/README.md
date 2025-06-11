#  Microsoft 365 Copilot APIs Python Core Client Library

The  Microsoft 365 Copilot APIs Python Core Client Library contains core classes used by the [Microsoft 365 Copilot APIs Library](https://github.com/microsoft/Agents-M365Copilot/tree/main/python) to send native HTTP requests to the [Microsoft 365 Copilot APIs](https://aka.ms/M365CopilotAPIs).

> **Note:**
>
>Because the Microsoft 365 Copilot APIs in the beta endpoint are subject to breaking changes, don't use a preview release of the client libraries in production apps.

## Prerequisites

- Python 3.9+

This library doesn't support [older](https://devguide.python.org/versions/) versions of Python.

## Getting started

### 1. Register your application

To call the Copilot endpoints, your app must acquire an access token from the Microsoft identity platform. Learn more about this:

- [Authentication and authorization basics for Microsoft](https://docs.microsoft.com/en-us/graph/auth/auth-concepts)
- [Register your app with the Microsoft identity platform](https://docs.microsoft.com/en-us/graph/auth-register-app-v2)

### 2. Install the required packages

```cmd
pip install azure-identity
pip install python-dotenv
```

The `python-dotenv` is a utility library to load environment variables. Ensure you **DO NOT** commit the file holding your secrets.

You have to build `microsoft-agents-m365copilot-core` locally. To build it, run the following command from the root of the `python` folder:

```cmd
pip install -r requirements-dev.txt
```

This will install the core library with the latest version attached to it in the environment.

Alternatively, you can switch to the root of the core library and run:

```cmd
pip install -e .
```

This will install the core library and it's dependencies to the environment.

### 3. Create a `.env` file with the following values:

```
TENANT_ID = "YOUR_TENANT_ID"
CLIENT_ID = "YOUR_CLIENT_ID"
```

>**Note:**
>
> Your tenant must have a Microsoft 365 Copilot license.

### 4. Create a `main.py` file with the following snippet:

```python
import asyncio
import os
from datetime import datetime

from azure.identity import DeviceCodeCredential
from dotenv import load_dotenv
from kiota_abstractions.api_error import APIError

from microsoft_agents_m365copilot_beta import AgentsM365CopilotBetaServiceClient
from microsoft_agents_m365copilot_beta.generated.copilot.retrieval.retrieval_post_request_body import (
    RetrievalPostRequestBody,
)
from microsoft_agents_m365copilot_beta.generated.models.retrieval_data_source import RetrievalDataSource

load_dotenv()

TENANT_ID = os.getenv("TENANT_ID")
CLIENT_ID = os.getenv("CLIENT_ID")

# Define a proper callback function that accepts all three parameters
def auth_callback(verification_uri: str, user_code: str, expires_on: datetime):
    print(f"\nTo sign in, use a web browser to open the page {verification_uri}")
    print(f"Enter the code {user_code} to authenticate.")
    print(f"The code will expire at {expires_on}")

# Create device code credential with correct callback
credentials = DeviceCodeCredential(
    client_id=CLIENT_ID,
    tenant_id=TENANT_ID,
    prompt_callback=auth_callback
)

# Use the Graph API beta endpoint explicitly
scopes = ['https://graph.microsoft.com/.default']
client = AgentsM365CopilotBetaServiceClient(credentials=credentials, scopes=scopes)

# Make sure the base URL is set to beta
client.request_adapter.base_url = "https://graph.microsoft.com/beta"

async def retrieve():
    try:
        # Print the URL being used
        print(f"Using API base URL: {client.request_adapter.base_url}\n")
            
        # Create the retrieval request body
        retrieval_body = RetrievalPostRequestBody()
        retrieval_body.data_source = RetrievalDataSource.SharePoint
        retrieval_body.query_string = "What is the latest in my organization?"
            
        # Try more parameters that might be required
        # retrieval_body.maximum_number_of_results = 10
            
        # Make the API call
        print("Making retrieval API request...")
        retrieval = await client.copilot.retrieval.post(retrieval_body)
        
        # Process the results
        if retrieval and hasattr(retrieval, "retrieval_hits"):
            print(f"Received {len(retrieval.retrieval_hits)} hits")
            for r in retrieval.retrieval_hits:
                print(f"Web URL: {r.web_url}\n")
                for extract in r.extracts:
                    print(f"Text:\n{extract.text}\n")
        else:
            print(f"Retrieval response structure: {dir(retrieval)}")
    except APIError as e:
        print(f"Error: {e.error.code}: {e.error.message}")
        if hasattr(e, 'error') and hasattr(e.error, 'inner_error'):
            print(f"Inner error details: {e.error.inner_error}")
        raise e

# Run the async function
asyncio.run(retrieve())
```

### 5. If successful, you should get a list of `retrievalHits` collection.

> **Note**:
> This client library offers an asynchronous API by default. Async is a concurrency model that is far more efficient than multi-threading, and can provide significant performance benefits and enable the use of long-lived network connections such as WebSockets. We support popular python async environments such as `asyncio`, `anyio` or `trio`. For authentication you need to use one of the async credential classes from `azure.identity`.

## Telemetry Metadata

This library captures metadata by default that provides insights into its usage and helps to improve the developer experience. This metadata includes the `SdkVersion`, `RuntimeEnvironment` and `HostOs` on which the client is running.

## Issues

View or log issues on the [Issues](https://github.com/microsoft/Agents-M365Copilot/issues) tab in the repo and tag them as `python` or `python-core`.

## Copyright and license

Copyright (c) Microsoft Corporation. All Rights Reserved. Licensed under the MIT [license](https://github.com/microsoft/Agents-M365Copilot/tree/main/python/LICENSE).

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
