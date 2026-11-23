from enum import Enum

class RepositoryPullRequestState(str, Enum):
    # Pull request is open.
    Open = "open",
    # Pull request is closed.
    Closed = "closed",
    # A marker value for members added after the release of this API.
    UnknownFutureValue = "unknownFutureValue",
    # Pull request was merged.
    Merged = "merged",

