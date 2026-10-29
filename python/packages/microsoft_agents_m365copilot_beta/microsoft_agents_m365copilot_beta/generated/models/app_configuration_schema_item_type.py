from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .app_configuration_schema_item_boolean_type import AppConfigurationSchemaItemBooleanType
    from .app_configuration_schema_item_bundle_array import AppConfigurationSchemaItemBundleArray
    from .app_configuration_schema_item_bundle_type import AppConfigurationSchemaItemBundleType
    from .app_configuration_schema_item_choice_type import AppConfigurationSchemaItemChoiceType
    from .app_configuration_schema_item_hidden_type import AppConfigurationSchemaItemHiddenType
    from .app_configuration_schema_item_integer_type import AppConfigurationSchemaItemIntegerType
    from .app_configuration_schema_item_multiselect_type import AppConfigurationSchemaItemMultiselectType
    from .app_configuration_schema_item_string_type import AppConfigurationSchemaItemStringType

@dataclass
class AppConfigurationSchemaItemType(AdditionalDataHolder, Parsable):
    """
    Single configuration item inside an Android application's configuration schema.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Description of what the item controls within the application
    description: Optional[str] = None
    # Human readable name
    display_name: Optional[str] = None
    # Unique index the application uses to maintain nested schema items. Valid values 0 to 2147483647
    index: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Index of parent schema item to track nested schema items. Valid values 0 to 2147483647
    parent_index: Optional[int] = None
    # Unique key the application uses to identify the item
    schema_item_key: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AppConfigurationSchemaItemType:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AppConfigurationSchemaItemType
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appConfigurationSchemaItemBooleanType".casefold():
            from .app_configuration_schema_item_boolean_type import AppConfigurationSchemaItemBooleanType

            return AppConfigurationSchemaItemBooleanType()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appConfigurationSchemaItemBundleArray".casefold():
            from .app_configuration_schema_item_bundle_array import AppConfigurationSchemaItemBundleArray

            return AppConfigurationSchemaItemBundleArray()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appConfigurationSchemaItemBundleType".casefold():
            from .app_configuration_schema_item_bundle_type import AppConfigurationSchemaItemBundleType

            return AppConfigurationSchemaItemBundleType()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appConfigurationSchemaItemChoiceType".casefold():
            from .app_configuration_schema_item_choice_type import AppConfigurationSchemaItemChoiceType

            return AppConfigurationSchemaItemChoiceType()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appConfigurationSchemaItemHiddenType".casefold():
            from .app_configuration_schema_item_hidden_type import AppConfigurationSchemaItemHiddenType

            return AppConfigurationSchemaItemHiddenType()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appConfigurationSchemaItemIntegerType".casefold():
            from .app_configuration_schema_item_integer_type import AppConfigurationSchemaItemIntegerType

            return AppConfigurationSchemaItemIntegerType()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appConfigurationSchemaItemMultiselectType".casefold():
            from .app_configuration_schema_item_multiselect_type import AppConfigurationSchemaItemMultiselectType

            return AppConfigurationSchemaItemMultiselectType()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appConfigurationSchemaItemStringType".casefold():
            from .app_configuration_schema_item_string_type import AppConfigurationSchemaItemStringType

            return AppConfigurationSchemaItemStringType()
        return AppConfigurationSchemaItemType()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .app_configuration_schema_item_boolean_type import AppConfigurationSchemaItemBooleanType
        from .app_configuration_schema_item_bundle_array import AppConfigurationSchemaItemBundleArray
        from .app_configuration_schema_item_bundle_type import AppConfigurationSchemaItemBundleType
        from .app_configuration_schema_item_choice_type import AppConfigurationSchemaItemChoiceType
        from .app_configuration_schema_item_hidden_type import AppConfigurationSchemaItemHiddenType
        from .app_configuration_schema_item_integer_type import AppConfigurationSchemaItemIntegerType
        from .app_configuration_schema_item_multiselect_type import AppConfigurationSchemaItemMultiselectType
        from .app_configuration_schema_item_string_type import AppConfigurationSchemaItemStringType

        from .app_configuration_schema_item_boolean_type import AppConfigurationSchemaItemBooleanType
        from .app_configuration_schema_item_bundle_array import AppConfigurationSchemaItemBundleArray
        from .app_configuration_schema_item_bundle_type import AppConfigurationSchemaItemBundleType
        from .app_configuration_schema_item_choice_type import AppConfigurationSchemaItemChoiceType
        from .app_configuration_schema_item_hidden_type import AppConfigurationSchemaItemHiddenType
        from .app_configuration_schema_item_integer_type import AppConfigurationSchemaItemIntegerType
        from .app_configuration_schema_item_multiselect_type import AppConfigurationSchemaItemMultiselectType
        from .app_configuration_schema_item_string_type import AppConfigurationSchemaItemStringType

        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "index": lambda n : setattr(self, 'index', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "parentIndex": lambda n : setattr(self, 'parent_index', n.get_int_value()),
            "schemaItemKey": lambda n : setattr(self, 'schema_item_key', n.get_str_value()),
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
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_int_value("index", self.index)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("parentIndex", self.parent_index)
        writer.write_str_value("schemaItemKey", self.schema_item_key)
        writer.write_additional_data_value(self.additional_data)
    

