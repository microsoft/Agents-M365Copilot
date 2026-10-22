from enum import Enum

class WorkplaceSensorType(str, Enum):
    # The occupancy sensor type.
    Occupancy = "occupancy",
    # The people count sensor type.
    PeopleCount = "peopleCount",
    # The inferred Occupancy sensor type.
    InferredOccupancy = "inferredOccupancy",
    # The heartbeat sensor type.
    Heartbeat = "heartbeat",
    # The badge swipe sensor type.
    Badge = "badge",
    # The unknown feature value.
    UnknownFutureValue = "unknownFutureValue",
    # The Wifi sensor type.
    Wifi = "wifi",

