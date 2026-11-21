from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .investigation_message_author import InvestigationMessageAuthor
    from .investigation_message_role import InvestigationMessageRole
    from .investigation_message_type import InvestigationMessageType

from .entity import Entity

@dataclass
class InvestigationMessage(Entity, Parsable):
    """
    Addressable transcript entity owned only by an agent run and referenced by the session aggregate. The key explicitly maps Graph id to backend messageId without shadowing an inherited property; ids are unique across the containing session.
    """
    # Opaque identifier of the agent-processing turn associated with this message, when available. Does not identify the overall session or run.
    agent_turn_id: Optional[str] = None
    # Embedded message-author role and identifier, not an independently addressable resource.
    author: Optional[InvestigationMessageAuthor] = None
    # Optional in historical transcript reads when the source omits content.
    content: Optional[str] = None
    # UTC persistence timestamp. Backend wire name: timestamp.
    created_date_time: Optional[datetime.datetime] = None
    # Read-only message categories from the existing transcript contract.
    kind: Optional[InvestigationMessageType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Transcript message role or recorded author kind. These are independent fields; a tool or system message can have an agent author.
    role: Optional[InvestigationMessageRole] = None
    # Opaque chronological sequence identifier, when available. Does not advertise Graph delta or a message-item key.
    sequence_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> InvestigationMessage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InvestigationMessage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return InvestigationMessage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .investigation_message_author import InvestigationMessageAuthor
        from .investigation_message_role import InvestigationMessageRole
        from .investigation_message_type import InvestigationMessageType

        from .entity import Entity
        from .investigation_message_author import InvestigationMessageAuthor
        from .investigation_message_role import InvestigationMessageRole
        from .investigation_message_type import InvestigationMessageType

        fields: dict[str, Callable[[Any], None]] = {
            "agentTurnId": lambda n : setattr(self, 'agent_turn_id', n.get_str_value()),
            "author": lambda n : setattr(self, 'author', n.get_object_value(InvestigationMessageAuthor)),
            "content": lambda n : setattr(self, 'content', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "kind": lambda n : setattr(self, 'kind', n.get_enum_value(InvestigationMessageType)),
            "role": lambda n : setattr(self, 'role', n.get_enum_value(InvestigationMessageRole)),
            "sequenceId": lambda n : setattr(self, 'sequence_id', n.get_str_value()),
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
        writer.write_object_value("author", self.author)
        writer.write_str_value("content", self.content)
        writer.write_enum_value("kind", self.kind)
        writer.write_enum_value("role", self.role)
    

