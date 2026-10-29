from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_firewall_action import CloudFirewallAction
    from .cloud_firewall_matching_conditions import CloudFirewallMatchingConditions
    from .cloud_firewall_rule_settings import CloudFirewallRuleSettings
    from .policy_rule import PolicyRule

from .policy_rule import PolicyRule

@dataclass
class CloudFirewallRule(PolicyRule, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.networkaccess.cloudFirewallRule"
    # The action property
    action: Optional[CloudFirewallAction] = None
    # A human-readable description of the rule's purpose. Optional.
    description: Optional[str] = None
    # The matchingConditions property
    matching_conditions: Optional[CloudFirewallMatchingConditions] = None
    # A unique priority value that determines the rule evaluation order; lower values are evaluated first. Required.
    priority: Optional[int] = None
    # The settings property
    settings: Optional[CloudFirewallRuleSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudFirewallRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudFirewallRule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudFirewallRule()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_firewall_action import CloudFirewallAction
        from .cloud_firewall_matching_conditions import CloudFirewallMatchingConditions
        from .cloud_firewall_rule_settings import CloudFirewallRuleSettings
        from .policy_rule import PolicyRule

        from .cloud_firewall_action import CloudFirewallAction
        from .cloud_firewall_matching_conditions import CloudFirewallMatchingConditions
        from .cloud_firewall_rule_settings import CloudFirewallRuleSettings
        from .policy_rule import PolicyRule

        fields: dict[str, Callable[[Any], None]] = {
            "action": lambda n : setattr(self, 'action', n.get_enum_value(CloudFirewallAction)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "matchingConditions": lambda n : setattr(self, 'matching_conditions', n.get_object_value(CloudFirewallMatchingConditions)),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(CloudFirewallRuleSettings)),
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
        writer.write_str_value("description", self.description)
        writer.write_object_value("matchingConditions", self.matching_conditions)
        writer.write_int_value("priority", self.priority)
        writer.write_object_value("settings", self.settings)
    

