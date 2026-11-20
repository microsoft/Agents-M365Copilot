from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .approval_operation_status import ApprovalOperationStatus
    from .entity import Entity
    from .public_error import PublicError

from .entity import Entity

@dataclass
class ApprovalOperation(Entity, Parsable):
    # The date and time when the operation was created.
    created_date_time: Optional[datetime.datetime] = None
    # The error if the operation failed.
    error: Optional[PublicError] = None
    # The date and time when this operation was most recently updated.
    last_action_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The URL for the resource that was newly created or acted upon.
    resource_location: Optional[str] = None
    # The status of the operation. The possible values are: scheduled, inProgress, succeeded, failed, timeout, unknownFutureValue.
    status: Optional[ApprovalOperationStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ApprovalOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ApprovalOperation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ApprovalOperation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .approval_operation_status import ApprovalOperationStatus
        from .entity import Entity
        from .public_error import PublicError

        from .approval_operation_status import ApprovalOperationStatus
        from .entity import Entity
        from .public_error import PublicError

        fields: dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "error": lambda n : setattr(self, 'error', n.get_object_value(PublicError)),
            "lastActionDateTime": lambda n : setattr(self, 'last_action_date_time', n.get_datetime_value()),
            "resourceLocation": lambda n : setattr(self, 'resource_location', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(ApprovalOperationStatus)),
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("error", self.error)
        writer.write_datetime_value("lastActionDateTime", self.last_action_date_time)
        writer.write_str_value("resourceLocation", self.resource_location)
        writer.write_enum_value("status", self.status)
    

