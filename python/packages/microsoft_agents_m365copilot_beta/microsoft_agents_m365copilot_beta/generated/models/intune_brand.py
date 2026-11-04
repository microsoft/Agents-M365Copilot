from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .company_portal_blocked_action import CompanyPortalBlockedAction
    from .enrollment_availability_options import EnrollmentAvailabilityOptions
    from .mime_content import MimeContent
    from .rgb_color import RgbColor

@dataclass
class IntuneBrand(AdditionalDataHolder, Parsable):
    """
    intuneBrand contains data which is used in customizing the appearance of the Company Portal applications as well as the end user web portal.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Collection of blocked actions on the company portal as per platform and device ownership types.
    company_portal_blocked_actions: Optional[list[CompanyPortalBlockedAction]] = None
    # Email address of the person/organization responsible for IT support.
    contact_i_t_email_address: Optional[str] = None
    # Name of the person/organization responsible for IT support.
    contact_i_t_name: Optional[str] = None
    # Text comments regarding the person/organization responsible for IT support.
    contact_i_t_notes: Optional[str] = None
    # Phone number of the person/organization responsible for IT support.
    contact_i_t_phone_number: Optional[str] = None
    # The custom privacy message used to explain what the organization can see and do on managed devices.
    custom_can_see_privacy_message: Optional[str] = None
    # The custom privacy message used to explain what the organization can’t see or do on managed devices.
    custom_cant_see_privacy_message: Optional[str] = None
    # The custom privacy message used to explain what the organization can’t see or do on managed devices.
    custom_privacy_message: Optional[str] = None
    # Logo image displayed in Company Portal apps which have a dark background behind the logo.
    dark_background_logo: Optional[MimeContent] = None
    # Applies to telemetry sent from all clients to the Intune service. When disabled, all proactive troubleshooting and issue warnings within the client are turned off, and telemetry settings appear inactive or hidden to the device user.
    disable_client_telemetry: Optional[bool] = None
    # Boolean that indicates if Device Category Selection will be shown in Company Portal
    disable_device_category_selection: Optional[bool] = None
    # Company/organization name that is displayed to end users.
    display_name: Optional[str] = None
    # Options available for enrollment flow customization
    enrollment_availability: Optional[EnrollmentAvailabilityOptions] = None
    # Boolean that represents whether the adminsistrator has disabled the 'Factory Reset' action on corporate owned devices.
    is_factory_reset_disabled: Optional[bool] = None
    # Boolean that represents whether the adminsistrator has disabled the 'Remove Device' action on corporate owned devices.
    is_remove_device_disabled: Optional[bool] = None
    # Customized image displayed in Company Portal app landing page
    landing_page_customized_image: Optional[MimeContent] = None
    # Logo image displayed in Company Portal apps which have a light background behind the logo.
    light_background_logo: Optional[MimeContent] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Display name of the company/organization’s IT helpdesk site.
    online_support_site_name: Optional[str] = None
    # URL to the company/organization’s IT helpdesk site.
    online_support_site_url: Optional[str] = None
    # URL to the company/organization’s privacy policy.
    privacy_url: Optional[str] = None
    # List of scope tags assigned to the default branding profile
    role_scope_tag_ids: Optional[list[str]] = None
    # Boolean that indicates if AzureAD Enterprise Apps will be shown in Company Portal
    show_azure_a_d_enterprise_apps: Optional[bool] = None
    # Boolean that indicates if ConfigurationManagerApps will be shown in Company Portal
    show_configuration_manager_apps: Optional[bool] = None
    # Boolean that represents whether the administrator-supplied display name will be shown next to the logo image.
    show_display_name_next_to_logo: Optional[bool] = None
    # Boolean that represents whether the administrator-supplied logo images are shown or not shown.
    show_logo: Optional[bool] = None
    # Boolean that represents whether the administrator-supplied display name will be shown next to the logo image.
    show_name_next_to_logo: Optional[bool] = None
    # Boolean that indicates if Office WebApps will be shown in Company Portal
    show_office_web_apps: Optional[bool] = None
    # Primary theme color used in the Company Portal applications and web portal.
    theme_color: Optional[RgbColor] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IntuneBrand:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IntuneBrand
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IntuneBrand()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .company_portal_blocked_action import CompanyPortalBlockedAction
        from .enrollment_availability_options import EnrollmentAvailabilityOptions
        from .mime_content import MimeContent
        from .rgb_color import RgbColor

        from .company_portal_blocked_action import CompanyPortalBlockedAction
        from .enrollment_availability_options import EnrollmentAvailabilityOptions
        from .mime_content import MimeContent
        from .rgb_color import RgbColor

        fields: dict[str, Callable[[Any], None]] = {
            "companyPortalBlockedActions": lambda n : setattr(self, 'company_portal_blocked_actions', n.get_collection_of_object_values(CompanyPortalBlockedAction)),
            "contactITEmailAddress": lambda n : setattr(self, 'contact_i_t_email_address', n.get_str_value()),
            "contactITName": lambda n : setattr(self, 'contact_i_t_name', n.get_str_value()),
            "contactITNotes": lambda n : setattr(self, 'contact_i_t_notes', n.get_str_value()),
            "contactITPhoneNumber": lambda n : setattr(self, 'contact_i_t_phone_number', n.get_str_value()),
            "customCanSeePrivacyMessage": lambda n : setattr(self, 'custom_can_see_privacy_message', n.get_str_value()),
            "customCantSeePrivacyMessage": lambda n : setattr(self, 'custom_cant_see_privacy_message', n.get_str_value()),
            "customPrivacyMessage": lambda n : setattr(self, 'custom_privacy_message', n.get_str_value()),
            "darkBackgroundLogo": lambda n : setattr(self, 'dark_background_logo', n.get_object_value(MimeContent)),
            "disableClientTelemetry": lambda n : setattr(self, 'disable_client_telemetry', n.get_bool_value()),
            "disableDeviceCategorySelection": lambda n : setattr(self, 'disable_device_category_selection', n.get_bool_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "enrollmentAvailability": lambda n : setattr(self, 'enrollment_availability', n.get_enum_value(EnrollmentAvailabilityOptions)),
            "isFactoryResetDisabled": lambda n : setattr(self, 'is_factory_reset_disabled', n.get_bool_value()),
            "isRemoveDeviceDisabled": lambda n : setattr(self, 'is_remove_device_disabled', n.get_bool_value()),
            "landingPageCustomizedImage": lambda n : setattr(self, 'landing_page_customized_image', n.get_object_value(MimeContent)),
            "lightBackgroundLogo": lambda n : setattr(self, 'light_background_logo', n.get_object_value(MimeContent)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "onlineSupportSiteName": lambda n : setattr(self, 'online_support_site_name', n.get_str_value()),
            "onlineSupportSiteUrl": lambda n : setattr(self, 'online_support_site_url', n.get_str_value()),
            "privacyUrl": lambda n : setattr(self, 'privacy_url', n.get_str_value()),
            "roleScopeTagIds": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "showAzureADEnterpriseApps": lambda n : setattr(self, 'show_azure_a_d_enterprise_apps', n.get_bool_value()),
            "showConfigurationManagerApps": lambda n : setattr(self, 'show_configuration_manager_apps', n.get_bool_value()),
            "showDisplayNameNextToLogo": lambda n : setattr(self, 'show_display_name_next_to_logo', n.get_bool_value()),
            "showLogo": lambda n : setattr(self, 'show_logo', n.get_bool_value()),
            "showNameNextToLogo": lambda n : setattr(self, 'show_name_next_to_logo', n.get_bool_value()),
            "showOfficeWebApps": lambda n : setattr(self, 'show_office_web_apps', n.get_bool_value()),
            "themeColor": lambda n : setattr(self, 'theme_color', n.get_object_value(RgbColor)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_object_values("companyPortalBlockedActions", self.company_portal_blocked_actions)
        writer.write_str_value("contactITEmailAddress", self.contact_i_t_email_address)
        writer.write_str_value("contactITName", self.contact_i_t_name)
        writer.write_str_value("contactITNotes", self.contact_i_t_notes)
        writer.write_str_value("contactITPhoneNumber", self.contact_i_t_phone_number)
        writer.write_str_value("customCanSeePrivacyMessage", self.custom_can_see_privacy_message)
        writer.write_str_value("customCantSeePrivacyMessage", self.custom_cant_see_privacy_message)
        writer.write_str_value("customPrivacyMessage", self.custom_privacy_message)
        writer.write_object_value("darkBackgroundLogo", self.dark_background_logo)
        writer.write_bool_value("disableClientTelemetry", self.disable_client_telemetry)
        writer.write_bool_value("disableDeviceCategorySelection", self.disable_device_category_selection)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("enrollmentAvailability", self.enrollment_availability)
        writer.write_bool_value("isFactoryResetDisabled", self.is_factory_reset_disabled)
        writer.write_bool_value("isRemoveDeviceDisabled", self.is_remove_device_disabled)
        writer.write_object_value("landingPageCustomizedImage", self.landing_page_customized_image)
        writer.write_object_value("lightBackgroundLogo", self.light_background_logo)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("onlineSupportSiteName", self.online_support_site_name)
        writer.write_str_value("onlineSupportSiteUrl", self.online_support_site_url)
        writer.write_str_value("privacyUrl", self.privacy_url)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
        writer.write_bool_value("showAzureADEnterpriseApps", self.show_azure_a_d_enterprise_apps)
        writer.write_bool_value("showConfigurationManagerApps", self.show_configuration_manager_apps)
        writer.write_bool_value("showDisplayNameNextToLogo", self.show_display_name_next_to_logo)
        writer.write_bool_value("showLogo", self.show_logo)
        writer.write_bool_value("showNameNextToLogo", self.show_name_next_to_logo)
        writer.write_bool_value("showOfficeWebApps", self.show_office_web_apps)
        writer.write_object_value("themeColor", self.theme_color)
        writer.write_additional_data_value(self.additional_data)
    

