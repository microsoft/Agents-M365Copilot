from enum import Enum

class AndroidDeviceOwnerSystemUpdateInstallType(str, Enum):
    # Device default behavior, which typically prompts the user to accept system updates.
    DeviceDefault = "deviceDefault",
    # Postpone automatic install of updates up to 30 days.
    Postpone = "postpone",
    # Install automatically inside a daily maintenance window.
    Windowed = "windowed",
    # Automatically install updates as soon as possible.
    Automatic = "automatic",

