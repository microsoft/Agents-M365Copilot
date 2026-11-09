from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_configuration import DeviceConfiguration

from .device_configuration import DeviceConfiguration

@dataclass
class WindowsDomainJoinConfiguration(DeviceConfiguration, Parsable):
    """
    Windows Domain Join device configuration.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsDomainJoinConfiguration"
    # Active Directory domain name to join.
    active_directory_domain_name: Optional[str] = None
    # Fixed prefix to be used for computer name.
    computer_name_static_prefix: Optional[str] = None
    # Dynamically generated characters used as suffix for computer name. Valid values 3 to 14
    computer_name_suffix_random_char_count: Optional[int] = None
    # Reference to device configurations required for network connectivity. This collection can contain a maximum of 2 elements.
    network_access_configurations: Optional[list[DeviceConfiguration]] = None
    # Organizational unit (OU) where the computer account will be created. If this parameter is NULL, the well known computer object container will be used as published in the domain.
    organizational_unit: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsDomainJoinConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsDomainJoinConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsDomainJoinConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_configuration import DeviceConfiguration

        from .device_configuration import DeviceConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "activeDirectoryDomainName": lambda n : setattr(self, 'active_directory_domain_name', n.get_str_value()),
            "computerNameStaticPrefix": lambda n : setattr(self, 'computer_name_static_prefix', n.get_str_value()),
            "computerNameSuffixRandomCharCount": lambda n : setattr(self, 'computer_name_suffix_random_char_count', n.get_int_value()),
            "networkAccessConfigurations": lambda n : setattr(self, 'network_access_configurations', n.get_collection_of_object_values(DeviceConfiguration)),
            "organizationalUnit": lambda n : setattr(self, 'organizational_unit', n.get_str_value()),
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
        writer.write_str_value("activeDirectoryDomainName", self.active_directory_domain_name)
        writer.write_str_value("computerNameStaticPrefix", self.computer_name_static_prefix)
        writer.write_int_value("computerNameSuffixRandomCharCount", self.computer_name_suffix_random_char_count)
        writer.write_collection_of_object_values("networkAccessConfigurations", self.network_access_configurations)
        writer.write_str_value("organizationalUnit", self.organizational_unit)
    

