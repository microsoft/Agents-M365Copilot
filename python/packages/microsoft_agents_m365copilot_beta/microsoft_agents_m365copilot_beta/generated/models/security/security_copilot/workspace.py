from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...entity import Entity
    from .plugin import Plugin
    from .session import Session

from ...entity import Entity

@dataclass
class Workspace(Entity, Parsable):
    # Name of the Security Copilot workspace.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents plugins in Security Copilot.
    plugins: Optional[list[Plugin]] = None
    # Represents sessions in Security Copilot.
    sessions: Optional[list[Session]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Workspace:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Workspace
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Workspace()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ...entity import Entity
        from .plugin import Plugin
        from .session import Session

        from ...entity import Entity
        from .plugin import Plugin
        from .session import Session

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "plugins": lambda n : setattr(self, 'plugins', n.get_collection_of_object_values(Plugin)),
            "sessions": lambda n : setattr(self, 'sessions', n.get_collection_of_object_values(Session)),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("plugins", self.plugins)
        writer.write_collection_of_object_values("sessions", self.sessions)
    

