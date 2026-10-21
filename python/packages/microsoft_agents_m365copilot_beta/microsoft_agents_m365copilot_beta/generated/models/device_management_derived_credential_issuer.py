from enum import Enum

class DeviceManagementDerivedCredentialIssuer(str, Enum):
    # Intercede
    Intercede = "intercede",
    # Entrust
    EntrustDatacard = "entrustDatacard",
    # Purebred
    Purebred = "purebred",
    # XTec
    XTec = "xTec",

