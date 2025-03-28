# Microsoft Agents M365 Copilot Core Python Client Library

The Microsoft Agents M365 Copilot Core Python Client Library contains core classes used by [Microsoft Agents M365 Copilot Python Client Library](https://github.com/microsof/agents-m365copilot/python) to send native HTTP requests to [Microsoft Graph API](https://graph.microsoft.com).

## Prerequisites

1. Python 3.9+

This library doesn't support [older](https://devguide.python.org/versions/) versions of Python.

## Getting started

### 1. Register your application

To call the Copilot endpoints, your app must acquire an access token from the Microsoft identity platform. Learn more about this -

- [Authentication and authorization basics for Microsoft Graph](https://docs.microsoft.com/en-us/graph/auth/auth-concepts)
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


### 3. Call the client

```python
import asyncio
import os

from azure.identity.aio import ClientSecretCredential
from dotenv import load_dotenv
from kiota_abstractions.api_error import APIError

from microsoft_agents_m365copilot_beta import MicrosoftAgentsM365CopilotServiceClient
from microsoft_agents_m365copilot_beta.generated.copilot.retrieval.retrieval_post_request_body import (
    RetrievalPostRequestBody,
)

load_dotenv()

TENANT_ID = os.getenv("TENANT_ID")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET_ID = os.getenv("CLIENT_SECRET_ID")

credentials = ClientSecretCredential(TENANT_ID, CLIENT_ID, CLIENT_SECRET_ID)
scopes = ['https://graph.microsoft.com/.default']
client = MicrosoftAgentsM365CopilotServiceClient(credentials=credentials, scopes=scopes)


async def retrieve():
    try:
        retrieval_body = RetrievalPostRequestBody()
        retrieval_body.query_string = "What is the latest in my organization"
        retrieval = await client.copilot.retrieval.post(retrieval_body)
        if retrieval:
            for r in retrieval["retrievalHits"]:
                print(r)
    except APIError as e:
        print(f"Error: {e.error.code}: {e.error.message}")
        raise e


asyncio.run(retrieve())
```

> **Note**:
> This client library offers an asynchronous API by default. Async is a concurrency model that is far more efficient than multi-threading, and can provide significant performance benefits and enable the use of long-lived network connections such as WebSockets. We support popular python async environments such as `asyncio`, `anyio` or `trio`. For authentication you need to use one of the async credential classes from `azure.identity`.

## Telemetry Metadata

This library captures metadata by default that provides insights into its usage and helps to improve the developer experience. This metadata includes the `SdkVersion`, `RuntimeEnvironment` and `HostOs` on which the client is running.

## Issues

View or log issues on the [Issues](https://github.com/microsof/agents-m365copilot/issues) tab in the repo and tag them as `python` or `python-core`.

## Contributing

Please see the [contributing guidelines](CONTRIBUTING.md).

## Copyright and license

Copyright (c) Microsoft Corporation. All Rights Reserved. Licensed under the MIT [license](LICENSE).

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
