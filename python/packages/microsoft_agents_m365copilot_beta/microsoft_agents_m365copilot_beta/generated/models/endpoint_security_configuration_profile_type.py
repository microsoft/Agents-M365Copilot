from enum import Enum

class EndpointSecurityConfigurationProfileType(str, Enum):
    # Unknown.
    Unknown = "unknown",
    # Antivirus.
    Antivirus = "antivirus",
    # Windows Security.
    WindowsSecurity = "windowsSecurity",
    # BitLocker.
    BitLocker = "bitLocker",
    # FileVault.
    FileVault = "fileVault",
    # Firewall.
    Firewall = "firewall",
    # Firewall rules.
    FirewallRules = "firewallRules",
    # Endpoint detection and response.
    EndpointDetectionAndResponse = "endpointDetectionAndResponse",
    # Device control.
    DeviceControl = "deviceControl",
    # App and browser isolation.
    AppAndBrowserIsolation = "appAndBrowserIsolation",
    # Exploit protection.
    ExploitProtection = "exploitProtection",
    # Web protection.
    WebProtection = "webProtection",
    # Application control.
    ApplicationControl = "applicationControl",
    # Attack surface reduction rules.
    AttackSurfaceReductionRules = "attackSurfaceReductionRules",
    # Account protection.
    AccountProtection = "accountProtection",

