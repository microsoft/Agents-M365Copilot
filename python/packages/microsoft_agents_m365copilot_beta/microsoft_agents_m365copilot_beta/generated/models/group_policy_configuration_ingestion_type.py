from enum import Enum

class GroupPolicyConfigurationIngestionType(str, Enum):
    # Unknown policy configuration ingestion type
    Unknown = "unknown",
    # Indicates policy created have definitions ingested by IT admin with sufficient permissions through custom ingestion process
    Custom = "custom",
    # Indicates policy created have definitions ingested through system ingestion process
    BuiltIn = "builtIn",
    # Indicated atleast 1 tenant admin & system ingested definitions configured for this policy
    Mixed = "mixed",
    # Unknown future enum value
    UnknownFutureValue = "unknownFutureValue",

