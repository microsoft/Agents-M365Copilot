from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ip_range import IpRange
    from .proxied_domain import ProxiedDomain

@dataclass
class WindowsNetworkIsolationPolicy(AdditionalDataHolder, Parsable):
    """
    Windows Network Isolation Policy
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Contains a list of enterprise resource domains hosted in the cloud that need to be protected. Connections to these resources are considered enterprise data. If a proxy is paired with a cloud resource, traffic to the cloud resource will be routed through the enterprise network via the denoted proxy server (on Port 80). A proxy server used for this purpose must also be configured using the EnterpriseInternalProxyServers policy. This collection can contain a maximum of 500 elements.
    enterprise_cloud_resources: Optional[list[ProxiedDomain]] = None
    # Sets the enterprise IP ranges that define the computers in the enterprise network. Data that comes from those computers will be considered part of the enterprise and protected. These locations will be considered a safe destination for enterprise data to be shared to. This collection can contain a maximum of 500 elements.
    enterprise_i_p_ranges: Optional[list[IpRange]] = None
    # Boolean value that tells the client to accept the configured list and not to use heuristics to attempt to find other subnets. Default is false.
    enterprise_i_p_ranges_are_authoritative: Optional[bool] = None
    # This is the comma-separated list of internal proxy servers. For example, '157.54.14.28, 157.54.11.118, 10.202.14.167, 157.53.14.163, 157.69.210.59'. These proxies have been configured by the admin to connect to specific resources on the Internet. They are considered to be enterprise network locations. The proxies are only leveraged in configuring the EnterpriseCloudResources policy to force traffic to the matched cloud resources through these proxies.
    enterprise_internal_proxy_servers: Optional[list[str]] = None
    # This is the list of domains that comprise the boundaries of the enterprise. Data from one of these domains that is sent to a device will be considered enterprise data and protected. These locations will be considered a safe destination for enterprise data to be shared to.
    enterprise_network_domain_names: Optional[list[str]] = None
    # This is a list of proxy servers. Any server not on this list is considered non-enterprise.
    enterprise_proxy_servers: Optional[list[str]] = None
    # Boolean value that tells the client to accept the configured list of proxies and not try to detect other work proxies. Default is false
    enterprise_proxy_servers_are_authoritative: Optional[bool] = None
    # List of domain names that can used for work or personal resource.
    neutral_domain_resources: Optional[list[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsNetworkIsolationPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsNetworkIsolationPolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsNetworkIsolationPolicy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .ip_range import IpRange
        from .proxied_domain import ProxiedDomain

        from .ip_range import IpRange
        from .proxied_domain import ProxiedDomain

        fields: dict[str, Callable[[Any], None]] = {
            "enterpriseCloudResources": lambda n : setattr(self, 'enterprise_cloud_resources', n.get_collection_of_object_values(ProxiedDomain)),
            "enterpriseIPRanges": lambda n : setattr(self, 'enterprise_i_p_ranges', n.get_collection_of_object_values(IpRange)),
            "enterpriseIPRangesAreAuthoritative": lambda n : setattr(self, 'enterprise_i_p_ranges_are_authoritative', n.get_bool_value()),
            "enterpriseInternalProxyServers": lambda n : setattr(self, 'enterprise_internal_proxy_servers', n.get_collection_of_primitive_values(str)),
            "enterpriseNetworkDomainNames": lambda n : setattr(self, 'enterprise_network_domain_names', n.get_collection_of_primitive_values(str)),
            "enterpriseProxyServers": lambda n : setattr(self, 'enterprise_proxy_servers', n.get_collection_of_primitive_values(str)),
            "enterpriseProxyServersAreAuthoritative": lambda n : setattr(self, 'enterprise_proxy_servers_are_authoritative', n.get_bool_value()),
            "neutralDomainResources": lambda n : setattr(self, 'neutral_domain_resources', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_object_values("enterpriseCloudResources", self.enterprise_cloud_resources)
        writer.write_collection_of_object_values("enterpriseIPRanges", self.enterprise_i_p_ranges)
        writer.write_bool_value("enterpriseIPRangesAreAuthoritative", self.enterprise_i_p_ranges_are_authoritative)
        writer.write_collection_of_primitive_values("enterpriseInternalProxyServers", self.enterprise_internal_proxy_servers)
        writer.write_collection_of_primitive_values("enterpriseNetworkDomainNames", self.enterprise_network_domain_names)
        writer.write_collection_of_primitive_values("enterpriseProxyServers", self.enterprise_proxy_servers)
        writer.write_bool_value("enterpriseProxyServersAreAuthoritative", self.enterprise_proxy_servers_are_authoritative)
        writer.write_collection_of_primitive_values("neutralDomainResources", self.neutral_domain_resources)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

