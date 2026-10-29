from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .hardware_oath_token_authentication_method_device import HardwareOathTokenAuthenticationMethodDevice

from .entity import Entity

@dataclass
class AuthenticationMethodDevice(Entity, Parsable):
    # Optional name given to the hardware OATH device.
    display_name: Optional[str] = None
    # Exposes the hardware OATH method in the directory.
    hardware_oath_devices: Optional[list[HardwareOathTokenAuthenticationMethodDevice]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuthenticationMethodDevice:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationMethodDevice
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.hardwareOathTokenAuthenticationMethodDevice".casefold():
            from .hardware_oath_token_authentication_method_device import HardwareOathTokenAuthenticationMethodDevice

            return HardwareOathTokenAuthenticationMethodDevice()
        return AuthenticationMethodDevice()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .hardware_oath_token_authentication_method_device import HardwareOathTokenAuthenticationMethodDevice

        from .entity import Entity
        from .hardware_oath_token_authentication_method_device import HardwareOathTokenAuthenticationMethodDevice

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "hardwareOathDevices": lambda n : setattr(self, 'hardware_oath_devices', n.get_collection_of_object_values(HardwareOathTokenAuthenticationMethodDevice)),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("hardwareOathDevices", self.hardware_oath_devices)
    

