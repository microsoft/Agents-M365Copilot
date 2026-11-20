from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class NetworkInterface(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Description of the NIC (for example, Ethernet adapter, Wireless LAN adapter Local Area Connection, and so on).
    description: Optional[str] = None
    # Last IPv4 address associated with this NIC.
    ip_v4_address: Optional[str] = None
    # Last Public (also known as global) IPv6 address associated with this NIC.
    ip_v6_address: Optional[str] = None
    # Last local (link-local or site-local) IPv6 address associated with this NIC.
    local_ip_v6_address: Optional[str] = None
    # MAC address of the NIC on this host.
    mac_address: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> NetworkInterface:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: NetworkInterface
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return NetworkInterface()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "ipV4Address": lambda n : setattr(self, 'ip_v4_address', n.get_str_value()),
            "ipV6Address": lambda n : setattr(self, 'ip_v6_address', n.get_str_value()),
            "localIpV6Address": lambda n : setattr(self, 'local_ip_v6_address', n.get_str_value()),
            "macAddress": lambda n : setattr(self, 'mac_address', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_str_value("description", self.description)
        writer.write_str_value("ipV4Address", self.ip_v4_address)
        writer.write_str_value("ipV6Address", self.ip_v6_address)
        writer.write_str_value("localIpV6Address", self.local_ip_v6_address)
        writer.write_str_value("macAddress", self.mac_address)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

