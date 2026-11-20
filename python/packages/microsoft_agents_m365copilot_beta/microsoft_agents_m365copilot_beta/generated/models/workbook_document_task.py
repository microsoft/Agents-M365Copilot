from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .workbook_comment import WorkbookComment
    from .workbook_document_task_change import WorkbookDocumentTaskChange
    from .workbook_document_task_schedule import WorkbookDocumentTaskSchedule
    from .workbook_email_identity import WorkbookEmailIdentity

from .entity import Entity

@dataclass
class WorkbookDocumentTask(Entity, Parsable):
    # A collection of user identities the task is assigned to.
    assignees: Optional[list[WorkbookEmailIdentity]] = None
    # A collection of task change histories.
    changes: Optional[list[WorkbookDocumentTaskChange]] = None
    # The comment that the task is associated with.
    comment: Optional[WorkbookComment] = None
    # The identity of the user who completed the task. Nullable.
    completed_by: Optional[WorkbookEmailIdentity] = None
    # Date and time when the task was completed. Nullable. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    completed_date_time: Optional[datetime.datetime] = None
    # A user identity that creates the task. Nullable.
    created_by: Optional[WorkbookEmailIdentity] = None
    # Date and time when the task was created. Nullable. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # An integer value from 0 to 100 that represents the percentage of the completion of the task. 100 means that the task is completed. Nullable.
    percent_complete: Optional[int] = None
    # An integer value from 0 to 10 that represents the priority of the task. A lower value indicates a higher priority. Nullable.
    priority: Optional[int] = None
    # Start and due date of the task. Nullable.
    start_and_due_date_time: Optional[WorkbookDocumentTaskSchedule] = None
    # The title of the task.
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WorkbookDocumentTask:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookDocumentTask
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WorkbookDocumentTask()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .workbook_comment import WorkbookComment
        from .workbook_document_task_change import WorkbookDocumentTaskChange
        from .workbook_document_task_schedule import WorkbookDocumentTaskSchedule
        from .workbook_email_identity import WorkbookEmailIdentity

        from .entity import Entity
        from .workbook_comment import WorkbookComment
        from .workbook_document_task_change import WorkbookDocumentTaskChange
        from .workbook_document_task_schedule import WorkbookDocumentTaskSchedule
        from .workbook_email_identity import WorkbookEmailIdentity

        fields: dict[str, Callable[[Any], None]] = {
            "assignees": lambda n : setattr(self, 'assignees', n.get_collection_of_object_values(WorkbookEmailIdentity)),
            "changes": lambda n : setattr(self, 'changes', n.get_collection_of_object_values(WorkbookDocumentTaskChange)),
            "comment": lambda n : setattr(self, 'comment', n.get_object_value(WorkbookComment)),
            "completedBy": lambda n : setattr(self, 'completed_by', n.get_object_value(WorkbookEmailIdentity)),
            "completedDateTime": lambda n : setattr(self, 'completed_date_time', n.get_datetime_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(WorkbookEmailIdentity)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "percentComplete": lambda n : setattr(self, 'percent_complete', n.get_int_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "startAndDueDateTime": lambda n : setattr(self, 'start_and_due_date_time', n.get_object_value(WorkbookDocumentTaskSchedule)),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
        writer.write_collection_of_object_values("assignees", self.assignees)
        writer.write_collection_of_object_values("changes", self.changes)
        writer.write_object_value("comment", self.comment)
        writer.write_object_value("completedBy", self.completed_by)
        writer.write_datetime_value("completedDateTime", self.completed_date_time)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_int_value("percentComplete", self.percent_complete)
        writer.write_int_value("priority", self.priority)
        writer.write_object_value("startAndDueDateTime", self.start_and_due_date_time)
        writer.write_str_value("title", self.title)
    

