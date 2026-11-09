from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_derived_credential_issuer import DeviceManagementDerivedCredentialIssuer
    from .device_management_derived_credential_notification_type import DeviceManagementDerivedCredentialNotificationType
    from .entity import Entity

from .entity import Entity

@dataclass
class DeviceManagementDerivedCredentialSettings(Entity, Parsable):
    """
    Entity that describes tenant level settings for derived credentials
    """
    # The display name for the profile.
    display_name: Optional[str] = None
    # The URL that will be accessible to end users as they retrieve a derived credential using the Company Portal.
    help_url: Optional[str] = None
    # Supported values for the derived credential issuer.
    issuer: Optional[DeviceManagementDerivedCredentialIssuer] = None
    # Supported values for the notification type to use.
    notification_type: Optional[DeviceManagementDerivedCredentialNotificationType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The nominal percentage of time before certificate renewal is initiated by the client.
    renewal_threshold_percentage: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementDerivedCredentialSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementDerivedCredentialSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementDerivedCredentialSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_derived_credential_issuer import DeviceManagementDerivedCredentialIssuer
        from .device_management_derived_credential_notification_type import DeviceManagementDerivedCredentialNotificationType
        from .entity import Entity

        from .device_management_derived_credential_issuer import DeviceManagementDerivedCredentialIssuer
        from .device_management_derived_credential_notification_type import DeviceManagementDerivedCredentialNotificationType
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "helpUrl": lambda n : setattr(self, 'help_url', n.get_str_value()),
            "issuer": lambda n : setattr(self, 'issuer', n.get_enum_value(DeviceManagementDerivedCredentialIssuer)),
            "notificationType": lambda n : setattr(self, 'notification_type', n.get_collection_of_enum_values(DeviceManagementDerivedCredentialNotificationType)),
            "renewalThresholdPercentage": lambda n : setattr(self, 'renewal_threshold_percentage', n.get_int_value()),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("helpUrl", self.help_url)
        writer.write_enum_value("issuer", self.issuer)
        writer.write_enum_value("notificationType", self.notification_type)
        writer.write_int_value("renewalThresholdPercentage", self.renewal_threshold_percentage)
    

