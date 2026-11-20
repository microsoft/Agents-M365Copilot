from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .business_scenario_task import BusinessScenarioTask
    from .entity import Entity
    from .planner_plan_configuration import PlannerPlanConfiguration
    from .planner_task_configuration import PlannerTaskConfiguration

from .entity import Entity

@dataclass
class BusinessScenarioPlanner(Entity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    # The configuration of Planner plans that will be created for the scenario.
    plan_configuration: Optional[PlannerPlanConfiguration] = None
    # The configuration of Planner tasks that will be created for the scenario.
    task_configuration: Optional[PlannerTaskConfiguration] = None
    # The Planner tasks for the scenario.
    tasks: Optional[list[BusinessScenarioTask]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BusinessScenarioPlanner:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BusinessScenarioPlanner
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BusinessScenarioPlanner()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .business_scenario_task import BusinessScenarioTask
        from .entity import Entity
        from .planner_plan_configuration import PlannerPlanConfiguration
        from .planner_task_configuration import PlannerTaskConfiguration

        from .business_scenario_task import BusinessScenarioTask
        from .entity import Entity
        from .planner_plan_configuration import PlannerPlanConfiguration
        from .planner_task_configuration import PlannerTaskConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "planConfiguration": lambda n : setattr(self, 'plan_configuration', n.get_object_value(PlannerPlanConfiguration)),
            "taskConfiguration": lambda n : setattr(self, 'task_configuration', n.get_object_value(PlannerTaskConfiguration)),
            "tasks": lambda n : setattr(self, 'tasks', n.get_collection_of_object_values(BusinessScenarioTask)),
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
        writer.write_object_value("planConfiguration", self.plan_configuration)
        writer.write_object_value("taskConfiguration", self.task_configuration)
        writer.write_collection_of_object_values("tasks", self.tasks)
    

