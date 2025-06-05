# Microsoft Copilot APIs Python Client Library

Integrate the Microsoft Copilot APIs into your Python application!

## Installation

The Copilot APIs Python client libraries will soon to be available in the Python Package Index.

```py
pip install microsoft-agents-m365copilot-beta
```

## Create a Copilot APIs client and make an API call

The following code example shows how to create an instance of a Microsoft 365 Copilot APIs client with an authentication provider in the supported languages. The authentication provider handles acquiring access tokens for the application. Many different authentication providers are available for each language and platform. The different authentication providers support different client scenarios. For details about which provider and options are appropriate for your scenario, see [Choose an Authentication Provider](/graph/sdks/choose-authentication-providers). 

The example also shows how to make a call to the Retrieval API. To call this API, you first need to create a request object and then run the POST method on the request.

The client ID is the app registration ID that is generated when you [register your app in the Azure portal](/graph/auth-register-app-v2).

1. Create a `.env` file with the following values:

    ```
    TENANT_ID = "YOUR_TENANT_ID"
    CLIENT_ID = "YOUR_CLIENT_ID"
    ```

    **NOTE:**
    
    > Your tenant must have a Copilot license.

2. Create a `main.py` file with the following snippet:

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

3. If successful, you should get a list of `retrievalHits` collection.
