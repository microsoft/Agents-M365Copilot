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
from .models import PageResult, LargeFileUploadSession, UploadResult, UploadSessionDataHolder
from .requests import (
    BatchRequestBuilder,
    BatchRequestContent,
    BatchRequestContentCollection,
    BatchRequestItem,
    BatchResponseContent,
    BatchResponseContentCollection,
    BatchResponseItem,
)

from .middleware import MicrosoftAgentsM365CopilotTelemetryHandlerOption, MicrosoftAgentsM365CopilotRequestContext, AsyncMicrosoftAgentsM365CopilotTransport, MicrosoftAgentsM365CopilotTelemetryHandler
from .tasks import PageIterator, LargeFileUploadTask

__all__ = [
    "BatchRequestBuilder", "BatchRequestContentCollection", "BatchRequestContent",
    "BatchRequestItem", "BatchResponseContentCollection", "BatchResponseContent",
    "BatchResponseItem", "MicrosoftAgentsM365CopilotClientFactory",
    "BaseMicrosoftAgentsM365CopilotRequestAdapter", "PageResult", "PageIterator",
    "AzureIdentityAuthenticationProvider", "FeatureUsageFlag", "NationalClouds", "APIVersion",
    "LargeFileUploadTask", "LargeFileUploadSession", "UploadResult", "UploadSessionDataHolder",
    "MicrosoftAgentsM365CopilotTelemetryHandlerOption", "MicrosoftAgentsM365CopilotRequestContext",
    "AsyncMicrosoftAgentsM365CopilotTransport", "MicrosoftAgentsM365CopilotTelemetryHandler"
]

__version__ = SDK_VERSION
