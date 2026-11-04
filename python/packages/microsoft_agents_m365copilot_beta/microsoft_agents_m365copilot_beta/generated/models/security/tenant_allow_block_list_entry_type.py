from enum import Enum

class TenantAllowBlockListEntryType(str, Enum):
    Url = "url",
    FileHash = "fileHash",
    Sender = "sender",
    Recipient = "recipient",
    UnknownFutureValue = "unknownFutureValue",

