from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .bucket import Bucket
    from .business_scenario_task import BusinessScenarioTask
    from .category_definition import CategoryDefinition
    from .checklist_item_v4 import ChecklistItemV4
    from .content_link import ContentLink
    from .custom_choice_option import CustomChoiceOption
    from .custom_field_definition import CustomFieldDefinition
    from .custom_field_value import CustomFieldValue
    from .dependency import Dependency
    from .entity import Entity
    from .goal import Goal
    from .history_item import HistoryItem
    from .plan import Plan
    from .planner_assigned_to_task_board_task_format import PlannerAssignedToTaskBoardTaskFormat
    from .planner_bucket import PlannerBucket
    from .planner_bucket_task_board_task_format import PlannerBucketTaskBoardTaskFormat
    from .planner_chat_message import PlannerChatMessage
    from .planner_goal import PlannerGoal
    from .planner_history_item import PlannerHistoryItem
    from .planner_plan import PlannerPlan
    from .planner_plan_details import PlannerPlanDetails
    from .planner_progress_task_board_task_format import PlannerProgressTaskBoardTaskFormat
    from .planner_task import PlannerTask
    from .planner_task_details import PlannerTaskDetails
    from .planner_user import PlannerUser
    from .plan_context_link import PlanContextLink
    from .task import Task
    from .task_history_item import TaskHistoryItem
    from .user_assignment import UserAssignment

from .entity import Entity

@dataclass
class PlannerDelta(Entity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlannerDelta:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlannerDelta
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.bucket".casefold():
            from .bucket import Bucket

            return Bucket()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.businessScenarioTask".casefold():
            from .business_scenario_task import BusinessScenarioTask

            return BusinessScenarioTask()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.categoryDefinition".casefold():
            from .category_definition import CategoryDefinition

            return CategoryDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.checklistItemV4".casefold():
            from .checklist_item_v4 import ChecklistItemV4

            return ChecklistItemV4()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.contentLink".casefold():
            from .content_link import ContentLink

            return ContentLink()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.customChoiceOption".casefold():
            from .custom_choice_option import CustomChoiceOption

            return CustomChoiceOption()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.customFieldDefinition".casefold():
            from .custom_field_definition import CustomFieldDefinition

            return CustomFieldDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.customFieldValue".casefold():
            from .custom_field_value import CustomFieldValue

            return CustomFieldValue()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.dependency".casefold():
            from .dependency import Dependency

            return Dependency()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.goal".casefold():
            from .goal import Goal

            return Goal()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.historyItem".casefold():
            from .history_item import HistoryItem

            return HistoryItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plan".casefold():
            from .plan import Plan

            return Plan()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.planContextLink".casefold():
            from .plan_context_link import PlanContextLink

            return PlanContextLink()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerAssignedToTaskBoardTaskFormat".casefold():
            from .planner_assigned_to_task_board_task_format import PlannerAssignedToTaskBoardTaskFormat

            return PlannerAssignedToTaskBoardTaskFormat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerBucket".casefold():
            from .planner_bucket import PlannerBucket

            return PlannerBucket()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerBucketTaskBoardTaskFormat".casefold():
            from .planner_bucket_task_board_task_format import PlannerBucketTaskBoardTaskFormat

            return PlannerBucketTaskBoardTaskFormat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerChatMessage".casefold():
            from .planner_chat_message import PlannerChatMessage

            return PlannerChatMessage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerGoal".casefold():
            from .planner_goal import PlannerGoal

            return PlannerGoal()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerHistoryItem".casefold():
            from .planner_history_item import PlannerHistoryItem

            return PlannerHistoryItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerPlan".casefold():
            from .planner_plan import PlannerPlan

            return PlannerPlan()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerPlanDetails".casefold():
            from .planner_plan_details import PlannerPlanDetails

            return PlannerPlanDetails()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerProgressTaskBoardTaskFormat".casefold():
            from .planner_progress_task_board_task_format import PlannerProgressTaskBoardTaskFormat

            return PlannerProgressTaskBoardTaskFormat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerTask".casefold():
            from .planner_task import PlannerTask

            return PlannerTask()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerTaskDetails".casefold():
            from .planner_task_details import PlannerTaskDetails

            return PlannerTaskDetails()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerUser".casefold():
            from .planner_user import PlannerUser

            return PlannerUser()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.task".casefold():
            from .task import Task

            return Task()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.taskHistoryItem".casefold():
            from .task_history_item import TaskHistoryItem

            return TaskHistoryItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userAssignment".casefold():
            from .user_assignment import UserAssignment

            return UserAssignment()
        return PlannerDelta()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .bucket import Bucket
        from .business_scenario_task import BusinessScenarioTask
        from .category_definition import CategoryDefinition
        from .checklist_item_v4 import ChecklistItemV4
        from .content_link import ContentLink
        from .custom_choice_option import CustomChoiceOption
        from .custom_field_definition import CustomFieldDefinition
        from .custom_field_value import CustomFieldValue
        from .dependency import Dependency
        from .entity import Entity
        from .goal import Goal
        from .history_item import HistoryItem
        from .plan import Plan
        from .planner_assigned_to_task_board_task_format import PlannerAssignedToTaskBoardTaskFormat
        from .planner_bucket import PlannerBucket
        from .planner_bucket_task_board_task_format import PlannerBucketTaskBoardTaskFormat
        from .planner_chat_message import PlannerChatMessage
        from .planner_goal import PlannerGoal
        from .planner_history_item import PlannerHistoryItem
        from .planner_plan import PlannerPlan
        from .planner_plan_details import PlannerPlanDetails
        from .planner_progress_task_board_task_format import PlannerProgressTaskBoardTaskFormat
        from .planner_task import PlannerTask
        from .planner_task_details import PlannerTaskDetails
        from .planner_user import PlannerUser
        from .plan_context_link import PlanContextLink
        from .task import Task
        from .task_history_item import TaskHistoryItem
        from .user_assignment import UserAssignment

        from .bucket import Bucket
        from .business_scenario_task import BusinessScenarioTask
        from .category_definition import CategoryDefinition
        from .checklist_item_v4 import ChecklistItemV4
        from .content_link import ContentLink
        from .custom_choice_option import CustomChoiceOption
        from .custom_field_definition import CustomFieldDefinition
        from .custom_field_value import CustomFieldValue
        from .dependency import Dependency
        from .entity import Entity
        from .goal import Goal
        from .history_item import HistoryItem
        from .plan import Plan
        from .planner_assigned_to_task_board_task_format import PlannerAssignedToTaskBoardTaskFormat
        from .planner_bucket import PlannerBucket
        from .planner_bucket_task_board_task_format import PlannerBucketTaskBoardTaskFormat
        from .planner_chat_message import PlannerChatMessage
        from .planner_goal import PlannerGoal
        from .planner_history_item import PlannerHistoryItem
        from .planner_plan import PlannerPlan
        from .planner_plan_details import PlannerPlanDetails
        from .planner_progress_task_board_task_format import PlannerProgressTaskBoardTaskFormat
        from .planner_task import PlannerTask
        from .planner_task_details import PlannerTaskDetails
        from .planner_user import PlannerUser
        from .plan_context_link import PlanContextLink
        from .task import Task
        from .task_history_item import TaskHistoryItem
        from .user_assignment import UserAssignment

        fields: dict[str, Callable[[Any], None]] = {
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
    

