from enum import Enum

class EmailType(str, Enum):
    Unknown = "unknown",
    Work = "work",
    Personal = "personal",
    Main = "main",
    Other = "other",

