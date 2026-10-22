from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .dep_i_o_s_enrollment_profile import DepIOSEnrollmentProfile
    from .dep_mac_o_s_enrollment_profile import DepMacOSEnrollmentProfile
    from .enrollment_profile import EnrollmentProfile

from .enrollment_profile import EnrollmentProfile

@dataclass
class DepEnrollmentBaseProfile(EnrollmentProfile, Parsable):
    """
    The DepEnrollmentBaseProfile resource represents an Apple Device Enrollment Program (DEP) enrollment profile. This type of profile must be assigned to Apple DEP serial numbers before the corresponding devices can enroll via DEP.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.depEnrollmentBaseProfile"
    # Indicates if Apple id setup pane is disabled
    apple_id_disabled: Optional[bool] = None
    # Indicates if Apple pay setup pane is disabled
    apple_pay_disabled: Optional[bool] = None
    # URL for setup assistant login
    configuration_web_url: Optional[bool] = None
    # Sets a literal or name pattern.
    device_name_template: Optional[str] = None
    # Indicates if diagnostics setup pane is disabled
    diagnostics_disabled: Optional[bool] = None
    # Indicates if displaytone setup screen is disabled
    display_tone_setup_disabled: Optional[bool] = None
    # enabledSkipKeys contains all the enabled skip keys as strings
    enabled_skip_keys: Optional[list[str]] = None
    # EnrollmentTimeAzureAdGroupIds contains list of enrollment time Azure Group Ids to be associated with profile
    enrollment_time_azure_ad_group_ids: Optional[list[UUID]] = None
    # Indicates if this is the default profile
    is_default: Optional[bool] = None
    # Indicates if the profile is mandatory
    is_mandatory: Optional[bool] = None
    # Indicates if Location service setup pane is disabled
    location_disabled: Optional[bool] = None
    # Indicates if privacy screen is disabled
    privacy_pane_disabled: Optional[bool] = None
    # Indicates if the profile removal option is disabled
    profile_removal_disabled: Optional[bool] = None
    # Indicates if Restore setup pane is blocked
    restore_blocked: Optional[bool] = None
    # Indicates if screen timeout setup is disabled
    screen_time_screen_disabled: Optional[bool] = None
    # Indicates if siri setup pane is disabled
    siri_disabled: Optional[bool] = None
    # Supervised mode, True to enable, false otherwise. See https://learn.microsoft.com/intune/deploy-use/enroll-devices-in-microsoft-intune for additional information.
    supervised_mode_enabled: Optional[bool] = None
    # Support department information
    support_department: Optional[str] = None
    # Support phone number
    support_phone_number: Optional[str] = None
    # Indicates if 'Terms and Conditions' setup pane is disabled
    terms_and_conditions_disabled: Optional[bool] = None
    # Indicates if touch id setup pane is disabled
    touch_id_disabled: Optional[bool] = None
    # Indicates if the device will need to wait for configured confirmation
    wait_for_device_configured_confirmation: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DepEnrollmentBaseProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DepEnrollmentBaseProfile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.depIOSEnrollmentProfile".casefold():
            from .dep_i_o_s_enrollment_profile import DepIOSEnrollmentProfile

            return DepIOSEnrollmentProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.depMacOSEnrollmentProfile".casefold():
            from .dep_mac_o_s_enrollment_profile import DepMacOSEnrollmentProfile

            return DepMacOSEnrollmentProfile()
        return DepEnrollmentBaseProfile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .dep_i_o_s_enrollment_profile import DepIOSEnrollmentProfile
        from .dep_mac_o_s_enrollment_profile import DepMacOSEnrollmentProfile
        from .enrollment_profile import EnrollmentProfile

        from .dep_i_o_s_enrollment_profile import DepIOSEnrollmentProfile
        from .dep_mac_o_s_enrollment_profile import DepMacOSEnrollmentProfile
        from .enrollment_profile import EnrollmentProfile

        fields: dict[str, Callable[[Any], None]] = {
            "appleIdDisabled": lambda n : setattr(self, 'apple_id_disabled', n.get_bool_value()),
            "applePayDisabled": lambda n : setattr(self, 'apple_pay_disabled', n.get_bool_value()),
            "configurationWebUrl": lambda n : setattr(self, 'configuration_web_url', n.get_bool_value()),
            "deviceNameTemplate": lambda n : setattr(self, 'device_name_template', n.get_str_value()),
            "diagnosticsDisabled": lambda n : setattr(self, 'diagnostics_disabled', n.get_bool_value()),
            "displayToneSetupDisabled": lambda n : setattr(self, 'display_tone_setup_disabled', n.get_bool_value()),
            "enabledSkipKeys": lambda n : setattr(self, 'enabled_skip_keys', n.get_collection_of_primitive_values(str)),
            "enrollmentTimeAzureAdGroupIds": lambda n : setattr(self, 'enrollment_time_azure_ad_group_ids', n.get_collection_of_primitive_values(UUID)),
            "isDefault": lambda n : setattr(self, 'is_default', n.get_bool_value()),
            "isMandatory": lambda n : setattr(self, 'is_mandatory', n.get_bool_value()),
            "locationDisabled": lambda n : setattr(self, 'location_disabled', n.get_bool_value()),
            "privacyPaneDisabled": lambda n : setattr(self, 'privacy_pane_disabled', n.get_bool_value()),
            "profileRemovalDisabled": lambda n : setattr(self, 'profile_removal_disabled', n.get_bool_value()),
            "restoreBlocked": lambda n : setattr(self, 'restore_blocked', n.get_bool_value()),
            "screenTimeScreenDisabled": lambda n : setattr(self, 'screen_time_screen_disabled', n.get_bool_value()),
            "siriDisabled": lambda n : setattr(self, 'siri_disabled', n.get_bool_value()),
            "supervisedModeEnabled": lambda n : setattr(self, 'supervised_mode_enabled', n.get_bool_value()),
            "supportDepartment": lambda n : setattr(self, 'support_department', n.get_str_value()),
            "supportPhoneNumber": lambda n : setattr(self, 'support_phone_number', n.get_str_value()),
            "termsAndConditionsDisabled": lambda n : setattr(self, 'terms_and_conditions_disabled', n.get_bool_value()),
            "touchIdDisabled": lambda n : setattr(self, 'touch_id_disabled', n.get_bool_value()),
            "waitForDeviceConfiguredConfirmation": lambda n : setattr(self, 'wait_for_device_configured_confirmation', n.get_bool_value()),
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
        writer.write_bool_value("appleIdDisabled", self.apple_id_disabled)
        writer.write_bool_value("applePayDisabled", self.apple_pay_disabled)
        writer.write_bool_value("configurationWebUrl", self.configuration_web_url)
        writer.write_str_value("deviceNameTemplate", self.device_name_template)
        writer.write_bool_value("diagnosticsDisabled", self.diagnostics_disabled)
        writer.write_bool_value("displayToneSetupDisabled", self.display_tone_setup_disabled)
        writer.write_collection_of_primitive_values("enabledSkipKeys", self.enabled_skip_keys)
        writer.write_collection_of_primitive_values("enrollmentTimeAzureAdGroupIds", self.enrollment_time_azure_ad_group_ids)
        writer.write_bool_value("isDefault", self.is_default)
        writer.write_bool_value("isMandatory", self.is_mandatory)
        writer.write_bool_value("locationDisabled", self.location_disabled)
        writer.write_bool_value("privacyPaneDisabled", self.privacy_pane_disabled)
        writer.write_bool_value("profileRemovalDisabled", self.profile_removal_disabled)
        writer.write_bool_value("restoreBlocked", self.restore_blocked)
        writer.write_bool_value("screenTimeScreenDisabled", self.screen_time_screen_disabled)
        writer.write_bool_value("siriDisabled", self.siri_disabled)
        writer.write_bool_value("supervisedModeEnabled", self.supervised_mode_enabled)
        writer.write_str_value("supportDepartment", self.support_department)
        writer.write_str_value("supportPhoneNumber", self.support_phone_number)
        writer.write_bool_value("termsAndConditionsDisabled", self.terms_and_conditions_disabled)
        writer.write_bool_value("touchIdDisabled", self.touch_id_disabled)
        writer.write_bool_value("waitForDeviceConfiguredConfirmation", self.wait_for_device_configured_confirmation)
    

