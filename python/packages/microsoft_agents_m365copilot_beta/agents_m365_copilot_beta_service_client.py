# ------------------------------------
# Copyright (c) Microsoft Corporation. All Rights Reserved.
# Licensed under the MIT License.
# See License in the project root for license information.
# -----------------------------------

from __future__ import annotations
from typing import List, Optional, TYPE_CHECKING, Union
from azure.core.credentials import TokenCredential
from azure.core.credentials_async import AsyncTokenCredential
from kiota_authentication_azure.azure_identity_authentication_provider import AzureIdentityAuthenticationProvider

from .generated.base_agents_m365_copilot_beta_service_client import BaseAgentsM365CopilotBetaServiceClient
from .agents_m365_copilot_beta_request_adapter import AgentsM365CopilotBetaRequestAdapter

if TYPE_CHECKING:
    from .generated.copilot.users.users_request_builder import AiUserItemRequestBuilder
    from microsoft_agents_m365copilot_core import BatchRequestBuilder

class AgentsM365CopilotBetaServiceClient(BaseAgentsM365CopilotBetaServiceClient):

    def __init__(
        self,
        credentials: Optional[Union[TokenCredential, AsyncTokenCredential]] = None,
        scopes: Optional[List[str]] = None,
        request_adapter: Optional[AgentsM365CopilotBetaRequestAdapter] = None,
    ) -> None:
        """Constructs a client instance to use for making requests.

        Args:
            credentials (Union[TokenCredential, AsyncTokenCredential]): The
            tokenCredential to use for authentication. 
            scopes (Optional[List[str]]): The scopes to use for authentication.
            Defaults to ['https://graph.microsoft.com/.default'].
            request_adapter (Optional[AgentsM365CopilotBetaRequestAdapter], optional): The request
            adapter to use for requests. Defaults to None.
        """

        if not request_adapter:
            if not credentials:
                raise ValueError("Missing request adapter or valid credentials")

            if scopes:
                auth_provider = AzureIdentityAuthenticationProvider(credentials, scopes=scopes)
            else:
                auth_provider = AzureIdentityAuthenticationProvider(credentials)

            request_adapter = AgentsM365CopilotBetaRequestAdapter(auth_provider)

        super().__init__(request_adapter)
