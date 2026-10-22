from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TeamworkNetworkConfiguration(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The default gateway is the path used to pass information when the destination is unknown to the device.
    default_gateway: Optional[str] = None
    # The network domain of the device, for example, contoso.com.
    domain_name: Optional[str] = None
    # The device name on a network.
    host_name: Optional[str] = None
    # The IP address is a numerical label that uniquely identifies every device connected to the internet.
    ip_address: Optional[str] = None
    # True if DHCP is enabled.
    is_dhcp_enabled: Optional[bool] = None
    # True if the PC port is enabled.
    is_p_c_port_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A primary DNS is the first point of contact for a device that translates the hostname into an IP address.
    primary_dns: Optional[str] = None
    # A secondary DNS is used when the primary DNS is not available.
    secondary_dns: Optional[str] = None
    # A subnet mask is a number that distinguishes the network address and the host address within an IP address.
    subnet_mask: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamworkNetworkConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkNetworkConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TeamworkNetworkConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "defaultGateway": lambda n : setattr(self, 'default_gateway', n.get_str_value()),
            "domainName": lambda n : setattr(self, 'domain_name', n.get_str_value()),
            "hostName": lambda n : setattr(self, 'host_name', n.get_str_value()),
            "ipAddress": lambda n : setattr(self, 'ip_address', n.get_str_value()),
            "isDhcpEnabled": lambda n : setattr(self, 'is_dhcp_enabled', n.get_bool_value()),
            "isPCPortEnabled": lambda n : setattr(self, 'is_p_c_port_enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "primaryDns": lambda n : setattr(self, 'primary_dns', n.get_str_value()),
            "secondaryDns": lambda n : setattr(self, 'secondary_dns', n.get_str_value()),
            "subnetMask": lambda n : setattr(self, 'subnet_mask', n.get_str_value()),
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
        writer.write_str_value("defaultGateway", self.default_gateway)
        writer.write_str_value("domainName", self.domain_name)
        writer.write_str_value("hostName", self.host_name)
        writer.write_str_value("ipAddress", self.ip_address)
        writer.write_bool_value("isDhcpEnabled", self.is_dhcp_enabled)
        writer.write_bool_value("isPCPortEnabled", self.is_p_c_port_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("primaryDns", self.primary_dns)
        writer.write_str_value("secondaryDns", self.secondary_dns)
        writer.write_str_value("subnetMask", self.subnet_mask)
        writer.write_additional_data_value(self.additional_data)
    

