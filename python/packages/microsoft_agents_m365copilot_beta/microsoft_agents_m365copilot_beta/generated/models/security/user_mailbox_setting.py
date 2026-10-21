from enum import Enum

class UserMailboxSetting(str, Enum):
    None_ = "none",
    JunkMailDeletion = "junkMailDeletion",
    IsFromAddressInAddressBook = "isFromAddressInAddressBook",
    IsFromAddressInAddressSafeList = "isFromAddressInAddressSafeList",
    IsFromAddressInAddressBlockList = "isFromAddressInAddressBlockList",
    IsFromAddressInAddressImplicitSafeList = "isFromAddressInAddressImplicitSafeList",
    IsFromAddressInAddressImplicitJunkList = "isFromAddressInAddressImplicitJunkList",
    IsFromDomainInDomainSafeList = "isFromDomainInDomainSafeList",
    IsFromDomainInDomainBlockList = "isFromDomainInDomainBlockList",
    IsRecipientInRecipientSafeList = "isRecipientInRecipientSafeList",
    CustomRule = "customRule",
    JunkMailRule = "junkMailRule",
    SenderPraPresent = "senderPraPresent",
    FromFirstTimeSender = "fromFirstTimeSender",
    Exclusive = "exclusive",
    PriorSeenPass = "priorSeenPass",
    SenderAuthenticationSucceeded = "senderAuthenticationSucceeded",
    IsJunkMailRuleEnabled = "isJunkMailRuleEnabled",
    UnknownFutureValue = "unknownFutureValue",

