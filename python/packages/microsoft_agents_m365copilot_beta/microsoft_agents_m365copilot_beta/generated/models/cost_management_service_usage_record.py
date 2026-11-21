from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cost_management_unit import CostManagementUnit

@dataclass
class CostManagementServiceUsageRecord(AdditionalDataHolder, Parsable):
    """
    One service's share of reported consumption for one completed UTC day.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Consumption attributed to this service for the requested completed UTC day. Read-only.
    consumed_quantity: Optional[float] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The governed service identifier, such as cowork or workIQ. Discover valid values from theservice catalog using a category identifier, not the catalog entry's own id. Read-only.
    service_id: Optional[str] = None
    # Unit in which consumption quantities are expressed. Values are consumption units, not currency.
    unit: Optional[CostManagementUnit] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CostManagementServiceUsageRecord:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CostManagementServiceUsageRecord
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CostManagementServiceUsageRecord()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cost_management_unit import CostManagementUnit

        from .cost_management_unit import CostManagementUnit

        fields: dict[str, Callable[[Any], None]] = {
            "consumedQuantity": lambda n : setattr(self, 'consumed_quantity', n.get_float_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "serviceId": lambda n : setattr(self, 'service_id', n.get_str_value()),
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
    

