from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .email_address import EmailAddress
    from .entity import Entity

from .entity import Entity

@dataclass
class Mention(Entity, Parsable):
    # The name of the application where the mention is created. Optional. Not used and defaulted as null for message.
    application: Optional[str] = None
    # A unique identifier that represents a parent of the resource instance. Optional. Not used and defaulted as null for message.
    client_reference: Optional[str] = None
    # The email information of the user who made the mention.
    created_by: Optional[EmailAddress] = None
    # The date and time that the mention is created on the client.
    created_date_time: Optional[datetime.datetime] = None
    # A deep web link to the context of the mention in the resource instance. Optional. Not used and defaulted as null for message.
    deep_link: Optional[str] = None
    # Optional. Not used and defaulted as null for message. To get the mentions in a message, see the bodyPreview property of the message instead.
    mention_text: Optional[str] = None
    # The mentioned property
    mentioned: Optional[EmailAddress] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The date and time that the mention is created on the server. Optional. Not used and defaulted as null for message.
    server_created_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Mention:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Mention
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Mention()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .email_address import EmailAddress
        from .entity import Entity

        from .email_address import EmailAddress
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "application": lambda n : setattr(self, 'application', n.get_str_value()),
            "clientReference": lambda n : setattr(self, 'client_reference', n.get_str_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(EmailAddress)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "deepLink": lambda n : setattr(self, 'deep_link', n.get_str_value()),
            "mentionText": lambda n : setattr(self, 'mention_text', n.get_str_value()),
            "mentioned": lambda n : setattr(self, 'mentioned', n.get_object_value(EmailAddress)),
            "serverCreatedDateTime": lambda n : setattr(self, 'server_created_date_time', n.get_datetime_value()),
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
        writer.write_str_value("application", self.application)
        writer.write_str_value("clientReference", self.client_reference)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("deepLink", self.deep_link)
        writer.write_str_value("mentionText", self.mention_text)
        writer.write_object_value("mentioned", self.mentioned)
        writer.write_datetime_value("serverCreatedDateTime", self.server_created_date_time)
    

