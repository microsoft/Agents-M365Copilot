from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_device_owner_kiosk_mode_app import AndroidDeviceOwnerKioskModeApp
    from .android_device_owner_kiosk_mode_home_screen_item import AndroidDeviceOwnerKioskModeHomeScreenItem
    from .android_device_owner_kiosk_mode_weblink import AndroidDeviceOwnerKioskModeWeblink

from .android_device_owner_kiosk_mode_home_screen_item import AndroidDeviceOwnerKioskModeHomeScreenItem

@dataclass
class AndroidDeviceOwnerKioskModeFolderItem(AndroidDeviceOwnerKioskModeHomeScreenItem, Parsable):
    """
    Represents an item that can be added to Android Device Owner folder (application or weblink)
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.androidDeviceOwnerKioskModeFolderItem"
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AndroidDeviceOwnerKioskModeFolderItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidDeviceOwnerKioskModeFolderItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidDeviceOwnerKioskModeApp".casefold():
            from .android_device_owner_kiosk_mode_app import AndroidDeviceOwnerKioskModeApp

            return AndroidDeviceOwnerKioskModeApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidDeviceOwnerKioskModeWeblink".casefold():
            from .android_device_owner_kiosk_mode_weblink import AndroidDeviceOwnerKioskModeWeblink

            return AndroidDeviceOwnerKioskModeWeblink()
        return AndroidDeviceOwnerKioskModeFolderItem()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .android_device_owner_kiosk_mode_app import AndroidDeviceOwnerKioskModeApp
        from .android_device_owner_kiosk_mode_home_screen_item import AndroidDeviceOwnerKioskModeHomeScreenItem
        from .android_device_owner_kiosk_mode_weblink import AndroidDeviceOwnerKioskModeWeblink

        from .android_device_owner_kiosk_mode_app import AndroidDeviceOwnerKioskModeApp
        from .android_device_owner_kiosk_mode_home_screen_item import AndroidDeviceOwnerKioskModeHomeScreenItem
        from .android_device_owner_kiosk_mode_weblink import AndroidDeviceOwnerKioskModeWeblink

        fields: dict[str, Callable[[Any], None]] = {
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
    

