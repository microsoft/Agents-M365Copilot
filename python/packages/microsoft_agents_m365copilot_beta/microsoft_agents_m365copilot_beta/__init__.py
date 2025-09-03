# ------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  
# Licensed under the MIT License.  See License in the project root for license information.
# ------------------------------------------------------------------------------

"""
Python client for the Microsoft CCS Python SDK.
"""
from ._version import VERSION
from .agents_m365_copilot_beta_request_adapter import AgentsM365CopilotBetaRequestAdapter
from .agents_m365_copilot_beta_service_client import AgentsM365CopilotBetaServiceClient

__version__ = VERSION

__all__ = [
    "AgentsM365CopilotBetaServiceClient", "AgentsM365CopilotBetaRequestAdapter"
]
