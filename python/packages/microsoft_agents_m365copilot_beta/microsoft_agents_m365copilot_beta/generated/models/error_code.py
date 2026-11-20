from enum import Enum

class ErrorCode(str, Enum):
    # Default Value to indicate no error.
    NoError = "noError",
    # The current user does not have access due to lack of RBAC permissions on the resource.
    Unauthorized = "unauthorized",
    # The current user does not have access due to lack of RBAC Scope Tags on the resource.
    NotFound = "notFound",
    # The resource has been deleted.
    Deleted = "deleted",

