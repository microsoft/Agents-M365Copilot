# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
import platform
import re
import uuid

import httpx
import pytest

from microsoft_agents_m365copilot_core import (
    SDK_VERSION,
    APIVersion,
    MicrosoftAgentsM365CopilotRequestContext,
    MicrosoftAgentsM365CopilotTelemetryHandler,
    MicrosoftAgentsM365CopilotTelemetryHandlerOption,
    NationalClouds,
)

BASE_URL = NationalClouds.Global + '/' + APIVersion.v1


def test_is_graph_url(mock_graph_request):
    """
    Test method that checks whether a request url is a graph endpoint
    """
    telemetry_handler = MicrosoftAgentsM365CopilotTelemetryHandler()
    assert telemetry_handler.is_graph_url(mock_graph_request.url)


def test_is_not_graph_url(mock_request):
    """
    Test method that checks whether a request url is a graph endpoint with a
    non-graph url.
    """
    telemetry_handler = MicrosoftAgentsM365CopilotTelemetryHandler()
    assert not telemetry_handler.is_graph_url(mock_request.url)


def test_add_client_request_id_header(mock_graph_request):
    """
    Test that client_request_id is added to the request headers
    """
    telemetry_handler = MicrosoftAgentsM365CopilotTelemetryHandler()
    telemetry_handler._add_client_request_id_header(mock_graph_request)

    assert 'client-request-id' in mock_graph_request.headers
    assert _is_valid_uuid(mock_graph_request.headers.get('client-request-id'))


def test_custom_client_request_id_header():
    """
    Test that a custom client request id is used, if provided
    """
    custom_id = str(uuid.uuid4())
    request = httpx.Request('GET', BASE_URL)
    request.context = MicrosoftAgentsM365CopilotRequestContext({}, {'client-request-id': custom_id})

    telemetry_handler = MicrosoftAgentsM365CopilotTelemetryHandler()
    telemetry_handler._add_client_request_id_header(request)

    assert 'client-request-id' in request.headers
    assert _is_valid_uuid(request.headers.get('client-request-id'))
    assert request.headers.get('client-request-id') == custom_id


def test_append_sdk_version_header(mock_graph_request):
    """
    Test that sdkVersion is added to the request headers
    """
    telemetry_handler = MicrosoftAgentsM365CopilotTelemetryHandler()
    telemetry_handler._append_sdk_version_header(mock_graph_request, telemetry_handler.options)

    assert 'sdkVersion' in mock_graph_request.headers
    assert mock_graph_request.headers.get('sdkVersion'
                                          ).startswith('microsoft-agents-m365copilot-core/' + SDK_VERSION)


def test_append_sdk_version_header_beta(mock_graph_request):
    """
    Test that sdkVersion is added to the request headers
    """
    telemetry_options = MicrosoftAgentsM365CopilotTelemetryHandlerOption(
        api_version=APIVersion.beta, sdk_version='1.0.0'
    )
    telemetry_handler = MicrosoftAgentsM365CopilotTelemetryHandler(options=telemetry_options)
    telemetry_handler._append_sdk_version_header(mock_graph_request, telemetry_options)

    assert 'sdkVersion' in mock_graph_request.headers
    assert mock_graph_request.headers.get('sdkVersion').startswith('microsoft-agents-m365copilot-beta/' + '1.0.0')


def test_add_host_os_header(mock_graph_request):
    """
    Test that HostOs is added to the request headers
    """
    system = platform.system()
    version = platform.version()
    host_os = f'{system} {version}'

    telemetry_handler = MicrosoftAgentsM365CopilotTelemetryHandler()
    telemetry_handler._add_host_os_header(mock_graph_request)

    assert 'HostOs' in mock_graph_request.headers
    assert mock_graph_request.headers.get('HostOs') == host_os


def test_add_runtime_environment_header(mock_graph_request):
    """
    Test that RuntimeEnvironment is added to the request headers
    """
    python_version = platform.python_version()
    runtime_environment = f'Python/{python_version}'

    telemetry_handler = MicrosoftAgentsM365CopilotTelemetryHandler()
    telemetry_handler._add_runtime_environment_header(mock_graph_request)

    assert 'RuntimeEnvironment' in mock_graph_request.headers
    assert mock_graph_request.headers.get('RuntimeEnvironment') == runtime_environment


def _is_valid_uuid(guid):
    regex = "^[{]?[0-9a-fA-F]{8}" + "-([0-9a-fA-F]{4}-)" + "{3}[0-9a-fA-F]{12}[}]?$"
    pattern = re.compile(regex)
    if re.search(pattern, guid):
        return True
    return False
