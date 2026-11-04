from enum import Enum

class PrivilegeManagementProcessType(str, Enum):
    # Default. If the type was unknown on the client for some reasons
    Undefined = "undefined",
    # The elevated process is a parent process
    Parent = "parent",
    # The elevated process is a child process
    Child = "child",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

