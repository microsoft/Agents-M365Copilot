from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .operation_status import OperationStatus

@dataclass
class SecurityActionState(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The Application ID of the calling application that submitted an update (PATCH) to the action. The appId should be extracted from the auth token and not entered manually by the calling application.
    app_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Status of the securityAction in this update. The possible values are: NotStarted, Running, Completed, Failed.
    status: Optional[OperationStatus] = None
    # Timestamp when the actionState was updated. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    updated_date_time: Optional[datetime.datetime] = None
    # The user principal name of the signed-in user that submitted an update (PATCH) to the action. The user should be extracted from the auth token and not entered manually by the calling application.
    user: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SecurityActionState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SecurityActionState
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SecurityActionState()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .operation_status import OperationStatus

        from .operation_status import OperationStatus

        fields: dict[str, Callable[[Any], None]] = {
            "appId": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(OperationStatus)),
            "updatedDateTime": lambda n : setattr(self, 'updated_date_time', n.get_datetime_value()),
            "user": lambda n : setattr(self, 'user', n.get_str_value()),
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
        writer.write_str_value("appId", self.app_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("status", self.status)
        writer.write_datetime_value("updatedDateTime", self.updated_date_time)
        writer.write_str_value("user", self.user)
        writer.write_additional_data_value(self.additional_data)
    

