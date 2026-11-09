from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .audit_activity_initiator import AuditActivityInitiator
    from .entity import Entity
    from .key_value import KeyValue
    from .operation_result import OperationResult
    from .target_resource import TargetResource

from .entity import Entity

@dataclass
class CustomSecurityAttributeAudit(Entity, Parsable):
    # The activityDateTime property
    activity_date_time: Optional[datetime.datetime] = None
    # The activityDisplayName property
    activity_display_name: Optional[str] = None
    # The additionalDetails property
    additional_details: Optional[list[KeyValue]] = None
    # The category property
    category: Optional[str] = None
    # The correlationId property
    correlation_id: Optional[str] = None
    # The initiatedBy property
    initiated_by: Optional[AuditActivityInitiator] = None
    # The loggedByService property
    logged_by_service: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The operationType property
    operation_type: Optional[str] = None
    # The result property
    result: Optional[OperationResult] = None
    # The resultReason property
    result_reason: Optional[str] = None
    # The targetResources property
    target_resources: Optional[list[TargetResource]] = None
    # The userAgent property
    user_agent: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomSecurityAttributeAudit:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomSecurityAttributeAudit
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomSecurityAttributeAudit()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .audit_activity_initiator import AuditActivityInitiator
        from .entity import Entity
        from .key_value import KeyValue
        from .operation_result import OperationResult
        from .target_resource import TargetResource

        from .audit_activity_initiator import AuditActivityInitiator
        from .entity import Entity
        from .key_value import KeyValue
        from .operation_result import OperationResult
        from .target_resource import TargetResource

        fields: dict[str, Callable[[Any], None]] = {
            "activityDateTime": lambda n : setattr(self, 'activity_date_time', n.get_datetime_value()),
            "activityDisplayName": lambda n : setattr(self, 'activity_display_name', n.get_str_value()),
            "additionalDetails": lambda n : setattr(self, 'additional_details', n.get_collection_of_object_values(KeyValue)),
            "category": lambda n : setattr(self, 'category', n.get_str_value()),
            "correlationId": lambda n : setattr(self, 'correlation_id', n.get_str_value()),
            "initiatedBy": lambda n : setattr(self, 'initiated_by', n.get_object_value(AuditActivityInitiator)),
            "loggedByService": lambda n : setattr(self, 'logged_by_service', n.get_str_value()),
            "operationType": lambda n : setattr(self, 'operation_type', n.get_str_value()),
            "result": lambda n : setattr(self, 'result', n.get_enum_value(OperationResult)),
            "resultReason": lambda n : setattr(self, 'result_reason', n.get_str_value()),
            "targetResources": lambda n : setattr(self, 'target_resources', n.get_collection_of_object_values(TargetResource)),
            "userAgent": lambda n : setattr(self, 'user_agent', n.get_str_value()),
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
        writer.write_datetime_value("activityDateTime", self.activity_date_time)
        writer.write_str_value("activityDisplayName", self.activity_display_name)
        writer.write_collection_of_object_values("additionalDetails", self.additional_details)
        writer.write_str_value("category", self.category)
        writer.write_str_value("correlationId", self.correlation_id)
        writer.write_object_value("initiatedBy", self.initiated_by)
        writer.write_str_value("loggedByService", self.logged_by_service)
        writer.write_str_value("operationType", self.operation_type)
        writer.write_enum_value("result", self.result)
        writer.write_str_value("resultReason", self.result_reason)
        writer.write_collection_of_object_values("targetResources", self.target_resources)
        writer.write_str_value("userAgent", self.user_agent)
    

