from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_configuration import DeviceConfiguration
    from .extended_key_usage import ExtendedKeyUsage
    from .windows81_trusted_root_certificate import Windows81TrustedRootCertificate
    from .windows_ztdns_exemption_rule import WindowsZtdnsExemptionRule
    from .windows_ztdns_secure_dns_server import WindowsZtdnsSecureDnsServer

from .device_configuration import DeviceConfiguration

@dataclass
class WindowsZtdnsConfiguration(DeviceConfiguration, Parsable):
    """
    Windows Zero Trust DNS configuration profile
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsZtdnsConfiguration"
    # Indicates the audit operational mode. When true, unsecured traffic will be logged but not blocked. When false, unsecured DNS traffic will be blocked unless specifically exempted.
    audit_mode_enabled: Optional[bool] = None
    # Exemptions to the ZTDNS rules, allowing access to specific addresses or subnets via unsecured lookup. This collection can contain a maximum of 500 elements.
    exemption_rules: Optional[list[WindowsZtdnsExemptionRule]] = None
    # Extended key usage definitions for client authentication with secure DNS servers. This collection can contain a maximum of 500 elements.
    extended_key_usages_for_client_authentication: Optional[list[ExtendedKeyUsage]] = None
    # Indicates whether the DNS Client can resolve queries using the hosts file.
    hosts_file_resolution_enabled: Optional[bool] = None
    # Creates a localhost DNS server for securely forwarding plaintext queries to trusted DNS servers.
    loopback_dns_forwarder_enabled: Optional[bool] = None
    # Indicates whether traffic to loopback addresses should be blocked.
    loopback_traffic_blocked: Optional[bool] = None
    # Maximum time in seconds for which connections to an IP address will be allowed after successful name resolution. Valid values 30 to 604800
    maximum_connection_time_in_seconds: Optional[int] = None
    # Root certificates for client authentication. This collection can contain a maximum of 500 elements.
    root_certificates_for_client_validation: Optional[list[Windows81TrustedRootCertificate]] = None
    # Root certificates for server validation. This collection can contain a maximum of 500 elements.
    root_certificates_for_server_validation: Optional[list[Windows81TrustedRootCertificate]] = None
    # Collection of secure DNS servers used to resolve ZTDNS queries. Must contain at least one item. This collection can contain a maximum of 500 elements.
    secure_dns_servers: Optional[list[WindowsZtdnsSecureDnsServer]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsZtdnsConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsZtdnsConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsZtdnsConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_configuration import DeviceConfiguration
        from .extended_key_usage import ExtendedKeyUsage
        from .windows81_trusted_root_certificate import Windows81TrustedRootCertificate
        from .windows_ztdns_exemption_rule import WindowsZtdnsExemptionRule
        from .windows_ztdns_secure_dns_server import WindowsZtdnsSecureDnsServer

        from .device_configuration import DeviceConfiguration
        from .extended_key_usage import ExtendedKeyUsage
        from .windows81_trusted_root_certificate import Windows81TrustedRootCertificate
        from .windows_ztdns_exemption_rule import WindowsZtdnsExemptionRule
        from .windows_ztdns_secure_dns_server import WindowsZtdnsSecureDnsServer

        fields: dict[str, Callable[[Any], None]] = {
            "auditModeEnabled": lambda n : setattr(self, 'audit_mode_enabled', n.get_bool_value()),
            "exemptionRules": lambda n : setattr(self, 'exemption_rules', n.get_collection_of_object_values(WindowsZtdnsExemptionRule)),
            "extendedKeyUsagesForClientAuthentication": lambda n : setattr(self, 'extended_key_usages_for_client_authentication', n.get_collection_of_object_values(ExtendedKeyUsage)),
            "hostsFileResolutionEnabled": lambda n : setattr(self, 'hosts_file_resolution_enabled', n.get_bool_value()),
            "loopbackDnsForwarderEnabled": lambda n : setattr(self, 'loopback_dns_forwarder_enabled', n.get_bool_value()),
            "loopbackTrafficBlocked": lambda n : setattr(self, 'loopback_traffic_blocked', n.get_bool_value()),
            "maximumConnectionTimeInSeconds": lambda n : setattr(self, 'maximum_connection_time_in_seconds', n.get_int_value()),
            "rootCertificatesForClientValidation": lambda n : setattr(self, 'root_certificates_for_client_validation', n.get_collection_of_object_values(Windows81TrustedRootCertificate)),
            "rootCertificatesForServerValidation": lambda n : setattr(self, 'root_certificates_for_server_validation', n.get_collection_of_object_values(Windows81TrustedRootCertificate)),
            "secureDnsServers": lambda n : setattr(self, 'secure_dns_servers', n.get_collection_of_object_values(WindowsZtdnsSecureDnsServer)),
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
        writer.write_bool_value("auditModeEnabled", self.audit_mode_enabled)
        writer.write_collection_of_object_values("exemptionRules", self.exemption_rules)
        writer.write_collection_of_object_values("extendedKeyUsagesForClientAuthentication", self.extended_key_usages_for_client_authentication)
        writer.write_bool_value("hostsFileResolutionEnabled", self.hosts_file_resolution_enabled)
        writer.write_bool_value("loopbackDnsForwarderEnabled", self.loopback_dns_forwarder_enabled)
        writer.write_bool_value("loopbackTrafficBlocked", self.loopback_traffic_blocked)
        writer.write_int_value("maximumConnectionTimeInSeconds", self.maximum_connection_time_in_seconds)
        writer.write_collection_of_object_values("rootCertificatesForClientValidation", self.root_certificates_for_client_validation)
        writer.write_collection_of_object_values("rootCertificatesForServerValidation", self.root_certificates_for_server_validation)
        writer.write_collection_of_object_values("secureDnsServers", self.secure_dns_servers)
    

