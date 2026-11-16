from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..public_error import PublicError
    from .lifecycle_policy_scope_processing_attempt_status import LifecyclePolicyScopeProcessingAttemptStatus

@dataclass
class LifecyclePolicyScopeProcessingAttempt(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The date and time when the attempt completed.
    completed_date_time: Optional[datetime.datetime] = None
    # The error associated with an unsuccessful attempt.
    error: Optional[PublicError] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The date and time when the attempt started.
    started_date_time: Optional[datetime.datetime] = None
    # The status property
    status: Optional[LifecyclePolicyScopeProcessingAttemptStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LifecyclePolicyScopeProcessingAttempt:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LifecyclePolicyScopeProcessingAttempt
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LifecyclePolicyScopeProcessingAttempt()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..public_error import PublicError
        from .lifecycle_policy_scope_processing_attempt_status import LifecyclePolicyScopeProcessingAttemptStatus

        from ..public_error import PublicError
        from .lifecycle_policy_scope_processing_attempt_status import LifecyclePolicyScopeProcessingAttemptStatus

        fields: dict[str, Callable[[Any], None]] = {
            "completedDateTime": lambda n : setattr(self, 'completed_date_time', n.get_datetime_value()),
            "error": lambda n : setattr(self, 'error', n.get_object_value(PublicError)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "startedDateTime": lambda n : setattr(self, 'started_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(LifecyclePolicyScopeProcessingAttemptStatus)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_datetime_value("completedDateTime", self.completed_date_time)
        writer.write_object_value("error", self.error)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_datetime_value("startedDateTime", self.started_date_time)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

