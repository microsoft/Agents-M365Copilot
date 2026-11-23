from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cost_management_unit import CostManagementUnit
    from .entity import Entity

from .entity import Entity

@dataclass
class CostManagementUserUsageServiceDetail(Entity, Parsable):
    """
    One governed service's share of a user's raw usage detail.
    """
    # Raw, billable-flagged consumption attributed to this service within the containing user'sdetail window. Independently rounded; child rows are not guaranteed to sum exactly to thecontaining detail's consumedQuantity. Read-only.
    consumed_quantity: Optional[float] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Unit in which consumption quantities are expressed. Values are consumption units, not currency.
    unit: Optional[CostManagementUnit] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CostManagementUserUsageServiceDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CostManagementUserUsageServiceDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CostManagementUserUsageServiceDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cost_management_unit import CostManagementUnit
        from .entity import Entity

        from .cost_management_unit import CostManagementUnit
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "consumedQuantity": lambda n : setattr(self, 'consumed_quantity', n.get_float_value()),
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
        writer.write_enum_value("unit", self.unit)
    

