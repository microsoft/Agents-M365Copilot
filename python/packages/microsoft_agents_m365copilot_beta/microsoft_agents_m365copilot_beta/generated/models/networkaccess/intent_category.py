from enum import Enum

class IntentCategory(str, Enum):
    InitialAccess = "initialAccess",
    Persistence = "persistence",
    PrivilegeEscalation = "privilegeEscalation",
    DefenseEvasion = "defenseEvasion",
    CredentialAccess = "credentialAccess",
    Discovery = "discovery",
    LateralMovement = "lateralMovement",
    Execution = "execution",
    Collection = "collection",
    Exfiltration = "exfiltration",
    CommandAndControl = "commandAndControl",
    Impact = "impact",
    ImpairProcessControl = "impairProcessControl",
    InhibitResponseFunction = "inhibitResponseFunction",
    Reconnaissance = "reconnaissance",
    ResourceDevelopment = "resourceDevelopment",
    Evasion = "evasion",
    UnknownFutureValue = "unknownFutureValue",

