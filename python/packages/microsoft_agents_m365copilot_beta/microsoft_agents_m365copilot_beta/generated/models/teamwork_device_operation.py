from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .identity_set import IdentitySet
    from .operation_error import OperationError
    from .teamwork_device_operation_type import TeamworkDeviceOperationType

from .entity import Entity

@dataclass
class TeamworkDeviceOperation(Entity, Parsable):
    # Time at which the operation reached a final state (for example, Successful, Failed, and Cancelled).
    completed_date_time: Optional[datetime.datetime] = None
    # Identity of the user who created the device operation.
    created_by: Optional[IdentitySet] = None
    # The UTC date and time when the device operation was created.
    created_date_time: Optional[datetime.datetime] = None
    # Error details are available only in case of a failed status.
    error: Optional[OperationError] = None
    # Identity of the user who last modified the device operation.
    last_action_by: Optional[IdentitySet] = None
    # The UTC date and time when the device operation was last modified.
    last_action_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The operationType property
    operation_type: Optional[TeamworkDeviceOperationType] = None
    # Time at which the operation was started.
    started_date_time: Optional[datetime.datetime] = None
    # The current status of the async operation, for example, Queued, Scheduled, InProgress,  Successful, Cancelled, and Failed.
    status: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamworkDeviceOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkDeviceOperation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TeamworkDeviceOperation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .identity_set import IdentitySet
        from .operation_error import OperationError
        from .teamwork_device_operation_type import TeamworkDeviceOperationType

        from .entity import Entity
        from .identity_set import IdentitySet
        from .operation_error import OperationError
        from .teamwork_device_operation_type import TeamworkDeviceOperationType

        fields: dict[str, Callable[[Any], None]] = {
            "completedDateTime": lambda n : setattr(self, 'completed_date_time', n.get_datetime_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "error": lambda n : setattr(self, 'error', n.get_object_value(OperationError)),
            "lastActionBy": lambda n : setattr(self, 'last_action_by', n.get_object_value(IdentitySet)),
            "lastActionDateTime": lambda n : setattr(self, 'last_action_date_time', n.get_datetime_value()),
            "operationType": lambda n : setattr(self, 'operation_type', n.get_enum_value(TeamworkDeviceOperationType)),
            "startedDateTime": lambda n : setattr(self, 'started_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
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
        writer.write_datetime_value("completedDateTime", self.completed_date_time)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("error", self.error)
        writer.write_object_value("lastActionBy", self.last_action_by)
        writer.write_datetime_value("lastActionDateTime", self.last_action_date_time)
        writer.write_enum_value("operationType", self.operation_type)
        writer.write_datetime_value("startedDateTime", self.started_date_time)
        writer.write_str_value("status", self.status)
    

