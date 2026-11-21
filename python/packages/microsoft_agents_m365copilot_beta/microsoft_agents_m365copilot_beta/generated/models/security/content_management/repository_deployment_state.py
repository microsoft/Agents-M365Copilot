from enum import Enum

class RepositoryDeploymentState(str, Enum):
    # Deployment is in progress.
    InProgress = "inProgress",
    # Deployment completed.
    Completed = "completed",
    # Deployment is queued.
    Queued = "queued",
    # Deployment is being canceled.
    Canceling = "canceling",
    # A marker value for members added after the release of this API.
    UnknownFutureValue = "unknownFutureValue",

