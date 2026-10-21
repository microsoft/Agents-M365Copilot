from enum import Enum

class GroupPolicyType(str, Enum):
    # Group Policy administrative templates built-in to the Policy configuration service provider (CSP).
    AdmxBacked = "admxBacked",
    # Group Policy administrative templates installed using the Policy configuration service provider (CSP).
    AdmxIngested = "admxIngested",

