from enum import Enum

class DeviceManagementDomainJoinConnectorState(str, Enum):
    # Connector is actively pinging Intune.
    Active = "active",
    # There is no heart-beat from connector from last one hour.
    Error = "error",
    # There is no heart-beat from connector from last 5 days.
    Inactive = "inactive",

