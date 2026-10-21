from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_resource_access_profile_base import DeviceManagementResourceAccessProfileBase
    from .windows10_x_s_c_e_p_certificate_profile import Windows10XSCEPCertificateProfile

from .device_management_resource_access_profile_base import DeviceManagementResourceAccessProfileBase

@dataclass
class Windows10XCertificateProfile(DeviceManagementResourceAccessProfileBase, Parsable):
    """
    Base Profile Type for Authentication Certificates (SCEP or PFX Create)
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windows10XCertificateProfile"
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Windows10XCertificateProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Windows10XCertificateProfile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10XSCEPCertificateProfile".casefold():
            from .windows10_x_s_c_e_p_certificate_profile import Windows10XSCEPCertificateProfile

            return Windows10XSCEPCertificateProfile()
        return Windows10XCertificateProfile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_resource_access_profile_base import DeviceManagementResourceAccessProfileBase
        from .windows10_x_s_c_e_p_certificate_profile import Windows10XSCEPCertificateProfile

        from .device_management_resource_access_profile_base import DeviceManagementResourceAccessProfileBase
        from .windows10_x_s_c_e_p_certificate_profile import Windows10XSCEPCertificateProfile

        fields: dict[str, Callable[[Any], None]] = {
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
    

