from enum import Enum

class SignInAssistantOptions(str, Enum):
    # Not configured - wlidsvc Start will be set to SERVICE_DEMAND_START.
    NotConfigured = "notConfigured",
    # Disabled - wlidsvc Start will be set to SERVICE_DISABLED.
    Disabled = "disabled",

