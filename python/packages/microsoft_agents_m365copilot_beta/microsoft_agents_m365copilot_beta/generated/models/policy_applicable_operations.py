from enum import Enum

class PolicyApplicableOperations(str, Enum):
    Create = "create",
    UpdateOrUpsert = "updateOrUpsert",
    Delete = "delete",
    InvokeAction = "invokeAction",
    UnknownFutureValue = "unknownFutureValue",

