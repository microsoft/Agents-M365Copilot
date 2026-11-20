from enum import Enum

class LocalSecurityOptionsInformationDisplayedOnLockScreenType(str, Enum):
    # Not Configured
    NotConfigured = "notConfigured",
    # User display name, domain and user names
    Administrators = "administrators",
    # User display name only
    AdministratorsAndPowerUsers = "administratorsAndPowerUsers",
    # Do not display user information
    AdministratorsAndInteractiveUsers = "administratorsAndInteractiveUsers",

