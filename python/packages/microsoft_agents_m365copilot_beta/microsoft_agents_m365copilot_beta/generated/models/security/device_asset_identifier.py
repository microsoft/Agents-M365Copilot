from enum import Enum

class DeviceAssetIdentifier(str, Enum):
    DeviceId = "deviceId",
    DeviceName = "deviceName",
    RemoteDeviceName = "remoteDeviceName",
    TargetDeviceName = "targetDeviceName",
    DestinationDeviceName = "destinationDeviceName",
    UnknownFutureValue = "unknownFutureValue",

