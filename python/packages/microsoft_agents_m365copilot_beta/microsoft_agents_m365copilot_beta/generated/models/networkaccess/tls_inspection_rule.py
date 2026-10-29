from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .policy_rule import PolicyRule
    from .tls_inspection_matching_conditions import TlsInspectionMatchingConditions
    from .tls_inspection_rule_settings import TlsInspectionRuleSettings

from .policy_rule import PolicyRule

@dataclass
class TlsInspectionRule(PolicyRule, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.networkaccess.tlsInspectionRule"
    # Optional description explaining the purpose of the rule.
    description: Optional[str] = None
    # The conditions that determine when this rule should be applied to traffic.
    matching_conditions: Optional[TlsInspectionMatchingConditions] = None
    # The priority of the rule. Rules are evaluated in ascending order of priority. Lower numbers indicate higher priority. Supports $filter (eq, ne, not, ge, le, in) and $orderby.
    priority: Optional[int] = None
    # The settings property
    settings: Optional[TlsInspectionRuleSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TlsInspectionRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TlsInspectionRule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TlsInspectionRule()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .policy_rule import PolicyRule
        from .tls_inspection_matching_conditions import TlsInspectionMatchingConditions
        from .tls_inspection_rule_settings import TlsInspectionRuleSettings

        from .policy_rule import PolicyRule
        from .tls_inspection_matching_conditions import TlsInspectionMatchingConditions
        from .tls_inspection_rule_settings import TlsInspectionRuleSettings

        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "matchingConditions": lambda n : setattr(self, 'matching_conditions', n.get_object_value(TlsInspectionMatchingConditions)),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(TlsInspectionRuleSettings)),
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
        writer.write_object_value("matchingConditions", self.matching_conditions)
        writer.write_int_value("priority", self.priority)
        writer.write_object_value("settings", self.settings)
    

