from enum import Enum

class DerivedCredentialProviderType(str, Enum):
    # No Derived Credential Provider Configured.
    NotConfigured = "notConfigured",
    # Entrust.
    EntrustDataCard = "entrustDataCard",
    # Purebred - Defense Information Systems Agency.
    Purebred = "purebred",
    # Xtec - AuthentX.
    XTec = "xTec",
    # Intercede.
    Intercede = "intercede",

