from enum import Enum

class WindowsAutopilotDeviceType(str, Enum):
    # Default. Indicates that the device type  is a Windows PC.
    WindowsPc = "windowsPc",
    # Indicates that the device type is a HoloLens.
    HoloLens = "holoLens",
    # Surface Hub 2
    SurfaceHub2 = "surfaceHub2",
    # SurfaceHub2S
    SurfaceHub2S = "surfaceHub2S",
    # VirtualMachine
    VirtualMachine = "virtualMachine",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

