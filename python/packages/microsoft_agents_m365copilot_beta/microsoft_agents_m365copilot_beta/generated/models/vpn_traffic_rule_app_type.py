from enum import Enum

class VpnTrafficRuleAppType(str, Enum):
    # The traffic rule is not associated with an app.
    None_ = "none",
    # The traffic rule is associated with a desktop app.
    Desktop = "desktop",
    # The traffic rule is associated with a Universal app.
    Universal = "universal",

