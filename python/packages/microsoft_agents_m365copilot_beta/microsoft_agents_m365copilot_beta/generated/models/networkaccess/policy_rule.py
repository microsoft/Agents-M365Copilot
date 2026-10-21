from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .cloud_firewall_rule import CloudFirewallRule
    from .filtering_rule import FilteringRule
    from .forwarding_rule import ForwardingRule
    from .fqdn_filtering_rule import FqdnFilteringRule
    from .internet_access_forwarding_rule import InternetAccessForwardingRule
    from .m365_forwarding_rule import M365ForwardingRule
    from .private_access_forwarding_rule import PrivateAccessForwardingRule
    from .threat_intelligence_rule import ThreatIntelligenceRule
    from .tls_inspection_rule import TlsInspectionRule
    from .url_destination_filtering_rule import UrlDestinationFilteringRule
    from .web_category_filtering_rule import WebCategoryFilteringRule

from ..entity import Entity

@dataclass
class PolicyRule(Entity, Parsable):
    # Name.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PolicyRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PolicyRule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.cloudFirewallRule".casefold():
            from .cloud_firewall_rule import CloudFirewallRule

            return CloudFirewallRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.filteringRule".casefold():
            from .filtering_rule import FilteringRule

            return FilteringRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.forwardingRule".casefold():
            from .forwarding_rule import ForwardingRule

            return ForwardingRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.fqdnFilteringRule".casefold():
            from .fqdn_filtering_rule import FqdnFilteringRule

            return FqdnFilteringRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.internetAccessForwardingRule".casefold():
            from .internet_access_forwarding_rule import InternetAccessForwardingRule

            return InternetAccessForwardingRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.m365ForwardingRule".casefold():
            from .m365_forwarding_rule import M365ForwardingRule

            return M365ForwardingRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.privateAccessForwardingRule".casefold():
            from .private_access_forwarding_rule import PrivateAccessForwardingRule

            return PrivateAccessForwardingRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.threatIntelligenceRule".casefold():
            from .threat_intelligence_rule import ThreatIntelligenceRule

            return ThreatIntelligenceRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.tlsInspectionRule".casefold():
            from .tls_inspection_rule import TlsInspectionRule

            return TlsInspectionRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.urlDestinationFilteringRule".casefold():
            from .url_destination_filtering_rule import UrlDestinationFilteringRule

            return UrlDestinationFilteringRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.webCategoryFilteringRule".casefold():
            from .web_category_filtering_rule import WebCategoryFilteringRule

            return WebCategoryFilteringRule()
        return PolicyRule()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .cloud_firewall_rule import CloudFirewallRule
        from .filtering_rule import FilteringRule
        from .forwarding_rule import ForwardingRule
        from .fqdn_filtering_rule import FqdnFilteringRule
        from .internet_access_forwarding_rule import InternetAccessForwardingRule
        from .m365_forwarding_rule import M365ForwardingRule
        from .private_access_forwarding_rule import PrivateAccessForwardingRule
        from .threat_intelligence_rule import ThreatIntelligenceRule
        from .tls_inspection_rule import TlsInspectionRule
        from .url_destination_filtering_rule import UrlDestinationFilteringRule
        from .web_category_filtering_rule import WebCategoryFilteringRule

        from ..entity import Entity
        from .cloud_firewall_rule import CloudFirewallRule
        from .filtering_rule import FilteringRule
        from .forwarding_rule import ForwardingRule
        from .fqdn_filtering_rule import FqdnFilteringRule
        from .internet_access_forwarding_rule import InternetAccessForwardingRule
        from .m365_forwarding_rule import M365ForwardingRule
        from .private_access_forwarding_rule import PrivateAccessForwardingRule
        from .threat_intelligence_rule import ThreatIntelligenceRule
        from .tls_inspection_rule import TlsInspectionRule
        from .url_destination_filtering_rule import UrlDestinationFilteringRule
        from .web_category_filtering_rule import WebCategoryFilteringRule

        fields: dict[str, Callable[[Any], None]] = {
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
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
        writer.write_str_value("name", self.name)
    

