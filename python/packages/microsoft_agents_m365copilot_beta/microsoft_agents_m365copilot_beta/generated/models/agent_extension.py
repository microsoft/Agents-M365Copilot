from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .agent_extension_params import AgentExtensionParams

@dataclass
class AgentExtension(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # A human-readable description of how this agent uses the extension.
    description: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Extension-specific configuration parameters.
    params: Optional[AgentExtensionParams] = None
    # If true, the client must understand and comply with the extension's requirements to interact with the agent.
    required: Optional[bool] = None
    # The unique URI identifying the extension.
    uri: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AgentExtension:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AgentExtension
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AgentExtension()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .agent_extension_params import AgentExtensionParams

        from .agent_extension_params import AgentExtensionParams

        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "params": lambda n : setattr(self, 'params', n.get_object_value(AgentExtensionParams)),
            "required": lambda n : setattr(self, 'required', n.get_bool_value()),
            "uri": lambda n : setattr(self, 'uri', n.get_str_value()),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("params", self.params)
        writer.write_bool_value("required", self.required)
        writer.write_str_value("uri", self.uri)
        writer.write_additional_data_value(self.additional_data)
    

