from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .message_recipient import MessageRecipient

from .entity import Entity

@dataclass
class MessageTrace(Entity, Parsable):
    # The destinationIPAddress property
    destination_i_p_address: Optional[str] = None
    # The messageId property
    message_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The receivedDateTime property
    received_date_time: Optional[datetime.datetime] = None
    # The recipients property
    recipients: Optional[list[MessageRecipient]] = None
    # The senderEmail property
    sender_email: Optional[str] = None
    # The size property
    size: Optional[int] = None
    # The sourceIPAddress property
    source_i_p_address: Optional[str] = None
    # The subject property
    subject: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MessageTrace:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MessageTrace
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MessageTrace()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .message_recipient import MessageRecipient

        from .entity import Entity
        from .message_recipient import MessageRecipient

        fields: dict[str, Callable[[Any], None]] = {
            "destinationIPAddress": lambda n : setattr(self, 'destination_i_p_address', n.get_str_value()),
            "messageId": lambda n : setattr(self, 'message_id', n.get_str_value()),
            "receivedDateTime": lambda n : setattr(self, 'received_date_time', n.get_datetime_value()),
            "recipients": lambda n : setattr(self, 'recipients', n.get_collection_of_object_values(MessageRecipient)),
            "senderEmail": lambda n : setattr(self, 'sender_email', n.get_str_value()),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
            "sourceIPAddress": lambda n : setattr(self, 'source_i_p_address', n.get_str_value()),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
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
        writer.write_str_value("destinationIPAddress", self.destination_i_p_address)
        writer.write_str_value("messageId", self.message_id)
        writer.write_datetime_value("receivedDateTime", self.received_date_time)
        writer.write_collection_of_object_values("recipients", self.recipients)
        writer.write_str_value("senderEmail", self.sender_email)
        writer.write_int_value("size", self.size)
        writer.write_str_value("sourceIPAddress", self.source_i_p_address)
        writer.write_str_value("subject", self.subject)
    

