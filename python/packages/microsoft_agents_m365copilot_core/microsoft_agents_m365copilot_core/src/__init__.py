# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# -----------------------------------

# pylint: disable=line-too-long
# This is to allow complete package description on PyPI
"""
Core components of the Microsoft Microsoft Agents M365 Copilot Python SDK consisting of HTTP Client and a configurable middleware pipeline (Preview).
"""
from ._constants import SDK_VERSION
from ._enums import APIVersion, FeatureUsageFlag, NationalClouds
from .authentication import AzureIdentityAuthenticationProvider
from .base_request_adapter import BaseMicrosoftAgentsM365CopilotRequestAdapter
from .client_factory import MicrosoftAgentsM365CopilotClientFactory
from .middleware import (
    AsyncMicrosoftAgentsM365CopilotTransport,
    MicrosoftAgentsM365CopilotRequestContext,
    MicrosoftAgentsM365CopilotTelemetryHandler,
    MicrosoftAgentsM365CopilotTelemetryHandlerOption,
)

__all__ = [
    "APIVersion",
    "AsyncMicrosoftAgentsM365CopilotTransport",
    "AzureIdentityAuthenticationProvider",
    "BaseMicrosoftAgentsM365CopilotRequestAdapter",
    "FeatureUsageFlag",
    "MicrosoftAgentsM365CopilotClientFactory",
    "MicrosoftAgentsM365CopilotRequestContext",
    "MicrosoftAgentsM365CopilotTelemetryHandler",
    "MicrosoftAgentsM365CopilotTelemetryHandlerOption",
    "NationalClouds"
]

__version__ = SDK_VERSION
