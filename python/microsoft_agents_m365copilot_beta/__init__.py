"""
Python client for the Microsoft CCS Python SDK.
"""
from ._version import VERSION
from .service_client import MicrosoftAgentsM365CopilotServiceClient
from .request_adapter import MicrosoftAgentsM365CopilotRequestAdapter

__version__ = VERSION

__all__ = [
    "MicrosoftAgentsM365CopilotServiceClient", "MicrosoftAgentsM365CopilotRequestAdapter"
]
