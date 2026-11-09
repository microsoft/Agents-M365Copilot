from enum import Enum

class PermissionsDefinitionIdentityType(str, Enum):
    User = "user",
    Role = "role",
    Application = "application",
    ManagedIdentity = "managedIdentity",
    ServiceAccount = "serviceAccount",
    UnknownFutureValue = "unknownFutureValue",

