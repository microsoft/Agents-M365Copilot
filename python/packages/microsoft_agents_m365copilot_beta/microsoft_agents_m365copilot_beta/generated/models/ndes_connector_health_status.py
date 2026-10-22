from enum import Enum

class NdesConnectorHealthStatus(str, Enum):
    # Health has not been evaluated yet for this connector.
    Unknown = "unknown",
    # All health checks are passing. Error rates are below the attention threshold for all metrics.
    NoActionRequired = "noActionRequired",
    # One or more health checks have error rates between the attention and action thresholds.
    AttentionRequired = "attentionRequired",
    # One or more health checks have error rates above the action threshold. Investigation is required.
    ActionRequired = "actionRequired",
    # The connector has not connected within the staleness threshold. Applied at read time based on lastConnectionDateTime.
    Disconnected = "disconnected",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

