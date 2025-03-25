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
from ._enums import APIVersion, NationalClouds
from .requests import BatchRequestBuilder, BatchRequestContentCollection, BatchRequestContent, BatchRequestItem, BatchResponseContentCollection, BatchResponseContent, BatchResponseItem
from .authentication import AzureIdentityAuthenticationProvider
from .base_request_adapter import BaseMicrosoftAgentsM365CopilotRequestAdapter
from .client_factory import MicrosoftAgentsM365CopilotClient
from .models import PageResult
from .tasks import PageIterator

__all__ = [
    "BatchRequestBuilder", "BatchRequestContentCollection", "BatchRequestContent", "BatchRequestItem",
    "BatchResponseContentCollection", "BatchResponseContent", "BatchResponseItem", "MicrosoftAgentsM365CopilotClient",
    "BaseMicrosoftAgentsM365CopilotRequestAdapter", "PageResult", "PageIterator", "AzureIdentityAuthenticationProvider"
]


__version__ = SDK_VERSION
