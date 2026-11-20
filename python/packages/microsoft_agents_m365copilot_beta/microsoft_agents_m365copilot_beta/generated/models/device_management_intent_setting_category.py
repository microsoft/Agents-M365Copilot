from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_setting_category import DeviceManagementSettingCategory
    from .device_management_setting_instance import DeviceManagementSettingInstance

from .device_management_setting_category import DeviceManagementSettingCategory

@dataclass
class DeviceManagementIntentSettingCategory(DeviceManagementSettingCategory, Parsable):
    """
    Entity representing an intent setting category
    """
    # The OdataType property
    odata_type: Optional[str] = None
    # The settings this category contains
    settings: Optional[list[DeviceManagementSettingInstance]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementIntentSettingCategory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementIntentSettingCategory
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementIntentSettingCategory()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_setting_category import DeviceManagementSettingCategory
        from .device_management_setting_instance import DeviceManagementSettingInstance

        from .device_management_setting_category import DeviceManagementSettingCategory
        from .device_management_setting_instance import DeviceManagementSettingInstance

        fields: dict[str, Callable[[Any], None]] = {
            "settings": lambda n : setattr(self, 'settings', n.get_collection_of_object_values(DeviceManagementSettingInstance)),
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
        writer.write_collection_of_object_values("settings", self.settings)
    

