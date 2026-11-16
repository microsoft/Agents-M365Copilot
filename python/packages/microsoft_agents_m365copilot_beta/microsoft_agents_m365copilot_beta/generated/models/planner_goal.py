from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item_body import ItemBody
    from .planner_delta import PlannerDelta
    from .planner_goal_status import PlannerGoalStatus
    from .planner_task import PlannerTask

from .planner_delta import PlannerDelta

@dataclass
class PlannerGoal(PlannerDelta, Parsable):
    # Required. The display name of the goal.
    display_name: Optional[str] = None
    # Nullable. The date on which the goal is scheduled to finish.
    finish_date: Optional[datetime.date] = None
    # Nullable. The notes associated with the goal.
    notes: Optional[ItemBody] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Required. The ID of the plan that contains the goal.
    plan_id: Optional[str] = None
    # Optional. The relative priority of the goal. Valid values range from 0 to 10, inclusive. The default value is 5.
    priority: Optional[int] = None
    # Nullable. The date on which the goal is scheduled to start.
    start_date: Optional[datetime.date] = None
    # The status property
    status: Optional[PlannerGoalStatus] = None
    # Read-only. Nullable. The tasks associated with the goal. This relationship doesn't support direct retrieval or $expand. To identify the goals associated with a task, read the goalIds property of the plannerTask resource.
    tasks: Optional[list[PlannerTask]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlannerGoal:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlannerGoal
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PlannerGoal()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .item_body import ItemBody
        from .planner_delta import PlannerDelta
        from .planner_goal_status import PlannerGoalStatus
        from .planner_task import PlannerTask

        from .item_body import ItemBody
        from .planner_delta import PlannerDelta
        from .planner_goal_status import PlannerGoalStatus
        from .planner_task import PlannerTask

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "finishDate": lambda n : setattr(self, 'finish_date', n.get_date_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_object_value(ItemBody)),
            "planId": lambda n : setattr(self, 'plan_id', n.get_str_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "startDate": lambda n : setattr(self, 'start_date', n.get_date_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(PlannerGoalStatus)),
            "tasks": lambda n : setattr(self, 'tasks', n.get_collection_of_object_values(PlannerTask)),
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
        writer.write_date_value("finishDate", self.finish_date)
        writer.write_object_value("notes", self.notes)
        writer.write_str_value("planId", self.plan_id)
        writer.write_int_value("priority", self.priority)
        writer.write_date_value("startDate", self.start_date)
        writer.write_enum_value("status", self.status)
        writer.write_collection_of_object_values("tasks", self.tasks)
    

