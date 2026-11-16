from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .sla_policy_condition_base import SlaPolicyConditionBase
    from .sla_policy_condition_operator import SlaPolicyConditionOperator

from .sla_policy_condition_base import SlaPolicyConditionBase

@dataclass
class SlaPolicyCondition(SlaPolicyConditionBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.caseManagement.slaPolicyCondition"
    # The operator property
    operator: Optional[SlaPolicyConditionOperator] = None
    # The name of the case property to evaluate, such as priority.
    property_: Optional[str] = None
    # The comparison values for the condition.
    values: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SlaPolicyCondition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SlaPolicyCondition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SlaPolicyCondition()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .sla_policy_condition_base import SlaPolicyConditionBase
        from .sla_policy_condition_operator import SlaPolicyConditionOperator

        from .sla_policy_condition_base import SlaPolicyConditionBase
        from .sla_policy_condition_operator import SlaPolicyConditionOperator

        fields: dict[str, Callable[[Any], None]] = {
            "operator": lambda n : setattr(self, 'operator', n.get_enum_value(SlaPolicyConditionOperator)),
            "property": lambda n : setattr(self, 'property_', n.get_str_value()),
            "values": lambda n : setattr(self, 'values', n.get_collection_of_primitive_values(str)),
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
        writer.write_enum_value("operator", self.operator)
        writer.write_str_value("property", self.property_)
        writer.write_collection_of_primitive_values("values", self.values)
    

