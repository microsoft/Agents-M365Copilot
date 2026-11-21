from enum import Enum

class RepositoryDeploymentResult(str, Enum):
    # Deployment succeeded.
    Success = "success",
    # Deployment was canceled.
    Canceled = "canceled",
    # Deployment failed.
    Failed = "failed",
    # A marker value for members added after the release of this API.
    UnknownFutureValue = "unknownFutureValue",
    # The deployment has not produced a final result yet.
    Pending = "pending",

