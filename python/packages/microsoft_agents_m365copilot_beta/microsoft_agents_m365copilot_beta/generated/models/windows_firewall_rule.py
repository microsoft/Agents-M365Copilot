from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .state_management_setting import StateManagementSetting
    from .windows_firewall_rule_interface_types import WindowsFirewallRuleInterfaceTypes
    from .windows_firewall_rule_network_profile_types import WindowsFirewallRuleNetworkProfileTypes
    from .windows_firewall_rule_traffic_direction_type import WindowsFirewallRuleTrafficDirectionType

@dataclass
class WindowsFirewallRule(AdditionalDataHolder, Parsable):
    """
    A rule controlling traffic through the Windows Firewall.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # State Management Setting.
    action: Optional[StateManagementSetting] = None
    # The description of the rule.
    description: Optional[str] = None
    # The display name of the rule. Does not need to be unique.
    display_name: Optional[str] = None
    # State Management Setting.
    edge_traversal: Optional[StateManagementSetting] = None
    # The full file path of an app that's affected by the firewall rule.
    file_path: Optional[str] = None
    # Flags representing firewall rule interface types.
    interface_types: Optional[WindowsFirewallRuleInterfaceTypes] = None
    # List of local addresses covered by the rule. Default is any address. Valid tokens include:'' indicates any local address. If present, this must be the only token included.A subnet can be specified using either the subnet mask or network prefix notation. If neither a subnet mask nor a network prefix is specified, the subnet mask defaults to 255.255.255.255.A valid IPv6 address.An IPv4 address range in the format of 'start address - end address' with no spaces included.An IPv6 address range in the format of 'start address - end address' with no spaces included.
    local_address_ranges: Optional[list[str]] = None
    # List of local port ranges. For example, '100-120', '200', '300-320'. If not specified, the default is All.
    local_port_ranges: Optional[list[str]] = None
    # Specifies the list of authorized local users for the app container. This is a string in Security Descriptor Definition Language (SDDL) format.
    local_user_authorizations: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The package family name of a Microsoft Store application that's affected by the firewall rule.
    package_family_name: Optional[str] = None
    # Flags representing which network profile types apply to a firewall rule.
    profile_types: Optional[WindowsFirewallRuleNetworkProfileTypes] = None
    # 0-255 number representing the IP protocol (TCP = 6, UDP = 17). If not specified, the default is All. Valid values 0 to 255
    protocol: Optional[int] = None
    # List of tokens specifying the remote addresses covered by the rule. Tokens are case insensitive. Default is any address. Valid tokens include:'' indicates any remote address. If present, this must be the only token included.'Defaultgateway''DHCP''DNS''WINS''Intranet' (supported on Windows versions 1809+)'RmtIntranet' (supported on Windows versions 1809+)'Internet' (supported on Windows versions 1809+)'Ply2Renders' (supported on Windows versions 1809+)'LocalSubnet' indicates any local address on the local subnet.A subnet can be specified using either the subnet mask or network prefix notation. If neither a subnet mask nor a network prefix is specified, the subnet mask defaults to 255.255.255.255.A valid IPv6 address.An IPv4 address range in the format of 'start address - end address' with no spaces included.An IPv6 address range in the format of 'start address - end address' with no spaces included.
    remote_address_ranges: Optional[list[str]] = None
    # List of remote port ranges. For example, '100-120', '200', '300-320'. If not specified, the default is All.
    remote_port_ranges: Optional[list[str]] = None
    # The name used in cases when a service, not an application, is sending or receiving traffic.
    service_name: Optional[str] = None
    # Firewall rule traffic directions.
    traffic_direction: Optional[WindowsFirewallRuleTrafficDirectionType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsFirewallRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsFirewallRule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsFirewallRule()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .state_management_setting import StateManagementSetting
        from .windows_firewall_rule_interface_types import WindowsFirewallRuleInterfaceTypes
        from .windows_firewall_rule_network_profile_types import WindowsFirewallRuleNetworkProfileTypes
        from .windows_firewall_rule_traffic_direction_type import WindowsFirewallRuleTrafficDirectionType

        from .state_management_setting import StateManagementSetting
        from .windows_firewall_rule_interface_types import WindowsFirewallRuleInterfaceTypes
        from .windows_firewall_rule_network_profile_types import WindowsFirewallRuleNetworkProfileTypes
        from .windows_firewall_rule_traffic_direction_type import WindowsFirewallRuleTrafficDirectionType

        fields: dict[str, Callable[[Any], None]] = {
            "action": lambda n : setattr(self, 'action', n.get_enum_value(StateManagementSetting)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "edgeTraversal": lambda n : setattr(self, 'edge_traversal', n.get_enum_value(StateManagementSetting)),
            "filePath": lambda n : setattr(self, 'file_path', n.get_str_value()),
            "interfaceTypes": lambda n : setattr(self, 'interface_types', n.get_collection_of_enum_values(WindowsFirewallRuleInterfaceTypes)),
            "localAddressRanges": lambda n : setattr(self, 'local_address_ranges', n.get_collection_of_primitive_values(str)),
            "localPortRanges": lambda n : setattr(self, 'local_port_ranges', n.get_collection_of_primitive_values(str)),
            "localUserAuthorizations": lambda n : setattr(self, 'local_user_authorizations', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "packageFamilyName": lambda n : setattr(self, 'package_family_name', n.get_str_value()),
            "profileTypes": lambda n : setattr(self, 'profile_types', n.get_collection_of_enum_values(WindowsFirewallRuleNetworkProfileTypes)),
            "protocol": lambda n : setattr(self, 'protocol', n.get_int_value()),
            "remoteAddressRanges": lambda n : setattr(self, 'remote_address_ranges', n.get_collection_of_primitive_values(str)),
            "remotePortRanges": lambda n : setattr(self, 'remote_port_ranges', n.get_collection_of_primitive_values(str)),
            "serviceName": lambda n : setattr(self, 'service_name', n.get_str_value()),
            "trafficDirection": lambda n : setattr(self, 'traffic_direction', n.get_enum_value(WindowsFirewallRuleTrafficDirectionType)),
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
        writer.write_enum_value("action", self.action)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("edgeTraversal", self.edge_traversal)
        writer.write_str_value("filePath", self.file_path)
        writer.write_enum_value("interfaceTypes", self.interface_types)
        writer.write_collection_of_primitive_values("localAddressRanges", self.local_address_ranges)
        writer.write_collection_of_primitive_values("localPortRanges", self.local_port_ranges)
        writer.write_str_value("localUserAuthorizations", self.local_user_authorizations)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("packageFamilyName", self.package_family_name)
        writer.write_enum_value("profileTypes", self.profile_types)
        writer.write_int_value("protocol", self.protocol)
        writer.write_collection_of_primitive_values("remoteAddressRanges", self.remote_address_ranges)
        writer.write_collection_of_primitive_values("remotePortRanges", self.remote_port_ranges)
        writer.write_str_value("serviceName", self.service_name)
        writer.write_enum_value("trafficDirection", self.traffic_direction)
        writer.write_additional_data_value(self.additional_data)
    

