from enum import Enum

class ContentModelType(str, Enum):
    TeachingMethod = "teachingMethod",
    LayoutMethod = "layoutMethod",
    FreeformSelectionMethod = "freeformSelectionMethod",
    PrebuiltContractModel = "prebuiltContractModel",
    PrebuiltInvoiceModel = "prebuiltInvoiceModel",
    PrebuiltReceiptModel = "prebuiltReceiptModel",
    UnknownFutureValue = "unknownFutureValue",

