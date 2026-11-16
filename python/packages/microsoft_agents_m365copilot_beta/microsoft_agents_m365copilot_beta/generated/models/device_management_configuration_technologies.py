from enum import Enum

class DeviceManagementConfigurationTechnologies(str, Enum):
    # Default. Setting cannot be deployed through any channel.
    None_ = "none",
    # Setting can be deployed through the MDM channel.
    Mdm = "mdm",
    # Setting can be deployed through the Windows10XManagement channel
    Windows10XManagement = "windows10XManagement",
    # Setting can be deployed through the ConfigManager channel.
    ConfigManager = "configManager",
    # Setting can be deployed through the IntuneManagementExtension channel.
    IntuneManagementExtension = "intuneManagementExtension",
    # Setting can be deployed through a ThirdParty channel.
    ThirdParty = "thirdParty",
    # Setting can be deployed through Document Gateway Service.
    DocumentGateway = "documentGateway",
    # Setting can be deployed through the AppleRemoteManagement channel.
    AppleRemoteManagement = "appleRemoteManagement",
    # Setting can be deployed through the SENSE agent channel.
    MicrosoftSense = "microsoftSense",
    # Setting can be deployed through the Exchange Online agent channel.
    ExchangeOnline = "exchangeOnline",
    # Setting can be deployed through the Mobile Application Management (MAM) channel
    MobileApplicationManagement = "mobileApplicationManagement",
    # Setting can be deployed through the Linux Mdm channel.
    LinuxMdm = "linuxMdm",
    # Setting can be deployed through device enrollment.
    Enrollment = "enrollment",
    # Setting can be deployed using the Endpoint privilege management channel
    EndpointPrivilegeManagement = "endpointPrivilegeManagement",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",
    # Setting can be deployed using the Operating System Recovery channel
    WindowsOsRecovery = "windowsOsRecovery",
    # Indicates the settings that can be deployed through the Android channel.
    Android = "android",
    # Setting can be deployed through the Intune Open Extensibility channel for scenarios such as Windows Recovery Environment (WinRE) configuration policies.
    IntuneOpenExtensibility = "intuneOpenExtensibility",

