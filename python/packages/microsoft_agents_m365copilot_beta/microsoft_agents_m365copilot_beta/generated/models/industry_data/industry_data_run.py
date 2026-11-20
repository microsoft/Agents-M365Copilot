from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from ..public_error import PublicError
    from .industry_data_run_activity import IndustryDataRunActivity
    from .industry_data_run_status import IndustryDataRunStatus

from ..entity import Entity

@dataclass
class IndustryDataRun(Entity, Parsable):
    # The set of activities performed during the run.
    activities: Optional[list[IndustryDataRunActivity]] = None
    # An error object to diagnose critical failures in the run.
    blocking_error: Optional[PublicError] = None
    # The name of the run for rendering in a user interface.
    display_name: Optional[str] = None
    # The date and time when the run finished or null if the run is still in-progress. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    end_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The date and time when the run started. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    start_date_time: Optional[datetime.datetime] = None
    # The status property
    status: Optional[IndustryDataRunStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IndustryDataRun:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IndustryDataRun
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IndustryDataRun()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from ..public_error import PublicError
        from .industry_data_run_activity import IndustryDataRunActivity
        from .industry_data_run_status import IndustryDataRunStatus

        from ..entity import Entity
        from ..public_error import PublicError
        from .industry_data_run_activity import IndustryDataRunActivity
        from .industry_data_run_status import IndustryDataRunStatus

        fields: dict[str, Callable[[Any], None]] = {
            "activities": lambda n : setattr(self, 'activities', n.get_collection_of_object_values(IndustryDataRunActivity)),
            "blockingError": lambda n : setattr(self, 'blocking_error', n.get_object_value(PublicError)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(IndustryDataRunStatus)),
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
        writer.write_collection_of_object_values("activities", self.activities)
        writer.write_enum_value("status", self.status)
    

