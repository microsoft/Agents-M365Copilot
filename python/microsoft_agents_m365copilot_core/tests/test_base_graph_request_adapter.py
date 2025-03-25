import httpx
import pytest
from kiota_abstractions.serialization import (
    ParseNodeFactoryRegistry,
    SerializationWriterFactoryRegistry,
)

from microsoft_agents_m365copilot_core import BaseMicrosoftAgentsM365CopilotRequestAdapter


def test_create_graph_request_adapter(mock_auth_provider):
    request_adapter = BaseMicrosoftAgentsM365CopilotRequestAdapter(mock_auth_provider)
    assert request_adapter._authentication_provider is mock_auth_provider
    assert isinstance(request_adapter._parse_node_factory, ParseNodeFactoryRegistry)
    assert isinstance(
        request_adapter._serialization_writer_factory, SerializationWriterFactoryRegistry
    )
    assert isinstance(request_adapter._http_client, httpx.AsyncClient)
    assert request_adapter.base_url == 'https://graph.microsoft.com/v1.0/'


def test_create_request_adapter_no_auth_provider():
    with pytest.raises(TypeError):
        BaseMicrosoftAgentsM365CopilotRequestAdapter(None)
