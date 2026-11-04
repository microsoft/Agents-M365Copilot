from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_for_work_certificate_profile_base import AndroidForWorkCertificateProfileBase
    from .android_for_work_vpn_connection_type import AndroidForWorkVpnConnectionType
    from .device_configuration import DeviceConfiguration
    from .key_value import KeyValue
    from .key_value_pair import KeyValuePair
    from .vpn_authentication_method import VpnAuthenticationMethod
    from .vpn_server import VpnServer

from .device_configuration import DeviceConfiguration

@dataclass
class AndroidForWorkVpnConfiguration(DeviceConfiguration, Parsable):
    """
    By providing the configurations in this profile you can instruct the Android device to connect to desired VPN endpoint. By specifying the authentication method and security types expected by VPN endpoint you can make the VPN connection seamless for end user.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.androidForWorkVpnConfiguration"
    # VPN Authentication Method.
    authentication_method: Optional[VpnAuthenticationMethod] = None
    # Connection name displayed to the user.
    connection_name: Optional[str] = None
    # Android For Work VPN connection type.
    connection_type: Optional[AndroidForWorkVpnConnectionType] = None
    # Custom data when connection type is set to Citrix. This collection can contain a maximum of 25 elements.
    custom_data: Optional[list[KeyValue]] = None
    # Custom data when connection type is set to Citrix. This collection can contain a maximum of 25 elements.
    custom_key_value_data: Optional[list[KeyValuePair]] = None
    # Fingerprint is a string that will be used to verify the VPN server can be trusted, which is only applicable when connection type is Check Point Capsule VPN.
    fingerprint: Optional[str] = None
    # Identity certificate for client authentication when authentication method is certificate.
    identity_certificate: Optional[AndroidForWorkCertificateProfileBase] = None
    # Realm when connection type is set to Pulse Secure.
    realm: Optional[str] = None
    # Role when connection type is set to Pulse Secure.
    role: Optional[str] = None
    # List of VPN Servers on the network. Make sure end users can access these network locations. This collection can contain a maximum of 500 elements.
    servers: Optional[list[VpnServer]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AndroidForWorkVpnConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidForWorkVpnConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AndroidForWorkVpnConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .android_for_work_certificate_profile_base import AndroidForWorkCertificateProfileBase
        from .android_for_work_vpn_connection_type import AndroidForWorkVpnConnectionType
        from .device_configuration import DeviceConfiguration
        from .key_value import KeyValue
        from .key_value_pair import KeyValuePair
        from .vpn_authentication_method import VpnAuthenticationMethod
        from .vpn_server import VpnServer

        from .android_for_work_certificate_profile_base import AndroidForWorkCertificateProfileBase
        from .android_for_work_vpn_connection_type import AndroidForWorkVpnConnectionType
        from .device_configuration import DeviceConfiguration
        from .key_value import KeyValue
        from .key_value_pair import KeyValuePair
        from .vpn_authentication_method import VpnAuthenticationMethod
        from .vpn_server import VpnServer

        fields: dict[str, Callable[[Any], None]] = {
            "authenticationMethod": lambda n : setattr(self, 'authentication_method', n.get_enum_value(VpnAuthenticationMethod)),
            "connectionName": lambda n : setattr(self, 'connection_name', n.get_str_value()),
            "connectionType": lambda n : setattr(self, 'connection_type', n.get_enum_value(AndroidForWorkVpnConnectionType)),
            "customData": lambda n : setattr(self, 'custom_data', n.get_collection_of_object_values(KeyValue)),
            "customKeyValueData": lambda n : setattr(self, 'custom_key_value_data', n.get_collection_of_object_values(KeyValuePair)),
            "fingerprint": lambda n : setattr(self, 'fingerprint', n.get_str_value()),
            "identityCertificate": lambda n : setattr(self, 'identity_certificate', n.get_object_value(AndroidForWorkCertificateProfileBase)),
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
        writer.write_enum_value("connectionType", self.connection_type)
        writer.write_collection_of_object_values("customData", self.custom_data)
        writer.write_collection_of_object_values("customKeyValueData", self.custom_key_value_data)
        writer.write_str_value("fingerprint", self.fingerprint)
        writer.write_object_value("identityCertificate", self.identity_certificate)
        writer.write_str_value("realm", self.realm)
        writer.write_str_value("role", self.role)
        writer.write_collection_of_object_values("servers", self.servers)
    

