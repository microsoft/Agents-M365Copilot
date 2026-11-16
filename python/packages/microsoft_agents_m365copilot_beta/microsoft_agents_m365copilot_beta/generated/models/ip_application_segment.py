from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .action_type import ActionType
    from .application import Application
    from .application_segment import ApplicationSegment
    from .private_network_destination_type import PrivateNetworkDestinationType
    from .private_network_protocol import PrivateNetworkProtocol

from .application_segment import ApplicationSegment

@dataclass
class IpApplicationSegment(ApplicationSegment, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.ipApplicationSegment"
    # The action property
    action: Optional[ActionType] = None
    # The on-premises nonweb application published through Microsoft Entra application proxy. Expanded by default and supports $expand.
    application: Optional[Application] = None
    # Either the IP address, IP range, or FQDN of the applicationSegment, with or without wildcards.
    destination_host: Optional[str] = None
    # The possible values are: ipAddress, ipRange, ipRangeCidr, fqdn, dnsSuffix, unknownFutureValue.
    destination_type: Optional[PrivateNetworkDestinationType] = None
    # Port supported for the application segment. DO NOT USE.
    port: Optional[int] = None
    # List of ports supported for the application segment.
    ports: Optional[list[str]] = None
    # Indicates the protocol of the network traffic acquired for the application segment. The possible values are: tcp, udp, unknownFutureValue.
    protocol: Optional[PrivateNetworkProtocol] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IpApplicationSegment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IpApplicationSegment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IpApplicationSegment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .action_type import ActionType
        from .application import Application
        from .application_segment import ApplicationSegment
        from .private_network_destination_type import PrivateNetworkDestinationType
        from .private_network_protocol import PrivateNetworkProtocol

        from .action_type import ActionType
        from .application import Application
        from .application_segment import ApplicationSegment
        from .private_network_destination_type import PrivateNetworkDestinationType
        from .private_network_protocol import PrivateNetworkProtocol

        fields: dict[str, Callable[[Any], None]] = {
            "action": lambda n : setattr(self, 'action', n.get_enum_value(ActionType)),
            "application": lambda n : setattr(self, 'application', n.get_object_value(Application)),
            "destinationHost": lambda n : setattr(self, 'destination_host', n.get_str_value()),
            "destinationType": lambda n : setattr(self, 'destination_type', n.get_enum_value(PrivateNetworkDestinationType)),
            "port": lambda n : setattr(self, 'port', n.get_int_value()),
            "ports": lambda n : setattr(self, 'ports', n.get_collection_of_primitive_values(str)),
            "protocol": lambda n : setattr(self, 'protocol', n.get_collection_of_enum_values(PrivateNetworkProtocol)),
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
        writer.write_enum_value("action", self.action)
        writer.write_object_value("application", self.application)
        writer.write_str_value("destinationHost", self.destination_host)
        writer.write_enum_value("destinationType", self.destination_type)
        writer.write_int_value("port", self.port)
        writer.write_collection_of_primitive_values("ports", self.ports)
        writer.write_enum_value("protocol", self.protocol)
    

