from enum import Enum

class VpnOnDemandRuleConnectionDomainAction(str, Enum):
    # Connect if needed.
    ConnectIfNeeded = "connectIfNeeded",
    # Never connect.
    NeverConnect = "neverConnect",

