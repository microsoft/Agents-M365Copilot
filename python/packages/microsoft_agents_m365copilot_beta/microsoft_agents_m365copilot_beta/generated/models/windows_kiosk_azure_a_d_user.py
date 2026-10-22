from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .windows_kiosk_user import WindowsKioskUser

from .windows_kiosk_user import WindowsKioskUser

@dataclass
class WindowsKioskAzureADUser(WindowsKioskUser, Parsable):
    """
    The class used to identify an AzureAD user account for the kiosk configuration
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsKioskAzureADUser"
    # The ID of the AzureAD user that will be locked to this kiosk configuration
    user_id: Optional[str] = None
    # The user accounts that will be locked to this kiosk configuration
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsKioskAzureADUser:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsKioskAzureADUser
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsKioskAzureADUser()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .windows_kiosk_user import WindowsKioskUser

        from .windows_kiosk_user import WindowsKioskUser

        fields: dict[str, Callable[[Any], None]] = {
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
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
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    

