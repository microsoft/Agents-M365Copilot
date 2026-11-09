from enum import Enum

class MobileThreatPartnerTenantState(str, Enum):
    # Partner is unavailable.
    Unavailable = "unavailable",
    # Partner is available.
    Available = "available",
    # Partner is enabled.
    Enabled = "enabled",
    # Partner is unresponsive.
    Unresponsive = "unresponsive",
    # Indicates that the partner connector is not set up. This can occur when the connector is not provisioned and Intune has not received a heartbeat for the connector. Please see https://go.microsoft.com/fwlink/?linkid=2239039 for more information on connector states.
    NotSetUp = "notSetUp",
    # Indicates that the partner connector is in an error state. This can occur when the connector has a non-zero error code set due to an internal error in processing. Please see https://go.microsoft.com/fwlink/?linkid=2239039 for more information on connector states.
    Error = "error",
    # Indicates that the partner connector catalog entry exists but the tenant has never configured it.
    NeverConfigured = "neverConfigured",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

