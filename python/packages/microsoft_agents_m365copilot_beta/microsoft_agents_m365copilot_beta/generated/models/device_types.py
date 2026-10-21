from enum import Enum

class DeviceTypes(str, Enum):
    # Desktop.
    Desktop = "desktop",
    # WindowsRT.
    WindowsRT = "windowsRT",
    # WinMO6.
    WinMO6 = "winMO6",
    # Nokia.
    Nokia = "nokia",
    # Windows phone.
    WindowsPhone = "windowsPhone",
    # Mac.
    Mac = "mac",
    # WinCE.
    WinCE = "winCE",
    # WinEmbedded.
    WinEmbedded = "winEmbedded",
    # iPhone.
    IPhone = "iPhone",
    # iPad.
    IPad = "iPad",
    # iPodTouch.
    IPod = "iPod",
    # Android.
    Android = "android",
    # iSocConsumer.
    ISocConsumer = "iSocConsumer",
    # Unix.
    Unix = "unix",
    # Mac OS X client using built in MDM agent.
    MacMDM = "macMDM",
    # Representing the fancy Windows 10 goggles.
    HoloLens = "holoLens",
    # Surface HUB device.
    SurfaceHub = "surfaceHub",
    # Android for work device.
    AndroidForWork = "androidForWork",
    # Android enterprise device.
    AndroidEnterprise = "androidEnterprise",
    # Blackberry.
    Blackberry = "blackberry",
    # Palm.
    Palm = "palm",
    # Represents that the device type is unknown.
    Unknown = "unknown",

