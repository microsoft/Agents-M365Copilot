from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .sign_in_status import SignInStatus

from .entity import Entity

@dataclass
class ApplicationSignInDetailedSummary(Entity, Parsable):
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    aggregated_event_date_time: Optional[datetime.datetime] = None
    # Name of the application that the user signed in to.
    app_display_name: Optional[str] = None
    # ID of the application that the user signed in to.
    app_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Count of sign-ins made by the application.
    sign_in_count: Optional[int] = None
    # Details of the sign-in status.
    status: Optional[SignInStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ApplicationSignInDetailedSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ApplicationSignInDetailedSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ApplicationSignInDetailedSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .sign_in_status import SignInStatus

        from .entity import Entity
        from .sign_in_status import SignInStatus

        fields: dict[str, Callable[[Any], None]] = {
            "aggregatedEventDateTime": lambda n : setattr(self, 'aggregated_event_date_time', n.get_datetime_value()),
            "appDisplayName": lambda n : setattr(self, 'app_display_name', n.get_str_value()),
            "appId": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "signInCount": lambda n : setattr(self, 'sign_in_count', n.get_int_value()),
            "status": lambda n : setattr(self, 'status', n.get_object_value(SignInStatus)),
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
        writer.write_datetime_value("aggregatedEventDateTime", self.aggregated_event_date_time)
        writer.write_str_value("appDisplayName", self.app_display_name)
        writer.write_str_value("appId", self.app_id)
        writer.write_int_value("signInCount", self.sign_in_count)
        writer.write_object_value("status", self.status)
    

