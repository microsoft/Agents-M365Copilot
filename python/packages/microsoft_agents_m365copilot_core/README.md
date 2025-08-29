#  Microsoft 365 Copilot APIs Python Core Client Library

The  Microsoft 365 Copilot APIs Python Core Client Library contains core classes used by the [Microsoft 365 Copilot APIs Library](https://github.com/microsoft/Agents-M365Copilot/tree/main/python) to send native HTTP requests to the [Microsoft 365 Copilot APIs](https://aka.ms/M365CopilotAPIs).

> **Note:**
>
> Because the Microsoft 365 Copilot APIs in the beta endpoint are subject to breaking changes, don't use a preview release of the client libraries in production apps.

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

> **Note:**
>
> Your tenant must have a Microsoft 365 Copilot license.

### 4. Create a `main.py` file with the following snippet:

> **Note:**
>
> This example shows how to make a call to the Microsoft 365 Copilot Retrieval API using just the core library. Alternately, you can use the [Microsoft 365 Copilot APIs Python Beta Client Library](https://github.com/microsoft/Agents-M365Copilot/tree/main/python/packages/microsoft_agents_m365copilot_beta) to create a request object and then run the POST method on the request.

```python
import asyncio
import os
from datetime import datetime

from azure.identity import DeviceCodeCredential
from dotenv import load_dotenv 

from microsoft_agents_m365copilot_core.src._enums import APIVersion
from microsoft_agents_m365copilot_core.src.client_factory import  MicrosoftAgentsM365CopilotClientFactory

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

client = MicrosoftAgentsM365CopilotClientFactory.create_with_default_middleware(api_version=APIVersion.beta)

client.base_url = "https://graph.microsoft.com/beta" # Make sure the base URL is set to beta

async def retrieve():
    try:
        # Kick off device code flow and get the token.
        loop = asyncio.get_running_loop()
        token = await loop.run_in_executor(None, lambda: credentials.get_token("https://graph.microsoft.com/.default"))

        # Set the access token.
        headers = {"Authorization": f"Bearer {token.token}"}

        # Print the URL being used.
        print(f"Using API base URL for incoming request: {client.base_url}\n")

        # Directly use httpx to test the endpoint.
        response = await client.post("https://graph.microsoft.com/beta/copilot/retrieval", json={
            "queryString": "What is the latest in my organization?",
            "dataSource": "sharePoint",
            "resourceMetadata": [
                "title",
                "author"
            ],
            "maximumNumberOfResults": "10"
        }, headers=headers)

        # Show the response
        print(f"Response HTTP status: {response.status_code}")
        print(f"Response JSON content: {response.text}")
            
    finally:
        print("Your call to the Copilot APIs is now complete.")

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
