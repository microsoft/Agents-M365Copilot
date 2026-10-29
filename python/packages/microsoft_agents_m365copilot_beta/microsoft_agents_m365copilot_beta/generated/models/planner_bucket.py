from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .planner_archival_info import PlannerArchivalInfo
    from .planner_bucket_creation import PlannerBucketCreation
    from .planner_delta import PlannerDelta
    from .planner_task import PlannerTask

from .planner_delta import PlannerDelta

@dataclass
class PlannerBucket(PlannerDelta, Parsable):
    # Read-only. Nullable. Contains information about who archived or unarchived the bucket and why.
    archival_info: Optional[PlannerArchivalInfo] = None
    # Contains information about the origin of the bucket.
    creation_source: Optional[PlannerBucketCreation] = None
    # Read-only. If set totrue, the bucket is archived. An archived bucket is read-only.
    is_archived: Optional[bool] = None
    # Name of the bucket.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Hint used to order items of this type in a list view. For details about the supported format, see Using order hints in Planner.
    order_hint: Optional[str] = None
    # Plan ID to which the bucket belongs.
    plan_id: Optional[str] = None
    # Read-only. Nullable. The collection of tasks in the bucket.
    tasks: Optional[list[PlannerTask]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlannerBucket:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlannerBucket
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PlannerBucket()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .planner_archival_info import PlannerArchivalInfo
        from .planner_bucket_creation import PlannerBucketCreation
        from .planner_delta import PlannerDelta
        from .planner_task import PlannerTask

        from .planner_archival_info import PlannerArchivalInfo
        from .planner_bucket_creation import PlannerBucketCreation
        from .planner_delta import PlannerDelta
        from .planner_task import PlannerTask

        fields: dict[str, Callable[[Any], None]] = {
            "archivalInfo": lambda n : setattr(self, 'archival_info', n.get_object_value(PlannerArchivalInfo)),
            "creationSource": lambda n : setattr(self, 'creation_source', n.get_object_value(PlannerBucketCreation)),
            "isArchived": lambda n : setattr(self, 'is_archived', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "orderHint": lambda n : setattr(self, 'order_hint', n.get_str_value()),
            "planId": lambda n : setattr(self, 'plan_id', n.get_str_value()),
            "tasks": lambda n : setattr(self, 'tasks', n.get_collection_of_object_values(PlannerTask)),
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
        writer.write_object_value("creationSource", self.creation_source)
        writer.write_bool_value("isArchived", self.is_archived)
        writer.write_str_value("name", self.name)
        writer.write_str_value("orderHint", self.order_hint)
        writer.write_str_value("planId", self.plan_id)
        writer.write_collection_of_object_values("tasks", self.tasks)
    

