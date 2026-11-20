from enum import Enum

class MacOSSoftwareUpdateState(str, Enum):
    # The software update successfully installed
    Success = "success",
    # The software update is being downloaded
    Downloading = "downloading",
    # The software update has been downloaded
    Downloaded = "downloaded",
    # The software update is being installed
    Installing = "installing",
    # No action is being taken on this software update
    Idle = "idle",
    # The software update is available on the device
    Available = "available",
    # The software update has been scheduled on the device
    Scheduled = "scheduled",
    # The software update download has failed
    DownloadFailed = "downloadFailed",
    # There is not enough space to download the update
    DownloadInsufficientSpace = "downloadInsufficientSpace",
    # There is not enough power to download the update
    DownloadInsufficientPower = "downloadInsufficientPower",
    # There is insufficient network capacity to download the update
    DownloadInsufficientNetwork = "downloadInsufficientNetwork",
    # There is not enough space to install the update
    InstallInsufficientSpace = "installInsufficientSpace",
    # There is not enough power to install the update
    InstallInsufficientPower = "installInsufficientPower",
    # Installation has failed for an unspecified reason
    InstallFailed = "installFailed",
    # The schedule update command has failed for an unspecified reason
    CommandFailed = "commandFailed",

