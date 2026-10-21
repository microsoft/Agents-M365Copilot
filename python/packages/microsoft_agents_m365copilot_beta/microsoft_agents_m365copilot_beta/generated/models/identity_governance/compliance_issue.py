from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .attestation_compliance_issue import AttestationComplianceIssue

from ..entity import Entity

@dataclass
class ComplianceIssue(Entity, Parsable):
    # A human-readable description of the compliance issue.
    description: Optional[str] = None
    # The identifier of the lifecycle policy that generated the compliance issue.
    governing_policy_reference_id: Optional[str] = None
    # A code that identifies the type of compliance issue.
    issue_code: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The type of rule that generated the compliance issue, so callers can identify which rule caused non-compliance.
    rule_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ComplianceIssue:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ComplianceIssue
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityGovernance.attestationComplianceIssue".casefold():
            from .attestation_compliance_issue import AttestationComplianceIssue

            return AttestationComplianceIssue()
        return ComplianceIssue()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .attestation_compliance_issue import AttestationComplianceIssue

        from ..entity import Entity
        from .attestation_compliance_issue import AttestationComplianceIssue

        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "governingPolicyReferenceId": lambda n : setattr(self, 'governing_policy_reference_id', n.get_str_value()),
            "issueCode": lambda n : setattr(self, 'issue_code', n.get_str_value()),
            "ruleType": lambda n : setattr(self, 'rule_type', n.get_str_value()),
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
        writer.write_str_value("governingPolicyReferenceId", self.governing_policy_reference_id)
        writer.write_str_value("issueCode", self.issue_code)
        writer.write_str_value("ruleType", self.rule_type)
    

