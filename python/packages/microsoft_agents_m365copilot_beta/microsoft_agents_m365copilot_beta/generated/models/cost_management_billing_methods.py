from enum import Enum

class CostManagementBillingMethods(str, Enum):
    # No billing method is known or was specified.
    NotSpecified = "notSpecified",
    # Prepaid Copilot Credits, purchased through the P3 pre-purchase plan.
    PrepaidCredits = "prepaidCredits",
    # Consumption billed on demand, with no prepaid pool.
    PayAsYouGo = "payAsYouGo",
    # A marker value for members added after the release of this API.
    UnknownFutureValue = "unknownFutureValue",

