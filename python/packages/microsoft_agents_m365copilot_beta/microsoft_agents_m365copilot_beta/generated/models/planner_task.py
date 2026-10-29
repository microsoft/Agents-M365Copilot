from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .business_scenario_task import BusinessScenarioTask
    from .identity_set import IdentitySet
    from .planner_applied_categories import PlannerAppliedCategories
    from .planner_archival_info import PlannerArchivalInfo
    from .planner_assigned_to_task_board_task_format import PlannerAssignedToTaskBoardTaskFormat
    from .planner_assignments import PlannerAssignments
    from .planner_bucket_task_board_task_format import PlannerBucketTaskBoardTaskFormat
    from .planner_delta import PlannerDelta
    from .planner_preview_type import PlannerPreviewType
    from .planner_progress_task_board_task_format import PlannerProgressTaskBoardTaskFormat
    from .planner_task_chat_message import PlannerTaskChatMessage
    from .planner_task_completion_requirements import PlannerTaskCompletionRequirements
    from .planner_task_creation import PlannerTaskCreation
    from .planner_task_details import PlannerTaskDetails
    from .planner_task_recurrence import PlannerTaskRecurrence

from .planner_delta import PlannerDelta

@dataclass
class PlannerTask(PlannerDelta, Parsable):
    # The number of checklist items with value set to false, representing incomplete items.
    active_checklist_item_count: Optional[int] = None
    # The categories to which the task is applied. See plannerAppliedCategories resource type for possible values.
    applied_categories: Optional[PlannerAppliedCategories] = None
    # Read-only. Nullable. Contains information about who archived or unarchived the task and why.
    archival_info: Optional[PlannerArchivalInfo] = None
    # Read-only. Nullable. Used to render the task correctly in the task board view when grouped by assignedTo.
    assigned_to_task_board_format: Optional[PlannerAssignedToTaskBoardTaskFormat] = None
    # A hint that is used to order items of this type in a list view. For more information, see Using order hints in planner.
    assignee_priority: Optional[str] = None
    # The set of assignees the task is assigned to.
    assignments: Optional[PlannerAssignments] = None
    # Bucket ID to which the task belongs. The bucket needs to be in the same plan as the task. The value of the bucketId property is 28 characters long and case-sensitive. Format validation is done on the service.
    bucket_id: Optional[str] = None
    # Read-only. Nullable. Used to render the task correctly in the task board view when grouped by bucket.
    bucket_task_board_format: Optional[PlannerBucketTaskBoardTaskFormat] = None
    # The number of checklist items that are present on the task.
    checklist_item_count: Optional[int] = None
    # The identity of the user that completed the task.
    completed_by: Optional[IdentitySet] = None
    # Read-only. The date and time at which the 'percentComplete' of the task is set to '100'. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    completed_date_time: Optional[datetime.datetime] = None
    # The thread ID of the conversation on the task. This is the ID of the conversation thread object created in the group.
    conversation_thread_id: Optional[str] = None
    # The identity of the user who created the task.
    created_by: Optional[IdentitySet] = None
    # Read-only. The date and time at which the task is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    created_date_time: Optional[datetime.datetime] = None
    # Information about the origin of the task.
    creation_source: Optional[PlannerTaskCreation] = None
    # Read-only. Nullable. More details about the task.
    details: Optional[PlannerTaskDetails] = None
    # The date and time at which the task is due. The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    due_date_time: Optional[datetime.datetime] = None
    # Read-only. The IDs of the goals associated with the task.
    goal_ids: Optional[list[str]] = None
    # Read-only. This value is true if the task has chat messages associated with it. Otherwise, false.
    has_chat: Optional[bool] = None
    # Read-only. This value is true if the details object of the task has a nonempty description. Otherwise, false.
    has_description: Optional[bool] = None
    # Read-only. If set to true, the task is archived. An archived task is read-only.
    is_archived: Optional[bool] = None
    # Indicates whether to show this task in the MyDay view. If true, it shows the task.
    is_on_my_day: Optional[bool] = None
    # Read-only. The date on which task is added to or removed from MyDay.
    is_on_my_day_last_modified_date: Optional[datetime.date] = None
    # Read-only. User ID by which this is last modified.
    last_modified_by: Optional[IdentitySet] = None
    # Read-only. Date and time at which this is last modified. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    last_modified_date_time: Optional[datetime.datetime] = None
    # Read-only. Nullable. Chat messages associated with the task.
    messages: Optional[list[PlannerTaskChatMessage]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The hint used to order items of this type in a list view. For more information, see Using order hints in planner.
    order_hint: Optional[str] = None
    # The percentage of task completion. When set to 100, the task is completed.
    percent_complete: Optional[int] = None
    # Plan ID to which the task belongs.
    plan_id: Optional[str] = None
    # The type of preview that shows up on the task. The possible values are: automatic, noPreview, checklist, description, reference.
    preview_type: Optional[PlannerPreviewType] = None
    # The priority of the task. Valid values are between 0 and 10, inclusive. Larger values indicate lower priority. For example, 0 has the highest priority and 10 has the lowest priority. Currently, planner interprets values 0 and 1 as 'urgent', 2 and 3 and 4 as 'important', 5, 6, and 7 as 'medium', and 8, 9, and 10 as 'low'. Currently, planner sets the value 1 for 'urgent', 3 for 'important', 5 for 'medium', and 9 for 'low'.
    priority: Optional[int] = None
    # Read-only. Nullable. Used to render the task correctly in the task board view when grouped by progress.
    progress_task_board_format: Optional[PlannerProgressTaskBoardTaskFormat] = None
    # Defines active or inactive recurrence for the task. null when the recurrence has never been defined for the task.
    recurrence: Optional[PlannerTaskRecurrence] = None
    # Number of external references that exist on the task.
    reference_count: Optional[int] = None
    # Indicates all the requirements specified on the plannerTask. The possible values are: none, checklistCompletion, unknownFutureValue, formCompletion, approvalCompletion. Read-only. Use the Prefer: include-unknown-enum-members request header to get the following values in this evolvable enum: formCompletion, approvalCompletion. The plannerTaskCompletionRequirementDetails in plannerTaskDetails has details of the requirements specified, if any.
    specified_completion_requirements: Optional[PlannerTaskCompletionRequirements] = None
    # Date and time at which the task starts. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    start_date_time: Optional[datetime.datetime] = None
    # Title of the task.
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlannerTask:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlannerTask
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.businessScenarioTask".casefold():
            from .business_scenario_task import BusinessScenarioTask

            return BusinessScenarioTask()
        return PlannerTask()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .business_scenario_task import BusinessScenarioTask
        from .identity_set import IdentitySet
        from .planner_applied_categories import PlannerAppliedCategories
        from .planner_archival_info import PlannerArchivalInfo
        from .planner_assigned_to_task_board_task_format import PlannerAssignedToTaskBoardTaskFormat
        from .planner_assignments import PlannerAssignments
        from .planner_bucket_task_board_task_format import PlannerBucketTaskBoardTaskFormat
        from .planner_delta import PlannerDelta
        from .planner_preview_type import PlannerPreviewType
        from .planner_progress_task_board_task_format import PlannerProgressTaskBoardTaskFormat
        from .planner_task_chat_message import PlannerTaskChatMessage
        from .planner_task_completion_requirements import PlannerTaskCompletionRequirements
        from .planner_task_creation import PlannerTaskCreation
        from .planner_task_details import PlannerTaskDetails
        from .planner_task_recurrence import PlannerTaskRecurrence

        from .business_scenario_task import BusinessScenarioTask
        from .identity_set import IdentitySet
        from .planner_applied_categories import PlannerAppliedCategories
        from .planner_archival_info import PlannerArchivalInfo
        from .planner_assigned_to_task_board_task_format import PlannerAssignedToTaskBoardTaskFormat
        from .planner_assignments import PlannerAssignments
        from .planner_bucket_task_board_task_format import PlannerBucketTaskBoardTaskFormat
        from .planner_delta import PlannerDelta
        from .planner_preview_type import PlannerPreviewType
        from .planner_progress_task_board_task_format import PlannerProgressTaskBoardTaskFormat
        from .planner_task_chat_message import PlannerTaskChatMessage
        from .planner_task_completion_requirements import PlannerTaskCompletionRequirements
        from .planner_task_creation import PlannerTaskCreation
        from .planner_task_details import PlannerTaskDetails
        from .planner_task_recurrence import PlannerTaskRecurrence

        fields: dict[str, Callable[[Any], None]] = {
            "activeChecklistItemCount": lambda n : setattr(self, 'active_checklist_item_count', n.get_int_value()),
            "appliedCategories": lambda n : setattr(self, 'applied_categories', n.get_object_value(PlannerAppliedCategories)),
            "archivalInfo": lambda n : setattr(self, 'archival_info', n.get_object_value(PlannerArchivalInfo)),
            "assignedToTaskBoardFormat": lambda n : setattr(self, 'assigned_to_task_board_format', n.get_object_value(PlannerAssignedToTaskBoardTaskFormat)),
            "assigneePriority": lambda n : setattr(self, 'assignee_priority', n.get_str_value()),
            "assignments": lambda n : setattr(self, 'assignments', n.get_object_value(PlannerAssignments)),
            "bucketId": lambda n : setattr(self, 'bucket_id', n.get_str_value()),
            "bucketTaskBoardFormat": lambda n : setattr(self, 'bucket_task_board_format', n.get_object_value(PlannerBucketTaskBoardTaskFormat)),
            "checklistItemCount": lambda n : setattr(self, 'checklist_item_count', n.get_int_value()),
            "completedBy": lambda n : setattr(self, 'completed_by', n.get_object_value(IdentitySet)),
            "completedDateTime": lambda n : setattr(self, 'completed_date_time', n.get_datetime_value()),
            "conversationThreadId": lambda n : setattr(self, 'conversation_thread_id', n.get_str_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "creationSource": lambda n : setattr(self, 'creation_source', n.get_object_value(PlannerTaskCreation)),
            "details": lambda n : setattr(self, 'details', n.get_object_value(PlannerTaskDetails)),
            "dueDateTime": lambda n : setattr(self, 'due_date_time', n.get_datetime_value()),
            "goalIds": lambda n : setattr(self, 'goal_ids', n.get_collection_of_primitive_values(str)),
            "hasChat": lambda n : setattr(self, 'has_chat', n.get_bool_value()),
            "hasDescription": lambda n : setattr(self, 'has_description', n.get_bool_value()),
            "isArchived": lambda n : setattr(self, 'is_archived', n.get_bool_value()),
            "isOnMyDay": lambda n : setattr(self, 'is_on_my_day', n.get_bool_value()),
            "isOnMyDayLastModifiedDate": lambda n : setattr(self, 'is_on_my_day_last_modified_date', n.get_date_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "messages": lambda n : setattr(self, 'messages', n.get_collection_of_object_values(PlannerTaskChatMessage)),
            "orderHint": lambda n : setattr(self, 'order_hint', n.get_str_value()),
            "percentComplete": lambda n : setattr(self, 'percent_complete', n.get_int_value()),
            "planId": lambda n : setattr(self, 'plan_id', n.get_str_value()),
            "previewType": lambda n : setattr(self, 'preview_type', n.get_enum_value(PlannerPreviewType)),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "progressTaskBoardFormat": lambda n : setattr(self, 'progress_task_board_format', n.get_object_value(PlannerProgressTaskBoardTaskFormat)),
            "recurrence": lambda n : setattr(self, 'recurrence', n.get_object_value(PlannerTaskRecurrence)),
            "referenceCount": lambda n : setattr(self, 'reference_count', n.get_int_value()),
            "specifiedCompletionRequirements": lambda n : setattr(self, 'specified_completion_requirements', n.get_collection_of_enum_values(PlannerTaskCompletionRequirements)),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
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
        writer.write_int_value("activeChecklistItemCount", self.active_checklist_item_count)
        writer.write_object_value("appliedCategories", self.applied_categories)
        writer.write_object_value("archivalInfo", self.archival_info)
        writer.write_object_value("assignedToTaskBoardFormat", self.assigned_to_task_board_format)
        writer.write_str_value("assigneePriority", self.assignee_priority)
        writer.write_object_value("assignments", self.assignments)
        writer.write_str_value("bucketId", self.bucket_id)
        writer.write_object_value("bucketTaskBoardFormat", self.bucket_task_board_format)
        writer.write_int_value("checklistItemCount", self.checklist_item_count)
        writer.write_object_value("completedBy", self.completed_by)
        writer.write_datetime_value("completedDateTime", self.completed_date_time)
        writer.write_str_value("conversationThreadId", self.conversation_thread_id)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("creationSource", self.creation_source)
        writer.write_object_value("details", self.details)
        writer.write_datetime_value("dueDateTime", self.due_date_time)
        writer.write_collection_of_primitive_values("goalIds", self.goal_ids)
        writer.write_bool_value("hasChat", self.has_chat)
        writer.write_bool_value("hasDescription", self.has_description)
        writer.write_bool_value("isArchived", self.is_archived)
        writer.write_bool_value("isOnMyDay", self.is_on_my_day)
        writer.write_date_value("isOnMyDayLastModifiedDate", self.is_on_my_day_last_modified_date)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_object_values("messages", self.messages)
        writer.write_str_value("orderHint", self.order_hint)
        writer.write_int_value("percentComplete", self.percent_complete)
        writer.write_str_value("planId", self.plan_id)
        writer.write_enum_value("previewType", self.preview_type)
        writer.write_int_value("priority", self.priority)
        writer.write_object_value("progressTaskBoardFormat", self.progress_task_board_format)
        writer.write_object_value("recurrence", self.recurrence)
        writer.write_int_value("referenceCount", self.reference_count)
        writer.write_enum_value("specifiedCompletionRequirements", self.specified_completion_requirements)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_str_value("title", self.title)
    

