from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .identity import Identity
    from .identity_set import IdentitySet
    from .planner_delta import PlannerDelta
    from .user_assignment_capability import UserAssignmentCapability

from .planner_delta import PlannerDelta

@dataclass
class UserAssignment(PlannerDelta, Parsable):
    # Identity of the user (or application) that made the assignment.
    assigned_by: Optional[IdentitySet] = None
    # Date and time the assignment was made.
    assigned_date_time: Optional[datetime.datetime] = None
    # Server-computed, read-only capability flags indicating which optional features are enabled for the entity.
    capabilities: Optional[UserAssignmentCapability] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The user property
    user: Optional[Identity] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserAssignment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserAssignment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .identity import Identity
        from .identity_set import IdentitySet
        from .planner_delta import PlannerDelta
        from .user_assignment_capability import UserAssignmentCapability

        from .identity import Identity
        from .identity_set import IdentitySet
        from .planner_delta import PlannerDelta
        from .user_assignment_capability import UserAssignmentCapability

        fields: dict[str, Callable[[Any], None]] = {
            "assignedBy": lambda n : setattr(self, 'assigned_by', n.get_object_value(IdentitySet)),
            "assignedDateTime": lambda n : setattr(self, 'assigned_date_time', n.get_datetime_value()),
            "capabilities": lambda n : setattr(self, 'capabilities', n.get_object_value(UserAssignmentCapability)),
            "user": lambda n : setattr(self, 'user', n.get_object_value(Identity)),
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
        writer.write_object_value("assignedBy", self.assigned_by)
        writer.write_datetime_value("assignedDateTime", self.assigned_date_time)
        writer.write_object_value("user", self.user)
    

