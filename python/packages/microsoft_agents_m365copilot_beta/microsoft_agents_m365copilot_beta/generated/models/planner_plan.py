from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .content_sensitivity_label_assignment import ContentSensitivityLabelAssignment
    from .identity_set import IdentitySet
    from .planner_archival_info import PlannerArchivalInfo
    from .planner_bucket import PlannerBucket
    from .planner_delta import PlannerDelta
    from .planner_goal import PlannerGoal
    from .planner_history_item import PlannerHistoryItem
    from .planner_plan_container import PlannerPlanContainer
    from .planner_plan_context_collection import PlannerPlanContextCollection
    from .planner_plan_creation import PlannerPlanCreation
    from .planner_plan_details import PlannerPlanDetails
    from .planner_shared_with_container import PlannerSharedWithContainer
    from .planner_task import PlannerTask

from .planner_delta import PlannerDelta

@dataclass
class PlannerPlan(PlannerDelta, Parsable):
    # Read-only. Nullable. Contains information about who archived or unarchived the plan and why.
    archival_info: Optional[PlannerArchivalInfo] = None
    # Collection of buckets in the plan. Read-only. Nullable.
    buckets: Optional[list[PlannerBucket]] = None
    # Identifies the container of the plan. Either specify all properties, or specify only the url, the containerId, and type. After it's set, this property can’t be updated. It changes when a plan is moved from one container to another, using plan move to container. Required.
    container: Optional[PlannerPlanContainer] = None
    # The sensitivity label assignment for the plan. Used to classify and protect the plan content based on organizational policies. This property is null if no sensitivity label is assigned. Optional.
    content_sensitivity_label_assignment: Optional[ContentSensitivityLabelAssignment] = None
    # Read-only. Other user experiences in which this plan is used, represented as plannerPlanContext entries.
    contexts: Optional[PlannerPlanContextCollection] = None
    # Read-only. The user who created the plan.
    created_by: Optional[IdentitySet] = None
    # Read-only. Date and time at which the plan is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    created_date_time: Optional[datetime.datetime] = None
    # Contains information about the origin of the plan.
    creation_source: Optional[PlannerPlanCreation] = None
    # Extra details about the plan. Read-only. Nullable.
    details: Optional[PlannerPlanDetails] = None
    # Collection of goals in the plan. Read-only. Nullable.
    goals: Optional[list[PlannerGoal]] = None
    # Collection of history items for entities in the plan. Read-only. Nullable.
    history_items: Optional[list[PlannerHistoryItem]] = None
    # Read-only. If set to true, the plan is archived. An archived plan is read-only.
    is_archived: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Use the container property instead. ID of the group that owns the plan. After it's set, this property can’t be updated. This property doesn't return a valid group ID if the container of the plan isn't a group.
    owner: Optional[str] = None
    # List of containers the plan is shared with.
    shared_with_containers: Optional[list[PlannerSharedWithContainer]] = None
    # Collection of tasks in the plan. Read-only. Nullable.
    tasks: Optional[list[PlannerTask]] = None
    # Required. Title of the plan.
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlannerPlan:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlannerPlan
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PlannerPlan()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .content_sensitivity_label_assignment import ContentSensitivityLabelAssignment
        from .identity_set import IdentitySet
        from .planner_archival_info import PlannerArchivalInfo
        from .planner_bucket import PlannerBucket
        from .planner_delta import PlannerDelta
        from .planner_goal import PlannerGoal
        from .planner_history_item import PlannerHistoryItem
        from .planner_plan_container import PlannerPlanContainer
        from .planner_plan_context_collection import PlannerPlanContextCollection
        from .planner_plan_creation import PlannerPlanCreation
        from .planner_plan_details import PlannerPlanDetails
        from .planner_shared_with_container import PlannerSharedWithContainer
        from .planner_task import PlannerTask

        from .content_sensitivity_label_assignment import ContentSensitivityLabelAssignment
        from .identity_set import IdentitySet
        from .planner_archival_info import PlannerArchivalInfo
        from .planner_bucket import PlannerBucket
        from .planner_delta import PlannerDelta
        from .planner_goal import PlannerGoal
        from .planner_history_item import PlannerHistoryItem
        from .planner_plan_container import PlannerPlanContainer
        from .planner_plan_context_collection import PlannerPlanContextCollection
        from .planner_plan_creation import PlannerPlanCreation
        from .planner_plan_details import PlannerPlanDetails
        from .planner_shared_with_container import PlannerSharedWithContainer
        from .planner_task import PlannerTask

        fields: dict[str, Callable[[Any], None]] = {
            "archivalInfo": lambda n : setattr(self, 'archival_info', n.get_object_value(PlannerArchivalInfo)),
            "buckets": lambda n : setattr(self, 'buckets', n.get_collection_of_object_values(PlannerBucket)),
            "container": lambda n : setattr(self, 'container', n.get_object_value(PlannerPlanContainer)),
            "contentSensitivityLabelAssignment": lambda n : setattr(self, 'content_sensitivity_label_assignment', n.get_object_value(ContentSensitivityLabelAssignment)),
            "contexts": lambda n : setattr(self, 'contexts', n.get_object_value(PlannerPlanContextCollection)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "creationSource": lambda n : setattr(self, 'creation_source', n.get_object_value(PlannerPlanCreation)),
            "details": lambda n : setattr(self, 'details', n.get_object_value(PlannerPlanDetails)),
            "goals": lambda n : setattr(self, 'goals', n.get_collection_of_object_values(PlannerGoal)),
            "historyItems": lambda n : setattr(self, 'history_items', n.get_collection_of_object_values(PlannerHistoryItem)),
            "isArchived": lambda n : setattr(self, 'is_archived', n.get_bool_value()),
            "owner": lambda n : setattr(self, 'owner', n.get_str_value()),
            "sharedWithContainers": lambda n : setattr(self, 'shared_with_containers', n.get_collection_of_object_values(PlannerSharedWithContainer)),
            "tasks": lambda n : setattr(self, 'tasks', n.get_collection_of_object_values(PlannerTask)),
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
        writer.write_object_value("archivalInfo", self.archival_info)
        writer.write_collection_of_object_values("buckets", self.buckets)
        writer.write_object_value("container", self.container)
        writer.write_object_value("contentSensitivityLabelAssignment", self.content_sensitivity_label_assignment)
        writer.write_object_value("contexts", self.contexts)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("creationSource", self.creation_source)
        writer.write_object_value("details", self.details)
        writer.write_collection_of_object_values("goals", self.goals)
        writer.write_collection_of_object_values("historyItems", self.history_items)
        writer.write_bool_value("isArchived", self.is_archived)
        writer.write_str_value("owner", self.owner)
        writer.write_collection_of_object_values("sharedWithContainers", self.shared_with_containers)
        writer.write_collection_of_object_values("tasks", self.tasks)
        writer.write_str_value("title", self.title)
    

