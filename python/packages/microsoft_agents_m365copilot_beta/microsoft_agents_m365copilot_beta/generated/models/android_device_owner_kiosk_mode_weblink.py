from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_device_owner_kiosk_mode_folder_item import AndroidDeviceOwnerKioskModeFolderItem

from .android_device_owner_kiosk_mode_folder_item import AndroidDeviceOwnerKioskModeFolderItem

@dataclass
class AndroidDeviceOwnerKioskModeWeblink(AndroidDeviceOwnerKioskModeFolderItem, Parsable):
    """
    A weblink on the Android Device Owner Managed Home Screen
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.androidDeviceOwnerKioskModeWeblink"
    # Display name for weblink
    label: Optional[str] = None
    # Link for weblink
    link: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AndroidDeviceOwnerKioskModeWeblink:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidDeviceOwnerKioskModeWeblink
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AndroidDeviceOwnerKioskModeWeblink()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .android_device_owner_kiosk_mode_folder_item import AndroidDeviceOwnerKioskModeFolderItem

        from .android_device_owner_kiosk_mode_folder_item import AndroidDeviceOwnerKioskModeFolderItem

        fields: dict[str, Callable[[Any], None]] = {
            "label": lambda n : setattr(self, 'label', n.get_str_value()),
            "link": lambda n : setattr(self, 'link', n.get_str_value()),
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
        writer.write_str_value("label", self.label)
        writer.write_str_value("link", self.link)
    

