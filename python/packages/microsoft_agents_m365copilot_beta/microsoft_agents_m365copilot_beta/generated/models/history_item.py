from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .history_entity_type import HistoryEntityType
    from .history_event_type import HistoryEventType
    from .identity_set import IdentitySet
    from .planner_delta import PlannerDelta

from .planner_delta import PlannerDelta

@dataclass
class HistoryItem(PlannerDelta, Parsable):
    # Identity of the user (or application) that performed the change.
    actor: Optional[IdentitySet] = None
    # ID of the entity the history item describes.
    entity_id: Optional[str] = None
    # Type of the entity the history item describes. The possible values are: task, unknownFutureValue.
    entity_type: Optional[HistoryEntityType] = None
    # Type of the change event that occurred. The possible values are: created, updated, deleted, undeleted, moved, unknownFutureValue.
    event_type: Optional[HistoryEventType] = None
    # Serialized representation of the entity state after the change.
    new_data: Optional[str] = None
    # Date and time the change occurred. Read-only.
    occurred_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Serialized representation of the entity state before the change.
    old_data: Optional[str] = None
    # ID of the plan the change occurred in.
    plan_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> HistoryItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: HistoryItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return HistoryItem()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .history_entity_type import HistoryEntityType
        from .history_event_type import HistoryEventType
        from .identity_set import IdentitySet
        from .planner_delta import PlannerDelta

        from .history_entity_type import HistoryEntityType
        from .history_event_type import HistoryEventType
        from .identity_set import IdentitySet
        from .planner_delta import PlannerDelta

        fields: dict[str, Callable[[Any], None]] = {
            "actor": lambda n : setattr(self, 'actor', n.get_object_value(IdentitySet)),
            "entityId": lambda n : setattr(self, 'entity_id', n.get_str_value()),
            "entityType": lambda n : setattr(self, 'entity_type', n.get_enum_value(HistoryEntityType)),
            "eventType": lambda n : setattr(self, 'event_type', n.get_enum_value(HistoryEventType)),
            "newData": lambda n : setattr(self, 'new_data', n.get_str_value()),
            "occurredDateTime": lambda n : setattr(self, 'occurred_date_time', n.get_datetime_value()),
            "oldData": lambda n : setattr(self, 'old_data', n.get_str_value()),
            "planId": lambda n : setattr(self, 'plan_id', n.get_str_value()),
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
        writer.write_object_value("actor", self.actor)
        writer.write_str_value("entityId", self.entity_id)
        writer.write_enum_value("entityType", self.entity_type)
        writer.write_enum_value("eventType", self.event_type)
        writer.write_str_value("newData", self.new_data)
        writer.write_str_value("oldData", self.old_data)
        writer.write_str_value("planId", self.plan_id)
    

