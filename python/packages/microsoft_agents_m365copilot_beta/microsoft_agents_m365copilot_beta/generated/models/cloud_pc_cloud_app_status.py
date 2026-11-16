from enum import Enum

class CloudPcCloudAppStatus(str, Enum):
    Preparing = "preparing",
    Ready = "ready",
    Publishing = "publishing",
    Published = "published",
    Unpublishing = "unpublishing",
    Failed = "failed",
    UnknownFutureValue = "unknownFutureValue",

