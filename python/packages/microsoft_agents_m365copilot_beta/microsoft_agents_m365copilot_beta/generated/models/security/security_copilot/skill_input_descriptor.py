from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .skill_variable_descriptor import SkillVariableDescriptor

from .skill_variable_descriptor import SkillVariableDescriptor

@dataclass
class SkillInputDescriptor(SkillVariableDescriptor, Parsable):
    # Unsupported.
    default_value: Optional[str] = None
    # Unsupported.
    is_required: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Unsupported.
    placeholder_value: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SkillInputDescriptor:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SkillInputDescriptor
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SkillInputDescriptor()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .skill_variable_descriptor import SkillVariableDescriptor

        from .skill_variable_descriptor import SkillVariableDescriptor

        fields: dict[str, Callable[[Any], None]] = {
            "defaultValue": lambda n : setattr(self, 'default_value', n.get_str_value()),
            "isRequired": lambda n : setattr(self, 'is_required', n.get_bool_value()),
            "placeholderValue": lambda n : setattr(self, 'placeholder_value', n.get_str_value()),
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
        writer.write_str_value("defaultValue", self.default_value)
        writer.write_bool_value("isRequired", self.is_required)
        writer.write_str_value("placeholderValue", self.placeholder_value)
    

