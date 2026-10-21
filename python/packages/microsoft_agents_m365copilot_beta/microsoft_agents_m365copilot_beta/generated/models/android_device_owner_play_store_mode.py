from enum import Enum

class AndroidDeviceOwnerPlayStoreMode(str, Enum):
    # Not Configured
    NotConfigured = "notConfigured",
    # Only apps that are in the policy are available and any app not in the policy will be automatically uninstalled from the device.
    AllowList = "allowList",
    # All apps are available and any app that should not be on the device should be explicitly marked as 'BLOCKED' in the applications policy.
    BlockList = "blockList",

