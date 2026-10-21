from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class Office365GroupsActivityFileCounts(Entity, Parsable):
    # The number of files that were viewed, edited, shared, or synced in the group's SharePoint document library.
    active: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The date on which a number of files were active in the group's SharePoint site.
    report_date: Optional[datetime.date] = None
    # The number of days the report covers.
    report_period: Optional[str] = None
    # The latest date of the content.
    report_refresh_date: Optional[datetime.date] = None
    # The total number of files in the group's SharePoint document library.
    total: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Office365GroupsActivityFileCounts:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Office365GroupsActivityFileCounts
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Office365GroupsActivityFileCounts()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "active": lambda n : setattr(self, 'active', n.get_int_value()),
            "reportDate": lambda n : setattr(self, 'report_date', n.get_date_value()),
            "reportPeriod": lambda n : setattr(self, 'report_period', n.get_str_value()),
            "reportRefreshDate": lambda n : setattr(self, 'report_refresh_date', n.get_date_value()),
            "total": lambda n : setattr(self, 'total', n.get_int_value()),
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
        writer.write_int_value("active", self.active)
        writer.write_date_value("reportDate", self.report_date)
        writer.write_str_value("reportPeriod", self.report_period)
        writer.write_date_value("reportRefreshDate", self.report_refresh_date)
        writer.write_int_value("total", self.total)
    

