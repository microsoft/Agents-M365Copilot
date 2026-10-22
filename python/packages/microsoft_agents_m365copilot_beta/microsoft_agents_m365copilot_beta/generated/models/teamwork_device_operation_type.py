from enum import Enum

class TeamworkDeviceOperationType(str, Enum):
    DeviceRestart = "deviceRestart",
    ConfigUpdate = "configUpdate",
    DeviceDiagnostics = "deviceDiagnostics",
    SoftwareUpdate = "softwareUpdate",
    DeviceManagementAgentConfigUpdate = "deviceManagementAgentConfigUpdate",
    RemoteLogin = "remoteLogin",
    RemoteLogout = "remoteLogout",
    UnknownFutureValue = "unknownFutureValue",

