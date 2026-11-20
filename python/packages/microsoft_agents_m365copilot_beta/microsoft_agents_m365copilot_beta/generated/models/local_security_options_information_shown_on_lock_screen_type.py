from enum import Enum

class LocalSecurityOptionsInformationShownOnLockScreenType(str, Enum):
    # Not Configured
    NotConfigured = "notConfigured",
    # User display name, domain and user names
    UserDisplayNameDomainUser = "userDisplayNameDomainUser",
    # User display name only
    UserDisplayNameOnly = "userDisplayNameOnly",
    # Do not display user information
    DoNotDisplayUser = "doNotDisplayUser",

