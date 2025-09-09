from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .realtime_activity_feed_root import RealtimeActivityFeedRoot

from .entity import Entity

@dataclass
class CopilotCommunicationsRoot(Entity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    # The realtimeActivityFeed property
    realtime_activity_feed: Optional[RealtimeActivityFeedRoot] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CopilotCommunicationsRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CopilotCommunicationsRoot
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CopilotCommunicationsRoot()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .realtime_activity_feed_root import RealtimeActivityFeedRoot

        from .entity import Entity
        from .realtime_activity_feed_root import RealtimeActivityFeedRoot

        fields: dict[str, Callable[[Any], None]] = {
            "realtimeActivityFeed": lambda n : setattr(self, 'realtime_activity_feed', n.get_object_value(RealtimeActivityFeedRoot)),
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
        writer.write_object_value("realtimeActivityFeed", self.realtime_activity_feed)
    

