from enum import Enum

class NetworkSingleSignOnType(str, Enum):
    # Disabled
    Disabled = "disabled",
    # Pre-Logon
    Prelogon = "prelogon",
    # Post-Logon
    Postlogon = "postlogon",

