from enum import Enum

class AndroidForWorkSyncStatus(str, Enum):
    Success = "success",
    CredentialsNotValid = "credentialsNotValid",
    AndroidForWorkApiError = "androidForWorkApiError",
    ManagementServiceError = "managementServiceError",
    UnknownError = "unknownError",
    None_ = "none",

