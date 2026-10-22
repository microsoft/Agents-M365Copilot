from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .checklist_item_v4 import ChecklistItemV4
    from .content_link import ContentLink
    from .creation_info import CreationInfo
    from .custom_field_value import CustomFieldValue
    from .date_with_optional_time import DateWithOptionalTime
    from .extension_field_collection import ExtensionFieldCollection
    from .identity_set import IdentitySet
    from .item_body import ItemBody
    from .planner_archival_info import PlannerArchivalInfo
    from .planner_chat_message import PlannerChatMessage
    from .planner_delta import PlannerDelta
    from .planner_task_recurrence import PlannerTaskRecurrence
    from .planner_task_status import PlannerTaskStatus
    from .task_capability import TaskCapability
    from .task_personal_view import TaskPersonalView
    from .task_plan_view import TaskPlanView
    from .user_assignment import UserAssignment

from .planner_delta import PlannerDelta

@dataclass
class Task(PlannerDelta, Parsable):
    # Information about whether the entity is archived, and when it was archived.
    archival_info: Optional[PlannerArchivalInfo] = None
    # ID of the bucket that the task belongs to.
    bucket_id: Optional[str] = None
    # Server-computed, read-only capability flags indicating which optional features are enabled for the entity.
    capabilities: Optional[TaskCapability] = None
    # The collection of checklist items on the task. Read-only. Nullable.
    checklist: Optional[list[ChecklistItemV4]] = None
    # Identity of the user who marked the task complete.
    completed_by: Optional[IdentitySet] = None
    # Date and time the task was completed.
    completed_date_time: Optional[datetime.datetime] = None
    # Read-only creation metadata for the entity.
    creation_info: Optional[CreationInfo] = None
    # The collection of custom field values set on the task. Read-only. Nullable.
    custom_field_values: Optional[list[CustomFieldValue]] = None
    # Title of the task.
    display_name: Optional[str] = None
    # Date and, optionally, time the task is due.
    due_date_time: Optional[DateWithOptionalTime] = None
    # Custom extension field values set on the entity. Supports $select.
    extensions: Optional[ExtensionFieldCollection] = None
    # Date and, optionally, time the task was finished.
    finish_date_time: Optional[DateWithOptionalTime] = None
    # IDs of the goals that the task is associated with.
    goal_ids: Optional[list[str]] = None
    # Indicates whether the task has an associated chat.
    has_chat: Optional[bool] = None
    # Indicates whether the task has subtasks.
    has_children: Optional[bool] = None
    # Indicates whether the task is on the critical path, as computed from its dependencies.
    is_critical: Optional[bool] = None
    # Identity of the user (or application) who last modified the entity. Read-only.
    last_modified_by: Optional[IdentitySet] = None
    # Date and time the entity was last modified. The value is represented in ISO 8601 format and is always in UTC time. Read-only.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The collection of content links attached to the task. Read-only. Nullable.
    links: Optional[list[ContentLink]] = None
    # The collection of chat messages associated with the task. Read-only. Nullable.
    messages: Optional[list[PlannerChatMessage]] = None
    # Additional details or notes about the task.
    notes: Optional[ItemBody] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # ID of the parent task, if this task is a subtask.
    parent_task_id: Optional[str] = None
    # Percentage of the task's completion, ranging from 0 to 100.
    percent_complete: Optional[int] = None
    # Per-user personal view settings for the task, such as My Day membership.
    personal_view: Optional[TaskPersonalView] = None
    # ID of the plan that contains the task. Immutable after creation.
    plan_id: Optional[str] = None
    # Task view settings scoped to the plan, such as applied category IDs.
    plan_view: Optional[TaskPlanView] = None
    # Priority of the task. Supported values range from 0 (urgent) to 10 (low).
    priority: Optional[int] = None
    # Recurrence pattern for the task, if it repeats.
    recurrence: Optional[PlannerTaskRecurrence] = None
    # Date and, optionally, time the task is scheduled to start.
    start_date_time: Optional[DateWithOptionalTime] = None
    # Indicates progress on the task. The possible values are: notStarted, inProgress, completed, blocked, unknownFutureValue.
    status: Optional[PlannerTaskStatus] = None
    # The collection of user assignments on the task. Read-only. Nullable.
    user_assignments: Optional[list[UserAssignment]] = None
    
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
        from .checklist_item_v4 import ChecklistItemV4
        from .content_link import ContentLink
        from .creation_info import CreationInfo
        from .custom_field_value import CustomFieldValue
        from .date_with_optional_time import DateWithOptionalTime
        from .extension_field_collection import ExtensionFieldCollection
        from .identity_set import IdentitySet
        from .item_body import ItemBody
        from .planner_archival_info import PlannerArchivalInfo
        from .planner_chat_message import PlannerChatMessage
        from .planner_delta import PlannerDelta
        from .planner_task_recurrence import PlannerTaskRecurrence
        from .planner_task_status import PlannerTaskStatus
        from .task_capability import TaskCapability
        from .task_personal_view import TaskPersonalView
        from .task_plan_view import TaskPlanView
        from .user_assignment import UserAssignment

        from .checklist_item_v4 import ChecklistItemV4
        from .content_link import ContentLink
        from .creation_info import CreationInfo
        from .custom_field_value import CustomFieldValue
        from .date_with_optional_time import DateWithOptionalTime
        from .extension_field_collection import ExtensionFieldCollection
        from .identity_set import IdentitySet
        from .item_body import ItemBody
        from .planner_archival_info import PlannerArchivalInfo
        from .planner_chat_message import PlannerChatMessage
        from .planner_delta import PlannerDelta
        from .planner_task_recurrence import PlannerTaskRecurrence
        from .planner_task_status import PlannerTaskStatus
        from .task_capability import TaskCapability
        from .task_personal_view import TaskPersonalView
        from .task_plan_view import TaskPlanView
        from .user_assignment import UserAssignment

        fields: dict[str, Callable[[Any], None]] = {
            "archivalInfo": lambda n : setattr(self, 'archival_info', n.get_object_value(PlannerArchivalInfo)),
            "bucketId": lambda n : setattr(self, 'bucket_id', n.get_str_value()),
            "capabilities": lambda n : setattr(self, 'capabilities', n.get_object_value(TaskCapability)),
            "checklist": lambda n : setattr(self, 'checklist', n.get_collection_of_object_values(ChecklistItemV4)),
            "completedBy": lambda n : setattr(self, 'completed_by', n.get_object_value(IdentitySet)),
            "completedDateTime": lambda n : setattr(self, 'completed_date_time', n.get_datetime_value()),
            "creationInfo": lambda n : setattr(self, 'creation_info', n.get_object_value(CreationInfo)),
            "customFieldValues": lambda n : setattr(self, 'custom_field_values', n.get_collection_of_object_values(CustomFieldValue)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "dueDateTime": lambda n : setattr(self, 'due_date_time', n.get_object_value(DateWithOptionalTime)),
            "extensions": lambda n : setattr(self, 'extensions', n.get_object_value(ExtensionFieldCollection)),
            "finishDateTime": lambda n : setattr(self, 'finish_date_time', n.get_object_value(DateWithOptionalTime)),
            "goalIds": lambda n : setattr(self, 'goal_ids', n.get_collection_of_primitive_values(str)),
            "hasChat": lambda n : setattr(self, 'has_chat', n.get_bool_value()),
            "hasChildren": lambda n : setattr(self, 'has_children', n.get_bool_value()),
            "isCritical": lambda n : setattr(self, 'is_critical', n.get_bool_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "links": lambda n : setattr(self, 'links', n.get_collection_of_object_values(ContentLink)),
            "messages": lambda n : setattr(self, 'messages', n.get_collection_of_object_values(PlannerChatMessage)),
            "notes": lambda n : setattr(self, 'notes', n.get_object_value(ItemBody)),
            "parentTaskId": lambda n : setattr(self, 'parent_task_id', n.get_str_value()),
            "percentComplete": lambda n : setattr(self, 'percent_complete', n.get_int_value()),
            "personalView": lambda n : setattr(self, 'personal_view', n.get_object_value(TaskPersonalView)),
            "planId": lambda n : setattr(self, 'plan_id', n.get_str_value()),
            "planView": lambda n : setattr(self, 'plan_view', n.get_object_value(TaskPlanView)),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "recurrence": lambda n : setattr(self, 'recurrence', n.get_object_value(PlannerTaskRecurrence)),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_object_value(DateWithOptionalTime)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(PlannerTaskStatus)),
            "userAssignments": lambda n : setattr(self, 'user_assignments', n.get_collection_of_object_values(UserAssignment)),
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
        writer.write_object_value("archivalInfo", self.archival_info)
        writer.write_str_value("bucketId", self.bucket_id)
        writer.write_collection_of_object_values("checklist", self.checklist)
        writer.write_object_value("completedBy", self.completed_by)
        writer.write_datetime_value("completedDateTime", self.completed_date_time)
        writer.write_collection_of_object_values("customFieldValues", self.custom_field_values)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("dueDateTime", self.due_date_time)
        writer.write_object_value("extensions", self.extensions)
        writer.write_object_value("finishDateTime", self.finish_date_time)
        writer.write_collection_of_primitive_values("goalIds", self.goal_ids)
        writer.write_bool_value("hasChat", self.has_chat)
        writer.write_bool_value("hasChildren", self.has_children)
        writer.write_bool_value("isCritical", self.is_critical)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_object_values("links", self.links)
        writer.write_collection_of_object_values("messages", self.messages)
        writer.write_object_value("notes", self.notes)
        writer.write_str_value("parentTaskId", self.parent_task_id)
        writer.write_int_value("percentComplete", self.percent_complete)
        writer.write_object_value("personalView", self.personal_view)
        writer.write_str_value("planId", self.plan_id)
        writer.write_object_value("planView", self.plan_view)
        writer.write_int_value("priority", self.priority)
        writer.write_object_value("recurrence", self.recurrence)
        writer.write_object_value("startDateTime", self.start_date_time)
        writer.write_enum_value("status", self.status)
        writer.write_collection_of_object_values("userAssignments", self.user_assignments)
    

