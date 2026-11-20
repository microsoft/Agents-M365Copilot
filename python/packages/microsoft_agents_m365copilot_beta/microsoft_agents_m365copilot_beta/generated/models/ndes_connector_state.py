from enum import Enum

class NdesConnectorState(str, Enum):
    # State not available yet for this connector.
    None_ = "none",
    # Ndes connector has connected recently
    Active = "active",
    # No recent activity for the Ndes connector
    Inactive = "inactive",

