from enum import Enum

class AndroidForWorkEnrollmentTarget(str, Enum):
    None_ = "none",
    All = "all",
    Targeted = "targeted",
    TargetedAsEnrollmentRestrictions = "targetedAsEnrollmentRestrictions",

