from enum import Enum

class SharedPCAllowedAccountType(str, Enum):
    # Not configured. Default value.
    NotConfigured = "notConfigured",
    # Only guest accounts.
    Guest = "guest",
    # Only domain-joined accounts.
    Domain = "domain",

