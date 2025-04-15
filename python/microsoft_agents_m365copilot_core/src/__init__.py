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
from .models import PageResult, UploadResult, UploadSessionDataHolder

__all__ = [
    "MicrosoftAgentsM365CopilotClientFactory",
    "BaseMicrosoftAgentsM365CopilotRequestAdapter", "PageResult",
    "AzureIdentityAuthenticationProvider", "FeatureUsageFlag", "NationalClouds", "APIVersion",
    "UploadResult", "UploadSessionDataHolder",
    "MicrosoftAgentsM365CopilotTelemetryHandlerOption", "MicrosoftAgentsM365CopilotRequestContext",
    "AsyncMicrosoftAgentsM365CopilotTransport", "MicrosoftAgentsM365CopilotTelemetryHandler"
]

__version__ = SDK_VERSION
