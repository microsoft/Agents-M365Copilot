import pytest
from kiota_http.kiota_client_factory import KiotaClientFactory

from microsoft_agents_m365copilot_core import (
    AsyncMicrosoftAgentsM365CopilotTransport,
    FeatureUsageFlag,
    MicrosoftAgentsM365CopilotRequestContext,
)


def test_set_request_context_and_feature_usage(mock_request, mock_transport):
    middleware = KiotaClientFactory.get_default_middleware(None)
    pipeline = KiotaClientFactory.create_middleware_pipeline(middleware, mock_transport)
    transport = AsyncMicrosoftAgentsM365CopilotTransport(mock_transport, pipeline)
    transport.set_request_context_and_feature_usage(mock_request)

    assert hasattr(mock_request, 'context')
    assert isinstance(mock_request.context, MicrosoftAgentsM365CopilotRequestContext)
    assert mock_request.context.feature_usage == hex(
        FeatureUsageFlag.RETRY_HANDLER_ENABLED | FeatureUsageFlag.REDIRECT_HANDLER_ENABLED
    )
