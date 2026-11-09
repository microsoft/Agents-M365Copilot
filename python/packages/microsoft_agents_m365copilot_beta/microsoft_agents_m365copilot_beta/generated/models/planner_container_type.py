from enum import Enum

class PlannerContainerType(str, Enum):
    Group = "group",
    UnknownFutureValue = "unknownFutureValue",
    Roster = "roster",
    Project = "project",
    DriveItem = "driveItem",
    User = "user",
    TeamsChannel = "teamsChannel",
    OnlineMeeting = "onlineMeeting",
    PlannerTask = "plannerTask",
    OfficeDocument = "officeDocument",
    Meeting = "meeting",
    DataverseProject = "dataverseProject",

