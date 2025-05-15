from typing import Optional
import httpx
from kiota_abstractions.authentication import AuthenticationProvider
from kiota_http.middleware.options import UrlReplaceHandlerOption
from microsoft_agents_m365copilot_core import APIVersion, BaseMicrosoftAgentsM365CopilotRequestAdapter, MicrosoftAgentsM365CopilotClientFactory, MicrosoftAgentsM365CopilotTelemetryHandlerOption

from ._version import VERSION

options = {
    MicrosoftAgentsM365CopilotTelemetryHandlerOption.get_key(): MicrosoftAgentsM365CopilotTelemetryHandlerOption(
        api_version=APIVersion.beta,
        sdk_version=VERSION)
}


class AgentsM365CopilotBetaRequestAdapter(BaseMicrosoftAgentsM365CopilotRequestAdapter):
    def __init__(self, auth_provider: AuthenticationProvider,
                 client: Optional[httpx.AsyncClient] = None) -> None:
        if client is None:
            client = MicrosoftAgentsM365CopilotClientFactory.create_with_default_middleware(options=options)
        super().__init__(auth_provider, http_client=client)
