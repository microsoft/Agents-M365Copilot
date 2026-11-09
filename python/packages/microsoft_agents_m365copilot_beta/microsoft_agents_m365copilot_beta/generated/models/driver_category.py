from enum import Enum

class DriverCategory(str, Enum):
    # This indicates a driver is recommended by Microsoft.
    Recommended = "recommended",
    # This indicates a driver was recommended by Microsoft and IT admin has taken some approval action on it.
    PreviouslyApproved = "previouslyApproved",
    # This indicates a driver is never recommended by Microsoft.
    Other = "other",

