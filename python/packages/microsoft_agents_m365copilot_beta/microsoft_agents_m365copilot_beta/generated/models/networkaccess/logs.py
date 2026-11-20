from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .connection import Connection
    from .generative_a_i_insight import GenerativeAIInsight
    from .network_access_traffic import NetworkAccessTraffic
    from .remote_network_health_event import RemoteNetworkHealthEvent

from ..entity import Entity

@dataclass
class Logs(Entity, Parsable):
    # An aggregated log entry that contains comprehensive information about network traffic events.
    connections: Optional[list[Connection]] = None
    # The generativeAIInsights property
    generative_a_i_insights: Optional[list[GenerativeAIInsight]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A collection of remote network health events.
    remote_networks: Optional[list[RemoteNetworkHealthEvent]] = None
    # A network access traffic log entry that contains comprehensive information about network traffic events.
    traffic: Optional[list[NetworkAccessTraffic]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Logs:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Logs
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Logs()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .connection import Connection
        from .generative_a_i_insight import GenerativeAIInsight
        from .network_access_traffic import NetworkAccessTraffic
        from .remote_network_health_event import RemoteNetworkHealthEvent

        from ..entity import Entity
        from .connection import Connection
        from .generative_a_i_insight import GenerativeAIInsight
        from .network_access_traffic import NetworkAccessTraffic
        from .remote_network_health_event import RemoteNetworkHealthEvent

        fields: dict[str, Callable[[Any], None]] = {
            "connections": lambda n : setattr(self, 'connections', n.get_collection_of_object_values(Connection)),
            "generativeAIInsights": lambda n : setattr(self, 'generative_a_i_insights', n.get_collection_of_object_values(GenerativeAIInsight)),
            "remoteNetworks": lambda n : setattr(self, 'remote_networks', n.get_collection_of_object_values(RemoteNetworkHealthEvent)),
            "traffic": lambda n : setattr(self, 'traffic', n.get_collection_of_object_values(NetworkAccessTraffic)),
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
        writer.write_collection_of_object_values("connections", self.connections)
        writer.write_collection_of_object_values("generativeAIInsights", self.generative_a_i_insights)
        writer.write_collection_of_object_values("remoteNetworks", self.remote_networks)
        writer.write_collection_of_object_values("traffic", self.traffic)
    

