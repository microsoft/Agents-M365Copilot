from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class VirtualEventRegistrationQuestionAnswer(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Boolean answer to the virtualEventRegistrationCustomQuestion. Only appears when answerInputType is boolean.
    boolean_value: Optional[bool] = None
    # Display name of the registration question.
    display_name: Optional[str] = None
    # A collection of text answers to the virtualEventRegistrationCustomQuestion. Only appears when answerInputType is multiChoice.
    multi_choice_values: Optional[list[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The identifier of either a virtualEventRegistrationCustomQuestion or a virtualEventRegistrationPredefinedQuestion.
    question_id: Optional[str] = None
    # Text answer to the virtualEventRegistrationCustomQuestion or the virtualEventRegistrationPredefinedQuestion. Appears when answerInputType is text, multilineText or singleChoice.
    value: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VirtualEventRegistrationQuestionAnswer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VirtualEventRegistrationQuestionAnswer
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return VirtualEventRegistrationQuestionAnswer()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "booleanValue": lambda n : setattr(self, 'boolean_value', n.get_bool_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "multiChoiceValues": lambda n : setattr(self, 'multi_choice_values', n.get_collection_of_primitive_values(str)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "questionId": lambda n : setattr(self, 'question_id', n.get_str_value()),
            "value": lambda n : setattr(self, 'value', n.get_str_value()),
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
        writer.write_bool_value("booleanValue", self.boolean_value)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_primitive_values("multiChoiceValues", self.multi_choice_values)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("questionId", self.question_id)
        writer.write_str_value("value", self.value)
        writer.write_additional_data_value(self.additional_data)
    

