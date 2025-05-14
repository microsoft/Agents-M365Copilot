"""
Python client for the Microsoft CCS Python SDK.
"""
from ._version import VERSION
from .agents_m365_copilot_beta_systems_client import MicrosoftAgentsM365CopilotServiceClient
from .agents_m365_copilot_beta_request_adapter import MicrosoftAgentsM365CopilotBetaRequestAdapter

__version__ = VERSION

__all__ = [
    "MicrosoftAgentsM365CopilotServiceClient", "MicrosoftAgentsM365CopilotBetaRequestAdapter"
]
