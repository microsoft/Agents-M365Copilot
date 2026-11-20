from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .case_management_entity import CaseManagementEntity
    from .sla_policy_criteria_block import SlaPolicyCriteriaBlock
    from .sla_policy_recalculate_condition import SlaPolicyRecalculateCondition
    from .sla_policy_timer import SlaPolicyTimer

from .case_management_entity import CaseManagementEntity

@dataclass
class SlaPolicyDefinition(CaseManagementEntity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.caseManagement.slaPolicyDefinition"
    # The description of the policy. Maximum length: 5,000 characters.
    description: Optional[str] = None
    # The display name of the policy. Must be unique across the tenant, using a case-insensitive comparison. Maximum length: 150 characters.
    display_name: Optional[str] = None
    # The condition that removes a case from the policy's scope.
    exit_criteria: Optional[SlaPolicyCriteriaBlock] = None
    # Whether the policy is actively evaluated. Inactive policies are excluded from new case evaluations. The default value on creation is true.
    is_active: Optional[bool] = None
    # The condition that pauses the timer while a case matches it.
    pause_criteria: Optional[SlaPolicyCriteriaBlock] = None
    # The settings that control whether elapsed time resets when the policy is recalculated.
    recalculate_condition: Optional[SlaPolicyRecalculateCondition] = None
    # The condition a case must match to enter the policy's scope. When omitted, the policy applies to all cases of its owning case type. The maximum nesting depth is two.
    set_criteria: Optional[SlaPolicyCriteriaBlock] = None
    # The embedded warning and breach timers, evaluated in order, lowest first. Maximum: 15 timers. Exactly one timer must have isDefault set to true. Updating this property replaces the entire collection.
    timers: Optional[list[SlaPolicyTimer]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SlaPolicyDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SlaPolicyDefinition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SlaPolicyDefinition()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .case_management_entity import CaseManagementEntity
        from .sla_policy_criteria_block import SlaPolicyCriteriaBlock
        from .sla_policy_recalculate_condition import SlaPolicyRecalculateCondition
        from .sla_policy_timer import SlaPolicyTimer

        from .case_management_entity import CaseManagementEntity
        from .sla_policy_criteria_block import SlaPolicyCriteriaBlock
        from .sla_policy_recalculate_condition import SlaPolicyRecalculateCondition
        from .sla_policy_timer import SlaPolicyTimer

        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "exitCriteria": lambda n : setattr(self, 'exit_criteria', n.get_object_value(SlaPolicyCriteriaBlock)),
            "isActive": lambda n : setattr(self, 'is_active', n.get_bool_value()),
            "pauseCriteria": lambda n : setattr(self, 'pause_criteria', n.get_object_value(SlaPolicyCriteriaBlock)),
            "recalculateCondition": lambda n : setattr(self, 'recalculate_condition', n.get_object_value(SlaPolicyRecalculateCondition)),
            "setCriteria": lambda n : setattr(self, 'set_criteria', n.get_object_value(SlaPolicyCriteriaBlock)),
            "timers": lambda n : setattr(self, 'timers', n.get_collection_of_object_values(SlaPolicyTimer)),
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
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("exitCriteria", self.exit_criteria)
        writer.write_bool_value("isActive", self.is_active)
        writer.write_object_value("pauseCriteria", self.pause_criteria)
        writer.write_object_value("recalculateCondition", self.recalculate_condition)
        writer.write_object_value("setCriteria", self.set_criteria)
        writer.write_collection_of_object_values("timers", self.timers)
    

