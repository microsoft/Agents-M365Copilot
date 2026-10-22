from enum import Enum

class DriverApprovalStatus(str, Enum):
    # This indicates a driver needs IT admin's review.
    NeedsReview = "needsReview",
    # This indicates IT admin has declined a driver.
    Declined = "declined",
    # This indicates IT admin has approved a driver.
    Approved = "approved",
    # This indicates IT admin has suspended a driver.
    Suspended = "suspended",

