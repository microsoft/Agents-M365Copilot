from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .change_uefi_settings_permission import ChangeUefiSettingsPermission
    from .device_configuration import DeviceConfiguration
    from .enablement import Enablement

from .device_configuration import DeviceConfiguration

@dataclass
class Windows10DeviceFirmwareConfigurationInterface(DeviceConfiguration, Parsable):
    """
    Graph properties for Device Firmware Configuration Interface 
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windows10DeviceFirmwareConfigurationInterface"
    # Possible values of a property
    bluetooth: Optional[Enablement] = None
    # Possible values of a property
    boot_from_built_in_network_adapters: Optional[Enablement] = None
    # Possible values of a property
    boot_from_external_media: Optional[Enablement] = None
    # Possible values of a property
    cameras: Optional[Enablement] = None
    # Defines the permission level granted to users to enable them change Uefi settings
    change_uefi_settings_permission: Optional[ChangeUefiSettingsPermission] = None
    # Possible values of a property
    front_camera: Optional[Enablement] = None
    # Possible values of a property
    infrared_camera: Optional[Enablement] = None
    # Possible values of a property
    microphone: Optional[Enablement] = None
    # Possible values of a property
    microphones_and_speakers: Optional[Enablement] = None
    # Possible values of a property
    near_field_communication: Optional[Enablement] = None
    # Possible values of a property
    radios: Optional[Enablement] = None
    # Possible values of a property
    rear_camera: Optional[Enablement] = None
    # Possible values of a property
    sd_card: Optional[Enablement] = None
    # Possible values of a property
    simultaneous_multi_threading: Optional[Enablement] = None
    # Possible values of a property
    usb_type_a_port: Optional[Enablement] = None
    # Possible values of a property
    virtualization_of_cpu_and_i_o: Optional[Enablement] = None
    # Possible values of a property
    wake_on_l_a_n: Optional[Enablement] = None
    # Possible values of a property
    wake_on_power: Optional[Enablement] = None
    # Possible values of a property
    wi_fi: Optional[Enablement] = None
    # Possible values of a property
    windows_platform_binary_table: Optional[Enablement] = None
    # Possible values of a property
    wireless_wide_area_network: Optional[Enablement] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Windows10DeviceFirmwareConfigurationInterface:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Windows10DeviceFirmwareConfigurationInterface
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Windows10DeviceFirmwareConfigurationInterface()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .change_uefi_settings_permission import ChangeUefiSettingsPermission
        from .device_configuration import DeviceConfiguration
        from .enablement import Enablement

        from .change_uefi_settings_permission import ChangeUefiSettingsPermission
        from .device_configuration import DeviceConfiguration
        from .enablement import Enablement

        fields: dict[str, Callable[[Any], None]] = {
            "bluetooth": lambda n : setattr(self, 'bluetooth', n.get_enum_value(Enablement)),
            "bootFromBuiltInNetworkAdapters": lambda n : setattr(self, 'boot_from_built_in_network_adapters', n.get_enum_value(Enablement)),
            "bootFromExternalMedia": lambda n : setattr(self, 'boot_from_external_media', n.get_enum_value(Enablement)),
            "cameras": lambda n : setattr(self, 'cameras', n.get_enum_value(Enablement)),
            "changeUefiSettingsPermission": lambda n : setattr(self, 'change_uefi_settings_permission', n.get_enum_value(ChangeUefiSettingsPermission)),
            "frontCamera": lambda n : setattr(self, 'front_camera', n.get_enum_value(Enablement)),
            "infraredCamera": lambda n : setattr(self, 'infrared_camera', n.get_enum_value(Enablement)),
            "microphone": lambda n : setattr(self, 'microphone', n.get_enum_value(Enablement)),
            "microphonesAndSpeakers": lambda n : setattr(self, 'microphones_and_speakers', n.get_enum_value(Enablement)),
            "nearFieldCommunication": lambda n : setattr(self, 'near_field_communication', n.get_enum_value(Enablement)),
            "radios": lambda n : setattr(self, 'radios', n.get_enum_value(Enablement)),
            "rearCamera": lambda n : setattr(self, 'rear_camera', n.get_enum_value(Enablement)),
            "sdCard": lambda n : setattr(self, 'sd_card', n.get_enum_value(Enablement)),
            "simultaneousMultiThreading": lambda n : setattr(self, 'simultaneous_multi_threading', n.get_enum_value(Enablement)),
            "usbTypeAPort": lambda n : setattr(self, 'usb_type_a_port', n.get_enum_value(Enablement)),
            "virtualizationOfCpuAndIO": lambda n : setattr(self, 'virtualization_of_cpu_and_i_o', n.get_enum_value(Enablement)),
            "wakeOnLAN": lambda n : setattr(self, 'wake_on_l_a_n', n.get_enum_value(Enablement)),
            "wakeOnPower": lambda n : setattr(self, 'wake_on_power', n.get_enum_value(Enablement)),
            "wiFi": lambda n : setattr(self, 'wi_fi', n.get_enum_value(Enablement)),
            "windowsPlatformBinaryTable": lambda n : setattr(self, 'windows_platform_binary_table', n.get_enum_value(Enablement)),
            "wirelessWideAreaNetwork": lambda n : setattr(self, 'wireless_wide_area_network', n.get_enum_value(Enablement)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("bluetooth", self.bluetooth)
        writer.write_enum_value("bootFromBuiltInNetworkAdapters", self.boot_from_built_in_network_adapters)
        writer.write_enum_value("bootFromExternalMedia", self.boot_from_external_media)
        writer.write_enum_value("cameras", self.cameras)
        writer.write_enum_value("changeUefiSettingsPermission", self.change_uefi_settings_permission)
        writer.write_enum_value("frontCamera", self.front_camera)
        writer.write_enum_value("infraredCamera", self.infrared_camera)
        writer.write_enum_value("microphone", self.microphone)
        writer.write_enum_value("microphonesAndSpeakers", self.microphones_and_speakers)
        writer.write_enum_value("nearFieldCommunication", self.near_field_communication)
        writer.write_enum_value("radios", self.radios)
        writer.write_enum_value("rearCamera", self.rear_camera)
        writer.write_enum_value("sdCard", self.sd_card)
        writer.write_enum_value("simultaneousMultiThreading", self.simultaneous_multi_threading)
        writer.write_enum_value("usbTypeAPort", self.usb_type_a_port)
        writer.write_enum_value("virtualizationOfCpuAndIO", self.virtualization_of_cpu_and_i_o)
        writer.write_enum_value("wakeOnLAN", self.wake_on_l_a_n)
        writer.write_enum_value("wakeOnPower", self.wake_on_power)
        writer.write_enum_value("wiFi", self.wi_fi)
        writer.write_enum_value("windowsPlatformBinaryTable", self.windows_platform_binary_table)
        writer.write_enum_value("wirelessWideAreaNetwork", self.wireless_wide_area_network)
    

