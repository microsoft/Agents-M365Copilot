from enum import Enum

class UserAssetIdentifier(str, Enum):
    AccountObjectId = "accountObjectId",
    AccountSid = "accountSid",
    AccountUpn = "accountUpn",
    AccountName = "accountName",
    AccountDomain = "accountDomain",
    AccountId = "accountId",
    RequestAccountSid = "requestAccountSid",
    RequestAccountName = "requestAccountName",
    RequestAccountDomain = "requestAccountDomain",
    RecipientObjectId = "recipientObjectId",
    ProcessAccountObjectId = "processAccountObjectId",
    InitiatingAccountSid = "initiatingAccountSid",
    InitiatingProcessAccountUpn = "initiatingProcessAccountUpn",
    InitiatingAccountName = "initiatingAccountName",
    InitiatingAccountDomain = "initiatingAccountDomain",
    ServicePrincipalId = "servicePrincipalId",
    ServicePrincipalName = "servicePrincipalName",
    TargetAccountUpn = "targetAccountUpn",
    UnknownFutureValue = "unknownFutureValue",

