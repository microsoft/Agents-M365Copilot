from enum import Enum

class PlannerRelationshipUserRoles(str, Enum):
    DefaultRules = "defaultRules",
    GroupOwners = "groupOwners",
    GroupMembers = "groupMembers",
    TaskAssignees = "taskAssignees",
    Applications = "applications",
    UnknownFutureValue = "unknownFutureValue",

