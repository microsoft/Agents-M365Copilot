from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class CloudPCConnectivityIssue(Entity, Parsable):
    """
    The user experience analyte connectivity issue entity.
    """
    # The Intune DeviceId of the device the connection is associated with.
    device_id: Optional[str] = None
    # The error code of the connectivity issue.
    error_code: Optional[str] = None
    # The time that the connection initiated. The time is shown in ISO 8601 format and Coordinated Universal Time (UTC) time.
    error_date_time: Optional[datetime.datetime] = None
    # The detailed description of what went wrong.
    error_description: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The recommended action to fix the corresponding error.
    recommended_action: Optional[str] = None
    # The unique id of user who initialize the connection.
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPCConnectivityIssue:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPCConnectivityIssue
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPCConnectivityIssue()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "errorCode": lambda n : setattr(self, 'error_code', n.get_str_value()),
            "errorDateTime": lambda n : setattr(self, 'error_date_time', n.get_datetime_value()),
            "errorDescription": lambda n : setattr(self, 'error_description', n.get_str_value()),
            "recommendedAction": lambda n : setattr(self, 'recommended_action', n.get_str_value()),
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
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("errorCode", self.error_code)
        writer.write_datetime_value("errorDateTime", self.error_date_time)
        writer.write_str_value("errorDescription", self.error_description)
        writer.write_str_value("recommendedAction", self.recommended_action)
        writer.write_str_value("userId", self.user_id)
    

