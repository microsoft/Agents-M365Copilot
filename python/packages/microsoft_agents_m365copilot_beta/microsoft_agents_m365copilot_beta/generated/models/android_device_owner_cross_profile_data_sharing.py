from enum import Enum

class AndroidDeviceOwnerCrossProfileDataSharing(str, Enum):
    # Not configured; this value defaults to CROSS_PROFILE_DATA_SHARING_UNSPECIFIED.
    NotConfigured = "notConfigured",
    # Data cannot be shared from both the personal profile to work profile and the work profile to the personal profile.
    CrossProfileDataSharingBlocked = "crossProfileDataSharingBlocked",
    # Prevents users from sharing data from the work profile to apps in the personal profile. Personal data can be shared with work apps.
    DataSharingFromWorkToPersonalBlocked = "dataSharingFromWorkToPersonalBlocked",
    # Data from either profile can be shared with the other profile.
    CrossProfileDataSharingAllowed = "crossProfileDataSharingAllowed",
    # Unknown future value (reserved, not used right now)
    UnkownFutureValue = "unkownFutureValue",

