from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .device_enrollment_configuration import DeviceEnrollmentConfiguration
    from .enrollment_notification_branding_options import EnrollmentNotificationBrandingOptions
    from .enrollment_notification_template_type import EnrollmentNotificationTemplateType
    from .enrollment_restriction_platform_type import EnrollmentRestrictionPlatformType

from .device_enrollment_configuration import DeviceEnrollmentConfiguration

@dataclass
class DeviceEnrollmentNotificationConfiguration(DeviceEnrollmentConfiguration, Parsable):
    """
    Enrollment Notification Configuration which is used to send notification
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.deviceEnrollmentNotificationConfiguration"
    # Branding Options for the Message Template. Branding is defined in the Intune Admin Console.
    branding_options: Optional[EnrollmentNotificationBrandingOptions] = None
    # DefaultLocale for the Enrollment Notification
    default_locale: Optional[str] = None
    # Notification Message Template Id
    notification_message_template_id: Optional[UUID] = None
    # The list of notification data -
    notification_templates: Optional[list[str]] = None
    # This enum indicates the platform type for which the enrollment restriction applies.
    platform_type: Optional[EnrollmentRestrictionPlatformType] = None
    # This enum indicates the Template type for which the enrollment notification applies.
    template_type: Optional[EnrollmentNotificationTemplateType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceEnrollmentNotificationConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceEnrollmentNotificationConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceEnrollmentNotificationConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_enrollment_configuration import DeviceEnrollmentConfiguration
        from .enrollment_notification_branding_options import EnrollmentNotificationBrandingOptions
        from .enrollment_notification_template_type import EnrollmentNotificationTemplateType
        from .enrollment_restriction_platform_type import EnrollmentRestrictionPlatformType

        from .device_enrollment_configuration import DeviceEnrollmentConfiguration
        from .enrollment_notification_branding_options import EnrollmentNotificationBrandingOptions
        from .enrollment_notification_template_type import EnrollmentNotificationTemplateType
        from .enrollment_restriction_platform_type import EnrollmentRestrictionPlatformType

        fields: dict[str, Callable[[Any], None]] = {
            "brandingOptions": lambda n : setattr(self, 'branding_options', n.get_collection_of_enum_values(EnrollmentNotificationBrandingOptions)),
            "defaultLocale": lambda n : setattr(self, 'default_locale', n.get_str_value()),
            "notificationMessageTemplateId": lambda n : setattr(self, 'notification_message_template_id', n.get_uuid_value()),
            "notificationTemplates": lambda n : setattr(self, 'notification_templates', n.get_collection_of_primitive_values(str)),
            "platformType": lambda n : setattr(self, 'platform_type', n.get_enum_value(EnrollmentRestrictionPlatformType)),
            "templateType": lambda n : setattr(self, 'template_type', n.get_enum_value(EnrollmentNotificationTemplateType)),
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
        writer.write_enum_value("brandingOptions", self.branding_options)
        writer.write_str_value("defaultLocale", self.default_locale)
        writer.write_uuid_value("notificationMessageTemplateId", self.notification_message_template_id)
        writer.write_collection_of_primitive_values("notificationTemplates", self.notification_templates)
        writer.write_enum_value("platformType", self.platform_type)
        writer.write_enum_value("templateType", self.template_type)
    

