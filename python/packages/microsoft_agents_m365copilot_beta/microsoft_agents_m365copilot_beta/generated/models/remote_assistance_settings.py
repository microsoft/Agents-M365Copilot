from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .remote_assistance_state import RemoteAssistanceState

from .entity import Entity

@dataclass
class RemoteAssistanceSettings(Entity, Parsable):
    """
    Remote assistance settings for the account
    """
    # Indicates if sessions to unenrolled devices are allowed for the account. This setting is configurable by the admin. Default value is false.
    allow_sessions_to_unenrolled_devices: Optional[bool] = None
    # Indicates if sessions to block chat function. This setting is configurable by the admin. Default value is false.
    block_chat: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # State of remote assistance for the account
    remote_assistance_state: Optional[RemoteAssistanceState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RemoteAssistanceSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RemoteAssistanceSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RemoteAssistanceSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .remote_assistance_state import RemoteAssistanceState

        from .entity import Entity
        from .remote_assistance_state import RemoteAssistanceState

        fields: dict[str, Callable[[Any], None]] = {
            "allowSessionsToUnenrolledDevices": lambda n : setattr(self, 'allow_sessions_to_unenrolled_devices', n.get_bool_value()),
            "blockChat": lambda n : setattr(self, 'block_chat', n.get_bool_value()),
            "remoteAssistanceState": lambda n : setattr(self, 'remote_assistance_state', n.get_enum_value(RemoteAssistanceState)),
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
        writer.write_bool_value("allowSessionsToUnenrolledDevices", self.allow_sessions_to_unenrolled_devices)
        writer.write_bool_value("blockChat", self.block_chat)
        writer.write_enum_value("remoteAssistanceState", self.remote_assistance_state)
    

