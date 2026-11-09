from enum import Enum

class WindowsDefenderApplicationControlSupplementalPolicyStatuses(str, Enum):
    # The status of the WindowsDefenderApplicationControl supplemental policy is not known.
    Unknown = "unknown",
    # The WindowsDefenderApplicationControl supplemental policy is in effect.
    Success = "success",
    # The WindowsDefenderApplicationControl supplemental policy is structurally okay but there is an error with authorizing the token.
    TokenError = "tokenError",
    # The token does not authorize this WindowsDefenderApplicationControl supplemental policy.
    NotAuthorizedByToken = "notAuthorizedByToken",
    # The WindowsDefenderApplicationControl supplemental policy is not found.
    PolicyNotFound = "policyNotFound",

