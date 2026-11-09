from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .extension_field_collection import ExtensionFieldCollection
    from .goal_capability import GoalCapability
    from .identity_set import IdentitySet
    from .item_body import ItemBody
    from .planner_archival_info import PlannerArchivalInfo
    from .planner_delta import PlannerDelta
    from .planner_goal_status import PlannerGoalStatus
    from .task import Task

from .planner_delta import PlannerDelta

@dataclass
class Goal(PlannerDelta, Parsable):
    # Information about whether the entity is archived, and when it was archived.
    archival_info: Optional[PlannerArchivalInfo] = None
    # Server-computed, read-only capability flags indicating which optional features are enabled for the entity.
    capabilities: Optional[GoalCapability] = None
    # Identity of the user (or application) who created the entity. Read-only.
    created_by: Optional[IdentitySet] = None
    # Date and time the entity was created. The value is represented in ISO 8601 format and is always in UTC time. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    # Title of the goal.
    display_name: Optional[str] = None
    # Custom extension field values set on the entity. Supports $select.
    extensions: Optional[ExtensionFieldCollection] = None
    # Date the goal is targeted to finish.
    finish_date: Optional[datetime.date] = None
    # Identity of the user (or application) who last modified the entity. Read-only.
    last_modified_by: Optional[IdentitySet] = None
    # Date and time the entity was last modified. The value is represented in ISO 8601 format and is always in UTC time. Read-only.
    last_modified_date_time: Optional[datetime.datetime] = None
    # Additional details or notes about the goal.
    notes: Optional[ItemBody] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # ID of the plan that contains the goal. Required, and immutable after creation.
    plan_id: Optional[str] = None
    # Priority of the goal.
    priority: Optional[int] = None
    # Date the goal starts.
    start_date: Optional[datetime.date] = None
    # Progress status of the goal. The possible values are: notStarted, onTrack, behind, atRisk, closed, unknownFutureValue.
    status: Optional[PlannerGoalStatus] = None
    # The collection of tasks associated with the goal. Read-only. Nullable.
    tasks: Optional[list[Task]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Goal:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Goal
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Goal()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .extension_field_collection import ExtensionFieldCollection
        from .goal_capability import GoalCapability
        from .identity_set import IdentitySet
        from .item_body import ItemBody
        from .planner_archival_info import PlannerArchivalInfo
        from .planner_delta import PlannerDelta
        from .planner_goal_status import PlannerGoalStatus
        from .task import Task

        from .extension_field_collection import ExtensionFieldCollection
        from .goal_capability import GoalCapability
        from .identity_set import IdentitySet
        from .item_body import ItemBody
        from .planner_archival_info import PlannerArchivalInfo
        from .planner_delta import PlannerDelta
        from .planner_goal_status import PlannerGoalStatus
        from .task import Task

        fields: dict[str, Callable[[Any], None]] = {
            "archivalInfo": lambda n : setattr(self, 'archival_info', n.get_object_value(PlannerArchivalInfo)),
            "capabilities": lambda n : setattr(self, 'capabilities', n.get_object_value(GoalCapability)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "extensions": lambda n : setattr(self, 'extensions', n.get_object_value(ExtensionFieldCollection)),
            "finishDate": lambda n : setattr(self, 'finish_date', n.get_date_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_object_value(ItemBody)),
            "planId": lambda n : setattr(self, 'plan_id', n.get_str_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "startDate": lambda n : setattr(self, 'start_date', n.get_date_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(PlannerGoalStatus)),
            "tasks": lambda n : setattr(self, 'tasks', n.get_collection_of_object_values(Task)),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("extensions", self.extensions)
        writer.write_date_value("finishDate", self.finish_date)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_object_value("notes", self.notes)
        writer.write_str_value("planId", self.plan_id)
        writer.write_int_value("priority", self.priority)
        writer.write_date_value("startDate", self.start_date)
        writer.write_enum_value("status", self.status)
        writer.write_collection_of_object_values("tasks", self.tasks)
    

