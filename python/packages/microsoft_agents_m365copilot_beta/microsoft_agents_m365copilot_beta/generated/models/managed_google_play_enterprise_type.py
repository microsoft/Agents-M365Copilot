from enum import Enum

class ManagedGooglePlayEnterpriseType(str, Enum):
    # The enterprise type is not determined or is unknown. This value is not used.
    EnterpriseTypeUnspecified = "enterpriseTypeUnspecified",
    # The enterprise belongs to a managed Google domain.
    ManagedGoogleDomain = "managedGoogleDomain",
    # The enterprise is a managed Google Play Accounts enterprise.
    ManagedGooglePlayAccountsEnterprise = "managedGooglePlayAccountsEnterprise",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

