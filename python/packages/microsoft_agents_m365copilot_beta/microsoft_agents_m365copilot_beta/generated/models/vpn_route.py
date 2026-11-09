from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class VpnRoute(AdditionalDataHolder, Parsable):
    """
    VPN Route definition.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Destination prefix (IPv4/v6 address).
    destination_prefix: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Prefix size. (1-32). Valid values 1 to 32
    prefix_size: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VpnRoute:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VpnRoute
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return VpnRoute()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "destinationPrefix": lambda n : setattr(self, 'destination_prefix', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "prefixSize": lambda n : setattr(self, 'prefix_size', n.get_int_value()),
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
        writer.write_str_value("destinationPrefix", self.destination_prefix)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("prefixSize", self.prefix_size)
        writer.write_additional_data_value(self.additional_data)
    

