from enum import Enum

class AndroidManagedStoreAccountAppSyncStatus(str, Enum):
    Success = "success",
    CredentialsNotValid = "credentialsNotValid",
    AndroidForWorkApiError = "androidForWorkApiError",
    ManagementServiceError = "managementServiceError",
    UnknownError = "unknownError",
    None_ = "none",

