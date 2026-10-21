from enum import Enum

class UsernameSource(str, Enum):
    # User principal name.
    UserPrincipalName = "userPrincipalName",
    # Primary SMTP address.
    PrimarySmtpAddress = "primarySmtpAddress",
    # The user sam account name.
    SamAccountName = "samAccountName",

