from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .business_flow import BusinessFlow
    from .entity import Entity
    from .governance_policy_template import GovernancePolicyTemplate

from .entity import Entity

@dataclass
class ApprovalWorkflowProvider(Entity, Parsable):
    # The businessFlows property
    business_flows: Optional[list[BusinessFlow]] = None
    # The businessFlowsWithRequestsAwaitingMyDecision property
    business_flows_with_requests_awaiting_my_decision: Optional[list[BusinessFlow]] = None
    # The displayName property
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The policyTemplates property
    policy_templates: Optional[list[GovernancePolicyTemplate]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ApprovalWorkflowProvider:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ApprovalWorkflowProvider
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ApprovalWorkflowProvider()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .business_flow import BusinessFlow
        from .entity import Entity
        from .governance_policy_template import GovernancePolicyTemplate

        from .business_flow import BusinessFlow
        from .entity import Entity
        from .governance_policy_template import GovernancePolicyTemplate

        fields: dict[str, Callable[[Any], None]] = {
            "businessFlows": lambda n : setattr(self, 'business_flows', n.get_collection_of_object_values(BusinessFlow)),
            "businessFlowsWithRequestsAwaitingMyDecision": lambda n : setattr(self, 'business_flows_with_requests_awaiting_my_decision', n.get_collection_of_object_values(BusinessFlow)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "policyTemplates": lambda n : setattr(self, 'policy_templates', n.get_collection_of_object_values(GovernancePolicyTemplate)),
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
        writer.write_collection_of_object_values("businessFlows", self.business_flows)
        writer.write_collection_of_object_values("businessFlowsWithRequestsAwaitingMyDecision", self.business_flows_with_requests_awaiting_my_decision)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("policyTemplates", self.policy_templates)
    

