from enum import Enum

class AndroidUsernameSource(str, Enum):
    # The username.
    Username = "username",
    # The user principal name.
    UserPrincipalName = "userPrincipalName",
    # The user sam account name.
    SamAccountName = "samAccountName",
    # Primary SMTP address.
    PrimarySmtpAddress = "primarySmtpAddress",

