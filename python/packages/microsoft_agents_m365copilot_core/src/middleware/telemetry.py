import http
import json
import platform

import httpx
from kiota_http.middleware import BaseMiddleware
from urllib3.util import parse_url

from .._constants import SDK_VERSION
from .._enums import APIVersion, NationalClouds
from .async_transport import AsyncMicrosoftAgentsM365CopilotTransport
from .options import MicrosoftAgentsM365CopilotTelemetryHandlerOption
from .request_context import MicrosoftAgentsM365CopilotRequestContext


class MicrosoftAgentsM365CopilotRequest(httpx.Request):
    context: MicrosoftAgentsM365CopilotRequestContext


class MicrosoftAgentsM365CopilotTelemetryHandler(BaseMiddleware):
    """Middleware component that attaches metadata to a MicrosoftAgentsM365CopilotRequest request in
    order to help the SDK team improve the developer experience.
    """

    def __init__(self, options=MicrosoftAgentsM365CopilotTelemetryHandlerOption(), **kwargs):
        """Create an instance of MicrosoftAgentsM365CopilotTelemetryHandler

        Args:
            options (MicrosoftAgentsM365CopilotTelemetryHandlerOption, optional): The telemetry handler
            options value. Defaults to MicrosoftAgentsM365CopilotTelemetryHandlerOption
        """
        super().__init__()
        self.options = options

    async def send(
        self, request: MicrosoftAgentsM365CopilotRequest,
        transport: AsyncMicrosoftAgentsM365CopilotTransport
    ):
        """Adds telemetry headers and sends the http request.
        """
        current_options = self._get_current_options(request)

        if self.is_graph_url(request.url):
            self._add_client_request_id_header(request)
            self._append_sdk_version_header(request, current_options)
            self._add_host_os_header(request)
            self._add_runtime_environment_header(request)

        response = await super().send(request, transport)
        return response

    def _get_current_options(
        self, request: httpx.Request
    ) -> MicrosoftAgentsM365CopilotTelemetryHandlerOption:
        """Returns the options to use for the request.Overrides default options if
        request options are passed.

        Args:
            request (httpx.Request): The prepared request object

        Returns:
            MicrosoftAgentsM365CopilotTelemetryHandlerOption: The options to used.
        """
        current_options = self.options
        request_options = request.context.middleware_control.get(              # type:ignore
            MicrosoftAgentsM365CopilotTelemetryHandlerOption.get_key()
        )
        # Override default options with request options
        if request_options:
            current_options = request_options

        return current_options

    def is_graph_url(self, url):
        """Check if the request is made to a graph endpoint. We do not add telemetry headers to
        non-graph endpoints"""
        endpoints = set(item.value for item in NationalClouds)

        base_url = parse_url(str(url))
        endpoint = f"{base_url.scheme}://{base_url.netloc}"
        return endpoint in endpoints

    def _add_client_request_id_header(self, request) -> None:
        """Add a client-request-id header with GUID value to request"""
        request.headers.update({'client-request-id': f'{request.context.client_request_id}'})

    def _append_sdk_version_header(self, request, options) -> None:
        """Add SdkVersion request header to each request to identify the language and
        version of the client SDK library(s).
        Also adds the featureUsage value.
        """
        core_library_name = f'microsoft-agents-m365copilot-core/{SDK_VERSION}'
        service_lib_name = ''

        if options.api_version == APIVersion.v1:
            service_lib_name = f'microsoft-agents-m365copilot/{options.sdk_version}'
        if options.api_version == APIVersion.beta:
            service_lib_name = f'microsoft-agents-m365copilot-beta/{options.sdk_version}'

        if service_lib_name:
            telemetry_header_string = f'{service_lib_name}, '\
                f'{core_library_name} (featureUsage={request.context.feature_usage})'
        else:
            telemetry_header_string = f'{core_library_name} '\
                '(featureUsage={request.context.feature_usage})'

        if 'sdkVersion' in request.headers:
            sdk_version = request.headers.get('sdkVersion')
            if not sdk_version == telemetry_header_string:
                request.headers.update({'sdkVersion': telemetry_header_string})
        else:
            request.headers.update({'sdkVersion': telemetry_header_string})

    def _add_host_os_header(self, request) -> None:
        """
        Add HostOS request header to each request to help identify the OS
        on which our client SDK is running on
        """
        system = platform.system()
        version = platform.version()
        host_os = f'{system} {version}'
        request.headers.update({'HostOs': host_os})

    def _add_runtime_environment_header(self, request) -> None:
        """
        Add RuntimeEnvironment request header to capture the runtime framework
         on which the client SDK is running on.
        """
        python_version = platform.python_version()
        runtime_environment = f'Python/{python_version}'
        request.headers.update({'RuntimeEnvironment': runtime_environment})
