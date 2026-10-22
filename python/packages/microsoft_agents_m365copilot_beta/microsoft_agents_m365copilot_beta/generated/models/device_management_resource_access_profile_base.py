from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_resource_access_profile_assignment import DeviceManagementResourceAccessProfileAssignment
    from .entity import Entity
    from .windows10_x_certificate_profile import Windows10XCertificateProfile
    from .windows10_x_s_c_e_p_certificate_profile import Windows10XSCEPCertificateProfile
    from .windows10_x_trusted_root_certificate import Windows10XTrustedRootCertificate
    from .windows10_x_vpn_configuration import Windows10XVpnConfiguration
    from .windows10_x_wifi_configuration import Windows10XWifiConfiguration

from .entity import Entity

@dataclass
class DeviceManagementResourceAccessProfileBase(Entity, Parsable):
    """
    Base Profile Type for Resource Access
    """
    # The list of assignments for the device configuration profile.
    assignments: Optional[list[DeviceManagementResourceAccessProfileAssignment]] = None
    # DateTime profile was created
    creation_date_time: Optional[datetime.datetime] = None
    # Profile description
    description: Optional[str] = None
    # Profile display name
    display_name: Optional[str] = None
    # DateTime profile was last modified
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Scope Tags
    role_scope_tag_ids: Optional[list[str]] = None
    # Version of the profile
    version: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementResourceAccessProfileBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementResourceAccessProfileBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10XCertificateProfile".casefold():
            from .windows10_x_certificate_profile import Windows10XCertificateProfile

            return Windows10XCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10XSCEPCertificateProfile".casefold():
            from .windows10_x_s_c_e_p_certificate_profile import Windows10XSCEPCertificateProfile

            return Windows10XSCEPCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10XTrustedRootCertificate".casefold():
            from .windows10_x_trusted_root_certificate import Windows10XTrustedRootCertificate

            return Windows10XTrustedRootCertificate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10XVpnConfiguration".casefold():
            from .windows10_x_vpn_configuration import Windows10XVpnConfiguration

            return Windows10XVpnConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10XWifiConfiguration".casefold():
            from .windows10_x_wifi_configuration import Windows10XWifiConfiguration

            return Windows10XWifiConfiguration()
        return DeviceManagementResourceAccessProfileBase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_resource_access_profile_assignment import DeviceManagementResourceAccessProfileAssignment
        from .entity import Entity
        from .windows10_x_certificate_profile import Windows10XCertificateProfile
        from .windows10_x_s_c_e_p_certificate_profile import Windows10XSCEPCertificateProfile
        from .windows10_x_trusted_root_certificate import Windows10XTrustedRootCertificate
        from .windows10_x_vpn_configuration import Windows10XVpnConfiguration
        from .windows10_x_wifi_configuration import Windows10XWifiConfiguration

        from .device_management_resource_access_profile_assignment import DeviceManagementResourceAccessProfileAssignment
        from .entity import Entity
        from .windows10_x_certificate_profile import Windows10XCertificateProfile
        from .windows10_x_s_c_e_p_certificate_profile import Windows10XSCEPCertificateProfile
        from .windows10_x_trusted_root_certificate import Windows10XTrustedRootCertificate
        from .windows10_x_vpn_configuration import Windows10XVpnConfiguration
        from .windows10_x_wifi_configuration import Windows10XWifiConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(DeviceManagementResourceAccessProfileAssignment)),
            "creationDateTime": lambda n : setattr(self, 'creation_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "roleScopeTagIds": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
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
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_datetime_value("creationDateTime", self.creation_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
        writer.write_int_value("version", self.version)
    

