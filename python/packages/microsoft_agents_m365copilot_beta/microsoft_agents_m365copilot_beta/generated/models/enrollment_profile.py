from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .dep_enrollment_base_profile import DepEnrollmentBaseProfile
    from .dep_enrollment_profile import DepEnrollmentProfile
    from .dep_i_o_s_enrollment_profile import DepIOSEnrollmentProfile
    from .dep_mac_o_s_enrollment_profile import DepMacOSEnrollmentProfile
    from .dep_tv_o_s_enrollment_profile import DepTvOSEnrollmentProfile
    from .dep_vision_o_s_enrollment_profile import DepVisionOSEnrollmentProfile
    from .entity import Entity

from .entity import Entity

@dataclass
class EnrollmentProfile(Entity, Parsable):
    """
    The enrollmentProfile resource represents a collection of configurations which must be provided pre-enrollment to enable enrolling certain devices whose identities have been pre-staged. Pre-staged device identities are assigned to this type of profile to apply the profile's configurations at enrollment of the corresponding device.
    """
    # Configuration endpoint url to use for Enrollment
    configuration_endpoint_url: Optional[str] = None
    # Description of the profile
    description: Optional[str] = None
    # Name of the profile
    display_name: Optional[str] = None
    # Indicates to authenticate with Apple Setup Assistant instead of Company Portal.
    enable_authentication_via_company_portal: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates that Company Portal is required on setup assistant enrolled devices
    require_company_portal_on_setup_assistant_enrolled_devices: Optional[bool] = None
    # Indicates if the profile requires user authentication
    requires_user_authentication: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EnrollmentProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EnrollmentProfile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.depEnrollmentBaseProfile".casefold():
            from .dep_enrollment_base_profile import DepEnrollmentBaseProfile

            return DepEnrollmentBaseProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.depEnrollmentProfile".casefold():
            from .dep_enrollment_profile import DepEnrollmentProfile

            return DepEnrollmentProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.depIOSEnrollmentProfile".casefold():
            from .dep_i_o_s_enrollment_profile import DepIOSEnrollmentProfile

            return DepIOSEnrollmentProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.depMacOSEnrollmentProfile".casefold():
            from .dep_mac_o_s_enrollment_profile import DepMacOSEnrollmentProfile

            return DepMacOSEnrollmentProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.depTvOSEnrollmentProfile".casefold():
            from .dep_tv_o_s_enrollment_profile import DepTvOSEnrollmentProfile

            return DepTvOSEnrollmentProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.depVisionOSEnrollmentProfile".casefold():
            from .dep_vision_o_s_enrollment_profile import DepVisionOSEnrollmentProfile

            return DepVisionOSEnrollmentProfile()
        return EnrollmentProfile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .dep_enrollment_base_profile import DepEnrollmentBaseProfile
        from .dep_enrollment_profile import DepEnrollmentProfile
        from .dep_i_o_s_enrollment_profile import DepIOSEnrollmentProfile
        from .dep_mac_o_s_enrollment_profile import DepMacOSEnrollmentProfile
        from .dep_tv_o_s_enrollment_profile import DepTvOSEnrollmentProfile
        from .dep_vision_o_s_enrollment_profile import DepVisionOSEnrollmentProfile
        from .entity import Entity

        from .dep_enrollment_base_profile import DepEnrollmentBaseProfile
        from .dep_enrollment_profile import DepEnrollmentProfile
        from .dep_i_o_s_enrollment_profile import DepIOSEnrollmentProfile
        from .dep_mac_o_s_enrollment_profile import DepMacOSEnrollmentProfile
        from .dep_tv_o_s_enrollment_profile import DepTvOSEnrollmentProfile
        from .dep_vision_o_s_enrollment_profile import DepVisionOSEnrollmentProfile
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "configurationEndpointUrl": lambda n : setattr(self, 'configuration_endpoint_url', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "enableAuthenticationViaCompanyPortal": lambda n : setattr(self, 'enable_authentication_via_company_portal', n.get_bool_value()),
            "requireCompanyPortalOnSetupAssistantEnrolledDevices": lambda n : setattr(self, 'require_company_portal_on_setup_assistant_enrolled_devices', n.get_bool_value()),
            "requiresUserAuthentication": lambda n : setattr(self, 'requires_user_authentication', n.get_bool_value()),
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
        writer.write_str_value("configurationEndpointUrl", self.configuration_endpoint_url)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("enableAuthenticationViaCompanyPortal", self.enable_authentication_via_company_portal)
        writer.write_bool_value("requireCompanyPortalOnSetupAssistantEnrolledDevices", self.require_company_portal_on_setup_assistant_enrolled_devices)
        writer.write_bool_value("requiresUserAuthentication", self.requires_user_authentication)
    

