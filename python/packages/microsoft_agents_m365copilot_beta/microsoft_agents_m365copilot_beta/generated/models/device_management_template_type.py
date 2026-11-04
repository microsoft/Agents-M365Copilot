from enum import Enum

class DeviceManagementTemplateType(str, Enum):
    # Security baseline template
    SecurityBaseline = "securityBaseline",
    # Specialized devices template
    SpecializedDevices = "specializedDevices",
    # Advanced Threat Protection security baseline template
    AdvancedThreatProtectionSecurityBaseline = "advancedThreatProtectionSecurityBaseline",
    # Device configuration template
    DeviceConfiguration = "deviceConfiguration",
    # Custom admin defined template
    Custom = "custom",
    # Templates containing specific security focused settings
    SecurityTemplate = "securityTemplate",
    # Microsoft Edge security baseline template
    MicrosoftEdgeSecurityBaseline = "microsoftEdgeSecurityBaseline",
    # Microsoft Office 365 ProPlus security baseline template
    MicrosoftOffice365ProPlusSecurityBaseline = "microsoftOffice365ProPlusSecurityBaseline",
    # Device compliance template
    DeviceCompliance = "deviceCompliance",
    # Device Configuration for Microsoft Office 365 settings
    DeviceConfigurationForOffice365 = "deviceConfigurationForOffice365",
    # Windows 365 security baseline template
    CloudPC = "cloudPC",
    # Firewall Shared Object templates for reference settings
    FirewallSharedSettings = "firewallSharedSettings",

