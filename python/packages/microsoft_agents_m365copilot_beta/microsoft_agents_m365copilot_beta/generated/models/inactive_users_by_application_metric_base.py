from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .daily_inactive_users_by_application_metric import DailyInactiveUsersByApplicationMetric
    from .entity import Entity
    from .monthly_inactive_users_by_application_metric import MonthlyInactiveUsersByApplicationMetric

from .entity import Entity

@dataclass
class InactiveUsersByApplicationMetricBase(Entity, Parsable):
    # The appId property
    app_id: Optional[str] = None
    # The factDate property
    fact_date: Optional[datetime.date] = None
    # The inactive30DayCount property
    inactive30_day_count: Optional[int] = None
    # The inactive60DayCount property
    inactive60_day_count: Optional[int] = None
    # The inactive90DayCount property
    inactive90_day_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> InactiveUsersByApplicationMetricBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InactiveUsersByApplicationMetricBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.dailyInactiveUsersByApplicationMetric".casefold():
            from .daily_inactive_users_by_application_metric import DailyInactiveUsersByApplicationMetric

            return DailyInactiveUsersByApplicationMetric()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.monthlyInactiveUsersByApplicationMetric".casefold():
            from .monthly_inactive_users_by_application_metric import MonthlyInactiveUsersByApplicationMetric

            return MonthlyInactiveUsersByApplicationMetric()
        return InactiveUsersByApplicationMetricBase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .daily_inactive_users_by_application_metric import DailyInactiveUsersByApplicationMetric
        from .entity import Entity
        from .monthly_inactive_users_by_application_metric import MonthlyInactiveUsersByApplicationMetric

        from .daily_inactive_users_by_application_metric import DailyInactiveUsersByApplicationMetric
        from .entity import Entity
        from .monthly_inactive_users_by_application_metric import MonthlyInactiveUsersByApplicationMetric

        fields: dict[str, Callable[[Any], None]] = {
            "appId": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "factDate": lambda n : setattr(self, 'fact_date', n.get_date_value()),
            "inactive30DayCount": lambda n : setattr(self, 'inactive30_day_count', n.get_int_value()),
            "inactive60DayCount": lambda n : setattr(self, 'inactive60_day_count', n.get_int_value()),
            "inactive90DayCount": lambda n : setattr(self, 'inactive90_day_count', n.get_int_value()),
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
        writer.write_str_value("appId", self.app_id)
        writer.write_date_value("factDate", self.fact_date)
        writer.write_int_value("inactive30DayCount", self.inactive30_day_count)
        writer.write_int_value("inactive60DayCount", self.inactive60_day_count)
        writer.write_int_value("inactive90DayCount", self.inactive90_day_count)
    

