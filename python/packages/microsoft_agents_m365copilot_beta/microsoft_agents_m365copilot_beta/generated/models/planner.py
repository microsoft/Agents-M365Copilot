from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .plan import Plan
    from .planner_bucket import PlannerBucket
    from .planner_goal import PlannerGoal
    from .planner_plan import PlannerPlan
    from .planner_roster import PlannerRoster
    from .planner_task import PlannerTask
    from .task import Task

from .entity import Entity

@dataclass
class Planner(Entity, Parsable):
    # Read-only. Nullable. Returns a collection of the specified buckets
    buckets: Optional[list[PlannerBucket]] = None
    # Read-only. Nullable. Returns a collection of the specified goals
    goals: Optional[list[PlannerGoal]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Read-only. Nullable. Returns a collection of the specified plans
    plans: Optional[list[PlannerPlan]] = None
    # Read-only. Nullable. The collection of Planner Graph V4 plans.
    plans_v2: Optional[list[Plan]] = None
    # Read-only. Nullable. Returns a collection of the specified rosters
    rosters: Optional[list[PlannerRoster]] = None
    # Read-only. Nullable. Returns a collection of the specified tasks
    tasks: Optional[list[PlannerTask]] = None
    # Read-only. Nullable. The collection of Planner Graph V4 tasks.
    tasks_v2: Optional[list[Task]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Planner:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Planner
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Planner()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .plan import Plan
        from .planner_bucket import PlannerBucket
        from .planner_goal import PlannerGoal
        from .planner_plan import PlannerPlan
        from .planner_roster import PlannerRoster
        from .planner_task import PlannerTask
        from .task import Task

        from .entity import Entity
        from .plan import Plan
        from .planner_bucket import PlannerBucket
        from .planner_goal import PlannerGoal
        from .planner_plan import PlannerPlan
        from .planner_roster import PlannerRoster
        from .planner_task import PlannerTask
        from .task import Task

        fields: dict[str, Callable[[Any], None]] = {
            "buckets": lambda n : setattr(self, 'buckets', n.get_collection_of_object_values(PlannerBucket)),
            "goals": lambda n : setattr(self, 'goals', n.get_collection_of_object_values(PlannerGoal)),
            "plans": lambda n : setattr(self, 'plans', n.get_collection_of_object_values(PlannerPlan)),
            "plans_v2": lambda n : setattr(self, 'plans_v2', n.get_collection_of_object_values(Plan)),
            "rosters": lambda n : setattr(self, 'rosters', n.get_collection_of_object_values(PlannerRoster)),
            "tasks": lambda n : setattr(self, 'tasks', n.get_collection_of_object_values(PlannerTask)),
            "tasks_v2": lambda n : setattr(self, 'tasks_v2', n.get_collection_of_object_values(Task)),
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
        writer.write_collection_of_object_values("buckets", self.buckets)
        writer.write_collection_of_object_values("goals", self.goals)
        writer.write_collection_of_object_values("plans", self.plans)
        writer.write_collection_of_object_values("plans_v2", self.plans_v2)
        writer.write_collection_of_object_values("rosters", self.rosters)
        writer.write_collection_of_object_values("tasks", self.tasks)
        writer.write_collection_of_object_values("tasks_v2", self.tasks_v2)
    

