from enum import Enum

class AnalyticsActivityType(str, Enum):
    Email = "Email",
    Meeting = "Meeting",
    Focus = "Focus",
    Chat = "Chat",
    Call = "Call",

