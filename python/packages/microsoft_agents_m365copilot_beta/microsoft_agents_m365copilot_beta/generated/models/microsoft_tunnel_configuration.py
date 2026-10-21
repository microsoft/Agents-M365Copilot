from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .key_value_pair import KeyValuePair

from .entity import Entity

@dataclass
class MicrosoftTunnelConfiguration(Entity, Parsable):
    """
    Entity that represents a collection of Microsoft Tunnel settings
    """
    # Additional settings that may be applied to the server
    advanced_settings: Optional[list[KeyValuePair]] = None
    # The Default Domain appendix that will be used by the clients
    default_domain_suffix: Optional[str] = None
    # The configuration's description (optional)
    description: Optional[str] = None
    # When DisableUdpConnections is set, the clients and VPN server will not use DTLS connections to transfer data.
    disable_udp_connections: Optional[bool] = None
    # The display name for the server configuration. This property is required when a server is created.
    display_name: Optional[str] = None
    # The DNS servers that will be used by the clients
    dns_servers: Optional[list[str]] = None
    # The IPv6 subnet that will be used to allocate virtual address for the clients
    ipv6_network: Optional[str] = None
    # When the configuration was last updated
    last_update_date_time: Optional[datetime.datetime] = None
    # The port that both TCP and UPD will listen over on the server
    listen_port: Optional[int] = None
    # The IPv4 subnet that will be used to allocate virtual address for the clients
    network: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # List of Scope Tags for this Entity instance
    role_scope_tag_ids: Optional[list[str]] = None
    # Subsets of the routes that will not be routed by the server
    route_excludes: Optional[list[str]] = None
    # The routes that will be routed by the server
    route_includes: Optional[list[str]] = None
    # Subsets of the routes that will not be routed by the server. This property is going to be deprecated with the option of using the new property, 'RouteExcludes'.
    routes_exclude: Optional[list[str]] = None
    # The routes that will be routed by the server. This property is going to be deprecated with the option of using the new property, 'RouteIncludes'.
    routes_include: Optional[list[str]] = None
    # The domains that will be resolved using the provided dns servers
    split_d_n_s: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MicrosoftTunnelConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MicrosoftTunnelConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MicrosoftTunnelConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .key_value_pair import KeyValuePair

        from .entity import Entity
        from .key_value_pair import KeyValuePair

        fields: dict[str, Callable[[Any], None]] = {
            "advancedSettings": lambda n : setattr(self, 'advanced_settings', n.get_collection_of_object_values(KeyValuePair)),
            "defaultDomainSuffix": lambda n : setattr(self, 'default_domain_suffix', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "disableUdpConnections": lambda n : setattr(self, 'disable_udp_connections', n.get_bool_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "dnsServers": lambda n : setattr(self, 'dns_servers', n.get_collection_of_primitive_values(str)),
            "ipv6Network": lambda n : setattr(self, 'ipv6_network', n.get_str_value()),
            "lastUpdateDateTime": lambda n : setattr(self, 'last_update_date_time', n.get_datetime_value()),
            "listenPort": lambda n : setattr(self, 'listen_port', n.get_int_value()),
            "network": lambda n : setattr(self, 'network', n.get_str_value()),
            "roleScopeTagIds": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "routeExcludes": lambda n : setattr(self, 'route_excludes', n.get_collection_of_primitive_values(str)),
            "routeIncludes": lambda n : setattr(self, 'route_includes', n.get_collection_of_primitive_values(str)),
            "routesExclude": lambda n : setattr(self, 'routes_exclude', n.get_collection_of_primitive_values(str)),
            "routesInclude": lambda n : setattr(self, 'routes_include', n.get_collection_of_primitive_values(str)),
            "splitDNS": lambda n : setattr(self, 'split_d_n_s', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_object_values("advancedSettings", self.advanced_settings)
        writer.write_str_value("defaultDomainSuffix", self.default_domain_suffix)
        writer.write_str_value("description", self.description)
        writer.write_bool_value("disableUdpConnections", self.disable_udp_connections)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_primitive_values("dnsServers", self.dns_servers)
        writer.write_str_value("ipv6Network", self.ipv6_network)
        writer.write_datetime_value("lastUpdateDateTime", self.last_update_date_time)
        writer.write_int_value("listenPort", self.listen_port)
        writer.write_str_value("network", self.network)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
        writer.write_collection_of_primitive_values("routeExcludes", self.route_excludes)
        writer.write_collection_of_primitive_values("routeIncludes", self.route_includes)
        writer.write_collection_of_primitive_values("routesExclude", self.routes_exclude)
        writer.write_collection_of_primitive_values("routesInclude", self.routes_include)
        writer.write_collection_of_primitive_values("splitDNS", self.split_d_n_s)
    

