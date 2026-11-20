from enum import Enum

class AndroidDeviceOwnerEnrollmentMode(str, Enum):
    CorporateOwnedDedicatedDevice = "corporateOwnedDedicatedDevice",
    CorporateOwnedFullyManaged = "corporateOwnedFullyManaged",
    CorporateOwnedWorkProfile = "corporateOwnedWorkProfile",
    # Corporate owned, userless Android Open Source Project (AOSP) device, without Google Mobile Services.
    CorporateOwnedAOSPUserlessDevice = "corporateOwnedAOSPUserlessDevice",
    # Corporate owned, user-associated Android Open Source Project (AOSP) device, without Google Mobile Services.
    CorporateOwnedAOSPUserAssociatedDevice = "corporateOwnedAOSPUserAssociatedDevice",

