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
    from .task_history_item import TaskHistoryItem

from .planner_delta import PlannerDelta

@dataclass
class PlannerHistoryItem(PlannerDelta, Parsable):
    # The identity of the user or application that performed the change.
    actor: Optional[IdentitySet] = None
    # The ID of the entity that was changed.
    entity_id: Optional[str] = None
    # The entityType property
    entity_type: Optional[HistoryEntityType] = None
    # The eventType property
    event_type: Optional[HistoryEventType] = None
    # The date and time when the change occurred. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2024, is 2024-01-01T00:00:00Z.
    occurred_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The ID of the plan that contains the changed entity.
    plan_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlannerHistoryItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlannerHistoryItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.taskHistoryItem".casefold():
            from .task_history_item import TaskHistoryItem

            return TaskHistoryItem()
        return PlannerHistoryItem()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .history_entity_type import HistoryEntityType
        from .history_event_type import HistoryEventType
        from .identity_set import IdentitySet
        from .planner_delta import PlannerDelta
        from .task_history_item import TaskHistoryItem

        from .history_entity_type import HistoryEntityType
        from .history_event_type import HistoryEventType
        from .identity_set import IdentitySet
        from .planner_delta import PlannerDelta
        from .task_history_item import TaskHistoryItem

        fields: dict[str, Callable[[Any], None]] = {
            "actor": lambda n : setattr(self, 'actor', n.get_object_value(IdentitySet)),
            "entityId": lambda n : setattr(self, 'entity_id', n.get_str_value()),
            "entityType": lambda n : setattr(self, 'entity_type', n.get_enum_value(HistoryEntityType)),
            "eventType": lambda n : setattr(self, 'event_type', n.get_enum_value(HistoryEventType)),
            "occurredDateTime": lambda n : setattr(self, 'occurred_date_time', n.get_datetime_value()),
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
        writer.write_datetime_value("occurredDateTime", self.occurred_date_time)
        writer.write_str_value("planId", self.plan_id)
    

