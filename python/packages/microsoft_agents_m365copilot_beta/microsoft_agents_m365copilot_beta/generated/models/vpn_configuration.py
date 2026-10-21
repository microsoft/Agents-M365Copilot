from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_device_owner_vpn_configuration import AndroidDeviceOwnerVpnConfiguration
    from .device_configuration import DeviceConfiguration
    from .vpn_authentication_method import VpnAuthenticationMethod
    from .vpn_server import VpnServer

from .device_configuration import DeviceConfiguration

@dataclass
class VpnConfiguration(DeviceConfiguration, Parsable):
    """
    Base VPN Configuration profile.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.vpnConfiguration"
    # VPN Authentication Method.
    authentication_method: Optional[VpnAuthenticationMethod] = None
    # Connection name displayed to the user.
    connection_name: Optional[str] = None
    # Realm when connection type is set to Pulse Secure.
    realm: Optional[str] = None
    # Role when connection type is set to Pulse Secure.
    role: Optional[str] = None
    # List of VPN Servers on the network. Make sure end users can access these network locations. This collection can contain a maximum of 500 elements.
    servers: Optional[list[VpnServer]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VpnConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VpnConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidDeviceOwnerVpnConfiguration".casefold():
            from .android_device_owner_vpn_configuration import AndroidDeviceOwnerVpnConfiguration

            return AndroidDeviceOwnerVpnConfiguration()
        return VpnConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .android_device_owner_vpn_configuration import AndroidDeviceOwnerVpnConfiguration
        from .device_configuration import DeviceConfiguration
        from .vpn_authentication_method import VpnAuthenticationMethod
        from .vpn_server import VpnServer

        from .android_device_owner_vpn_configuration import AndroidDeviceOwnerVpnConfiguration
        from .device_configuration import DeviceConfiguration
        from .vpn_authentication_method import VpnAuthenticationMethod
        from .vpn_server import VpnServer

        fields: dict[str, Callable[[Any], None]] = {
            "authenticationMethod": lambda n : setattr(self, 'authentication_method', n.get_enum_value(VpnAuthenticationMethod)),
            "connectionName": lambda n : setattr(self, 'connection_name', n.get_str_value()),
            "realm": lambda n : setattr(self, 'realm', n.get_str_value()),
            "role": lambda n : setattr(self, 'role', n.get_str_value()),
            "servers": lambda n : setattr(self, 'servers', n.get_collection_of_object_values(VpnServer)),
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
        writer.write_enum_value("authenticationMethod", self.authentication_method)
        writer.write_str_value("connectionName", self.connection_name)
        writer.write_str_value("realm", self.realm)
        writer.write_str_value("role", self.role)
        writer.write_collection_of_object_values("servers", self.servers)
    

