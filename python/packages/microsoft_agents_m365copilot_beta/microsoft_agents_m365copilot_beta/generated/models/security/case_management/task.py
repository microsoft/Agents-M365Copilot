from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .case_management_entity import CaseManagementEntity
    from .case_task_category import CaseTaskCategory
    from .case_task_priority import CaseTaskPriority
    from .task_status import TaskStatus

from .case_management_entity import CaseManagementEntity

@dataclass
class Task(CaseManagementEntity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.caseManagement.task"
    # The user assigned to the task. Supports $filter.
    assigned_to: Optional[str] = None
    # The category property
    category: Optional[CaseTaskCategory] = None
    # Notes recorded when the task is completed. Supports $filter.
    closing_notes: Optional[str] = None
    # The description of the task. Supports $filter.
    description: Optional[str] = None
    # The title of the task. Supports $filter.
    display_name: Optional[str] = None
    # The target completion date and time for the task. Supports $filter.
    due_date_time: Optional[datetime.datetime] = None
    # The priority property
    priority: Optional[CaseTaskPriority] = None
    # The status property
    status: Optional[TaskStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Task:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Task
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Task()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .case_management_entity import CaseManagementEntity
        from .case_task_category import CaseTaskCategory
        from .case_task_priority import CaseTaskPriority
        from .task_status import TaskStatus

        from .case_management_entity import CaseManagementEntity
        from .case_task_category import CaseTaskCategory
        from .case_task_priority import CaseTaskPriority
        from .task_status import TaskStatus

        fields: dict[str, Callable[[Any], None]] = {
            "assignedTo": lambda n : setattr(self, 'assigned_to', n.get_str_value()),
            "category": lambda n : setattr(self, 'category', n.get_enum_value(CaseTaskCategory)),
            "closingNotes": lambda n : setattr(self, 'closing_notes', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "dueDateTime": lambda n : setattr(self, 'due_date_time', n.get_datetime_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_enum_value(CaseTaskPriority)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(TaskStatus)),
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
        writer.write_str_value("assignedTo", self.assigned_to)
        writer.write_enum_value("category", self.category)
        writer.write_str_value("closingNotes", self.closing_notes)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("dueDateTime", self.due_date_time)
        writer.write_enum_value("priority", self.priority)
        writer.write_enum_value("status", self.status)
    

