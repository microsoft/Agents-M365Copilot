from enum import Enum

class CertificateValidityPeriodScale(str, Enum):
    # Days.
    Days = "days",
    # Months.
    Months = "months",
    # Years.
    Years = "years",

