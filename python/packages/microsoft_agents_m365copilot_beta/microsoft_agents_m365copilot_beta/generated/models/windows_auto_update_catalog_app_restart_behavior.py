from enum import Enum

class WindowsAutoUpdateCatalogAppRestartBehavior(str, Enum):
    # Indicates that the Intune management extension restarts the device only if the app installer returns an exit code that signals a reboot is required (e.g., exit code 3010).
    BasedOnReturnCode = "basedOnReturnCode",
    # Indicates that the Intune management extension does not take any specific action to control restarts. If the app installer initiates a restart (e.g., an MSI with ForceReboot action), it is allowed to proceed.
    Allow = "allow",
    # Indicates that the Intune management extension attempts to suppress restarts initiated by the installer. For MSI-based installations, this passes the REBOOT=ReallySuppress property to msiexec. Not all installers honor suppression.
    Suppress = "suppress",
    # Indicates that the Intune management extension forces an immediate device restart after the app installation completes, regardless of the installer's exit code.
    Force = "force",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

