from enum import Enum

class ServiceNowConnectionStatus(str, Enum):
    # Tenant has disabled the connection
    Disabled = "disabled",
    # Tenant has enabled the connection
    Enabled = "enabled",
    # Future authentication method to be added here.
    UnknownFutureValue = "unknownFutureValue",

