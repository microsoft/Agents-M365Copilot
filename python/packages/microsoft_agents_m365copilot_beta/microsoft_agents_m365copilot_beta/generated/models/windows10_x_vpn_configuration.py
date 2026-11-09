from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .device_management_resource_access_profile_base import DeviceManagementResourceAccessProfileBase

from .device_management_resource_access_profile_base import DeviceManagementResourceAccessProfileBase

@dataclass
class Windows10XVpnConfiguration(DeviceManagementResourceAccessProfileBase, Parsable):
    """
    Windows X VPN configuration profile
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windows10XVpnConfiguration"
    # ID to the Authentication Certificate
    authentication_certificate_id: Optional[UUID] = None
    # Custom XML commands that configures the VPN connection. (UTF8 byte encoding)
    custom_xml: Optional[bytes] = None
    # Custom Xml file name.
    custom_xml_file_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Windows10XVpnConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Windows10XVpnConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Windows10XVpnConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_resource_access_profile_base import DeviceManagementResourceAccessProfileBase

        from .device_management_resource_access_profile_base import DeviceManagementResourceAccessProfileBase

        fields: dict[str, Callable[[Any], None]] = {
            "authenticationCertificateId": lambda n : setattr(self, 'authentication_certificate_id', n.get_uuid_value()),
            "customXml": lambda n : setattr(self, 'custom_xml', n.get_bytes_value()),
            "customXmlFileName": lambda n : setattr(self, 'custom_xml_file_name', n.get_str_value()),
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
        writer.write_uuid_value("authenticationCertificateId", self.authentication_certificate_id)
        writer.write_bytes_value("customXml", self.custom_xml)
        writer.write_str_value("customXmlFileName", self.custom_xml_file_name)
    

