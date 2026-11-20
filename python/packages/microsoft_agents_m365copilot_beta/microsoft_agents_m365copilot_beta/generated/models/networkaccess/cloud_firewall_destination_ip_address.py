from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_firewall_destination_address import CloudFirewallDestinationAddress

from .cloud_firewall_destination_address import CloudFirewallDestinationAddress

@dataclass
class CloudFirewallDestinationIpAddress(CloudFirewallDestinationAddress, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.networkaccess.cloudFirewallDestinationIpAddress"
    # A collection of IP addresses. Supports IPv4, IPv6, CIDR notation (for example, 192.168.0.0/16), and IP ranges (for example, 172.16.0.0-172.16.255.255). The collection must not be empty. Required.
    values: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudFirewallDestinationIpAddress:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudFirewallDestinationIpAddress
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudFirewallDestinationIpAddress()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_firewall_destination_address import CloudFirewallDestinationAddress

        from .cloud_firewall_destination_address import CloudFirewallDestinationAddress

        fields: dict[str, Callable[[Any], None]] = {
            "values": lambda n : setattr(self, 'values', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_primitive_values("values", self.values)
    

