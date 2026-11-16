from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_managed_store_app_configuration_schema_item_data_type import AndroidManagedStoreAppConfigurationSchemaItemDataType
    from .key_value_pair import KeyValuePair

@dataclass
class AndroidManagedStoreAppConfigurationSchemaItem(AdditionalDataHolder, Parsable):
    """
    Single configuration item inside an Android application's custom configuration schema.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Data type for a configuration item inside an Android application's custom configuration schema
    data_type: Optional[AndroidManagedStoreAppConfigurationSchemaItemDataType] = None
    # Default value for boolean type items, if specified by the app developer
    default_bool_value: Optional[bool] = None
    # Default value for integer type items, if specified by the app developer
    default_int_value: Optional[int] = None
    # Default value for string array type items, if specified by the app developer
    default_string_array_value: Optional[list[str]] = None
    # Default value for string type items, if specified by the app developer
    default_string_value: Optional[str] = None
    # Description of what the item controls within the application
    description: Optional[str] = None
    # Human readable name
    display_name: Optional[str] = None
    # Unique index the application uses to maintain nested schema items
    index: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Index of parent schema item to track nested schema items
    parent_index: Optional[int] = None
    # Unique key the application uses to identify the item
    schema_item_key: Optional[str] = None
    # List of human readable name/value pairs for the valid values that can be set for this item (Choice and Multiselect items only)
    selections: Optional[list[KeyValuePair]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AndroidManagedStoreAppConfigurationSchemaItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidManagedStoreAppConfigurationSchemaItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AndroidManagedStoreAppConfigurationSchemaItem()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .android_managed_store_app_configuration_schema_item_data_type import AndroidManagedStoreAppConfigurationSchemaItemDataType
        from .key_value_pair import KeyValuePair

        from .android_managed_store_app_configuration_schema_item_data_type import AndroidManagedStoreAppConfigurationSchemaItemDataType
        from .key_value_pair import KeyValuePair

        fields: dict[str, Callable[[Any], None]] = {
            "dataType": lambda n : setattr(self, 'data_type', n.get_enum_value(AndroidManagedStoreAppConfigurationSchemaItemDataType)),
            "defaultBoolValue": lambda n : setattr(self, 'default_bool_value', n.get_bool_value()),
            "defaultIntValue": lambda n : setattr(self, 'default_int_value', n.get_int_value()),
            "defaultStringArrayValue": lambda n : setattr(self, 'default_string_array_value', n.get_collection_of_primitive_values(str)),
            "defaultStringValue": lambda n : setattr(self, 'default_string_value', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "index": lambda n : setattr(self, 'index', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "parentIndex": lambda n : setattr(self, 'parent_index', n.get_int_value()),
            "schemaItemKey": lambda n : setattr(self, 'schema_item_key', n.get_str_value()),
            "selections": lambda n : setattr(self, 'selections', n.get_collection_of_object_values(KeyValuePair)),
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
        writer.write_enum_value("dataType", self.data_type)
        writer.write_bool_value("defaultBoolValue", self.default_bool_value)
        writer.write_int_value("defaultIntValue", self.default_int_value)
        writer.write_collection_of_primitive_values("defaultStringArrayValue", self.default_string_array_value)
        writer.write_str_value("defaultStringValue", self.default_string_value)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_int_value("index", self.index)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("parentIndex", self.parent_index)
        writer.write_str_value("schemaItemKey", self.schema_item_key)
        writer.write_collection_of_object_values("selections", self.selections)
        writer.write_additional_data_value(self.additional_data)
    

