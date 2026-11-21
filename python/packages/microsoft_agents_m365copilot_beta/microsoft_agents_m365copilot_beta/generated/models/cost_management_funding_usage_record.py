from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cost_management_funding_class import CostManagementFundingClass
    from .cost_management_unit import CostManagementUnit
    from .cost_management_usage_data_status import CostManagementUsageDataStatus
    from .entity import Entity

from .entity import Entity

@dataclass
class CostManagementFundingUsageRecord(Entity, Parsable):
    """
    One funding class's share of reported consumption for a calendar month.
    """
    # Consumption attributed to this funding class during the requested month, includingunbilled consumption where applicable. Read-only.
    consumed_quantity: Optional[float] = None
    # Freshness of the source data behind a Phase 2 usage report result that can report it.
    data_status: Optional[CostManagementUsageDataStatus] = None
    # The funding classification of reported consumption, including unbilled consumption.
    funding_class: Optional[CostManagementFundingClass] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Unit in which consumption quantities are expressed. Values are consumption units, not currency.
    unit: Optional[CostManagementUnit] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CostManagementFundingUsageRecord:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CostManagementFundingUsageRecord
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CostManagementFundingUsageRecord()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cost_management_funding_class import CostManagementFundingClass
        from .cost_management_unit import CostManagementUnit
        from .cost_management_usage_data_status import CostManagementUsageDataStatus
        from .entity import Entity

        from .cost_management_funding_class import CostManagementFundingClass
        from .cost_management_unit import CostManagementUnit
        from .cost_management_usage_data_status import CostManagementUsageDataStatus
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "consumedQuantity": lambda n : setattr(self, 'consumed_quantity', n.get_float_value()),
            "dataStatus": lambda n : setattr(self, 'data_status', n.get_object_value(CostManagementUsageDataStatus)),
            "fundingClass": lambda n : setattr(self, 'funding_class', n.get_enum_value(CostManagementFundingClass)),
            "unit": lambda n : setattr(self, 'unit', n.get_enum_value(CostManagementUnit)),
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
        writer.write_object_value("dataStatus", self.data_status)
        writer.write_enum_value("fundingClass", self.funding_class)
        writer.write_enum_value("unit", self.unit)
    

