from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .custom_field_definition import CustomFieldDefinition

from .custom_field_definition import CustomFieldDefinition

@dataclass
class OptionsCustomFieldDefinition(CustomFieldDefinition, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.caseManagement.optionsCustomFieldDefinition"
    # The option value or values selected by default on a new case.
    default_values: Optional[list[str]] = None
    # The allowed option values a case author can choose from.
    options: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OptionsCustomFieldDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OptionsCustomFieldDefinition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OptionsCustomFieldDefinition()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .custom_field_definition import CustomFieldDefinition

        from .custom_field_definition import CustomFieldDefinition

        fields: dict[str, Callable[[Any], None]] = {
            "defaultValues": lambda n : setattr(self, 'default_values', n.get_collection_of_primitive_values(str)),
            "options": lambda n : setattr(self, 'options', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_primitive_values("defaultValues", self.default_values)
        writer.write_collection_of_primitive_values("options", self.options)
    

