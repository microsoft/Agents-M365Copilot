from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_firewall_destination_matching import CloudFirewallDestinationMatching
    from .cloud_firewall_source_matching import CloudFirewallSourceMatching

@dataclass
class CloudFirewallMatchingConditions(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Destination address, port, and protocol matching criteria. null means don't match on destination. Optional.
    destinations: Optional[CloudFirewallDestinationMatching] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Source address and port matching criteria. null means don't match on source. Optional.
    sources: Optional[CloudFirewallSourceMatching] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudFirewallMatchingConditions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudFirewallMatchingConditions
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudFirewallMatchingConditions()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_firewall_destination_matching import CloudFirewallDestinationMatching
        from .cloud_firewall_source_matching import CloudFirewallSourceMatching

        from .cloud_firewall_destination_matching import CloudFirewallDestinationMatching
        from .cloud_firewall_source_matching import CloudFirewallSourceMatching

        fields: dict[str, Callable[[Any], None]] = {
            "destinations": lambda n : setattr(self, 'destinations', n.get_object_value(CloudFirewallDestinationMatching)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sources": lambda n : setattr(self, 'sources', n.get_object_value(CloudFirewallSourceMatching)),
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
        writer.write_object_value("destinations", self.destinations)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("sources", self.sources)
        writer.write_additional_data_value(self.additional_data)
    

