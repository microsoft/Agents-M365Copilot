from enum import Enum

class DmaGuardDeviceEnumerationPolicyType(str, Enum):
    # Default value. Devices with DMA remapping incompatible drivers will only be enumerated after the user unlocks the screen.
    DeviceDefault = "deviceDefault",
    # Devices with DMA remapping incompatible drivers will never be allowed to start and perform DMA at any time.
    BlockAll = "blockAll",
    # All external DMA capable PCIe devices will be enumerated at any time.
    AllowAll = "allowAll",

