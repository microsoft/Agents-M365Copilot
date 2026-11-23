from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .fetch_detail import FetchDetail
    from .policy_effect import PolicyEffect

@dataclass
class PolicyEvaluationDetail(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The applicabilityEvaluationError property
    applicability_evaluation_error: Optional[str] = None
    # The appliedPolicyEffects property
    applied_policy_effects: Optional[PolicyEffect] = None
    # The assignedPolicyDisplayName property
    assigned_policy_display_name: Optional[str] = None
    # The assignmentUniqueName property
    assignment_unique_name: Optional[str] = None
    # The evaluationError property
    evaluation_error: Optional[str] = None
    # The fetchDetails property
    fetch_details: Optional[list[FetchDetail]] = None
    # The isApplicable property
    is_applicable: Optional[bool] = None
    # The isCompliant property
    is_compliant: Optional[bool] = None
    # The isEnforced property
    is_enforced: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The policyLoadingError property
    policy_loading_error: Optional[str] = None
    # The policyMessage property
    policy_message: Optional[str] = None
    # The policyVersion property
    policy_version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PolicyEvaluationDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PolicyEvaluationDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PolicyEvaluationDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .fetch_detail import FetchDetail
        from .policy_effect import PolicyEffect

        from .fetch_detail import FetchDetail
        from .policy_effect import PolicyEffect

        fields: dict[str, Callable[[Any], None]] = {
            "applicabilityEvaluationError": lambda n : setattr(self, 'applicability_evaluation_error', n.get_str_value()),
            "appliedPolicyEffects": lambda n : setattr(self, 'applied_policy_effects', n.get_enum_value(PolicyEffect)),
            "assignedPolicyDisplayName": lambda n : setattr(self, 'assigned_policy_display_name', n.get_str_value()),
            "assignmentUniqueName": lambda n : setattr(self, 'assignment_unique_name', n.get_str_value()),
            "evaluationError": lambda n : setattr(self, 'evaluation_error', n.get_str_value()),
            "fetchDetails": lambda n : setattr(self, 'fetch_details', n.get_collection_of_object_values(FetchDetail)),
            "isApplicable": lambda n : setattr(self, 'is_applicable', n.get_bool_value()),
            "isCompliant": lambda n : setattr(self, 'is_compliant', n.get_bool_value()),
            "isEnforced": lambda n : setattr(self, 'is_enforced', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "policyLoadingError": lambda n : setattr(self, 'policy_loading_error', n.get_str_value()),
            "policyMessage": lambda n : setattr(self, 'policy_message', n.get_str_value()),
            "policyVersion": lambda n : setattr(self, 'policy_version', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("applicabilityEvaluationError", self.applicability_evaluation_error)
        writer.write_enum_value("appliedPolicyEffects", self.applied_policy_effects)
        writer.write_str_value("assignedPolicyDisplayName", self.assigned_policy_display_name)
        writer.write_str_value("assignmentUniqueName", self.assignment_unique_name)
        writer.write_str_value("evaluationError", self.evaluation_error)
        writer.write_collection_of_object_values("fetchDetails", self.fetch_details)
        writer.write_bool_value("isApplicable", self.is_applicable)
        writer.write_bool_value("isCompliant", self.is_compliant)
        writer.write_bool_value("isEnforced", self.is_enforced)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("policyLoadingError", self.policy_loading_error)
        writer.write_str_value("policyMessage", self.policy_message)
        writer.write_str_value("policyVersion", self.policy_version)
        writer.write_additional_data_value(self.additional_data)
    

