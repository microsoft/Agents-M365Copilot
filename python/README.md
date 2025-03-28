# Microsoft Agents M365 Copilot Python SDK

## Versions

1. [Beta](./microsoft_agents_m365copilot_beta/)
1. v1.0 - Coming soon.

### Beta SDK example

1. Create a `.env` file with the following values:

```
TENANT_ID = "YOUR_TENANT_ID"
CLIENT_ID = "YOUR_CLIENT_ID"
CLIENT_SECRET_ID = "YOUR_CLIENT_SECRET_ID"
```

> **NOTE:**
> Your tenant has to be able to access copilot.

2. Create a `main.py` file with the following snippet:

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

1. If successful, you should get a list of `retrievalHits` collection.

```json
{
    "retrievalHits": [
        {
            "webUrl": "https://microsoft-my.sharepoint-df.com/personal/andia_com/Documents/Contoso marketing.pptx",
            "extracts": [
                {
                    "text": "Some long extracts that can be implemented to improve future projects."
                }
            ],
            "resourceType": "listItem",
            "sensitivityLabel": {
                "sensitivityLabelId": "9fbde396-1a24-4c79-8edf-9254a0f35055",
                "displayName": "Confidential\\Company",
                "tooltip": "Data is classified and protected. Recipient can unprotect content with the right justification.",
                "priority": 5,
                "color": "#FF8C00",
                "isEncrypted": true
            }
        },
        {
            "webUrl": "https://microsoft.sharepoint-df.com/teams/Contoso/Engineering/Engineering System.one",
            "extracts": [
                {
                    "text": "Some other long text"
            ],
            "resourceType": "listItem",
            "sensitivityLabel": {
                "sensitivityLabelId": "1a19d03a-48bc-4359-8038-5b5f6d5847c3",
                "displayName": "Confidential\\Any User (No Protection)",
                "tooltip": "Data is classified as Confidential but is NOT PROTECTED to allow access by approved NDA business partners If a higher level of protection is needed, please use the Sensitivity button on the tool bar to change the protection level.",
                "priority": 4,
                "color": "#FF8C00"
            }
        }
    ]
}
```
