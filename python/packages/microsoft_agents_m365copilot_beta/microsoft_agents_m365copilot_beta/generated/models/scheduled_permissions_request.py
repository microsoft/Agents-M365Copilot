from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .permissions_definition import PermissionsDefinition
    from .request_schedule import RequestSchedule
    from .status_detail import StatusDetail
    from .ticket_info import TicketInfo
    from .unified_role_schedule_request_actions import UnifiedRoleScheduleRequestActions

from .entity import Entity

@dataclass
class ScheduledPermissionsRequest(Entity, Parsable):
    # The action property
    action: Optional[UnifiedRoleScheduleRequestActions] = None
    # Defines when the identity created the request.
    created_date_time: Optional[datetime.datetime] = None
    # The identity's justification for the request.
    justification: Optional[str] = None
    # Additional context for the permissions request.
    notes: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The requestedPermissions property
    requested_permissions: Optional[PermissionsDefinition] = None
    # When to assign the requested permissions.
    schedule_info: Optional[RequestSchedule] = None
    # The statusDetail property
    status_detail: Optional[StatusDetail] = None
    # Ticketing-related metadata that you can use to correlate to the request.
    ticket_info: Optional[TicketInfo] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ScheduledPermissionsRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ScheduledPermissionsRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ScheduledPermissionsRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .permissions_definition import PermissionsDefinition
        from .request_schedule import RequestSchedule
        from .status_detail import StatusDetail
        from .ticket_info import TicketInfo
        from .unified_role_schedule_request_actions import UnifiedRoleScheduleRequestActions

        from .entity import Entity
        from .permissions_definition import PermissionsDefinition
        from .request_schedule import RequestSchedule
        from .status_detail import StatusDetail
        from .ticket_info import TicketInfo
        from .unified_role_schedule_request_actions import UnifiedRoleScheduleRequestActions

        fields: dict[str, Callable[[Any], None]] = {
            "action": lambda n : setattr(self, 'action', n.get_enum_value(UnifiedRoleScheduleRequestActions)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "justification": lambda n : setattr(self, 'justification', n.get_str_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_str_value()),
            "requestedPermissions": lambda n : setattr(self, 'requested_permissions', n.get_object_value(PermissionsDefinition)),
            "scheduleInfo": lambda n : setattr(self, 'schedule_info', n.get_object_value(RequestSchedule)),
            "statusDetail": lambda n : setattr(self, 'status_detail', n.get_enum_value(StatusDetail)),
            "ticketInfo": lambda n : setattr(self, 'ticket_info', n.get_object_value(TicketInfo)),
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
        writer.write_enum_value("action", self.action)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("justification", self.justification)
        writer.write_str_value("notes", self.notes)
        writer.write_object_value("requestedPermissions", self.requested_permissions)
        writer.write_object_value("scheduleInfo", self.schedule_info)
        writer.write_enum_value("statusDetail", self.status_detail)
        writer.write_object_value("ticketInfo", self.ticket_info)
    

