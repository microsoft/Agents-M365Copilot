from enum import Enum

class AndroidTargetedPlatforms(str, Enum):
    # Indicates the Android targeted platform is Android Device Administrator.
    AndroidDeviceAdministrator = "androidDeviceAdministrator",
    # Indicates the Android targeted platform is Android Open Source Project.
    AndroidOpenSourceProject = "androidOpenSourceProject",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

