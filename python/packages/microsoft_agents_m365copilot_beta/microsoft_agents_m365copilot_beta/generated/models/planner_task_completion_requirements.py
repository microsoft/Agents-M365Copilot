from enum import Enum

class PlannerTaskCompletionRequirements(str, Enum):
    None_ = "none",
    ChecklistCompletion = "checklistCompletion",
    UnknownFutureValue = "unknownFutureValue",
    FormCompletion = "formCompletion",
    ApprovalCompletion = "approvalCompletion",
    CompletionInHostedApp = "completionInHostedApp",

