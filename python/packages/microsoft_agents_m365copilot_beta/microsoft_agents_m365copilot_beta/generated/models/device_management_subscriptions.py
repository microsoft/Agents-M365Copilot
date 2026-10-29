from enum import Enum

class DeviceManagementSubscriptions(str, Enum):
    # None
    None_ = "none",
    # Microsoft Intune Subscription
    Intune = "intune",
    # Office365 Subscription
    Office365 = "office365",
    # Microsoft Intune Premium Subscription
    IntunePremium = "intunePremium",
    # Microsoft Intune for Education Subscription
    Intune_EDU = "intune_EDU",
    # Microsoft Intune for Small Businesses Subscription
    Intune_SMB = "intune_SMB",

