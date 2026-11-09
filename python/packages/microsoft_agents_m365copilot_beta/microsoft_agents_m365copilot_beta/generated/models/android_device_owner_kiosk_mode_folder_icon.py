from enum import Enum

class AndroidDeviceOwnerKioskModeFolderIcon(str, Enum):
    # Not configured; this value is ignored.
    NotConfigured = "notConfigured",
    # Folder icon appears as dark square.
    DarkSquare = "darkSquare",
    # Folder icon appears as dark circle.
    DarkCircle = "darkCircle",
    # Folder icon appears as light square.
    LightSquare = "lightSquare",
    # Folder icon appears as light circle  .
    LightCircle = "lightCircle",

