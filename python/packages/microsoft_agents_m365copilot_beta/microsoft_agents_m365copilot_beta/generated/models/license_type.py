from enum import Enum

class LicenseType(str, Enum):
    # Indicates the tenant has neither trial or paid license.
    NotPaid = "notPaid",
    # Indicates the tenant has paid Endpoint Privilege Management license.
    Paid = "paid",
    # Indicates the tenant has trial Endpoint Privilege Management license.
    Trial = "trial",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

