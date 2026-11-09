from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_on_premises_connection_health_check_error_type import CloudPcOnPremisesConnectionHealthCheckErrorType
    from .cloud_pc_on_premises_connection_status import CloudPcOnPremisesConnectionStatus

@dataclass
class CloudPcOnPremisesConnectionHealthCheck(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # More details about the health check or the recommended action. Read-only.
    additional_detail: Optional[str] = None
    # More details about the health check or the recommended action. Read-only. The additionalDetails property is deprecated and stopped returning data on January 31, 2024. Goind forward, use the additionalDetail property.
    additional_details: Optional[str] = None
    # The unique identifier of the health check item-related activities. This identifier can be useful in troubleshooting.
    correlation_id: Optional[str] = None
    # The display name for this health check item.
    display_name: Optional[str] = None
    # The end time of the health check item. Read-only.
    end_date_time: Optional[datetime.datetime] = None
    # The type of error that occurred during this health check.
    error_type: Optional[CloudPcOnPremisesConnectionHealthCheckErrorType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The recommended action to fix the corresponding error.
    recommended_action: Optional[str] = None
    # The start time of the health check item. Read-only.
    start_date_time: Optional[datetime.datetime] = None
    # The status property
    status: Optional[CloudPcOnPremisesConnectionStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcOnPremisesConnectionHealthCheck:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcOnPremisesConnectionHealthCheck
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcOnPremisesConnectionHealthCheck()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_on_premises_connection_health_check_error_type import CloudPcOnPremisesConnectionHealthCheckErrorType
        from .cloud_pc_on_premises_connection_status import CloudPcOnPremisesConnectionStatus

        from .cloud_pc_on_premises_connection_health_check_error_type import CloudPcOnPremisesConnectionHealthCheckErrorType
        from .cloud_pc_on_premises_connection_status import CloudPcOnPremisesConnectionStatus

        fields: dict[str, Callable[[Any], None]] = {
            "additionalDetail": lambda n : setattr(self, 'additional_detail', n.get_str_value()),
            "additionalDetails": lambda n : setattr(self, 'additional_details', n.get_str_value()),
            "correlationId": lambda n : setattr(self, 'correlation_id', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "errorType": lambda n : setattr(self, 'error_type', n.get_enum_value(CloudPcOnPremisesConnectionHealthCheckErrorType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recommendedAction": lambda n : setattr(self, 'recommended_action', n.get_str_value()),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(CloudPcOnPremisesConnectionStatus)),
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
        writer.write_str_value("additionalDetail", self.additional_detail)
        writer.write_str_value("additionalDetails", self.additional_details)
        writer.write_str_value("correlationId", self.correlation_id)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_enum_value("errorType", self.error_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("recommendedAction", self.recommended_action)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

