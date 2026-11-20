from enum import Enum

class WindowsAutopilotProfileAssignmentDetailedStatus(str, Enum):
    # No assignment detailed status
    None_ = "none",
    # Hardware requirements are not met. This can happen if a self-deploying AutoPilot Profile is assigned to a device without TPM 2.0.
    HardwareRequirementsNotMet = "hardwareRequirementsNotMet",
    # Indicates that a Surface Hub AutoPilot Profile is assigned to a device that is not Surface Hub(Aruba).
    SurfaceHubProfileNotSupported = "surfaceHubProfileNotSupported",
    # Indicates that a HoloLens AutoPilot Profile is assigned to a device that is not HoloLens.
    HoloLensProfileNotSupported = "holoLensProfileNotSupported",
    # Indicates that a Windows PC AutoPilot Profile is assigned to a device that is not Windows PC.
    WindowsPcProfileNotSupported = "windowsPcProfileNotSupported",
    # Indicates that a surface Hub 2S  AutoPilot Profile is assigned to a device that is not surface Hub 2S.
    SurfaceHub2SProfileNotSupported = "surfaceHub2SProfileNotSupported",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

