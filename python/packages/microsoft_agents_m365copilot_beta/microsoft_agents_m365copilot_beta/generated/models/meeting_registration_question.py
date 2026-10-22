from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .answer_input_type import AnswerInputType
    from .entity import Entity

from .entity import Entity

@dataclass
class MeetingRegistrationQuestion(Entity, Parsable):
    # Answer input type of the custom registration question.
    answer_input_type: Optional[AnswerInputType] = None
    # Answer options when answerInputType is radioButton.
    answer_options: Optional[list[str]] = None
    # Display name of the custom registration question.
    display_name: Optional[str] = None
    # Indicates whether the question is required. Default value is false.
    is_required: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MeetingRegistrationQuestion:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MeetingRegistrationQuestion
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MeetingRegistrationQuestion()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .answer_input_type import AnswerInputType
        from .entity import Entity

        from .answer_input_type import AnswerInputType
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "answerInputType": lambda n : setattr(self, 'answer_input_type', n.get_enum_value(AnswerInputType)),
            "answerOptions": lambda n : setattr(self, 'answer_options', n.get_collection_of_primitive_values(str)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isRequired": lambda n : setattr(self, 'is_required', n.get_bool_value()),
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
        writer.write_enum_value("answerInputType", self.answer_input_type)
        writer.write_collection_of_primitive_values("answerOptions", self.answer_options)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isRequired", self.is_required)
    

