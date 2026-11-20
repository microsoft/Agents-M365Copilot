from enum import Enum

class CostManagementFundingClass(str, Enum):
    # Drawn from a prepaid Copilot Credits pool.
    Prepaid = "prepaid",
    # Billed on demand, with no prepaid pool.
    PayAsYouGo = "payAsYouGo",
    # Consumed above the purchased pool. Unbilled, not an invoiced excess charge.
    Overage = "overage",
    # Consumed but not billed.
    NonBillable = "nonBillable",
    # A marker value for members added after the release of this API.
    UnknownFutureValue = "unknownFutureValue",

