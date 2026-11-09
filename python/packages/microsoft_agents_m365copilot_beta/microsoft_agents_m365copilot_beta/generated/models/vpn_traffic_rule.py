from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .i_pv4_range import IPv4Range
    from .number_range import NumberRange
    from .vpn_traffic_direction import VpnTrafficDirection
    from .vpn_traffic_rule_app_type import VpnTrafficRuleAppType
    from .vpn_traffic_rule_routing_policy_type import VpnTrafficRuleRoutingPolicyType

@dataclass
class VpnTrafficRule(AdditionalDataHolder, Parsable):
    """
    VPN Traffic Rule definition.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # App identifier, if this traffic rule is triggered by an app.
    app_id: Optional[str] = None
    # Indicates the type of app that a VPN traffic rule is associated with.
    app_type: Optional[VpnTrafficRuleAppType] = None
    # Claims associated with this traffic rule.
    claims: Optional[str] = None
    # Local address range. This collection can contain a maximum of 500 elements.
    local_address_ranges: Optional[list[IPv4Range]] = None
    # Local port range can be set only when protocol is either TCP or UDP (6 or 17). This collection can contain a maximum of 500 elements.
    local_port_ranges: Optional[list[NumberRange]] = None
    # Name.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Protocols (0-255). Valid values 0 to 255
    protocols: Optional[int] = None
    # Remote address range. This collection can contain a maximum of 500 elements.
    remote_address_ranges: Optional[list[IPv4Range]] = None
    # Remote port range can be set only when protocol is either TCP or UDP (6 or 17). This collection can contain a maximum of 500 elements.
    remote_port_ranges: Optional[list[NumberRange]] = None
    # Specifies the routing policy for a VPN traffic rule.
    routing_policy_type: Optional[VpnTrafficRuleRoutingPolicyType] = None
    # Specify whether the rule applies to inbound traffic or outbound traffic.
    vpn_traffic_direction: Optional[VpnTrafficDirection] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VpnTrafficRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VpnTrafficRule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return VpnTrafficRule()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .i_pv4_range import IPv4Range
        from .number_range import NumberRange
        from .vpn_traffic_direction import VpnTrafficDirection
        from .vpn_traffic_rule_app_type import VpnTrafficRuleAppType
        from .vpn_traffic_rule_routing_policy_type import VpnTrafficRuleRoutingPolicyType

        from .i_pv4_range import IPv4Range
        from .number_range import NumberRange
        from .vpn_traffic_direction import VpnTrafficDirection
        from .vpn_traffic_rule_app_type import VpnTrafficRuleAppType
        from .vpn_traffic_rule_routing_policy_type import VpnTrafficRuleRoutingPolicyType

        fields: dict[str, Callable[[Any], None]] = {
            "appId": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "appType": lambda n : setattr(self, 'app_type', n.get_enum_value(VpnTrafficRuleAppType)),
            "claims": lambda n : setattr(self, 'claims', n.get_str_value()),
            "localAddressRanges": lambda n : setattr(self, 'local_address_ranges', n.get_collection_of_object_values(IPv4Range)),
            "localPortRanges": lambda n : setattr(self, 'local_port_ranges', n.get_collection_of_object_values(NumberRange)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "protocols": lambda n : setattr(self, 'protocols', n.get_int_value()),
            "remoteAddressRanges": lambda n : setattr(self, 'remote_address_ranges', n.get_collection_of_object_values(IPv4Range)),
            "remotePortRanges": lambda n : setattr(self, 'remote_port_ranges', n.get_collection_of_object_values(NumberRange)),
            "routingPolicyType": lambda n : setattr(self, 'routing_policy_type', n.get_enum_value(VpnTrafficRuleRoutingPolicyType)),
            "vpnTrafficDirection": lambda n : setattr(self, 'vpn_traffic_direction', n.get_enum_value(VpnTrafficDirection)),
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
        writer.write_str_value("appId", self.app_id)
        writer.write_enum_value("appType", self.app_type)
        writer.write_str_value("claims", self.claims)
        writer.write_collection_of_object_values("localAddressRanges", self.local_address_ranges)
        writer.write_collection_of_object_values("localPortRanges", self.local_port_ranges)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("protocols", self.protocols)
        writer.write_collection_of_object_values("remoteAddressRanges", self.remote_address_ranges)
        writer.write_collection_of_object_values("remotePortRanges", self.remote_port_ranges)
        writer.write_enum_value("routingPolicyType", self.routing_policy_type)
        writer.write_enum_value("vpnTrafficDirection", self.vpn_traffic_direction)
        writer.write_additional_data_value(self.additional_data)
    

