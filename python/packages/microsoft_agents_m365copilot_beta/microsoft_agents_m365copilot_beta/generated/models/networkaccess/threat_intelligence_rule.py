from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .policy_rule import PolicyRule
    from .threat_intelligence_action import ThreatIntelligenceAction
    from .threat_intelligence_matching_conditions import ThreatIntelligenceMatchingConditions
    from .threat_intelligence_rule_settings import ThreatIntelligenceRuleSettings

from .policy_rule import PolicyRule

@dataclass
class ThreatIntelligenceRule(PolicyRule, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.networkaccess.threatIntelligenceRule"
    # The action property
    action: Optional[ThreatIntelligenceAction] = None
    # A description of the threat intelligence rule. Supports $filter (eq).
    description: Optional[str] = None
    # The matchingConditions property
    matching_conditions: Optional[ThreatIntelligenceMatchingConditions] = None
    # The priority of the rule which determines the order of rule evaluation. Lower values indicate higher priority. Supports $filter (eq).
    priority: Optional[int] = None
    # The settings property
    settings: Optional[ThreatIntelligenceRuleSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ThreatIntelligenceRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ThreatIntelligenceRule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ThreatIntelligenceRule()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .policy_rule import PolicyRule
        from .threat_intelligence_action import ThreatIntelligenceAction
        from .threat_intelligence_matching_conditions import ThreatIntelligenceMatchingConditions
        from .threat_intelligence_rule_settings import ThreatIntelligenceRuleSettings

        from .policy_rule import PolicyRule
        from .threat_intelligence_action import ThreatIntelligenceAction
        from .threat_intelligence_matching_conditions import ThreatIntelligenceMatchingConditions
        from .threat_intelligence_rule_settings import ThreatIntelligenceRuleSettings

        fields: dict[str, Callable[[Any], None]] = {
            "action": lambda n : setattr(self, 'action', n.get_enum_value(ThreatIntelligenceAction)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "matchingConditions": lambda n : setattr(self, 'matching_conditions', n.get_object_value(ThreatIntelligenceMatchingConditions)),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(ThreatIntelligenceRuleSettings)),
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
    

