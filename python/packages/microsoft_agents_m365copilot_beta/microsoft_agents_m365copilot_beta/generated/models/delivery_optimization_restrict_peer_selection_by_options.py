from enum import Enum

class DeliveryOptimizationRestrictPeerSelectionByOptions(str, Enum):
    # Not configured.
    NotConfigured = "notConfigured",
    # Subnet mask.
    SubnetMask = "subnetMask",

