from enum import Enum

class MicrosoftTunnelServerHealthStatus(str, Enum):
    # Indicates that the health status of the server is unknown. This occurs when no health status has been reported, for example when the server is initialized, but has not yet been evaluated for its health.
    Unknown = "unknown",
    # Indicates that the health status of the server is healthy. This should be the normal operational health status.
    Healthy = "healthy",
    # Indicates that the health status of the server is unhealthy. This is normally a transient condition that will last up to 5 minutes. If the server cannot be remediated while reporting unhealthy state, the health state will change to 'warning'. If it can be remediated, the health state will return to 'healthy'.
    Unhealthy = "unhealthy",
    # Indicates a warning based on the Tunnel Gateway server's CPU usage, memory usage, latency, TLS certificate, version
    Warning = "warning",
    # Indicates the server state is offline
    Offline = "offline",
    # Indicates the upgrade in progress during the upgrade cycle of when Intune begins upgrading servers, one server at a time
    UpgradeInProgress = "upgradeInProgress",
    # Indicates the failure of the upgrade during the upgrade cycle of when Intune begins upgrading servers, one server at a time
    UpgradeFailed = "upgradeFailed",
    # Evolvable enumeration sentinel value. Do not use enums.
    UnknownFutureValue = "unknownFutureValue",

