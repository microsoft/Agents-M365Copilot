from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .identity_set import IdentitySet
    from .planner_applied_categories import PlannerAppliedCategories
    from .planner_archival_info import PlannerArchivalInfo
    from .planner_assignments import PlannerAssignments
    from .planner_preview_type import PlannerPreviewType
    from .planner_task_completion_requirements import PlannerTaskCompletionRequirements
    from .planner_task_creation import PlannerTaskCreation
    from .planner_task_details_data import PlannerTaskDetailsData
    from .planner_task_recurrence import PlannerTaskRecurrence

@dataclass
class PlannerTaskData(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The number of incomplete checklist items whose value is set to false.
    active_checklist_item_count: Optional[int] = None
    # The categories to which the task is applied.
    applied_categories: Optional[PlannerAppliedCategories] = None
    # Information about who archived or unarchived the task and why.
    archival_info: Optional[PlannerArchivalInfo] = None
    # The set of assignees the task is assigned to.
    assignments: Optional[PlannerAssignments] = None
    # Bucket ID to which the task belongs. The bucket needs to be in the same plan as the task.
    bucket_id: Optional[str] = None
    # The number of checklist items that are present on the task.
    checklist_item_count: Optional[int] = None
    # The identity of the user that completed the task.
    completed_by: Optional[IdentitySet] = None
    # The date and time at which the percentComplete of the task is set to 100. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2024, is 2024-01-01T00:00:00Z.
    completed_date_time: Optional[datetime.datetime] = None
    # The thread ID of the conversation on the task that corresponds to the ID of the conversation thread object created in the group.
    conversation_thread_id: Optional[str] = None
    # The identity of the user who created the task.
    created_by: Optional[IdentitySet] = None
    # The date and time at which the task was created. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2024, is 2024-01-01T00:00:00Z.
    created_date_time: Optional[datetime.datetime] = None
    # Information about the origin of the task.
    creation_source: Optional[PlannerTaskCreation] = None
    # Additional details about the task.
    details: Optional[PlannerTaskDetailsData] = None
    # The date and time at which the task is due. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2024, is 2024-01-01T00:00:00Z.
    due_date_time: Optional[datetime.datetime] = None
    # Set to true if the task has a chat associated with it; otherwise, false.
    has_chat: Optional[bool] = None
    # Set to true if the details object of the task has a nonempty description; otherwise, false.
    has_description: Optional[bool] = None
    # Set to true if the task is archived; otherwise, false.
    is_archived: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Hint used to order items of this type in a list view.
    order_hint: Optional[str] = None
    # Percentage of task completion. When set to 100, the task is considered completed.
    percent_complete: Optional[int] = None
    # The previewType property
    preview_type: Optional[PlannerPreviewType] = None
    # The priority of the task. Valid values are between 0 and 10, inclusive. Larger values indicate lower priority. For example, 0 has the highest priority and 10 has the lowest priority.
    priority: Optional[int] = None
    # Defines active or inactive recurrence for the task. A null value indicates that the recurrence was never defined for the task.
    recurrence: Optional[PlannerTaskRecurrence] = None
    # Number of external references that exist on the task.
    reference_count: Optional[int] = None
    # The specifiedCompletionRequirements property
    specified_completion_requirements: Optional[PlannerTaskCompletionRequirements] = None
    # The date and time at which the task starts. The date and time information uses ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2021 is 2021-01-01T00:00:00Z.
    start_date_time: Optional[datetime.datetime] = None
    # Title of the task.
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlannerTaskData:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlannerTaskData
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PlannerTaskData()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .identity_set import IdentitySet
        from .planner_applied_categories import PlannerAppliedCategories
        from .planner_archival_info import PlannerArchivalInfo
        from .planner_assignments import PlannerAssignments
        from .planner_preview_type import PlannerPreviewType
        from .planner_task_completion_requirements import PlannerTaskCompletionRequirements
        from .planner_task_creation import PlannerTaskCreation
        from .planner_task_details_data import PlannerTaskDetailsData
        from .planner_task_recurrence import PlannerTaskRecurrence

        from .identity_set import IdentitySet
        from .planner_applied_categories import PlannerAppliedCategories
        from .planner_archival_info import PlannerArchivalInfo
        from .planner_assignments import PlannerAssignments
        from .planner_preview_type import PlannerPreviewType
        from .planner_task_completion_requirements import PlannerTaskCompletionRequirements
        from .planner_task_creation import PlannerTaskCreation
        from .planner_task_details_data import PlannerTaskDetailsData
        from .planner_task_recurrence import PlannerTaskRecurrence

        fields: dict[str, Callable[[Any], None]] = {
            "activeChecklistItemCount": lambda n : setattr(self, 'active_checklist_item_count', n.get_int_value()),
            "appliedCategories": lambda n : setattr(self, 'applied_categories', n.get_object_value(PlannerAppliedCategories)),
            "archivalInfo": lambda n : setattr(self, 'archival_info', n.get_object_value(PlannerArchivalInfo)),
            "assignments": lambda n : setattr(self, 'assignments', n.get_object_value(PlannerAssignments)),
            "bucketId": lambda n : setattr(self, 'bucket_id', n.get_str_value()),
            "checklistItemCount": lambda n : setattr(self, 'checklist_item_count', n.get_int_value()),
            "completedBy": lambda n : setattr(self, 'completed_by', n.get_object_value(IdentitySet)),
            "completedDateTime": lambda n : setattr(self, 'completed_date_time', n.get_datetime_value()),
            "conversationThreadId": lambda n : setattr(self, 'conversation_thread_id', n.get_str_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "creationSource": lambda n : setattr(self, 'creation_source', n.get_object_value(PlannerTaskCreation)),
            "details": lambda n : setattr(self, 'details', n.get_object_value(PlannerTaskDetailsData)),
            "dueDateTime": lambda n : setattr(self, 'due_date_time', n.get_datetime_value()),
            "hasChat": lambda n : setattr(self, 'has_chat', n.get_bool_value()),
            "hasDescription": lambda n : setattr(self, 'has_description', n.get_bool_value()),
            "isArchived": lambda n : setattr(self, 'is_archived', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "orderHint": lambda n : setattr(self, 'order_hint', n.get_str_value()),
            "percentComplete": lambda n : setattr(self, 'percent_complete', n.get_int_value()),
            "previewType": lambda n : setattr(self, 'preview_type', n.get_enum_value(PlannerPreviewType)),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "recurrence": lambda n : setattr(self, 'recurrence', n.get_object_value(PlannerTaskRecurrence)),
            "referenceCount": lambda n : setattr(self, 'reference_count', n.get_int_value()),
            "specifiedCompletionRequirements": lambda n : setattr(self, 'specified_completion_requirements', n.get_collection_of_enum_values(PlannerTaskCompletionRequirements)),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
        writer.write_int_value("activeChecklistItemCount", self.active_checklist_item_count)
        writer.write_object_value("appliedCategories", self.applied_categories)
        writer.write_object_value("archivalInfo", self.archival_info)
        writer.write_object_value("assignments", self.assignments)
        writer.write_str_value("bucketId", self.bucket_id)
        writer.write_int_value("checklistItemCount", self.checklist_item_count)
        writer.write_object_value("completedBy", self.completed_by)
        writer.write_datetime_value("completedDateTime", self.completed_date_time)
        writer.write_str_value("conversationThreadId", self.conversation_thread_id)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("creationSource", self.creation_source)
        writer.write_object_value("details", self.details)
        writer.write_datetime_value("dueDateTime", self.due_date_time)
        writer.write_bool_value("hasChat", self.has_chat)
        writer.write_bool_value("hasDescription", self.has_description)
        writer.write_bool_value("isArchived", self.is_archived)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("orderHint", self.order_hint)
        writer.write_int_value("percentComplete", self.percent_complete)
        writer.write_enum_value("previewType", self.preview_type)
        writer.write_int_value("priority", self.priority)
        writer.write_object_value("recurrence", self.recurrence)
        writer.write_int_value("referenceCount", self.reference_count)
        writer.write_enum_value("specifiedCompletionRequirements", self.specified_completion_requirements)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_str_value("title", self.title)
        writer.write_additional_data_value(self.additional_data)
    

