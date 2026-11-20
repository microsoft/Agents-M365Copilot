from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_firewall_source_address import CloudFirewallSourceAddress

@dataclass
class CloudFirewallSourceMatching(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The source addresses to match. An empty collection means don't filter by source addresses (match all). Required.
    addresses: Optional[list[CloudFirewallSourceAddress]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The source ports to match, for example, 80, 443, 1024-2048. An empty collection means don't filter by source ports (match all). Required.
    ports: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudFirewallSourceMatching:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudFirewallSourceMatching
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudFirewallSourceMatching()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_firewall_source_address import CloudFirewallSourceAddress

        from .cloud_firewall_source_address import CloudFirewallSourceAddress

        fields: dict[str, Callable[[Any], None]] = {
            "addresses": lambda n : setattr(self, 'addresses', n.get_collection_of_object_values(CloudFirewallSourceAddress)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "ports": lambda n : setattr(self, 'ports', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_object_values("addresses", self.addresses)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_primitive_values("ports", self.ports)
        writer.write_additional_data_value(self.additional_data)
    

