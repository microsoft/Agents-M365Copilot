from enum import Enum

class MailboxRecipientType(str, Enum):
    Unknown = "unknown",
    User = "user",
    Linked = "linked",
    Shared = "shared",
    Room = "room",
    Equipment = "equipment",
    Others = "others",

