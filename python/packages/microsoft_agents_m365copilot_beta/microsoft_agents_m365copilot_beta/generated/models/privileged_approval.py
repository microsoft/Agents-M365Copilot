from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .approval_state import ApprovalState
    from .entity import Entity
    from .privileged_role import PrivilegedRole
    from .privileged_role_assignment_request import PrivilegedRoleAssignmentRequest

from .entity import Entity

@dataclass
class PrivilegedApproval(Entity, Parsable):
    # The approvalDuration property
    approval_duration: Optional[datetime.timedelta] = None
    # The approvalState property
    approval_state: Optional[ApprovalState] = None
    # The approvalType property
    approval_type: Optional[str] = None
    # The approverReason property
    approver_reason: Optional[str] = None
    # The endDateTime property
    end_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The request property
    request: Optional[PrivilegedRoleAssignmentRequest] = None
    # The requestorReason property
    requestor_reason: Optional[str] = None
    # The roleId property
    role_id: Optional[str] = None
    # The roleInfo property
    role_info: Optional[PrivilegedRole] = None
    # The startDateTime property
    start_date_time: Optional[datetime.datetime] = None
    # The userId property
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PrivilegedApproval:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PrivilegedApproval
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PrivilegedApproval()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .approval_state import ApprovalState
        from .entity import Entity
        from .privileged_role import PrivilegedRole
        from .privileged_role_assignment_request import PrivilegedRoleAssignmentRequest

        from .approval_state import ApprovalState
        from .entity import Entity
        from .privileged_role import PrivilegedRole
        from .privileged_role_assignment_request import PrivilegedRoleAssignmentRequest

        fields: dict[str, Callable[[Any], None]] = {
            "approvalDuration": lambda n : setattr(self, 'approval_duration', n.get_timedelta_value()),
            "approvalState": lambda n : setattr(self, 'approval_state', n.get_enum_value(ApprovalState)),
            "approvalType": lambda n : setattr(self, 'approval_type', n.get_str_value()),
            "approverReason": lambda n : setattr(self, 'approver_reason', n.get_str_value()),
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "request": lambda n : setattr(self, 'request', n.get_object_value(PrivilegedRoleAssignmentRequest)),
            "requestorReason": lambda n : setattr(self, 'requestor_reason', n.get_str_value()),
            "roleId": lambda n : setattr(self, 'role_id', n.get_str_value()),
            "roleInfo": lambda n : setattr(self, 'role_info', n.get_object_value(PrivilegedRole)),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
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
        writer.write_timedelta_value("approvalDuration", self.approval_duration)
        writer.write_enum_value("approvalState", self.approval_state)
        writer.write_str_value("approvalType", self.approval_type)
        writer.write_str_value("approverReason", self.approver_reason)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_object_value("request", self.request)
        writer.write_str_value("requestorReason", self.requestor_reason)
        writer.write_str_value("roleId", self.role_id)
        writer.write_object_value("roleInfo", self.role_info)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_str_value("userId", self.user_id)
    

