from enum import Enum

class DeviceManagementConfigurationSecretSettingValueState(str, Enum):
    # default invalid value
    Invalid = "invalid",
    # secret value is not encrypted
    NotEncrypted = "notEncrypted",
    # a token for the encrypted value is returned by the service
    EncryptedValueToken = "encryptedValueToken",

