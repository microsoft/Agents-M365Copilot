from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .custom_emoji_from_identity_set import CustomEmojiFromIdentitySet
    from .entity import Entity

from .entity import Entity

@dataclass
class TeamworkCustomEmoji(Entity, Parsable):
    # The base64-encoded image content of the emoji. Supported formats include PNG and GIF.
    content_bytes: Optional[str] = None
    # The createdBy property
    created_by: Optional[CustomEmojiFromIdentitySet] = None
    # The date and time when the emoji was created. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2024, is 2024-01-01T00:00:00Z.
    created_date_time: Optional[datetime.datetime] = None
    # The unique display name of the custom emoji. Key. Must be unique and must not conflict with existing emoji names.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamworkCustomEmoji:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkCustomEmoji
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TeamworkCustomEmoji()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .custom_emoji_from_identity_set import CustomEmojiFromIdentitySet
        from .entity import Entity

        from .custom_emoji_from_identity_set import CustomEmojiFromIdentitySet
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "contentBytes": lambda n : setattr(self, 'content_bytes', n.get_str_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(CustomEmojiFromIdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
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
        writer.write_str_value("contentBytes", self.content_bytes)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("displayName", self.display_name)
    

