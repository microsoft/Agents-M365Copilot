from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_managed_store_app_configuration_schema_item import AndroidManagedStoreAppConfigurationSchemaItem
    from .entity import Entity

from .entity import Entity

@dataclass
class AndroidManagedStoreAppConfigurationSchema(Entity, Parsable):
    """
    Schema describing an Android application's custom configurations.
    """
    # UTF8 encoded byte array containing example JSON string conforming to this schema that demonstrates how to set the configuration for this app
    example_json: Optional[bytes] = None
    # Collection of items each representing a named configuration option in the schema. It contains a flat list of all configuration.
    nested_schema_items: Optional[list[AndroidManagedStoreAppConfigurationSchemaItem]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Collection of items each representing a named configuration option in the schema. It only contains the root-level configuration.
    schema_items: Optional[list[AndroidManagedStoreAppConfigurationSchemaItem]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AndroidManagedStoreAppConfigurationSchema:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidManagedStoreAppConfigurationSchema
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AndroidManagedStoreAppConfigurationSchema()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .android_managed_store_app_configuration_schema_item import AndroidManagedStoreAppConfigurationSchemaItem
        from .entity import Entity

        from .android_managed_store_app_configuration_schema_item import AndroidManagedStoreAppConfigurationSchemaItem
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "exampleJson": lambda n : setattr(self, 'example_json', n.get_bytes_value()),
            "nestedSchemaItems": lambda n : setattr(self, 'nested_schema_items', n.get_collection_of_object_values(AndroidManagedStoreAppConfigurationSchemaItem)),
            "schemaItems": lambda n : setattr(self, 'schema_items', n.get_collection_of_object_values(AndroidManagedStoreAppConfigurationSchemaItem)),
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
        writer.write_bytes_value("exampleJson", self.example_json)
        writer.write_collection_of_object_values("nestedSchemaItems", self.nested_schema_items)
        writer.write_collection_of_object_values("schemaItems", self.schema_items)
    

