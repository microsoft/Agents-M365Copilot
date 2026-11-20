from enum import Enum

class PrivilegeManagementElevationType(str, Enum):
    # Default. If the type was unknown on the client for some reasons.
    Undetermined = "undetermined",
    # The elevation was done without any use of endpoint privilege management. For example: the administrator on a client machine elevated an application with their admin right.
    UnmanagedElevation = "unmanagedElevation",
    # The elevation was done using the endpoint privilege management zero touch elevation policy.
    ZeroTouchElevation = "zeroTouchElevation",
    # The elevation was done using the endpoint privilege management user confirmed elevation policy.
    UserConfirmedElevation = "userConfirmedElevation",
    # The elevation was done using the endpoint privilege management support approved elevation policy.
    SupportApprovedElevation = "supportApprovedElevation",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

