from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .business_scenario_group_target import BusinessScenarioGroupTarget
    from .planner_task_target_kind import PlannerTaskTargetKind

@dataclass
class BusinessScenarioTaskTargetBase(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # The taskTargetKind property
    task_target_kind: Optional[PlannerTaskTargetKind] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BusinessScenarioTaskTargetBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BusinessScenarioTaskTargetBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.businessScenarioGroupTarget".casefold():
            from .business_scenario_group_target import BusinessScenarioGroupTarget

            return BusinessScenarioGroupTarget()
        return BusinessScenarioTaskTargetBase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .business_scenario_group_target import BusinessScenarioGroupTarget
        from .planner_task_target_kind import PlannerTaskTargetKind

        from .business_scenario_group_target import BusinessScenarioGroupTarget
        from .planner_task_target_kind import PlannerTaskTargetKind

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "taskTargetKind": lambda n : setattr(self, 'task_target_kind', n.get_enum_value(PlannerTaskTargetKind)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("taskTargetKind", self.task_target_kind)
        writer.write_additional_data_value(self.additional_data)
    

