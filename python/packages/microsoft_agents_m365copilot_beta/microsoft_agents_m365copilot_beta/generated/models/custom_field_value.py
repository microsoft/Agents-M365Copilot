from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .planner_delta import PlannerDelta

from .planner_delta import PlannerDelta

@dataclass
class CustomFieldValue(PlannerDelta, Parsable):
    # ID of the customFieldDefinition this value is for. Immutable after creation.
    custom_field_definition_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The value of the custom field, formatted according to the field's valueType.
    value: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomFieldValue:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomFieldValue
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomFieldValue()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .planner_delta import PlannerDelta

        from .planner_delta import PlannerDelta

        fields: dict[str, Callable[[Any], None]] = {
            "customFieldDefinitionId": lambda n : setattr(self, 'custom_field_definition_id', n.get_str_value()),
            "value": lambda n : setattr(self, 'value', n.get_str_value()),
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
        writer.write_str_value("customFieldDefinitionId", self.custom_field_definition_id)
        writer.write_str_value("value", self.value)
    

