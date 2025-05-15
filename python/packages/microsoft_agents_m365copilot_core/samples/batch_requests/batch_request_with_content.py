# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
#pylint: disable=undefined-variable
"""Demonstrates using the Batch request with content"""
import asyncio

from kiota_abstractions.headers_collection import HeadersCollection as RequestHeaders
from kiota_abstractions.method import Method
from kiota_abstractions.request_information import RequestInformation

from microsoft_agents_m365copilot_core import (
    BatchRequestContent,
    BatchRequestItem,
    MicrosoftAgentsM365CopilotClient,
)

# Create a client
# code to create a copilot client
copilot_client = MicrosoftAgentsM365CopilotClient(credentials=token, scopes=copilot_scopes)

# Create a  request adapter from the clinet
request_adapter = copilot_client.request_adapter

# Create batch Items
request_info1 = RequestInformation()
request_info1.http_method = "GET"
request_info1.url = "https://graph.microsoft.com/v1.0/me"
request_info1.url = "/me"

request_info1.headers = RequestHeaders()
request_info1.headers.add("Content-Type", "application/json")

request_info2 = RequestInformation()
request_info2.http_method = "GET"
request_info2.url = "/users"
request_info2.headers = RequestHeaders()
request_info2.headers.add("Content-Type", "application/json")

batch_request_item1 = BatchRequestItem(request_information=request_info1)
batch_request_item2 = BatchRequestItem(request_information=request_info2)

# Create a batch request content
batch_request_content = {
    batch_request_item1.id: batch_request_item1,
    batch_request_item2.id: batch_request_item2
}
batch_content = BatchRequestContent(batch_request_content)


async def main():
    batch_response_content = await copilot_client.batch.post(batch_request_content=batch_content)

    # Print the batch response content
    print(f"Batch Response Content: {batch_response_content.responses}")
    for response in batch_response_content.responses:
        print(f"Request ID: {response.id}, Status: {response.status}")
        print(f"Response body: {response.body}, headers: {response.headers}")
        print("-------------------------------------------------------------")


asyncio.run(main())
