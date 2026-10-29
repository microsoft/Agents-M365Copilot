from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .client_fallback_action import ClientFallbackAction
    from .forwarding_rule_action import ForwardingRuleAction
    from .internet_access_forwarding_rule import InternetAccessForwardingRule
    from .m365_forwarding_rule import M365ForwardingRule
    from .network_destination_type import NetworkDestinationType
    from .policy_rule import PolicyRule
    from .private_access_forwarding_rule import PrivateAccessForwardingRule
    from .rule_destination import RuleDestination

from .policy_rule import PolicyRule

@dataclass
class ForwardingRule(PolicyRule, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.networkaccess.forwardingRule"
    # The action property
    action: Optional[ForwardingRuleAction] = None
    # The clientFallbackAction property
    client_fallback_action: Optional[ClientFallbackAction] = None
    # Destinations maintain a list of potential destinations and destination types that the user may access within the context of a network filtering policy. This includes IP addresses and fully qualified domain names (FQDNs)/URLs.
    destinations: Optional[list[RuleDestination]] = None
    # The ruleType property
    rule_type: Optional[NetworkDestinationType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ForwardingRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ForwardingRule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.internetAccessForwardingRule".casefold():
            from .internet_access_forwarding_rule import InternetAccessForwardingRule

            return InternetAccessForwardingRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.m365ForwardingRule".casefold():
            from .m365_forwarding_rule import M365ForwardingRule

            return M365ForwardingRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.privateAccessForwardingRule".casefold():
            from .private_access_forwarding_rule import PrivateAccessForwardingRule

            return PrivateAccessForwardingRule()
        return ForwardingRule()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .client_fallback_action import ClientFallbackAction
        from .forwarding_rule_action import ForwardingRuleAction
        from .internet_access_forwarding_rule import InternetAccessForwardingRule
        from .m365_forwarding_rule import M365ForwardingRule
        from .network_destination_type import NetworkDestinationType
        from .policy_rule import PolicyRule
        from .private_access_forwarding_rule import PrivateAccessForwardingRule
        from .rule_destination import RuleDestination

        from .client_fallback_action import ClientFallbackAction
        from .forwarding_rule_action import ForwardingRuleAction
        from .internet_access_forwarding_rule import InternetAccessForwardingRule
        from .m365_forwarding_rule import M365ForwardingRule
        from .network_destination_type import NetworkDestinationType
        from .policy_rule import PolicyRule
        from .private_access_forwarding_rule import PrivateAccessForwardingRule
        from .rule_destination import RuleDestination

        fields: dict[str, Callable[[Any], None]] = {
            "action": lambda n : setattr(self, 'action', n.get_enum_value(ForwardingRuleAction)),
            "clientFallbackAction": lambda n : setattr(self, 'client_fallback_action', n.get_enum_value(ClientFallbackAction)),
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
        writer.write_enum_value("action", self.action)
        writer.write_enum_value("clientFallbackAction", self.client_fallback_action)
        writer.write_collection_of_object_values("destinations", self.destinations)
        writer.write_enum_value("ruleType", self.rule_type)
    

