from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_configuration_choice_setting_collection_instance import DeviceManagementConfigurationChoiceSettingCollectionInstance
    from .device_management_configuration_choice_setting_instance import DeviceManagementConfigurationChoiceSettingInstance
    from .device_management_configuration_group_setting_collection_instance import DeviceManagementConfigurationGroupSettingCollectionInstance
    from .device_management_configuration_group_setting_instance import DeviceManagementConfigurationGroupSettingInstance
    from .device_management_configuration_setting_group_collection_instance import DeviceManagementConfigurationSettingGroupCollectionInstance
    from .device_management_configuration_setting_group_instance import DeviceManagementConfigurationSettingGroupInstance
    from .device_management_configuration_setting_instance_template_reference import DeviceManagementConfigurationSettingInstanceTemplateReference
    from .device_management_configuration_simple_setting_collection_instance import DeviceManagementConfigurationSimpleSettingCollectionInstance
    from .device_management_configuration_simple_setting_instance import DeviceManagementConfigurationSimpleSettingInstance

@dataclass
class DeviceManagementConfigurationSettingInstance(AdditionalDataHolder, Parsable):
    """
    Setting instance within policy
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # Setting Definition Id
    setting_definition_id: Optional[str] = None
    # Setting Instance Template Reference
    setting_instance_template_reference: Optional[DeviceManagementConfigurationSettingInstanceTemplateReference] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementConfigurationSettingInstance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationSettingInstance
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationChoiceSettingCollectionInstance".casefold():
            from .device_management_configuration_choice_setting_collection_instance import DeviceManagementConfigurationChoiceSettingCollectionInstance

            return DeviceManagementConfigurationChoiceSettingCollectionInstance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationChoiceSettingInstance".casefold():
            from .device_management_configuration_choice_setting_instance import DeviceManagementConfigurationChoiceSettingInstance

            return DeviceManagementConfigurationChoiceSettingInstance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationGroupSettingCollectionInstance".casefold():
            from .device_management_configuration_group_setting_collection_instance import DeviceManagementConfigurationGroupSettingCollectionInstance

            return DeviceManagementConfigurationGroupSettingCollectionInstance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationGroupSettingInstance".casefold():
            from .device_management_configuration_group_setting_instance import DeviceManagementConfigurationGroupSettingInstance

            return DeviceManagementConfigurationGroupSettingInstance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationSettingGroupCollectionInstance".casefold():
            from .device_management_configuration_setting_group_collection_instance import DeviceManagementConfigurationSettingGroupCollectionInstance

            return DeviceManagementConfigurationSettingGroupCollectionInstance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationSettingGroupInstance".casefold():
            from .device_management_configuration_setting_group_instance import DeviceManagementConfigurationSettingGroupInstance

            return DeviceManagementConfigurationSettingGroupInstance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationSimpleSettingCollectionInstance".casefold():
            from .device_management_configuration_simple_setting_collection_instance import DeviceManagementConfigurationSimpleSettingCollectionInstance

            return DeviceManagementConfigurationSimpleSettingCollectionInstance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationSimpleSettingInstance".casefold():
            from .device_management_configuration_simple_setting_instance import DeviceManagementConfigurationSimpleSettingInstance

            return DeviceManagementConfigurationSimpleSettingInstance()
        return DeviceManagementConfigurationSettingInstance()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_configuration_choice_setting_collection_instance import DeviceManagementConfigurationChoiceSettingCollectionInstance
        from .device_management_configuration_choice_setting_instance import DeviceManagementConfigurationChoiceSettingInstance
        from .device_management_configuration_group_setting_collection_instance import DeviceManagementConfigurationGroupSettingCollectionInstance
        from .device_management_configuration_group_setting_instance import DeviceManagementConfigurationGroupSettingInstance
        from .device_management_configuration_setting_group_collection_instance import DeviceManagementConfigurationSettingGroupCollectionInstance
        from .device_management_configuration_setting_group_instance import DeviceManagementConfigurationSettingGroupInstance
        from .device_management_configuration_setting_instance_template_reference import DeviceManagementConfigurationSettingInstanceTemplateReference
        from .device_management_configuration_simple_setting_collection_instance import DeviceManagementConfigurationSimpleSettingCollectionInstance
        from .device_management_configuration_simple_setting_instance import DeviceManagementConfigurationSimpleSettingInstance

        from .device_management_configuration_choice_setting_collection_instance import DeviceManagementConfigurationChoiceSettingCollectionInstance
        from .device_management_configuration_choice_setting_instance import DeviceManagementConfigurationChoiceSettingInstance
        from .device_management_configuration_group_setting_collection_instance import DeviceManagementConfigurationGroupSettingCollectionInstance
        from .device_management_configuration_group_setting_instance import DeviceManagementConfigurationGroupSettingInstance
        from .device_management_configuration_setting_group_collection_instance import DeviceManagementConfigurationSettingGroupCollectionInstance
        from .device_management_configuration_setting_group_instance import DeviceManagementConfigurationSettingGroupInstance
        from .device_management_configuration_setting_instance_template_reference import DeviceManagementConfigurationSettingInstanceTemplateReference
        from .device_management_configuration_simple_setting_collection_instance import DeviceManagementConfigurationSimpleSettingCollectionInstance
        from .device_management_configuration_simple_setting_instance import DeviceManagementConfigurationSimpleSettingInstance

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "settingDefinitionId": lambda n : setattr(self, 'setting_definition_id', n.get_str_value()),
            "settingInstanceTemplateReference": lambda n : setattr(self, 'setting_instance_template_reference', n.get_object_value(DeviceManagementConfigurationSettingInstanceTemplateReference)),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("settingDefinitionId", self.setting_definition_id)
        writer.write_object_value("settingInstanceTemplateReference", self.setting_instance_template_reference)
        writer.write_additional_data_value(self.additional_data)
    

