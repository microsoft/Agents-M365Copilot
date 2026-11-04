from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .inactive_users_by_application_metric_base import InactiveUsersByApplicationMetricBase

from .inactive_users_by_application_metric_base import InactiveUsersByApplicationMetricBase

@dataclass
class MonthlyInactiveUsersByApplicationMetric(InactiveUsersByApplicationMetricBase, Parsable):
    # The inactiveCalendarMonthCount property
    inactive_calendar_month_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MonthlyInactiveUsersByApplicationMetric:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MonthlyInactiveUsersByApplicationMetric
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MonthlyInactiveUsersByApplicationMetric()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .inactive_users_by_application_metric_base import InactiveUsersByApplicationMetricBase

        from .inactive_users_by_application_metric_base import InactiveUsersByApplicationMetricBase

        fields: dict[str, Callable[[Any], None]] = {
            "inactiveCalendarMonthCount": lambda n : setattr(self, 'inactive_calendar_month_count', n.get_int_value()),
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
        writer.write_int_value("inactiveCalendarMonthCount", self.inactive_calendar_month_count)
    

