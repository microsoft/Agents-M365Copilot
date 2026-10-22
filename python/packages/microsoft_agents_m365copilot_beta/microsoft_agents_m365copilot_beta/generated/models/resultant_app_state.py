from enum import Enum

class ResultantAppState(str, Enum):
    # The application is not applicable.
    NotApplicable = "notApplicable",
    # The application is installed with no errors.
    Installed = "installed",
    # The application failed to install.
    Failed = "failed",
    # The application is not installed.
    NotInstalled = "notInstalled",
    # The application failed to uninstall.
    UninstallFailed = "uninstallFailed",
    # The installation of the application is in progress.
    PendingInstall = "pendingInstall",
    # The status of the application is unknown.
    Unknown = "unknown",

