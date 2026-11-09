from enum import Enum

class ServiceSettingState(str, Enum):
    # The service is governed by the policy.
    Enabled = "enabled",
    # The service is excluded from the policy.
    Disabled = "disabled",
    # A marker value for members added after the release of this API.
    UnknownFutureValue = "unknownFutureValue",

