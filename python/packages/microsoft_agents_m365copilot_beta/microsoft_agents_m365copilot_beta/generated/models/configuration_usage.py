from enum import Enum

class ConfigurationUsage(str, Enum):
    # Disallowed.
    Blocked = "blocked",
    # Required.
    Required = "required",
    # Optional.
    Allowed = "allowed",
    # Not Configured.
    NotConfigured = "notConfigured",

