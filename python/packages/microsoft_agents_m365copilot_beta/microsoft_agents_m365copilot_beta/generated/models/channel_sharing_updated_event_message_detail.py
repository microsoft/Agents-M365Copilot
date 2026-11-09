from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .event_message_detail import EventMessageDetail
    from .identity_set import IdentitySet

from .event_message_detail import EventMessageDetail

@dataclass
class ChannelSharingUpdatedEventMessageDetail(EventMessageDetail, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.channelSharingUpdatedEventMessageDetail"
    # Initiator of the event.
    initiator: Optional[IdentitySet] = None
    # The ID of the team to which the shared channel belongs.
    owner_team_id: Optional[str] = None
    # The ID of the tenant to which the shared channel belongs.
    owner_tenant_id: Optional[str] = None
    # The ID of the shared channel.
    shared_channel_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ChannelSharingUpdatedEventMessageDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ChannelSharingUpdatedEventMessageDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ChannelSharingUpdatedEventMessageDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .event_message_detail import EventMessageDetail
        from .identity_set import IdentitySet

        from .event_message_detail import EventMessageDetail
        from .identity_set import IdentitySet

        fields: dict[str, Callable[[Any], None]] = {
            "initiator": lambda n : setattr(self, 'initiator', n.get_object_value(IdentitySet)),
            "ownerTeamId": lambda n : setattr(self, 'owner_team_id', n.get_str_value()),
            "ownerTenantId": lambda n : setattr(self, 'owner_tenant_id', n.get_str_value()),
            "sharedChannelId": lambda n : setattr(self, 'shared_channel_id', n.get_str_value()),
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
        writer.write_object_value("initiator", self.initiator)
        writer.write_str_value("ownerTeamId", self.owner_team_id)
        writer.write_str_value("ownerTenantId", self.owner_tenant_id)
        writer.write_str_value("sharedChannelId", self.shared_channel_id)
    

