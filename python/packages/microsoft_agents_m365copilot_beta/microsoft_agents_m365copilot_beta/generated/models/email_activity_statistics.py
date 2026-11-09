from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .activity_statistics import ActivityStatistics

from .activity_statistics import ActivityStatistics

@dataclass
class EmailActivityStatistics(ActivityStatistics, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.emailActivityStatistics"
    # Total hours spent on email outside of working hours, which is based on the user's Outlook calendar setting for work hours. The value is represented in ISO 8601 format for durations.
    after_hours: Optional[datetime.timedelta] = None
    # Total hours spent reading email. The value is represented in ISO 8601 format for durations.
    read_email: Optional[datetime.timedelta] = None
    # Total hours spent writing and sending email. The value is represented in ISO 8601 format for durations.
    sent_email: Optional[datetime.timedelta] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EmailActivityStatistics:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EmailActivityStatistics
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EmailActivityStatistics()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .activity_statistics import ActivityStatistics

        from .activity_statistics import ActivityStatistics

        fields: dict[str, Callable[[Any], None]] = {
            "afterHours": lambda n : setattr(self, 'after_hours', n.get_timedelta_value()),
            "readEmail": lambda n : setattr(self, 'read_email', n.get_timedelta_value()),
            "sentEmail": lambda n : setattr(self, 'sent_email', n.get_timedelta_value()),
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
        writer.write_timedelta_value("afterHours", self.after_hours)
        writer.write_timedelta_value("readEmail", self.read_email)
        writer.write_timedelta_value("sentEmail", self.sent_email)
    

