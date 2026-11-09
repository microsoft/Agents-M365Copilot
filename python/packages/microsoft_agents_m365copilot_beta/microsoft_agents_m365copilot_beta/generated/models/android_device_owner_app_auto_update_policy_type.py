from enum import Enum

class AndroidDeviceOwnerAppAutoUpdatePolicyType(str, Enum):
    # Not configured; this value is ignored.
    NotConfigured = "notConfigured",
    # The user can control auto-updates.
    UserChoice = "userChoice",
    # Apps are never auto-updated.
    Never = "never",
    # Apps are auto-updated over Wi-Fi only.
    WiFiOnly = "wiFiOnly",
    # Apps are auto-updated at any time. Data charges may apply.
    Always = "always",

