from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .security_requirement import SecurityRequirement

@dataclass
class AgentSkill(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # A detailed description of the skill, intended to help clients or users understand its purpose and functionality.
    description: Optional[str] = None
    # A human-readable name for the skill.
    display_name: Optional[str] = None
    # Example prompts or scenarios that this skill can handle. Provides a hint to the client on how to use the skill.
    examples: Optional[list[str]] = None
    # A unique identifier for the agent's skill.
    id: Optional[str] = None
    # The set of supported input MIME types for this skill, overriding the agent's defaults.
    input_modes: Optional[list[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The set of supported output MIME types for this skill, overriding the agent's defaults.
    output_modes: Optional[list[str]] = None
    # Security schemes necessary for the agent to leverage this skill.
    security: Optional[list[SecurityRequirement]] = None
    # A set of keywords describing the skill's capabilities.
    tags: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AgentSkill:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AgentSkill
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AgentSkill()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .security_requirement import SecurityRequirement

        from .security_requirement import SecurityRequirement

        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "examples": lambda n : setattr(self, 'examples', n.get_collection_of_primitive_values(str)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "inputModes": lambda n : setattr(self, 'input_modes', n.get_collection_of_primitive_values(str)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "outputModes": lambda n : setattr(self, 'output_modes', n.get_collection_of_primitive_values(str)),
            "security": lambda n : setattr(self, 'security', n.get_collection_of_object_values(SecurityRequirement)),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_primitive_values("examples", self.examples)
        writer.write_str_value("id", self.id)
        writer.write_collection_of_primitive_values("inputModes", self.input_modes)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_primitive_values("outputModes", self.output_modes)
        writer.write_collection_of_object_values("security", self.security)
        writer.write_collection_of_primitive_values("tags", self.tags)
        writer.write_additional_data_value(self.additional_data)
    

