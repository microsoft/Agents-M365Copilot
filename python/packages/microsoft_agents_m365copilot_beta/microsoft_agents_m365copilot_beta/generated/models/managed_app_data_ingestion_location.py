from enum import Enum

class ManagedAppDataIngestionLocation(str, Enum):
    # OneDrive for business
    OneDriveForBusiness = "oneDriveForBusiness",
    # SharePoint Online
    SharePoint = "sharePoint",
    # The device's camera
    Camera = "camera",
    # The device's photo library
    PhotoLibrary = "photoLibrary",

