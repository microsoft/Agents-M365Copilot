from enum import Enum

class MarkUserAsCompromisedEntityIdentifier(str, Enum):
    AccountObjectId = "accountObjectId",
    InitiatingProcessAccountObjectId = "initiatingProcessAccountObjectId",
    ServicePrincipalId = "servicePrincipalId",
    RecipientObjectId = "recipientObjectId",
    UnknownFutureValue = "unknownFutureValue",

