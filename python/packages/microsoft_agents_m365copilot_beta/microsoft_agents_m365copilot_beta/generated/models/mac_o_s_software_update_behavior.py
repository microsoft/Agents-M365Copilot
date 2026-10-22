from enum import Enum

class MacOSSoftwareUpdateBehavior(str, Enum):
    # Not configured.
    NotConfigured = "notConfigured",
    # Download and/or install the software update, depending on the current device state.
    Default = "default",
    # Download the software update without installing it.
    DownloadOnly = "downloadOnly",
    # Install an already downloaded software update.
    InstallASAP = "installASAP",
    # Download the software update and notify the user via the App Store.
    NotifyOnly = "notifyOnly",
    # Download the software update and install it at a later time.
    InstallLater = "installLater",

