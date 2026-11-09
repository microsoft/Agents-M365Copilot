from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_event_handler_result import AuthenticationEventHandlerResult

from .authentication_event_handler_result import AuthenticationEventHandlerResult

@dataclass
class CustomExtensionCalloutResult(AuthenticationEventHandlerResult, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.customExtensionCalloutResult"
    # When the API transaction was initiated, the date and time information uses ISO 8601 format and is always in UTC time. Example: midnight on Jan 1, 2014, is reported as 2014-01-01T00:00:00Z.
    callout_date_time: Optional[datetime.datetime] = None
    # Identifier of the custom extension that was called.
    custom_extension_id: Optional[str] = None
    # Error code that was returned when the last API attempt failed.
    error_code: Optional[int] = None
    # The HTTP status code that was returned by the target API endpoint after the last API attempt.
    http_status: Optional[int] = None
    # The number of API calls to the customer's API.
    number_of_attempts: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomExtensionCalloutResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomExtensionCalloutResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomExtensionCalloutResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_event_handler_result import AuthenticationEventHandlerResult

        from .authentication_event_handler_result import AuthenticationEventHandlerResult

        fields: dict[str, Callable[[Any], None]] = {
            "calloutDateTime": lambda n : setattr(self, 'callout_date_time', n.get_datetime_value()),
            "customExtensionId": lambda n : setattr(self, 'custom_extension_id', n.get_str_value()),
            "errorCode": lambda n : setattr(self, 'error_code', n.get_int_value()),
            "httpStatus": lambda n : setattr(self, 'http_status', n.get_int_value()),
            "numberOfAttempts": lambda n : setattr(self, 'number_of_attempts', n.get_int_value()),
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
        writer.write_datetime_value("calloutDateTime", self.callout_date_time)
        writer.write_str_value("customExtensionId", self.custom_extension_id)
        writer.write_int_value("errorCode", self.error_code)
        writer.write_int_value("httpStatus", self.http_status)
        writer.write_int_value("numberOfAttempts", self.number_of_attempts)
    

