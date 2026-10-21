from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .bucket import Bucket
    from .content_link import ContentLink
    from .content_sensitivity_label_assignment import ContentSensitivityLabelAssignment
    from .creation_info import CreationInfo
    from .custom_field_definition import CustomFieldDefinition
    from .dependency import Dependency
    from .extension_field_collection import ExtensionFieldCollection
    from .goal import Goal
    from .history_item import HistoryItem
    from .identity_set import IdentitySet
    from .planner_archival_info import PlannerArchivalInfo
    from .planner_delta import PlannerDelta
    from .planner_shared_with_container import PlannerSharedWithContainer
    from .plan_calendar import PlanCalendar
    from .plan_capability import PlanCapability
    from .plan_container import PlanContainer
    from .plan_context_link import PlanContextLink
    from .plan_view import PlanView
    from .task import Task

from .planner_delta import PlannerDelta

@dataclass
class Plan(PlannerDelta, Parsable):
    # Information about whether the entity is archived, and when it was archived.
    archival_info: Optional[PlannerArchivalInfo] = None
    # The collection of buckets in the plan. Read-only. Nullable.
    buckets: Optional[list[Bucket]] = None
    # Working-time calendar settings for the plan.
    calendar: Optional[PlanCalendar] = None
    # Server-computed, read-only capability flags indicating which optional features are enabled for the entity.
    capabilities: Optional[PlanCapability] = None
    # Identifies the group, Teams channel, or user that owns the plan. Required, and immutable after creation.
    container: Optional[PlanContainer] = None
    # The sensitivity label assigned to content associated with the plan.
    content_sensitivity_label_assignment: Optional[ContentSensitivityLabelAssignment] = None
    # The collection of context links describing where the plan is surfaced. Read-only. Nullable.
    contexts: Optional[list[PlanContextLink]] = None
    # Read-only creation metadata for the entity.
    creation_info: Optional[CreationInfo] = None
    # The collection of custom field definitions in the plan. Read-only. Nullable.
    custom_field_definitions: Optional[list[CustomFieldDefinition]] = None
    # The collection of dependencies between items in the plan. Read-only. Nullable.
    dependencies: Optional[list[Dependency]] = None
    # Title of the plan.
    display_name: Optional[str] = None
    # Duration of the plan, in days.
    duration: Optional[int] = None
    # Custom extension field values set on the entity. Supports $select.
    extensions: Optional[ExtensionFieldCollection] = None
    # The collection of goals in the plan. Read-only. Nullable.
    goals: Optional[list[Goal]] = None
    # Indicates whether the plan has an associated chat.
    has_chat: Optional[bool] = None
    # The collection of history (audit) items for the plan. Read-only. Nullable.
    history_items: Optional[list[HistoryItem]] = None
    # Identity of the user (or application) who last modified the entity. Read-only.
    last_modified_by: Optional[IdentitySet] = None
    # Date and time the entity was last modified. The value is represented in ISO 8601 format and is always in UTC time. Read-only.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The collection of content links attached to the plan. Read-only. Nullable.
    links: Optional[list[ContentLink]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Plan-scoped view settings, including category definitions.
    plan_view: Optional[PlanView] = None
    # The list of containers (for example, additional groups or channels) that the plan is shared with.
    shared_with_containers: Optional[list[PlannerSharedWithContainer]] = None
    # The collection of tasks in the plan. Read-only. Nullable.
    tasks: Optional[list[Task]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Plan:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Plan
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Plan()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .bucket import Bucket
        from .content_link import ContentLink
        from .content_sensitivity_label_assignment import ContentSensitivityLabelAssignment
        from .creation_info import CreationInfo
        from .custom_field_definition import CustomFieldDefinition
        from .dependency import Dependency
        from .extension_field_collection import ExtensionFieldCollection
        from .goal import Goal
        from .history_item import HistoryItem
        from .identity_set import IdentitySet
        from .planner_archival_info import PlannerArchivalInfo
        from .planner_delta import PlannerDelta
        from .planner_shared_with_container import PlannerSharedWithContainer
        from .plan_calendar import PlanCalendar
        from .plan_capability import PlanCapability
        from .plan_container import PlanContainer
        from .plan_context_link import PlanContextLink
        from .plan_view import PlanView
        from .task import Task

        from .bucket import Bucket
        from .content_link import ContentLink
        from .content_sensitivity_label_assignment import ContentSensitivityLabelAssignment
        from .creation_info import CreationInfo
        from .custom_field_definition import CustomFieldDefinition
        from .dependency import Dependency
        from .extension_field_collection import ExtensionFieldCollection
        from .goal import Goal
        from .history_item import HistoryItem
        from .identity_set import IdentitySet
        from .planner_archival_info import PlannerArchivalInfo
        from .planner_delta import PlannerDelta
        from .planner_shared_with_container import PlannerSharedWithContainer
        from .plan_calendar import PlanCalendar
        from .plan_capability import PlanCapability
        from .plan_container import PlanContainer
        from .plan_context_link import PlanContextLink
        from .plan_view import PlanView
        from .task import Task

        fields: dict[str, Callable[[Any], None]] = {
            "archivalInfo": lambda n : setattr(self, 'archival_info', n.get_object_value(PlannerArchivalInfo)),
            "buckets": lambda n : setattr(self, 'buckets', n.get_collection_of_object_values(Bucket)),
            "calendar": lambda n : setattr(self, 'calendar', n.get_object_value(PlanCalendar)),
            "capabilities": lambda n : setattr(self, 'capabilities', n.get_object_value(PlanCapability)),
            "container": lambda n : setattr(self, 'container', n.get_object_value(PlanContainer)),
            "contentSensitivityLabelAssignment": lambda n : setattr(self, 'content_sensitivity_label_assignment', n.get_object_value(ContentSensitivityLabelAssignment)),
            "contexts": lambda n : setattr(self, 'contexts', n.get_collection_of_object_values(PlanContextLink)),
            "creationInfo": lambda n : setattr(self, 'creation_info', n.get_object_value(CreationInfo)),
            "customFieldDefinitions": lambda n : setattr(self, 'custom_field_definitions', n.get_collection_of_object_values(CustomFieldDefinition)),
            "dependencies": lambda n : setattr(self, 'dependencies', n.get_collection_of_object_values(Dependency)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "duration": lambda n : setattr(self, 'duration', n.get_int_value()),
            "extensions": lambda n : setattr(self, 'extensions', n.get_object_value(ExtensionFieldCollection)),
            "goals": lambda n : setattr(self, 'goals', n.get_collection_of_object_values(Goal)),
            "hasChat": lambda n : setattr(self, 'has_chat', n.get_bool_value()),
            "historyItems": lambda n : setattr(self, 'history_items', n.get_collection_of_object_values(HistoryItem)),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "links": lambda n : setattr(self, 'links', n.get_collection_of_object_values(ContentLink)),
            "planView": lambda n : setattr(self, 'plan_view', n.get_object_value(PlanView)),
            "sharedWithContainers": lambda n : setattr(self, 'shared_with_containers', n.get_collection_of_object_values(PlannerSharedWithContainer)),
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
        writer.write_collection_of_object_values("buckets", self.buckets)
        writer.write_object_value("calendar", self.calendar)
        writer.write_object_value("container", self.container)
        writer.write_object_value("contentSensitivityLabelAssignment", self.content_sensitivity_label_assignment)
        writer.write_collection_of_object_values("contexts", self.contexts)
        writer.write_collection_of_object_values("customFieldDefinitions", self.custom_field_definitions)
        writer.write_collection_of_object_values("dependencies", self.dependencies)
        writer.write_str_value("displayName", self.display_name)
        writer.write_int_value("duration", self.duration)
        writer.write_object_value("extensions", self.extensions)
        writer.write_collection_of_object_values("goals", self.goals)
        writer.write_bool_value("hasChat", self.has_chat)
        writer.write_collection_of_object_values("historyItems", self.history_items)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_object_values("links", self.links)
        writer.write_object_value("planView", self.plan_view)
        writer.write_collection_of_object_values("sharedWithContainers", self.shared_with_containers)
        writer.write_collection_of_object_values("tasks", self.tasks)
    

