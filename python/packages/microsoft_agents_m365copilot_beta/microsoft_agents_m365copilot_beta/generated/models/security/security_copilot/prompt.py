from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...dictionary import Dictionary
    from ...entity import Entity
    from .evaluation import Evaluation
    from .prompt_type import PromptType
    from .skill_input_descriptor import SkillInputDescriptor

from ...entity import Entity

@dataclass
class Prompt(Entity, Parsable):
    # Input content to the prompt.
    content: Optional[str] = None
    # Created time.
    created_date_time: Optional[datetime.datetime] = None
    # Collection of evaluations
    evaluations: Optional[list[Evaluation]] = None
    # Not implemented.
    inputs: Optional[Dictionary] = None
    # Last modified time.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Skill Input descriptor.
    skill_input_descriptors: Optional[list[SkillInputDescriptor]] = None
    # Skill name.
    skill_name: Optional[str] = None
    # The type property
    type: Optional[PromptType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Prompt:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Prompt
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Prompt()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ...dictionary import Dictionary
        from ...entity import Entity
        from .evaluation import Evaluation
        from .prompt_type import PromptType
        from .skill_input_descriptor import SkillInputDescriptor

        from ...dictionary import Dictionary
        from ...entity import Entity
        from .evaluation import Evaluation
        from .prompt_type import PromptType
        from .skill_input_descriptor import SkillInputDescriptor

        fields: dict[str, Callable[[Any], None]] = {
            "content": lambda n : setattr(self, 'content', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "evaluations": lambda n : setattr(self, 'evaluations', n.get_collection_of_object_values(Evaluation)),
            "inputs": lambda n : setattr(self, 'inputs', n.get_object_value(Dictionary)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "skillInputDescriptors": lambda n : setattr(self, 'skill_input_descriptors', n.get_collection_of_object_values(SkillInputDescriptor)),
            "skillName": lambda n : setattr(self, 'skill_name', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(PromptType)),
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
        writer.write_str_value("content", self.content)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_collection_of_object_values("evaluations", self.evaluations)
        writer.write_object_value("inputs", self.inputs)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_object_values("skillInputDescriptors", self.skill_input_descriptors)
        writer.write_str_value("skillName", self.skill_name)
        writer.write_enum_value("type", self.type)
    

