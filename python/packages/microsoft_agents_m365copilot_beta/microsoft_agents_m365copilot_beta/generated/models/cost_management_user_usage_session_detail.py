from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cost_management_unit import CostManagementUnit
    from .entity import Entity

from .entity import Entity

@dataclass
class CostManagementUserUsageSessionDetail(Entity, Parsable):
    """
    A native-source session grouping within a user's raw usage detail. Activity without a sessionidentifier may be omitted, even when it contributes to the parent total.
    """
    # Raw, billable-flagged consumption attributed to this source-returned session grouping withinthe containing user's detail window. Session rows need not sum to the parent's consumedQuantity.Read-only.
    consumed_quantity: Optional[float] = None
    # Time the earliest activity in this session was recorded, or null when the source did notreport one. Read-only.
    first_activity_date_time: Optional[datetime.datetime] = None
    # Time the latest activity in this session was recorded, or null when the source did notreport one. Read-only.
    last_activity_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The native session identifier on a row returned by the source, preserved verbatim, includingnull if the source returns it. Distinct from this row's opaque id. A nullable value does notguarantee a returned group for activity without a session identifier; such activity may beabsent from the session breakdown while contributing to the parent total. Read-only.
    source_session_id: Optional[str] = None
    # Unit in which consumption quantities are expressed. Values are consumption units, not currency.
    unit: Optional[CostManagementUnit] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CostManagementUserUsageSessionDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CostManagementUserUsageSessionDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CostManagementUserUsageSessionDetail()
    
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
            "firstActivityDateTime": lambda n : setattr(self, 'first_activity_date_time', n.get_datetime_value()),
            "lastActivityDateTime": lambda n : setattr(self, 'last_activity_date_time', n.get_datetime_value()),
            "sourceSessionId": lambda n : setattr(self, 'source_session_id', n.get_str_value()),
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
    

