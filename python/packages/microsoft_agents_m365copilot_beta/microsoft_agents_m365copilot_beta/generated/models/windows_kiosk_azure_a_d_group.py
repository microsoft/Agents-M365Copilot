from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .windows_kiosk_user import WindowsKioskUser

from .windows_kiosk_user import WindowsKioskUser

@dataclass
class WindowsKioskAzureADGroup(WindowsKioskUser, Parsable):
    """
    The class used to identify an AzureAD group for the kiosk configuration
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsKioskAzureADGroup"
    # The display name of the AzureAD group that will be locked to this kiosk configuration
    display_name: Optional[str] = None
    # The ID of the AzureAD group that will be locked to this kiosk configuration
    group_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsKioskAzureADGroup:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsKioskAzureADGroup
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsKioskAzureADGroup()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .windows_kiosk_user import WindowsKioskUser

        from .windows_kiosk_user import WindowsKioskUser

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "groupId": lambda n : setattr(self, 'group_id', n.get_str_value()),
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
        writer.write_str_value("groupId", self.group_id)
    

