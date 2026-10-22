from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .reply_restriction import ReplyRestriction
    from .user_new_message_restriction import UserNewMessageRestriction

@dataclass
class ChannelModerationSettings(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Indicates whether bots are allowed to post messages.
    allow_new_message_from_bots: Optional[bool] = None
    # Indicates whether connectors are allowed to post messages.
    allow_new_message_from_connectors: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates who is allowed to reply to the teams channel. The possible values are: everyone, authorAndModerators, unknownFutureValue.
    reply_restriction: Optional[ReplyRestriction] = None
    # Indicates who is allowed to post messages to teams channel. The possible values are: everyone, everyoneExceptGuests, moderators, unknownFutureValue.
    user_new_message_restriction: Optional[UserNewMessageRestriction] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ChannelModerationSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ChannelModerationSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ChannelModerationSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .reply_restriction import ReplyRestriction
        from .user_new_message_restriction import UserNewMessageRestriction

        from .reply_restriction import ReplyRestriction
        from .user_new_message_restriction import UserNewMessageRestriction

        fields: dict[str, Callable[[Any], None]] = {
            "allowNewMessageFromBots": lambda n : setattr(self, 'allow_new_message_from_bots', n.get_bool_value()),
            "allowNewMessageFromConnectors": lambda n : setattr(self, 'allow_new_message_from_connectors', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "replyRestriction": lambda n : setattr(self, 'reply_restriction', n.get_enum_value(ReplyRestriction)),
            "userNewMessageRestriction": lambda n : setattr(self, 'user_new_message_restriction', n.get_enum_value(UserNewMessageRestriction)),
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
        writer.write_bool_value("allowNewMessageFromBots", self.allow_new_message_from_bots)
        writer.write_bool_value("allowNewMessageFromConnectors", self.allow_new_message_from_connectors)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("replyRestriction", self.reply_restriction)
        writer.write_enum_value("userNewMessageRestriction", self.user_new_message_restriction)
        writer.write_additional_data_value(self.additional_data)
    

