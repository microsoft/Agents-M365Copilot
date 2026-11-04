from enum import Enum

class DeviceManagementTemplateSubtype(str, Enum):
    # Template has no subtype
    None_ = "none",
    # Endpoint security firewall subtype
    Firewall = "firewall",
    # Endpoint security disk encryption subtype
    DiskEncryption = "diskEncryption",
    # Endpoint security attack surface reduction subtype
    AttackSurfaceReduction = "attackSurfaceReduction",
    # Endpoint security endpoint detection and response subtype
    EndpointDetectionReponse = "endpointDetectionReponse",
    # Endpoint security account protection subtype
    AccountProtection = "accountProtection",
    # Endpoint security anitivirus subtype
    Antivirus = "antivirus",
    # Endpoint security firewall shared app subtype
    FirewallSharedAppList = "firewallSharedAppList",
    # Endpoint security firewall shared ip range list subtype
    FirewallSharedIpList = "firewallSharedIpList",
    # Endpoint security firewall shared port range list subtype
    FirewallSharedPortlist = "firewallSharedPortlist",

