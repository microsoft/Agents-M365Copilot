from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .auto_admitted_users_type import AutoAdmittedUsersType

@dataclass
class MeetingCapability(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Indicates whether anonymous users dialout is allowed in a meeting.
    allow_anonymous_users_to_dial_out: Optional[bool] = None
    # Indicates whether anonymous users are allowed to start a meeting.
    allow_anonymous_users_to_start_meeting: Optional[bool] = None
    # The autoAdmittedUsers property
    auto_admitted_users: Optional[AutoAdmittedUsersType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MeetingCapability:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MeetingCapability
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MeetingCapability()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .auto_admitted_users_type import AutoAdmittedUsersType

        from .auto_admitted_users_type import AutoAdmittedUsersType

        fields: dict[str, Callable[[Any], None]] = {
            "allowAnonymousUsersToDialOut": lambda n : setattr(self, 'allow_anonymous_users_to_dial_out', n.get_bool_value()),
            "allowAnonymousUsersToStartMeeting": lambda n : setattr(self, 'allow_anonymous_users_to_start_meeting', n.get_bool_value()),
            "autoAdmittedUsers": lambda n : setattr(self, 'auto_admitted_users', n.get_enum_value(AutoAdmittedUsersType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_bool_value("allowAnonymousUsersToDialOut", self.allow_anonymous_users_to_dial_out)
        writer.write_bool_value("allowAnonymousUsersToStartMeeting", self.allow_anonymous_users_to_start_meeting)
        writer.write_enum_value("autoAdmittedUsers", self.auto_admitted_users)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

