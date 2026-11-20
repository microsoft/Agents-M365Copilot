from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .vpn_on_demand_rule_connection_action import VpnOnDemandRuleConnectionAction
    from .vpn_on_demand_rule_connection_domain_action import VpnOnDemandRuleConnectionDomainAction
    from .vpn_on_demand_rule_interface_type_match import VpnOnDemandRuleInterfaceTypeMatch

@dataclass
class VpnOnDemandRule(AdditionalDataHolder, Parsable):
    """
    VPN On-Demand Rule definition.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # VPN On-Demand Rule Connection Action.
    action: Optional[VpnOnDemandRuleConnectionAction] = None
    # DNS Search Domains.
    dns_search_domains: Optional[list[str]] = None
    # DNS Search Server Address.
    dns_server_address_match: Optional[list[str]] = None
    # VPN On-Demand Rule Connection Domain Action.
    domain_action: Optional[VpnOnDemandRuleConnectionDomainAction] = None
    # Domains (Only applicable when Action is evaluate connection).
    domains: Optional[list[str]] = None
    # VPN On-Demand Rule Connection network interface type.
    interface_type_match: Optional[VpnOnDemandRuleInterfaceTypeMatch] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Probe Required Url (Only applicable when Action is evaluate connection and DomainAction is connect if needed).
    probe_required_url: Optional[str] = None
    # A URL to probe. If this URL is successfully fetched (returning a 200 HTTP status code) without redirection, this rule matches.
    probe_url: Optional[str] = None
    # Network Service Set Identifiers (SSIDs).
    ssids: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VpnOnDemandRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VpnOnDemandRule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return VpnOnDemandRule()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .vpn_on_demand_rule_connection_action import VpnOnDemandRuleConnectionAction
        from .vpn_on_demand_rule_connection_domain_action import VpnOnDemandRuleConnectionDomainAction
        from .vpn_on_demand_rule_interface_type_match import VpnOnDemandRuleInterfaceTypeMatch

        from .vpn_on_demand_rule_connection_action import VpnOnDemandRuleConnectionAction
        from .vpn_on_demand_rule_connection_domain_action import VpnOnDemandRuleConnectionDomainAction
        from .vpn_on_demand_rule_interface_type_match import VpnOnDemandRuleInterfaceTypeMatch

        fields: dict[str, Callable[[Any], None]] = {
            "action": lambda n : setattr(self, 'action', n.get_enum_value(VpnOnDemandRuleConnectionAction)),
            "dnsSearchDomains": lambda n : setattr(self, 'dns_search_domains', n.get_collection_of_primitive_values(str)),
            "dnsServerAddressMatch": lambda n : setattr(self, 'dns_server_address_match', n.get_collection_of_primitive_values(str)),
            "domainAction": lambda n : setattr(self, 'domain_action', n.get_enum_value(VpnOnDemandRuleConnectionDomainAction)),
            "domains": lambda n : setattr(self, 'domains', n.get_collection_of_primitive_values(str)),
            "interfaceTypeMatch": lambda n : setattr(self, 'interface_type_match', n.get_enum_value(VpnOnDemandRuleInterfaceTypeMatch)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "probeRequiredUrl": lambda n : setattr(self, 'probe_required_url', n.get_str_value()),
            "probeUrl": lambda n : setattr(self, 'probe_url', n.get_str_value()),
            "ssids": lambda n : setattr(self, 'ssids', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_primitive_values("dnsSearchDomains", self.dns_search_domains)
        writer.write_collection_of_primitive_values("dnsServerAddressMatch", self.dns_server_address_match)
        writer.write_enum_value("domainAction", self.domain_action)
        writer.write_collection_of_primitive_values("domains", self.domains)
        writer.write_enum_value("interfaceTypeMatch", self.interface_type_match)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("probeRequiredUrl", self.probe_required_url)
        writer.write_str_value("probeUrl", self.probe_url)
        writer.write_collection_of_primitive_values("ssids", self.ssids)
        writer.write_additional_data_value(self.additional_data)
    

