from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .business_scenario_properties import BusinessScenarioProperties
    from .business_scenario_task_target_base import BusinessScenarioTaskTargetBase
    from .planner_task import PlannerTask

from .planner_task import PlannerTask

@dataclass
class BusinessScenarioTask(PlannerTask, Parsable):
    # Scenario-specific properties of the task. externalObjectId and externalBucketId properties must be specified when creating a task.
    business_scenario_properties: Optional[BusinessScenarioProperties] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Target of the task that specifies where the task should be placed. Must be specified when creating a task.
    target: Optional[BusinessScenarioTaskTargetBase] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BusinessScenarioTask:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BusinessScenarioTask
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BusinessScenarioTask()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .business_scenario_properties import BusinessScenarioProperties
        from .business_scenario_task_target_base import BusinessScenarioTaskTargetBase
        from .planner_task import PlannerTask

        from .business_scenario_properties import BusinessScenarioProperties
        from .business_scenario_task_target_base import BusinessScenarioTaskTargetBase
        from .planner_task import PlannerTask

        fields: dict[str, Callable[[Any], None]] = {
            "businessScenarioProperties": lambda n : setattr(self, 'business_scenario_properties', n.get_object_value(BusinessScenarioProperties)),
            "target": lambda n : setattr(self, 'target', n.get_object_value(BusinessScenarioTaskTargetBase)),
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
        writer.write_object_value("businessScenarioProperties", self.business_scenario_properties)
        writer.write_object_value("target", self.target)
    

