from enum import Enum

class AssignmentFilterEvaluationMode(str, Enum):
    # The filter is evaluated when the device checks in.
    CheckinTimeEvaluation = "checkinTimeEvaluation",
    # The filter is evaluated from inventory-backed device properties.
    InventoryEvaluation = "inventoryEvaluation",
    # The filter requires both check-in-time and inventory-backed device properties.
    MixedEvaluation = "mixedEvaluation",
    # Inventory-based evaluation is disabled for the requesting account.
    Disabled = "disabled",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

