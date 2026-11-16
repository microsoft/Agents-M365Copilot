from enum import Enum

class MailboxAssetIdentifier(str, Enum):
    AccountUpn = "accountUpn",
    FileOwnerUpn = "fileOwnerUpn",
    InitiatingProcessAccountUpn = "initiatingProcessAccountUpn",
    LastModifyingAccountUpn = "lastModifyingAccountUpn",
    TargetAccountUpn = "targetAccountUpn",
    SenderFromAddress = "senderFromAddress",
    SenderDisplayName = "senderDisplayName",
    RecipientEmailAddress = "recipientEmailAddress",
    SenderMailFromAddress = "senderMailFromAddress",
    UnknownFutureValue = "unknownFutureValue",

