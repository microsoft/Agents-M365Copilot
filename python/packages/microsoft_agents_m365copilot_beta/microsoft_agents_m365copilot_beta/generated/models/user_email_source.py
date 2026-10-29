from enum import Enum

class UserEmailSource(str, Enum):
    # User principal name.
    UserPrincipalName = "userPrincipalName",
    # Primary SMTP address.
    PrimarySmtpAddress = "primarySmtpAddress",

