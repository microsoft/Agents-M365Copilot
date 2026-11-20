from enum import Enum

class EmailSyncSchedule(str, Enum):
    # User Defined, default value, no intent.
    UserDefined = "userDefined",
    # Sync as messages arrive.
    AsMessagesArrive = "asMessagesArrive",
    # Sync manually.
    Manual = "manual",
    # Sync every fifteen minutes.
    FifteenMinutes = "fifteenMinutes",
    # Sync every thirty minutes.
    ThirtyMinutes = "thirtyMinutes",
    # Sync every sixty minutes.
    SixtyMinutes = "sixtyMinutes",
    # Sync based on my usage.
    BasedOnMyUsage = "basedOnMyUsage",

