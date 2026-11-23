from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .investigation_session import InvestigationSession
    from .playbook_definition import PlaybookDefinition

from .entity import Entity

@dataclass
class AgenticSecurityRoot(Entity, Parsable):
    """
    Container for agentic security playbook definitions and sessions.
    """
    # The OdataType property
    odata_type: Optional[str] = None
    # The read-only playbook catalog. Supports list and keyed GET with $select. Doesn't support $filter, $orderby, $search, $expand, $count, $top, $skip, or delta tracking.
    playbook_definitions: Optional[list[PlaybookDefinition]] = None
    # The agentic sessions visible to the caller. Supports list with $filter on status (eq, or, in), $top, and $select; session creation; and keyed reads. Doesn't support $count, $orderby, $search, $expand, $skip, or delta tracking.
    sessions: Optional[list[InvestigationSession]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AgenticSecurityRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AgenticSecurityRoot
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AgenticSecurityRoot()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .investigation_session import InvestigationSession
        from .playbook_definition import PlaybookDefinition

        from .entity import Entity
        from .investigation_session import InvestigationSession
        from .playbook_definition import PlaybookDefinition

        fields: dict[str, Callable[[Any], None]] = {
            "playbookDefinitions": lambda n : setattr(self, 'playbook_definitions', n.get_collection_of_object_values(PlaybookDefinition)),
            "sessions": lambda n : setattr(self, 'sessions', n.get_collection_of_object_values(InvestigationSession)),
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
        writer.write_collection_of_object_values("playbookDefinitions", self.playbook_definitions)
        writer.write_collection_of_object_values("sessions", self.sessions)
    

