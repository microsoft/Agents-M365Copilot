from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .workbook_email_identity import WorkbookEmailIdentity

from .entity import Entity

@dataclass
class WorkbookDocumentTaskChange(Entity, Parsable):
    # The user identity the task is assigned to. Only present when the type property is assign. Nullable.
    assignee: Optional[WorkbookEmailIdentity] = None
    # The changedBy property
    changed_by: Optional[WorkbookEmailIdentity] = None
    # The identifier of the associated comment.
    comment_id: Optional[str] = None
    # Date and time when the task was changed. Nullable. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime.datetime] = None
    # The due date and time for the task. Only present when the type property is setSchedule. Nullable. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    due_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # An integer value from 0 to 100 that represents the percentage of the completion of the task and associated comment. 100 means that the task and associated comment are completed. If you change the completion from 100 to a lower value, the associated task and comment are reactivated. Only present when the type property is setPercentComplete. Nullable.
    percent_complete: Optional[int] = None
    # An integer value from 0 to 10 that represents the priority of the task. A lower value indicates a higher priority. 5 indicates the default priority if not set. Only present when the type property is setPriority. Nullable.
    priority: Optional[int] = None
    # The start date and time for the task. Only present when the type property is setSchedule. Nullable. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    start_date_time: Optional[datetime.datetime] = None
    # The title of the task. Only present when the type property is setTitle. Nullable.
    title: Optional[str] = None
    # The type of the change history. The possible values are: create, assign, unassign, unassignAll, setPriority, setTitle, setPercentComplete, setSchedule, remove, restore, undo.
    type: Optional[str] = None
    # The ID of the workbookDocumentTaskChange that was undone for the undo change action. Only exists on an undo change history. Nullable.
    undo_change_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WorkbookDocumentTaskChange:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookDocumentTaskChange
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WorkbookDocumentTaskChange()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .workbook_email_identity import WorkbookEmailIdentity

        from .entity import Entity
        from .workbook_email_identity import WorkbookEmailIdentity

        fields: dict[str, Callable[[Any], None]] = {
            "assignee": lambda n : setattr(self, 'assignee', n.get_object_value(WorkbookEmailIdentity)),
            "changedBy": lambda n : setattr(self, 'changed_by', n.get_object_value(WorkbookEmailIdentity)),
            "commentId": lambda n : setattr(self, 'comment_id', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "dueDateTime": lambda n : setattr(self, 'due_date_time', n.get_datetime_value()),
            "percentComplete": lambda n : setattr(self, 'percent_complete', n.get_int_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
            "undoChangeId": lambda n : setattr(self, 'undo_change_id', n.get_str_value()),
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
        writer.write_object_value("assignee", self.assignee)
        writer.write_object_value("changedBy", self.changed_by)
        writer.write_str_value("commentId", self.comment_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_datetime_value("dueDateTime", self.due_date_time)
        writer.write_int_value("percentComplete", self.percent_complete)
        writer.write_int_value("priority", self.priority)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_str_value("title", self.title)
        writer.write_str_value("type", self.type)
        writer.write_str_value("undoChangeId", self.undo_change_id)
    

