from enum import Enum

class ZebraFotaConnectorState(str, Enum):
    # Default value when the connector has not been setup (the feature has not been used yet).
    None_ = "none",
    # Connected state indicates that Intune is linked to Zebra Update Services for the current tenant.
    Connected = "connected",
    # Disconnected state indicates that the account was connected in the past and later disconnected.
    Disconnected = "disconnected",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

