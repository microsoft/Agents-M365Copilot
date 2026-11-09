from enum import Enum

class AndroidDeviceOwnerVirtualHomeButtonType(str, Enum):
    # Not configured; this value is ignored.
    NotConfigured = "notConfigured",
    # Swipe-up for home button.
    SwipeUp = "swipeUp",
    # Floating home button.
    Floating = "floating",

