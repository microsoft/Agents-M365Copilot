from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .planner_history_item import PlannerHistoryItem
    from .planner_task_data import PlannerTaskData

from .planner_history_item import PlannerHistoryItem

@dataclass
class TaskHistoryItem(PlannerHistoryItem, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.taskHistoryItem"
    # A snapshot of the task state after the change. This property is null for deletion events.
    new_data: Optional[PlannerTaskData] = None
    # A snapshot of the task state before the change. This property is null for creation and undeletion events.
    old_data: Optional[PlannerTaskData] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TaskHistoryItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TaskHistoryItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TaskHistoryItem()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .planner_history_item import PlannerHistoryItem
        from .planner_task_data import PlannerTaskData

        from .planner_history_item import PlannerHistoryItem
        from .planner_task_data import PlannerTaskData

        fields: dict[str, Callable[[Any], None]] = {
            "newData": lambda n : setattr(self, 'new_data', n.get_object_value(PlannerTaskData)),
            "oldData": lambda n : setattr(self, 'old_data', n.get_object_value(PlannerTaskData)),
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
        writer.write_object_value("newData", self.new_data)
        writer.write_object_value("oldData", self.old_data)
    

