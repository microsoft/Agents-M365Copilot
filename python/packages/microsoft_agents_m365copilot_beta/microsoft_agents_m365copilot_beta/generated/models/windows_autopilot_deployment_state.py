from enum import Enum

class WindowsAutopilotDeploymentState(str, Enum):
    # The deployment state is unknown.
    Unknown = "unknown",
    # The deployment succeeded.
    Success = "success",
    # The deployment state is in progress.
    InProgress = "inProgress",
    # The deployment failed.
    Failure = "failure",
    # The deployment timed out but user clicked past failure.
    SuccessWithTimeout = "successWithTimeout",
    # The deployment was not run.
    NotAttempted = "notAttempted",
    # The deployment is disabled.
    Disabled = "disabled",
    # The deployment succeeded after hitting an initial timeout failure.
    SuccessOnRetry = "successOnRetry",

