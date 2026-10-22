from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .cloud_firewall_policy import CloudFirewallPolicy
    from .filtering_policy import FilteringPolicy
    from .forwarding_policy import ForwardingPolicy
    from .policy_rule import PolicyRule
    from .threat_intelligence_policy import ThreatIntelligencePolicy
    from .tls_inspection_policy import TlsInspectionPolicy

from ..entity import Entity

@dataclass
class Policy(Entity, Parsable):
    # Description.
    description: Optional[str] = None
    # Policy name.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents the definition of the policy ruleset that makes up the core definition of a policy.
    policy_rules: Optional[list[PolicyRule]] = None
    # Version.
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Policy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Policy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.cloudFirewallPolicy".casefold():
            from .cloud_firewall_policy import CloudFirewallPolicy

            return CloudFirewallPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.filteringPolicy".casefold():
            from .filtering_policy import FilteringPolicy

            return FilteringPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.forwardingPolicy".casefold():
            from .forwarding_policy import ForwardingPolicy

            return ForwardingPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.threatIntelligencePolicy".casefold():
            from .threat_intelligence_policy import ThreatIntelligencePolicy

            return ThreatIntelligencePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.tlsInspectionPolicy".casefold():
            from .tls_inspection_policy import TlsInspectionPolicy

            return TlsInspectionPolicy()
        return Policy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .cloud_firewall_policy import CloudFirewallPolicy
        from .filtering_policy import FilteringPolicy
        from .forwarding_policy import ForwardingPolicy
        from .policy_rule import PolicyRule
        from .threat_intelligence_policy import ThreatIntelligencePolicy
        from .tls_inspection_policy import TlsInspectionPolicy

        from ..entity import Entity
        from .cloud_firewall_policy import CloudFirewallPolicy
        from .filtering_policy import FilteringPolicy
        from .forwarding_policy import ForwardingPolicy
        from .policy_rule import PolicyRule
        from .threat_intelligence_policy import ThreatIntelligencePolicy
        from .tls_inspection_policy import TlsInspectionPolicy

        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "policyRules": lambda n : setattr(self, 'policy_rules', n.get_collection_of_object_values(PolicyRule)),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
        writer.write_str_value("description", self.description)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_object_values("policyRules", self.policy_rules)
        writer.write_str_value("version", self.version)
    

