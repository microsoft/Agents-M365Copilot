import httpx
import pytest
from kiota_abstractions.authentication import AnonymousAuthenticationProvider

from microsoft_agents_m365copilot_core import (
    APIVersion,
    MicrosoftAgentsM365CopilotClientFactory,
    MicrosoftAgentsM365CopilotRequestContext,
    NationalClouds,
)

BASE_URL = NationalClouds.Global + '/' + APIVersion.v1


class MockAuthenticationProvider(AnonymousAuthenticationProvider):

    async def get_authorization_token(self, request: httpx.Request) -> str:
        """Returns a string representing a dummy token
        Args:
            request (GraphRequest): Graph request object
        """
        request.headers['Authorization'] = 'Sample token'
        return


@pytest.fixture
def mock_auth_provider():
    return MockAuthenticationProvider()


@pytest.fixture
def mock_transport():
    client = MicrosoftAgentsM365CopilotClientFactory.create_with_default_middleware()
    return client._transport


@pytest.fixture
def mock_request():
    req = httpx.Request('GET', "https://example.org")
    req.options = {}
    return req


@pytest.fixture
def mock_graph_request():
    req = httpx.Request('GET', BASE_URL)
    req.context = MicrosoftAgentsM365CopilotRequestContext({}, req.headers)
    return req


@pytest.fixture
def mock_response():
    return httpx.Response(
        json={'message': 'Success!'}, status_code=200, headers={"Content-Type": "application/json"}
    )
