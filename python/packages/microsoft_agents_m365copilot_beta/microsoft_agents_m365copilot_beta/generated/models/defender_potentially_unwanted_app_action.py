from enum import Enum

class DefenderPotentiallyUnwantedAppAction(str, Enum):
    # PUA Protection is off. Defender will not protect against potentially unwanted applications.
    DeviceDefault = "deviceDefault",
    # PUA Protection is on. Detected items are blocked. They will show in history along with other threats.
    Block = "block",
    # Audit mode. Defender will detect potentially unwanted applications, but take no actions. You can review information about applications Defender would have taken action against by searching for events created by Defender in the Event Viewer.
    Audit = "audit",

