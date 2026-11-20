from enum import Enum

class AndroidManagedStoreAccountEnrollmentTarget(str, Enum):
    None_ = "none",
    All = "all",
    Targeted = "targeted",
    TargetedAsEnrollmentRestrictions = "targetedAsEnrollmentRestrictions",

