from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .governance_schedule import GovernanceSchedule
    from .privileged_role import PrivilegedRole

from .entity import Entity

@dataclass
class PrivilegedRoleAssignmentRequest(Entity, Parsable):
    # The assignmentState property
    assignment_state: Optional[str] = None
    # The duration property
    duration: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The reason property
    reason: Optional[str] = None
    # The requestedDateTime property
    requested_date_time: Optional[datetime.datetime] = None
    # The roleId property
    role_id: Optional[str] = None
    # The roleInfo property
    role_info: Optional[PrivilegedRole] = None
    # The schedule property
    schedule: Optional[GovernanceSchedule] = None
    # The status property
    status: Optional[str] = None
    # The ticketNumber property
    ticket_number: Optional[str] = None
    # The ticketSystem property
    ticket_system: Optional[str] = None
    # The type property
    type: Optional[str] = None
    # The userId property
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PrivilegedRoleAssignmentRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PrivilegedRoleAssignmentRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PrivilegedRoleAssignmentRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .governance_schedule import GovernanceSchedule
        from .privileged_role import PrivilegedRole

        from .entity import Entity
        from .governance_schedule import GovernanceSchedule
        from .privileged_role import PrivilegedRole

        fields: dict[str, Callable[[Any], None]] = {
            "assignmentState": lambda n : setattr(self, 'assignment_state', n.get_str_value()),
            "duration": lambda n : setattr(self, 'duration', n.get_str_value()),
            "reason": lambda n : setattr(self, 'reason', n.get_str_value()),
            "requestedDateTime": lambda n : setattr(self, 'requested_date_time', n.get_datetime_value()),
            "roleId": lambda n : setattr(self, 'role_id', n.get_str_value()),
            "roleInfo": lambda n : setattr(self, 'role_info', n.get_object_value(PrivilegedRole)),
            "schedule": lambda n : setattr(self, 'schedule', n.get_object_value(GovernanceSchedule)),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "ticketNumber": lambda n : setattr(self, 'ticket_number', n.get_str_value()),
            "ticketSystem": lambda n : setattr(self, 'ticket_system', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
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
        writer.write_str_value("assignmentState", self.assignment_state)
        writer.write_str_value("duration", self.duration)
        writer.write_str_value("reason", self.reason)
        writer.write_datetime_value("requestedDateTime", self.requested_date_time)
        writer.write_str_value("roleId", self.role_id)
        writer.write_object_value("roleInfo", self.role_info)
        writer.write_object_value("schedule", self.schedule)
        writer.write_str_value("status", self.status)
        writer.write_str_value("ticketNumber", self.ticket_number)
        writer.write_str_value("ticketSystem", self.ticket_system)
        writer.write_str_value("type", self.type)
        writer.write_str_value("userId", self.user_id)
    

