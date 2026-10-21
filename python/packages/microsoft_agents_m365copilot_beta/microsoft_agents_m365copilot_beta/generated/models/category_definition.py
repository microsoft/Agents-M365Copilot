from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .category_definition_capability import CategoryDefinitionCapability
    from .extension_field_collection import ExtensionFieldCollection
    from .planner_delta import PlannerDelta

from .planner_delta import PlannerDelta

@dataclass
class CategoryDefinition(PlannerDelta, Parsable):
    # Server-computed, read-only capability flags indicating which optional features are enabled for the entity.
    capabilities: Optional[CategoryDefinitionCapability] = None
    # Name of the category.
    display_name: Optional[str] = None
    # Custom extension field values set on the entity. Supports $select.
    extensions: Optional[ExtensionFieldCollection] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CategoryDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CategoryDefinition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CategoryDefinition()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .category_definition_capability import CategoryDefinitionCapability
        from .extension_field_collection import ExtensionFieldCollection
        from .planner_delta import PlannerDelta

        from .category_definition_capability import CategoryDefinitionCapability
        from .extension_field_collection import ExtensionFieldCollection
        from .planner_delta import PlannerDelta

        fields: dict[str, Callable[[Any], None]] = {
            "capabilities": lambda n : setattr(self, 'capabilities', n.get_object_value(CategoryDefinitionCapability)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "extensions": lambda n : setattr(self, 'extensions', n.get_object_value(ExtensionFieldCollection)),
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
        writer.write_object_value("extensions", self.extensions)
    

