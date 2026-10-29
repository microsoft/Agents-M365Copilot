from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .lifecycle_policy_scope_processing_attempt import LifecyclePolicyScopeProcessingAttempt
    from .lifecycle_policy_scope_processing_status import LifecyclePolicyScopeProcessingStatus

@dataclass
class LifecyclePolicyScopeProcessing(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The date and time when the current scope-processing operation started.
    current_started_date_time: Optional[datetime.datetime] = None
    # The currentStatus property
    current_status: Optional[LifecyclePolicyScopeProcessingStatus] = None
    # The date and time when scope processing last completed successfully.
    last_successful_processing_date_time: Optional[datetime.datetime] = None
    # The latest retained scope-processing attempt.
    latest_attempt: Optional[LifecyclePolicyScopeProcessingAttempt] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LifecyclePolicyScopeProcessing:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LifecyclePolicyScopeProcessing
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LifecyclePolicyScopeProcessing()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .lifecycle_policy_scope_processing_attempt import LifecyclePolicyScopeProcessingAttempt
        from .lifecycle_policy_scope_processing_status import LifecyclePolicyScopeProcessingStatus

        from .lifecycle_policy_scope_processing_attempt import LifecyclePolicyScopeProcessingAttempt
        from .lifecycle_policy_scope_processing_status import LifecyclePolicyScopeProcessingStatus

        fields: dict[str, Callable[[Any], None]] = {
            "currentStartedDateTime": lambda n : setattr(self, 'current_started_date_time', n.get_datetime_value()),
            "currentStatus": lambda n : setattr(self, 'current_status', n.get_enum_value(LifecyclePolicyScopeProcessingStatus)),
            "lastSuccessfulProcessingDateTime": lambda n : setattr(self, 'last_successful_processing_date_time', n.get_datetime_value()),
            "latestAttempt": lambda n : setattr(self, 'latest_attempt', n.get_object_value(LifecyclePolicyScopeProcessingAttempt)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_datetime_value("currentStartedDateTime", self.current_started_date_time)
        writer.write_enum_value("currentStatus", self.current_status)
        writer.write_datetime_value("lastSuccessfulProcessingDateTime", self.last_successful_processing_date_time)
        writer.write_object_value("latestAttempt", self.latest_attempt)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

