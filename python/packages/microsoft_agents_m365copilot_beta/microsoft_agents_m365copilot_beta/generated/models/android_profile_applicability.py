from enum import Enum

class AndroidProfileApplicability(str, Enum):
    Default = "default",
    AndroidWorkProfile = "androidWorkProfile",
    AndroidDeviceOwner = "androidDeviceOwner",

