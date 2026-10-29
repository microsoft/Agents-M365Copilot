from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cost_management_unit import CostManagementUnit
    from .limited_cost_management_quantity import LimitedCostManagementQuantity
    from .unlimited_cost_management_quantity import UnlimitedCostManagementQuantity

@dataclass
class CostManagementQuantity(AdditionalDataHolder, Parsable):
    """
    A unit-bearing quantity that is either limited to a value or unlimited. Every quantity isone of its derived types, identified by @odata.type on create.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # Unit in which consumption quantities are expressed. Values are consumption units, not currency.
    unit: Optional[CostManagementUnit] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CostManagementQuantity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CostManagementQuantity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.limitedCostManagementQuantity".casefold():
            from .limited_cost_management_quantity import LimitedCostManagementQuantity

            return LimitedCostManagementQuantity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unlimitedCostManagementQuantity".casefold():
            from .unlimited_cost_management_quantity import UnlimitedCostManagementQuantity

            return UnlimitedCostManagementQuantity()
        return CostManagementQuantity()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cost_management_unit import CostManagementUnit
        from .limited_cost_management_quantity import LimitedCostManagementQuantity
        from .unlimited_cost_management_quantity import UnlimitedCostManagementQuantity

        from .cost_management_unit import CostManagementUnit
        from .limited_cost_management_quantity import LimitedCostManagementQuantity
        from .unlimited_cost_management_quantity import UnlimitedCostManagementQuantity

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "unit": lambda n : setattr(self, 'unit', n.get_enum_value(CostManagementUnit)),
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
        writer.write_enum_value("unit", self.unit)
        writer.write_additional_data_value(self.additional_data)
    

