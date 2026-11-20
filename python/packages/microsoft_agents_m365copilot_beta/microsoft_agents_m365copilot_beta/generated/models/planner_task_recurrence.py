from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .planner_recurrence_schedule import PlannerRecurrenceSchedule

@dataclass
class PlannerTaskRecurrence(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The taskId of the next task in this series. This value is assigned at the time the next task in the series is created, and is null prior to that time.
    next_in_series_task_id: Optional[str] = None
    # The 1-based index of this task within the recurrence series. The first task in a series has the value 1, the next task in the series has the value 2, and so on.
    occurrence_id: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The taskId of the previous task in this series. null for the first task in a series since it has no predecessor. All subsequent tasks in the series have a value that corresponds to their predecessors.
    previous_in_series_task_id: Optional[str] = None
    # The date and time when this recurrence series begin. For the first task in a series (occurrenceId = 1) this value is copied from schedule.patternStartDateTime. For subsequent tasks in the series (occurrenceId >= 2) this value is copied from the previous task and never changes; it preserves the start date of the recurring series. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    recurrence_start_date_time: Optional[datetime.datetime] = None
    # The schedule for recurrence. Clients define and edit recurrence by specifying the schedule. If nextInSeriesTaskId isn't assigned, clients may terminate the series by assigning null to this property.
    schedule: Optional[PlannerRecurrenceSchedule] = None
    # The recurrence series this task belongs to. A GUID-based value that serves as the unique identifier for a series.
    series_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlannerTaskRecurrence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlannerTaskRecurrence
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PlannerTaskRecurrence()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .planner_recurrence_schedule import PlannerRecurrenceSchedule

        from .planner_recurrence_schedule import PlannerRecurrenceSchedule

        fields: dict[str, Callable[[Any], None]] = {
            "nextInSeriesTaskId": lambda n : setattr(self, 'next_in_series_task_id', n.get_str_value()),
            "occurrenceId": lambda n : setattr(self, 'occurrence_id', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "previousInSeriesTaskId": lambda n : setattr(self, 'previous_in_series_task_id', n.get_str_value()),
            "recurrenceStartDateTime": lambda n : setattr(self, 'recurrence_start_date_time', n.get_datetime_value()),
            "schedule": lambda n : setattr(self, 'schedule', n.get_object_value(PlannerRecurrenceSchedule)),
            "seriesId": lambda n : setattr(self, 'series_id', n.get_str_value()),
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
        writer.write_str_value("nextInSeriesTaskId", self.next_in_series_task_id)
        writer.write_int_value("occurrenceId", self.occurrence_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("previousInSeriesTaskId", self.previous_in_series_task_id)
        writer.write_datetime_value("recurrenceStartDateTime", self.recurrence_start_date_time)
        writer.write_object_value("schedule", self.schedule)
        writer.write_str_value("seriesId", self.series_id)
        writer.write_additional_data_value(self.additional_data)
    

