from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .sla_policy_condition_base import SlaPolicyConditionBase
    from .sla_policy_logical_operator import SlaPolicyLogicalOperator

from .sla_policy_condition_base import SlaPolicyConditionBase

@dataclass
class SlaPolicyCriteriaBlock(SlaPolicyConditionBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.caseManagement.slaPolicyCriteriaBlock"
    # The leaf conditions or nested groups evaluated by this block. The maximum nesting depth is two.
    conditions: Optional[list[SlaPolicyConditionBase]] = None
    # The logicalOperator property
    logical_operator: Optional[SlaPolicyLogicalOperator] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SlaPolicyCriteriaBlock:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SlaPolicyCriteriaBlock
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SlaPolicyCriteriaBlock()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .sla_policy_condition_base import SlaPolicyConditionBase
        from .sla_policy_logical_operator import SlaPolicyLogicalOperator

        from .sla_policy_condition_base import SlaPolicyConditionBase
        from .sla_policy_logical_operator import SlaPolicyLogicalOperator

        fields: dict[str, Callable[[Any], None]] = {
            "conditions": lambda n : setattr(self, 'conditions', n.get_collection_of_object_values(SlaPolicyConditionBase)),
            "logicalOperator": lambda n : setattr(self, 'logical_operator', n.get_enum_value(SlaPolicyLogicalOperator)),
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
        writer.write_collection_of_object_values("conditions", self.conditions)
        writer.write_enum_value("logicalOperator", self.logical_operator)
    

