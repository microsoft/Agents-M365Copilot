from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_abstract_complex_setting_instance import DeviceManagementAbstractComplexSettingInstance
    from .device_management_boolean_setting_instance import DeviceManagementBooleanSettingInstance
    from .device_management_collection_setting_instance import DeviceManagementCollectionSettingInstance
    from .device_management_complex_setting_instance import DeviceManagementComplexSettingInstance
    from .device_management_integer_setting_instance import DeviceManagementIntegerSettingInstance
    from .device_management_string_setting_instance import DeviceManagementStringSettingInstance
    from .entity import Entity

from .entity import Entity

@dataclass
class DeviceManagementSettingInstance(Entity, Parsable):
    """
    Base type for a setting instance
    """
    # The ID of the setting definition for this instance
    definition_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # JSON representation of the value
    value_json: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementSettingInstance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementSettingInstance
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementAbstractComplexSettingInstance".casefold():
            from .device_management_abstract_complex_setting_instance import DeviceManagementAbstractComplexSettingInstance

            return DeviceManagementAbstractComplexSettingInstance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementBooleanSettingInstance".casefold():
            from .device_management_boolean_setting_instance import DeviceManagementBooleanSettingInstance

            return DeviceManagementBooleanSettingInstance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementCollectionSettingInstance".casefold():
            from .device_management_collection_setting_instance import DeviceManagementCollectionSettingInstance

            return DeviceManagementCollectionSettingInstance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementComplexSettingInstance".casefold():
            from .device_management_complex_setting_instance import DeviceManagementComplexSettingInstance

            return DeviceManagementComplexSettingInstance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementIntegerSettingInstance".casefold():
            from .device_management_integer_setting_instance import DeviceManagementIntegerSettingInstance

            return DeviceManagementIntegerSettingInstance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementStringSettingInstance".casefold():
            from .device_management_string_setting_instance import DeviceManagementStringSettingInstance

            return DeviceManagementStringSettingInstance()
        return DeviceManagementSettingInstance()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_abstract_complex_setting_instance import DeviceManagementAbstractComplexSettingInstance
        from .device_management_boolean_setting_instance import DeviceManagementBooleanSettingInstance
        from .device_management_collection_setting_instance import DeviceManagementCollectionSettingInstance
        from .device_management_complex_setting_instance import DeviceManagementComplexSettingInstance
        from .device_management_integer_setting_instance import DeviceManagementIntegerSettingInstance
        from .device_management_string_setting_instance import DeviceManagementStringSettingInstance
        from .entity import Entity

        from .device_management_abstract_complex_setting_instance import DeviceManagementAbstractComplexSettingInstance
        from .device_management_boolean_setting_instance import DeviceManagementBooleanSettingInstance
        from .device_management_collection_setting_instance import DeviceManagementCollectionSettingInstance
        from .device_management_complex_setting_instance import DeviceManagementComplexSettingInstance
        from .device_management_integer_setting_instance import DeviceManagementIntegerSettingInstance
        from .device_management_string_setting_instance import DeviceManagementStringSettingInstance
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "definitionId": lambda n : setattr(self, 'definition_id', n.get_str_value()),
            "valueJson": lambda n : setattr(self, 'value_json', n.get_str_value()),
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
        writer.write_str_value("definitionId", self.definition_id)
        writer.write_str_value("valueJson", self.value_json)
    

