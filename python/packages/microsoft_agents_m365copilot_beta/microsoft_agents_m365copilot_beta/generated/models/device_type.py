from enum import Enum

class DeviceType(str, Enum):
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
    # Windows 10x device.
    Windows10x = "windows10x",
    # Android non Google managed device.
    AndroidnGMS = "androidnGMS",
    # ChromeOS device.
    ChromeOS = "chromeOS",
    # Linux device.
    Linux = "linux",
    # Indicates managed device is running on visionOS operating system.
    VisionOS = "visionOS",
    # Indicates managed device is running on tvOS operating system.
    TvOS = "tvOS",
    # Blackberry.
    Blackberry = "blackberry",
    # Palm.
    Palm = "palm",
    # Represents that the device type is unknown.
    Unknown = "unknown",
    # Cloud PC device.
    CloudPC = "cloudPC",

