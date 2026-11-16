from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .agent_extension import AgentExtension

@dataclass
class AgentCapabilities(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # A list of protocol extensions supported by the agent.
    extensions: Optional[list[AgentExtension]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates if the agent supports sending push notifications for asynchronous task updates.
    push_notifications: Optional[bool] = None
    # Indicates if the agent provides a history of state transitions for a task.
    state_transition_history: Optional[bool] = None
    # Indicates if the agent supports Server-Sent Events (SSE) for streaming responses.
    streaming: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AgentCapabilities:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AgentCapabilities
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AgentCapabilities()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .agent_extension import AgentExtension

        from .agent_extension import AgentExtension

        fields: dict[str, Callable[[Any], None]] = {
            "extensions": lambda n : setattr(self, 'extensions', n.get_collection_of_object_values(AgentExtension)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "pushNotifications": lambda n : setattr(self, 'push_notifications', n.get_bool_value()),
            "stateTransitionHistory": lambda n : setattr(self, 'state_transition_history', n.get_bool_value()),
            "streaming": lambda n : setattr(self, 'streaming', n.get_bool_value()),
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
        writer.write_collection_of_object_values("extensions", self.extensions)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("pushNotifications", self.push_notifications)
        writer.write_bool_value("stateTransitionHistory", self.state_transition_history)
        writer.write_bool_value("streaming", self.streaming)
        writer.write_additional_data_value(self.additional_data)
    

