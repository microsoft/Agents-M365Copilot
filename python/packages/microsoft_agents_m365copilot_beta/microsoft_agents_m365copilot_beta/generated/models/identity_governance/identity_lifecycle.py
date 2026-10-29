from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .agent_identity_lifecycle import AgentIdentityLifecycle
    from .compliance_issue import ComplianceIssue
    from .lifecycle_policy import LifecyclePolicy
    from .user_identity_lifecycle import UserIdentityLifecycle

from ..entity import Entity

@dataclass
class IdentityLifecycle(Entity, Parsable):
    # The collection of compliance issues that describe why the identity is currently non-compliant with its governing policy.
    compliance_issues: Optional[list[ComplianceIssue]] = None
    # The highest-priority lifecycle policy that currently governs the identity. Supports $expand.
    effective_governing_policy: Optional[LifecyclePolicy] = None
    # The date and time when the identity was last attested. This value can be null if the identity hasn't yet been attested.
    last_attestation_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IdentityLifecycle:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IdentityLifecycle
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityGovernance.agentIdentityLifecycle".casefold():
            from .agent_identity_lifecycle import AgentIdentityLifecycle

            return AgentIdentityLifecycle()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityGovernance.userIdentityLifecycle".casefold():
            from .user_identity_lifecycle import UserIdentityLifecycle

            return UserIdentityLifecycle()
        return IdentityLifecycle()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .agent_identity_lifecycle import AgentIdentityLifecycle
        from .compliance_issue import ComplianceIssue
        from .lifecycle_policy import LifecyclePolicy
        from .user_identity_lifecycle import UserIdentityLifecycle

        from ..entity import Entity
        from .agent_identity_lifecycle import AgentIdentityLifecycle
        from .compliance_issue import ComplianceIssue
        from .lifecycle_policy import LifecyclePolicy
        from .user_identity_lifecycle import UserIdentityLifecycle

        fields: dict[str, Callable[[Any], None]] = {
            "complianceIssues": lambda n : setattr(self, 'compliance_issues', n.get_collection_of_object_values(ComplianceIssue)),
            "effectiveGoverningPolicy": lambda n : setattr(self, 'effective_governing_policy', n.get_object_value(LifecyclePolicy)),
            "lastAttestationDateTime": lambda n : setattr(self, 'last_attestation_date_time', n.get_datetime_value()),
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
        writer.write_collection_of_object_values("complianceIssues", self.compliance_issues)
        writer.write_object_value("effectiveGoverningPolicy", self.effective_governing_policy)
        writer.write_datetime_value("lastAttestationDateTime", self.last_attestation_date_time)
    

