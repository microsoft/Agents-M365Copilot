from enum import Enum

class PlannerPlanContextType(str, Enum):
    TeamsTab = "teamsTab",
    SharePointPage = "sharePointPage",
    MeetingNotes = "meetingNotes",
    Other = "other",
    UnknownFutureValue = "unknownFutureValue",
    LoopPage = "loopPage",
    Project = "project",

