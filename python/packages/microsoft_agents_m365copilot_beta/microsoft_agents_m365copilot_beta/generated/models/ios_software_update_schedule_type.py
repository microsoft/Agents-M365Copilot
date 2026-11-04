from enum import Enum

class IosSoftwareUpdateScheduleType(str, Enum):
    # Update outside of active hours.
    UpdateOutsideOfActiveHours = "updateOutsideOfActiveHours",
    # Always update.
    AlwaysUpdate = "alwaysUpdate",
    # Update during time windows.
    UpdateDuringTimeWindows = "updateDuringTimeWindows",
    # Update outside of time windows.
    UpdateOutsideOfTimeWindows = "updateOutsideOfTimeWindows",

