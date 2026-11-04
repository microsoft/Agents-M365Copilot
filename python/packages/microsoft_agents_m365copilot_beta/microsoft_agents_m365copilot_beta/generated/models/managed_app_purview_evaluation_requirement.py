from enum import Enum

class ManagedAppPurviewEvaluationRequirement(str, Enum):
    # Microsoft Purview Data Loss Prevention (DLP) content evaluation is not required.
    NotRequired = "notRequired",
    # Microsoft Purview Data Loss Prevention (DLP) content evaluation is required when online; sharing is allowed if the service is unreachable.
    RequiredWhenOnline = "requiredWhenOnline",
    # Microsoft Purview Data Loss Prevention (DLP) content evaluation is always required; sharing is blocked if the service is unreachable.
    Required = "required",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

