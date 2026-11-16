from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .company_portal_blocked_action import CompanyPortalBlockedAction
    from .enrollment_availability_options import EnrollmentAvailabilityOptions
    from .entity import Entity
    from .intune_branding_profile_assignment import IntuneBrandingProfileAssignment
    from .mime_content import MimeContent
    from .rgb_color import RgbColor

from .entity import Entity

@dataclass
class IntuneBrandingProfile(Entity, Parsable):
    """
    This entity contains data which is used in customizing the tenant level appearance of the Company Portal applications as well as the end user web portal.
    """
    # The list of group assignments for the branding profile
    assignments: Optional[list[IntuneBrandingProfileAssignment]] = None
    # Collection of blocked actions on the company portal as per platform and device ownership types.
    company_portal_blocked_actions: Optional[list[CompanyPortalBlockedAction]] = None
    # E-mail address of the person/organization responsible for IT support
    contact_i_t_email_address: Optional[str] = None
    # Name of the person/organization responsible for IT support
    contact_i_t_name: Optional[str] = None
    # Text comments regarding the person/organization responsible for IT support
    contact_i_t_notes: Optional[str] = None
    # Phone number of the person/organization responsible for IT support
    contact_i_t_phone_number: Optional[str] = None
    # Time when the BrandingProfile was created
    created_date_time: Optional[datetime.datetime] = None
    # Text comments regarding what the admin has access to on the device
    custom_can_see_privacy_message: Optional[str] = None
    # Text comments regarding what the admin doesn't have access to on the device
    custom_cant_see_privacy_message: Optional[str] = None
    # Text comments regarding what the admin doesn't have access to on the device
    custom_privacy_message: Optional[str] = None
    # Applies to telemetry sent from all clients to the Intune service. When disabled, all proactive troubleshooting and issue warnings within the client are turned off, and telemetry settings appear inactive or hidden to the device user.
    disable_client_telemetry: Optional[bool] = None
    # Boolean that indicates if Device Category Selection will be shown in Company Portal
    disable_device_category_selection: Optional[bool] = None
    # Company/organization name that is displayed to end users
    display_name: Optional[str] = None
    # Options available for enrollment flow customization
    enrollment_availability: Optional[EnrollmentAvailabilityOptions] = None
    # Boolean that represents whether the profile is used as default or not
    is_default_profile: Optional[bool] = None
    # Boolean that represents whether the adminsistrator has disabled the 'Factory Reset' action on corporate owned devices.
    is_factory_reset_disabled: Optional[bool] = None
    # Boolean that represents whether the adminsistrator has disabled the 'Remove Device' action on corporate owned devices.
    is_remove_device_disabled: Optional[bool] = None
    # Customized image displayed in Company Portal apps landing page
    landing_page_customized_image: Optional[MimeContent] = None
    # Time when the BrandingProfile was last modified
    last_modified_date_time: Optional[datetime.datetime] = None
    # Logo image displayed in Company Portal apps which have a light background behind the logo
    light_background_logo: Optional[MimeContent] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Display name of the company/organization’s IT helpdesk site
    online_support_site_name: Optional[str] = None
    # URL to the company/organization’s IT helpdesk site
    online_support_site_url: Optional[str] = None
    # URL to the company/organization’s privacy policy
    privacy_url: Optional[str] = None
    # Description of the profile
    profile_description: Optional[str] = None
    # Name of the profile
    profile_name: Optional[str] = None
    # List of scope tags assigned to the branding profile
    role_scope_tag_ids: Optional[list[str]] = None
    # Boolean that indicates if AzureAD Enterprise Apps will be shown in Company Portal
    show_azure_a_d_enterprise_apps: Optional[bool] = None
    # Boolean that indicates if Configuration Manager Apps will be shown in Company Portal
    show_configuration_manager_apps: Optional[bool] = None
    # Boolean that represents whether the administrator-supplied display name will be shown next to the logo image or not
    show_display_name_next_to_logo: Optional[bool] = None
    # Boolean that represents whether the administrator-supplied logo images are shown or not
    show_logo: Optional[bool] = None
    # Boolean that indicates if Office WebApps will be shown in Company Portal
    show_office_web_apps: Optional[bool] = None
    # Primary theme color used in the Company Portal applications and web portal
    theme_color: Optional[RgbColor] = None
    # Logo image displayed in Company Portal apps which have a theme color background behind the logo
    theme_color_logo: Optional[MimeContent] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IntuneBrandingProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IntuneBrandingProfile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IntuneBrandingProfile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .company_portal_blocked_action import CompanyPortalBlockedAction
        from .enrollment_availability_options import EnrollmentAvailabilityOptions
        from .entity import Entity
        from .intune_branding_profile_assignment import IntuneBrandingProfileAssignment
        from .mime_content import MimeContent
        from .rgb_color import RgbColor

        from .company_portal_blocked_action import CompanyPortalBlockedAction
        from .enrollment_availability_options import EnrollmentAvailabilityOptions
        from .entity import Entity
        from .intune_branding_profile_assignment import IntuneBrandingProfileAssignment
        from .mime_content import MimeContent
        from .rgb_color import RgbColor

        fields: dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(IntuneBrandingProfileAssignment)),
            "companyPortalBlockedActions": lambda n : setattr(self, 'company_portal_blocked_actions', n.get_collection_of_object_values(CompanyPortalBlockedAction)),
            "contactITEmailAddress": lambda n : setattr(self, 'contact_i_t_email_address', n.get_str_value()),
            "contactITName": lambda n : setattr(self, 'contact_i_t_name', n.get_str_value()),
            "contactITNotes": lambda n : setattr(self, 'contact_i_t_notes', n.get_str_value()),
            "contactITPhoneNumber": lambda n : setattr(self, 'contact_i_t_phone_number', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "customCanSeePrivacyMessage": lambda n : setattr(self, 'custom_can_see_privacy_message', n.get_str_value()),
            "customCantSeePrivacyMessage": lambda n : setattr(self, 'custom_cant_see_privacy_message', n.get_str_value()),
            "customPrivacyMessage": lambda n : setattr(self, 'custom_privacy_message', n.get_str_value()),
            "disableClientTelemetry": lambda n : setattr(self, 'disable_client_telemetry', n.get_bool_value()),
            "disableDeviceCategorySelection": lambda n : setattr(self, 'disable_device_category_selection', n.get_bool_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "enrollmentAvailability": lambda n : setattr(self, 'enrollment_availability', n.get_enum_value(EnrollmentAvailabilityOptions)),
            "isDefaultProfile": lambda n : setattr(self, 'is_default_profile', n.get_bool_value()),
            "isFactoryResetDisabled": lambda n : setattr(self, 'is_factory_reset_disabled', n.get_bool_value()),
            "isRemoveDeviceDisabled": lambda n : setattr(self, 'is_remove_device_disabled', n.get_bool_value()),
            "landingPageCustomizedImage": lambda n : setattr(self, 'landing_page_customized_image', n.get_object_value(MimeContent)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "lightBackgroundLogo": lambda n : setattr(self, 'light_background_logo', n.get_object_value(MimeContent)),
            "onlineSupportSiteName": lambda n : setattr(self, 'online_support_site_name', n.get_str_value()),
            "onlineSupportSiteUrl": lambda n : setattr(self, 'online_support_site_url', n.get_str_value()),
            "privacyUrl": lambda n : setattr(self, 'privacy_url', n.get_str_value()),
            "profileDescription": lambda n : setattr(self, 'profile_description', n.get_str_value()),
            "profileName": lambda n : setattr(self, 'profile_name', n.get_str_value()),
            "roleScopeTagIds": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "showAzureADEnterpriseApps": lambda n : setattr(self, 'show_azure_a_d_enterprise_apps', n.get_bool_value()),
            "showConfigurationManagerApps": lambda n : setattr(self, 'show_configuration_manager_apps', n.get_bool_value()),
            "showDisplayNameNextToLogo": lambda n : setattr(self, 'show_display_name_next_to_logo', n.get_bool_value()),
            "showLogo": lambda n : setattr(self, 'show_logo', n.get_bool_value()),
            "showOfficeWebApps": lambda n : setattr(self, 'show_office_web_apps', n.get_bool_value()),
            "themeColor": lambda n : setattr(self, 'theme_color', n.get_object_value(RgbColor)),
            "themeColorLogo": lambda n : setattr(self, 'theme_color_logo', n.get_object_value(MimeContent)),
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
        writer.write_collection_of_object_values("companyPortalBlockedActions", self.company_portal_blocked_actions)
        writer.write_str_value("contactITEmailAddress", self.contact_i_t_email_address)
        writer.write_str_value("contactITName", self.contact_i_t_name)
        writer.write_str_value("contactITNotes", self.contact_i_t_notes)
        writer.write_str_value("contactITPhoneNumber", self.contact_i_t_phone_number)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("customCanSeePrivacyMessage", self.custom_can_see_privacy_message)
        writer.write_str_value("customCantSeePrivacyMessage", self.custom_cant_see_privacy_message)
        writer.write_str_value("customPrivacyMessage", self.custom_privacy_message)
        writer.write_bool_value("disableClientTelemetry", self.disable_client_telemetry)
        writer.write_bool_value("disableDeviceCategorySelection", self.disable_device_category_selection)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("enrollmentAvailability", self.enrollment_availability)
        writer.write_bool_value("isDefaultProfile", self.is_default_profile)
        writer.write_bool_value("isFactoryResetDisabled", self.is_factory_reset_disabled)
        writer.write_bool_value("isRemoveDeviceDisabled", self.is_remove_device_disabled)
        writer.write_object_value("landingPageCustomizedImage", self.landing_page_customized_image)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_object_value("lightBackgroundLogo", self.light_background_logo)
        writer.write_str_value("onlineSupportSiteName", self.online_support_site_name)
        writer.write_str_value("onlineSupportSiteUrl", self.online_support_site_url)
        writer.write_str_value("privacyUrl", self.privacy_url)
        writer.write_str_value("profileDescription", self.profile_description)
        writer.write_str_value("profileName", self.profile_name)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
        writer.write_bool_value("showAzureADEnterpriseApps", self.show_azure_a_d_enterprise_apps)
        writer.write_bool_value("showConfigurationManagerApps", self.show_configuration_manager_apps)
        writer.write_bool_value("showDisplayNameNextToLogo", self.show_display_name_next_to_logo)
        writer.write_bool_value("showLogo", self.show_logo)
        writer.write_bool_value("showOfficeWebApps", self.show_office_web_apps)
        writer.write_object_value("themeColor", self.theme_color)
        writer.write_object_value("themeColorLogo", self.theme_color_logo)
    

