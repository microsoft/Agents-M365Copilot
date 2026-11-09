from enum import Enum

class RemoteAssistanceState(str, Enum):
    # Remote assistance is disabled for the account. With this value, Quick Assist remote assistance sessions are not allowed for the account.
    Disabled = "disabled",
    # Remote assistance is enabled for the account. With this value, enterprise Quick Assist remote assistance features are provided.
    Enabled = "enabled",

