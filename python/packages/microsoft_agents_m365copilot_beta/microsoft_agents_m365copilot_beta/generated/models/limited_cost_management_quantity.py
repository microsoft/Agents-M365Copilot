from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cost_management_quantity import CostManagementQuantity

from .cost_management_quantity import CostManagementQuantity

@dataclass
class LimitedCostManagementQuantity(CostManagementQuantity, Parsable):
    """
    A quantity limited to a specific value. A value of zero permits no consumption and isdistinct from unlimited.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.limitedCostManagementQuantity"
    # The numeric value of the quantity, expressed in the stated unit.
    value: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LimitedCostManagementQuantity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LimitedCostManagementQuantity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LimitedCostManagementQuantity()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cost_management_quantity import CostManagementQuantity

        from .cost_management_quantity import CostManagementQuantity

        fields: dict[str, Callable[[Any], None]] = {
            "value": lambda n : setattr(self, 'value', n.get_float_value()),
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
        writer.write_float_value("value", self.value)
    

