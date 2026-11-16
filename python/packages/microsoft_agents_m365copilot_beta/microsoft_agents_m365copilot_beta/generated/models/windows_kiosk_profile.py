from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .windows_kiosk_app_configuration import WindowsKioskAppConfiguration
    from .windows_kiosk_user import WindowsKioskUser

@dataclass
class WindowsKioskProfile(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The app base class used to identify the application info for the kiosk configuration
    app_configuration: Optional[WindowsKioskAppConfiguration] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Key of the entity.
    profile_id: Optional[str] = None
    # This is a friendly name used to identify a group of applications, the layout of these apps on the start menu and the users to whom this kiosk configuration is assigned.
    profile_name: Optional[str] = None
    # The user accounts that will be locked to this kiosk configuration. This collection can contain a maximum of 100 elements.
    user_accounts_configuration: Optional[list[WindowsKioskUser]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsKioskProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsKioskProfile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsKioskProfile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .windows_kiosk_app_configuration import WindowsKioskAppConfiguration
        from .windows_kiosk_user import WindowsKioskUser

        from .windows_kiosk_app_configuration import WindowsKioskAppConfiguration
        from .windows_kiosk_user import WindowsKioskUser

        fields: dict[str, Callable[[Any], None]] = {
            "appConfiguration": lambda n : setattr(self, 'app_configuration', n.get_object_value(WindowsKioskAppConfiguration)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "profileId": lambda n : setattr(self, 'profile_id', n.get_str_value()),
            "profileName": lambda n : setattr(self, 'profile_name', n.get_str_value()),
            "userAccountsConfiguration": lambda n : setattr(self, 'user_accounts_configuration', n.get_collection_of_object_values(WindowsKioskUser)),
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
        writer.write_object_value("appConfiguration", self.app_configuration)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("profileId", self.profile_id)
        writer.write_str_value("profileName", self.profile_name)
        writer.write_collection_of_object_values("userAccountsConfiguration", self.user_accounts_configuration)
        writer.write_additional_data_value(self.additional_data)
    

