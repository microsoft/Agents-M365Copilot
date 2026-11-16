from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .local_connectivity_configuration import LocalConnectivityConfiguration
    from .peer_connectivity_configuration import PeerConnectivityConfiguration

from ..entity import Entity

@dataclass
class ConnectivityConfigurationLink(Entity, Parsable):
    # Specifies the name of the link.
    display_name: Optional[str] = None
    # Specifies Microsoft's end of the tunnel configuration for a device link.
    local_configurations: Optional[list[LocalConnectivityConfiguration]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The peerConfiguration property
    peer_configuration: Optional[PeerConnectivityConfiguration] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ConnectivityConfigurationLink:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConnectivityConfigurationLink
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ConnectivityConfigurationLink()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .local_connectivity_configuration import LocalConnectivityConfiguration
        from .peer_connectivity_configuration import PeerConnectivityConfiguration

        from ..entity import Entity
        from .local_connectivity_configuration import LocalConnectivityConfiguration
        from .peer_connectivity_configuration import PeerConnectivityConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "localConfigurations": lambda n : setattr(self, 'local_configurations', n.get_collection_of_object_values(LocalConnectivityConfiguration)),
            "peerConfiguration": lambda n : setattr(self, 'peer_configuration', n.get_object_value(PeerConnectivityConfiguration)),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("localConfigurations", self.local_configurations)
        writer.write_object_value("peerConfiguration", self.peer_configuration)
    

