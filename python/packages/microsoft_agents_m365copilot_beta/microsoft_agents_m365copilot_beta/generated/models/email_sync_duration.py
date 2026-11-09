from enum import Enum

class EmailSyncDuration(str, Enum):
    # User Defined, default value, no intent.
    UserDefined = "userDefined",
    # Sync one day of email.
    OneDay = "oneDay",
    # Sync three days of email.
    ThreeDays = "threeDays",
    # Sync one week of email.
    OneWeek = "oneWeek",
    # Sync two weeks of email.
    TwoWeeks = "twoWeeks",
    # Sync one month of email.
    OneMonth = "oneMonth",
    # Sync an unlimited duration of email.
    Unlimited = "unlimited",

