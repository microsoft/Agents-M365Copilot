from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .remote_network_status import RemoteNetworkStatus

from ..entity import Entity

@dataclass
class RemoteNetworkHealthEvent(Entity, Parsable):
    # The number of BGP routes advertised through tunnel.
    bgp_routes_advertised_count: Optional[int] = None
    # The time of the original event generation in UTC. Supports $filter (ge, le) and $orderby.
    created_date_time: Optional[datetime.datetime] = None
    # The description of the event.
    description: Optional[str] = None
    # The IP address of the destination.
    destination_ip: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The number of bytes sent from the destination to the source.
    received_bytes: Optional[int] = None
    # A unique identifier for each remoteNetwork site. Supports $filter (eq).
    remote_network_id: Optional[str] = None
    # The number of bytes sent from the source to the destination for the connection or session.
    sent_bytes: Optional[int] = None
    # The public IP address.
    source_ip: Optional[str] = None
    # The status property
    status: Optional[RemoteNetworkStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RemoteNetworkHealthEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RemoteNetworkHealthEvent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RemoteNetworkHealthEvent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .remote_network_status import RemoteNetworkStatus

        from ..entity import Entity
        from .remote_network_status import RemoteNetworkStatus

        fields: dict[str, Callable[[Any], None]] = {
            "bgpRoutesAdvertisedCount": lambda n : setattr(self, 'bgp_routes_advertised_count', n.get_int_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "destinationIp": lambda n : setattr(self, 'destination_ip', n.get_str_value()),
            "receivedBytes": lambda n : setattr(self, 'received_bytes', n.get_int_value()),
            "remoteNetworkId": lambda n : setattr(self, 'remote_network_id', n.get_str_value()),
            "sentBytes": lambda n : setattr(self, 'sent_bytes', n.get_int_value()),
            "sourceIp": lambda n : setattr(self, 'source_ip', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(RemoteNetworkStatus)),
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
        writer.write_int_value("bgpRoutesAdvertisedCount", self.bgp_routes_advertised_count)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("destinationIp", self.destination_ip)
        writer.write_int_value("receivedBytes", self.received_bytes)
        writer.write_str_value("remoteNetworkId", self.remote_network_id)
        writer.write_int_value("sentBytes", self.sent_bytes)
        writer.write_str_value("sourceIp", self.source_ip)
        writer.write_enum_value("status", self.status)
    

