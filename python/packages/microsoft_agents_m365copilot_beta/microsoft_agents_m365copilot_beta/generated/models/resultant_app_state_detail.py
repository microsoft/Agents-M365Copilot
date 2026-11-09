from enum import Enum

class ResultantAppStateDetail(str, Enum):
    # Device architecture (e.g. x86/amd64) is not applicable for the application.
    ProcessorArchitectureNotApplicable = "processorArchitectureNotApplicable",
    # Available disk space on the target device is less than the configured minimum.
    MinimumDiskSpaceNotMet = "minimumDiskSpaceNotMet",
    # OS version on the target device is less than the configured minimum.
    MinimumOsVersionNotMet = "minimumOsVersionNotMet",
    # Amount of RAM on the target device is less than the configured minimum.
    MinimumPhysicalMemoryNotMet = "minimumPhysicalMemoryNotMet",
    # Count of logical processors on the target device is less than the configured minimum.
    MinimumLogicalProcessorCountNotMet = "minimumLogicalProcessorCountNotMet",
    # CPU speed on the target device is less than the configured minimum.
    MinimumCpuSpeedNotMet = "minimumCpuSpeedNotMet",
    # Application is not applicable to this platform. (e.g. Android app targeted to IOS)
    PlatformNotApplicable = "platformNotApplicable",
    # File system requirement rule is not met
    FileSystemRequirementNotMet = "fileSystemRequirementNotMet",
    # Registry requirement rule is not met
    RegistryRequirementNotMet = "registryRequirementNotMet",
    # PowerShell script requirement rule is not met
    PowerShellScriptRequirementNotMet = "powerShellScriptRequirementNotMet",
    # All targeted, superseding apps are not applicable.
    SupersedingAppsNotApplicable = "supersedingAppsNotApplicable",
    # No additional details are available.
    NoAdditionalDetails = "noAdditionalDetails",
    # One or more of the application's dependencies failed to install.
    DependencyFailedToInstall = "dependencyFailedToInstall",
    # One or more of the application's dependencies have requirements which are not met.
    DependencyWithRequirementsNotMet = "dependencyWithRequirementsNotMet",
    # One or more of the application's dependencies require a device reboot to complete installation.
    DependencyPendingReboot = "dependencyPendingReboot",
    # One or more of the application's dependencies are configured to not automatically install.
    DependencyWithAutoInstallDisabled = "dependencyWithAutoInstallDisabled",
    # A superseded app failed to uninstall.
    SupersededAppUninstallFailed = "supersededAppUninstallFailed",
    # A superseded app requires a reboot to complete uninstall.
    SupersededAppUninstallPendingReboot = "supersededAppUninstallPendingReboot",
    # Superseded apps are being removed.
    RemovingSupersededApps = "removingSupersededApps",
    # The latest version of the app failed to update from an earlier version.
    IosAppStoreUpdateFailedToInstall = "iosAppStoreUpdateFailedToInstall",
    # An update is available.
    VppAppHasUpdateAvailable = "vppAppHasUpdateAvailable",
    # The user rejected the app update.
    UserRejectedUpdate = "userRejectedUpdate",
    # To complete the removal of the app, the device must be rebooted.
    UninstallPendingReboot = "uninstallPendingReboot",
    # Superseding applications are detected.
    SupersedingAppsDetected = "supersedingAppsDetected",
    # Superseded applications are detected.
    SupersededAppsDetected = "supersededAppsDetected",
    # Application failed to install. See error code property for more details.
    SeeInstallErrorCode = "seeInstallErrorCode",
    # Application is configured to not be automatically installed.
    AutoInstallDisabled = "autoInstallDisabled",
    # The app is managed but no longer installed.
    ManagedAppNoLongerPresent = "managedAppNoLongerPresent",
    # The user rejected the app install.
    UserRejectedInstall = "userRejectedInstall",
    # The user must log into the App Store to install app.
    UserIsNotLoggedIntoAppStore = "userIsNotLoggedIntoAppStore",
    # App cannot be installed. An untargeted, superseding app was detected, which created a conflict.
    UntargetedSupersedingAppsDetected = "untargetedSupersedingAppsDetected",
    # App was removed in order to install a superseding app.
    AppRemovedBySupersedence = "appRemovedBySupersedence",
    # App cannot be installed. One or more of the application's dependencies are in use.
    DependencyAppInUse = "dependencyAppInUse",
    # Application failed to uninstall. See error code property for more details.
    SeeUninstallErrorCode = "seeUninstallErrorCode",
    # Device must be rebooted to complete installation of the application.
    PendingReboot = "pendingReboot",
    # One or more of the application's dependencies are installing.
    InstallingDependencies = "installingDependencies",
    # Application content was downloaded to the device.
    ContentDownloaded = "contentDownloaded",
    # App enforcement is pending because the app is currently in use.
    InUse = "inUse",
    # App enforcement was deferred by the user because the app is currently in use.
    Deferred = "deferred",
    # App enforcement was automatically deferred because the app is currently in use and a user response was not available.
    AutoDeferred = "autoDeferred",

