from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .fqdn_filtering_rule import FqdnFilteringRule
    from .network_destination_type import NetworkDestinationType
    from .policy_rule import PolicyRule
    from .rule_destination import RuleDestination
    from .url_destination_filtering_rule import UrlDestinationFilteringRule
    from .web_category_filtering_rule import WebCategoryFilteringRule

from .policy_rule import PolicyRule

@dataclass
class FilteringRule(PolicyRule, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.networkaccess.filteringRule"
    # Possible destinations and types of destinations accessed by the user in accordance with the network filtering policy, such as IP addresses and FQDNs/URLs.
    destinations: Optional[list[RuleDestination]] = None
    # The ruleType property
    rule_type: Optional[NetworkDestinationType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FilteringRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FilteringRule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.fqdnFilteringRule".casefold():
            from .fqdn_filtering_rule import FqdnFilteringRule

            return FqdnFilteringRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.urlDestinationFilteringRule".casefold():
            from .url_destination_filtering_rule import UrlDestinationFilteringRule

            return UrlDestinationFilteringRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.webCategoryFilteringRule".casefold():
            from .web_category_filtering_rule import WebCategoryFilteringRule

            return WebCategoryFilteringRule()
        return FilteringRule()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .fqdn_filtering_rule import FqdnFilteringRule
        from .network_destination_type import NetworkDestinationType
        from .policy_rule import PolicyRule
        from .rule_destination import RuleDestination
        from .url_destination_filtering_rule import UrlDestinationFilteringRule
        from .web_category_filtering_rule import WebCategoryFilteringRule

        from .fqdn_filtering_rule import FqdnFilteringRule
        from .network_destination_type import NetworkDestinationType
        from .policy_rule import PolicyRule
        from .rule_destination import RuleDestination
        from .url_destination_filtering_rule import UrlDestinationFilteringRule
        from .web_category_filtering_rule import WebCategoryFilteringRule

        fields: dict[str, Callable[[Any], None]] = {
            "destinations": lambda n : setattr(self, 'destinations', n.get_collection_of_object_values(RuleDestination)),
            "ruleType": lambda n : setattr(self, 'rule_type', n.get_enum_value(NetworkDestinationType)),
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
        writer.write_collection_of_object_values("destinations", self.destinations)
        writer.write_enum_value("ruleType", self.rule_type)
    

