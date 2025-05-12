# Microsoft Agents M365 Copilot Python SDK

## Versions

1. [Beta](./microsoft_agents_m365copilot_beta/)
1. v1.0 - Coming soon.

### Beta SDK example

1. Create a `.env` file with the following values:

    ```
    TENANT_ID = "YOUR_TENANT_ID"
    CLIENT_ID = "YOUR_CLIENT_ID"
    ```

    **NOTE:**
    
    > Your tenant has to have a Copilot license.

2. Create a `main.py` file with the following snippet:

    ```python
    import asyncio
    import os
    from datetime import datetime

    from azure.identity import DeviceCodeCredential
    from dotenv import load_dotenv
    from kiota_abstractions.api_error import APIError

    from microsoft_agents_m365copilot_beta import MicrosoftAgentsM365CopilotServiceClient
    from microsoft_agents_m365copilot_beta.generated.copilot.retrieval.retrieval_post_request_body import (
        RetrievalPostRequestBody,
    )

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
    client = MicrosoftAgentsM365CopilotServiceClient(credentials=credentials, scopes=scopes)

    # Make sure the base URL is set to beta
    client.request_adapter.base_url = "https://graph.microsoft.com/beta"

    async def retrieve():
        try:
            # Print the URL being used
            print(f"Using API base URL: {client.request_adapter.base_url}\n")
            
            # Create the retrieval request body
            retrieval_body = RetrievalPostRequestBody()
            retrieval_body.query_string = "What is the latest in my organization"
            
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

1. If successful, you should get a list of `retrievalHits` collection.

    ```text
    Web URL: https://vladtalkstech.com/microsoft-365/managing-sharepoint-online-storage-everything-you-need-to-know-theory-demo/

    Text:
    Skip to content Home About About Vlad Pluralsight Courses Blogs & Videos All Microsoft 365 SharePoint Microsoft Teams Power Platform Power BI Power Automate Azure Microsoft Copilot Managing SharePoint Online Storage – Everything You NEED to Know | Theory + Demo Managing SharePoint Online storage is no small task! Don’t worry. I’m here to help! This is a clip from my full Configuring and Managing SharePoint Online and OneDrive for Business course available on Pluralsight that goes in-depth into managing the full SharePoint Online and OneDrive for Business services. Full Course Video Summary Here are the key points from the video: Cloud Storage Benefits: One of the main advantages of using cloud services like SharePoint and OneDrive for Business is that you don’t have to manage storage hardware, just the licensing. 

    Web URL: https://vladtalkstech.com/category/microsoft-viva/

    Text:
    Skip to content Home About About Vlad Pluralsight Courses Blogs & Videos All Microsoft 365 SharePoint Microsoft Teams Power Platform Power BI Power Automate Azure Microsoft Copilot Copilot Studio Copilot for Microsoft 365 Learning News Study Guides Power Platform Certifications Microsoft 365 Certifications Security, Compliance, and Identity Certifications Azure Certifications Events and Discount Codes Newsletter Home About About Vlad Pluralsight Courses Blogs & Videos All Microsoft 365 SharePoint Microsoft Teams Power Platform Power BI Power Automate Azure Microsoft Copilot Copilot Studio Copilot for Microsoft 365 Learning News Study Guides Power Platform Certifications Microsoft 365 Certifications Security, Compliance, and Identity Certifications Azure Certifications Events and Discount Codes Newsletter Vlad Talks Microsoft Viva Get the latest news and knowledge on your favorite products and certifications. FULL Microsoft Viva Insights Overview + Guide Microsoft Viva, Viva Insights  Microsoft Viva, Viva Insights  FULL Microsoft Viva Insights Overview + Guide The wealth of knowledge gained through Viva Insights is remarkable.

    Web URL: https://vladtalkstech.com/external-blogs-and-videos/espc24-reporters-vlad-catrinescu-and-frane-borozan/

    Text:
    Skip to content Home About About Vlad Pluralsight Courses Blogs & Videos All Microsoft 365 SharePoint Microsoft Teams Power Platform Power BI Power Automate Azure Microsoft Copilot Copilot Studio Copilot for Microsoft 365 Learning News Study Guides Power Platform Certifications Microsoft 365 Certifications Security, Compliance, and Identity Certifications Azure Certifications Events and Discount Codes Newsletter Home About About Vlad Pluralsight Courses Blogs & Videos All Microsoft 365 SharePoint Microsoft Teams Power Platform Power BI Power Automate Azure Microsoft Copilot Copilot Studio Copilot for Microsoft 365 Learning News Study Guides Power Platform Certifications Microsoft 365 Certifications Security, Compliance, and Identity Certifications Azure Certifications Events and Discount Codes Newsletter [ESPC24 Reporters] Vlad Catrinescu and Frane Borozan Reporter: Vlad Catrinescu Interviewee: Frane Borozan In this insightful conversation, they share their expert take on key challenges like managing stale data, increasing the adoption of sensitivity labels, and ensuring compliance with tools like Copilot. Discover practical advice for organizations looking to implement Copilot effectively, from establishing a baseline for permissions to rolling out Copilot securely and responsibly. Highlights include: Why stale data is a challenge for Copilot and how it might evolve. The untapped potential of sensitivity labels in data governance.

    ...
    ```
