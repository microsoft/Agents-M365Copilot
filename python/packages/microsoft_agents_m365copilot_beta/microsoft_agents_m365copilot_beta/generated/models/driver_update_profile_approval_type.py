from enum import Enum

class DriverUpdateProfileApprovalType(str, Enum):
    # This indicates a driver and firmware profile needs to be approved manually.
    Manual = "manual",
    # This indicates a driver and firmware profile is approved automatically.
    Automatic = "automatic",

