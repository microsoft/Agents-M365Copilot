from enum import Enum

class CostManagementUnit(str, Enum):
    # The current Copilot Credits consumption unit.
    CopilotCredit = "copilotCredit",
    # A marker value for members added after the release of this API.
    UnknownFutureValue = "unknownFutureValue",

