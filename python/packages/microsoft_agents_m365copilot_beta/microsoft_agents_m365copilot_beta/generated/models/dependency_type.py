from enum import Enum

class DependencyType(str, Enum):
    SourceFinishDrivesTargetStart = "sourceFinishDrivesTargetStart",
    SourceStartDrivesTargetStart = "sourceStartDrivesTargetStart",
    SourceFinishDrivesTargetFinish = "sourceFinishDrivesTargetFinish",
    TargetStartDrivesSourceFinish = "targetStartDrivesSourceFinish",
    UnknownFutureValue = "unknownFutureValue",

