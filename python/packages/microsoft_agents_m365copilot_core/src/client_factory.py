# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
from __future__ import annotations

from typing import Optional

import httpx
from kiota_abstractions.request_option import RequestOption
from kiota_http.kiota_client_factory import KiotaClientFactory
from kiota_http.middleware.middleware import BaseMiddleware

from ._enums import APIVersion, NationalClouds
from .middleware import (
    AsyncMicrosoftAgentsM365CopilotTransport,
    MicrosoftAgentsM365CopilotTelemetryHandler,
    MicrosoftAgentsM365CopilotTelemetryHandlerOption,
)


class MicrosoftAgentsM365CopilotClientFactory(KiotaClientFactory):
    """Constructs httpx.AsyncClient instances configured with either custom or default
    pipeline of graph specific middleware.
    """

    @staticmethod
    def create_with_default_middleware( # type: ignore
        # Breaking change to remove KiotaClientFactory as base class
        api_version: APIVersion = APIVersion.v1,
        client: Optional[httpx.AsyncClient] = None,
        host: NationalClouds = NationalClouds.Global,
        options: Optional[dict[str, RequestOption]] = None
    ) -> httpx.AsyncClient:
        """Constructs native HTTP AsyncClient(httpx.AsyncClient) instances configured with
        a custom transport loaded with a default pipeline of middleware.

        Args:
            api_version (APIVersion): The Graph API version to be used.
            Defaults to APIVersion.v1.
            client  (httpx.AsyncClient): The httpx.AsyncClient instance to be used.
            Defaults to KiotaClientFactory.get_default_client().
            host (NationalClouds): The national clound endpoint to be used.
            Defaults to NationalClouds.Global.
            options (Optional[dict[str, RequestOption]]): The request options to use when
            instantiating default middleware. Defaults to dict[str, RequestOption]=None.

        Returns:
            httpx.AsyncClient: An instance of the AsyncClient object
        """
        if client is None:
            client = KiotaClientFactory.get_default_client()
        base_url = MicrosoftAgentsM365CopilotClientFactory._get_base_url(host, api_version)
        client.base_url = base_url
        middleware = KiotaClientFactory.get_default_middleware(options)
        telemetry_handler = MicrosoftAgentsM365CopilotClientFactory._get_telemetry_handler(options)
        middleware.append(telemetry_handler)
        return MicrosoftAgentsM365CopilotClientFactory._load_middleware_to_client(
            client, middleware
        )

    @staticmethod
    def create_with_custom_middleware( # type: ignore
        # Breaking change to remove Kiota client factory as base class
        middleware: Optional[list[BaseMiddleware]],
        api_version: APIVersion = APIVersion.v1,
        client: Optional[httpx.AsyncClient] = None,
        host: NationalClouds = NationalClouds.Global,
    ) -> httpx.AsyncClient:
        """Applies a custom middleware chain to the HTTP Client

        Args:
            middleware(list[BaseMiddleware]): Custom middleware list that will be used to create
            a middleware pipeline. The middleware should be arranged in the order in which they will
            modify the request.
            api_version (APIVersion): The Graph API version to be used.
            Defaults to APIVersion.v1.
            client  (httpx.AsyncClient): The httpx.AsyncClient instance to be used.
            Defaults to KiotaClientFactory.get_default_client().
            host (NationalClouds): The national clound endpoint to be used.
            Defaults to NationalClouds.Global.
        """
        if client is None:
            client = KiotaClientFactory.get_default_client()
        base_url = MicrosoftAgentsM365CopilotClientFactory._get_base_url(host, api_version)
        client.base_url = base_url
        return MicrosoftAgentsM365CopilotClientFactory._load_middleware_to_client(
            client, middleware
        )

    @staticmethod
    def _get_base_url(host: str, api_version: APIVersion) -> str:
        """Helper method to set the complete base url"""
        base_url = f'{host}/{api_version}'
        return base_url

    @staticmethod
    def _get_telemetry_handler(
        options: Optional[dict[str, RequestOption]]
    ) -> MicrosoftAgentsM365CopilotTelemetryHandler:
        """Helper method to get the telemetry handler instantiated with appropriate options"""

        if options:
            telemetry_options: MicrosoftAgentsM365CopilotTelemetryHandlerOption = options.get(
                MicrosoftAgentsM365CopilotTelemetryHandlerOption().get_key()
            )  # type: ignore # Unable to down cast type
            if telemetry_options:
                return MicrosoftAgentsM365CopilotTelemetryHandler(options=telemetry_options)
        return MicrosoftAgentsM365CopilotTelemetryHandler()

    @staticmethod
    def _load_middleware_to_client(
        client: httpx.AsyncClient, middleware: Optional[list[BaseMiddleware]]
    ) -> httpx.AsyncClient:
        current_transport = client._transport
        client._transport = MicrosoftAgentsM365CopilotClientFactory._replace_transport_with_custom_transport(
            current_transport, middleware
        )
        if client._mounts:
            mounts: dict = {}
            for pattern, transport in client._mounts.items():
                if transport is None:
                    mounts[pattern] = None
                else:
                    ps = MicrosoftAgentsM365CopilotClientFactory._replace_transport_with_custom_transport(
                        transport, middleware
                    )
                    mounts[pattern] = ps
            client._mounts = dict(sorted(mounts.items()))
        return client

    @staticmethod
    def _replace_transport_with_custom_transport(
        current_transport: httpx.AsyncBaseTransport, middleware: Optional[list[BaseMiddleware]]
    ) -> AsyncMicrosoftAgentsM365CopilotTransport:
        middleware_pipeline = KiotaClientFactory.create_middleware_pipeline(
            middleware, current_transport
        )
        new_transport = AsyncMicrosoftAgentsM365CopilotTransport(
            transport=current_transport, pipeline=middleware_pipeline
        )
        return new_transport
