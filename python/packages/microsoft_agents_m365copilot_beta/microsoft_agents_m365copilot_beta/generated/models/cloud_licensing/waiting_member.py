from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..directory_object import DirectoryObject
    from ..entity import Entity
    from .allotment import Allotment

from ..entity import Entity

@dataclass
class WaitingMember(Entity, Parsable):
    # The allotment property
    allotment: Optional[Allotment] = None
    # The assignedTo property
    assigned_to: Optional[DirectoryObject] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the moment when the user or device first waited for this license. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    waiting_since_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WaitingMember:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WaitingMember
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WaitingMember()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..directory_object import DirectoryObject
        from ..entity import Entity
        from .allotment import Allotment

        from ..directory_object import DirectoryObject
        from ..entity import Entity
        from .allotment import Allotment

        fields: dict[str, Callable[[Any], None]] = {
            "allotment": lambda n : setattr(self, 'allotment', n.get_object_value(Allotment)),
            "assignedTo": lambda n : setattr(self, 'assigned_to', n.get_object_value(DirectoryObject)),
            "waitingSinceDateTime": lambda n : setattr(self, 'waiting_since_date_time', n.get_datetime_value()),
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
        writer.write_object_value("allotment", self.allotment)
        writer.write_object_value("assignedTo", self.assigned_to)
        writer.write_datetime_value("waitingSinceDateTime", self.waiting_since_date_time)
    

