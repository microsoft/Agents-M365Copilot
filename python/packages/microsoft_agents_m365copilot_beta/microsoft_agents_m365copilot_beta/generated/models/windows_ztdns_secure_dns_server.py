from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .windows_ztdns_secure_dns_server_dns_over_https_configuration import WindowsZtdnsSecureDnsServerDnsOverHttpsConfiguration
    from .windows_ztdns_secure_dns_server_dns_over_tls_configuration import WindowsZtdnsSecureDnsServerDnsOverTlsConfiguration

@dataclass
class WindowsZtdnsSecureDnsServer(AdditionalDataHolder, Parsable):
    """
    Trusted DNS server configuration for Zero Trust DNS
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Name assigned to the trusted server entry
    display_name: Optional[str] = None
    # DNS over HTTPS (DoH) configuration settings for the secure DNS server
    dns_over_https_configuration: Optional[WindowsZtdnsSecureDnsServerDnsOverHttpsConfiguration] = None
    # DNS over TLS (DoT) configuration settings for the secure DNS server
    dns_over_tls_configuration: Optional[WindowsZtdnsSecureDnsServerDnsOverTlsConfiguration] = None
    # IP address of a trusted DNS server for ZTDNS (IPv4 or IPv6)
    ip_address: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsZtdnsSecureDnsServer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsZtdnsSecureDnsServer
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsZtdnsSecureDnsServer()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .windows_ztdns_secure_dns_server_dns_over_https_configuration import WindowsZtdnsSecureDnsServerDnsOverHttpsConfiguration
        from .windows_ztdns_secure_dns_server_dns_over_tls_configuration import WindowsZtdnsSecureDnsServerDnsOverTlsConfiguration

        from .windows_ztdns_secure_dns_server_dns_over_https_configuration import WindowsZtdnsSecureDnsServerDnsOverHttpsConfiguration
        from .windows_ztdns_secure_dns_server_dns_over_tls_configuration import WindowsZtdnsSecureDnsServerDnsOverTlsConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "dnsOverHttpsConfiguration": lambda n : setattr(self, 'dns_over_https_configuration', n.get_object_value(WindowsZtdnsSecureDnsServerDnsOverHttpsConfiguration)),
            "dnsOverTlsConfiguration": lambda n : setattr(self, 'dns_over_tls_configuration', n.get_object_value(WindowsZtdnsSecureDnsServerDnsOverTlsConfiguration)),
            "ipAddress": lambda n : setattr(self, 'ip_address', n.get_str_value()),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("dnsOverHttpsConfiguration", self.dns_over_https_configuration)
        writer.write_object_value("dnsOverTlsConfiguration", self.dns_over_tls_configuration)
        writer.write_str_value("ipAddress", self.ip_address)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

