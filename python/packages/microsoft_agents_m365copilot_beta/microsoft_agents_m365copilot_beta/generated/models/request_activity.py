from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class RequestActivity(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The action property
    action: Optional[str] = None
    # The actionDateTime property
    action_date_time: Optional[datetime.datetime] = None
    # The detail property
    detail: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The scheduledDateTime property
    scheduled_date_time: Optional[datetime.datetime] = None
    # The userDisplayName property
    user_display_name: Optional[str] = None
    # The userPrincipalName property
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RequestActivity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RequestActivity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RequestActivity()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "action": lambda n : setattr(self, 'action', n.get_str_value()),
            "actionDateTime": lambda n : setattr(self, 'action_date_time', n.get_datetime_value()),
            "detail": lambda n : setattr(self, 'detail', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "scheduledDateTime": lambda n : setattr(self, 'scheduled_date_time', n.get_datetime_value()),
            "userDisplayName": lambda n : setattr(self, 'user_display_name', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
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
        writer.write_str_value("action", self.action)
        writer.write_datetime_value("actionDateTime", self.action_date_time)
        writer.write_str_value("detail", self.detail)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_datetime_value("scheduledDateTime", self.scheduled_date_time)
        writer.write_str_value("userDisplayName", self.user_display_name)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_additional_data_value(self.additional_data)
    

