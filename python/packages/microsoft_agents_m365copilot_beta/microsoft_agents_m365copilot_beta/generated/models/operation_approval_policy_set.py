from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .operation_approval_policy_platform import OperationApprovalPolicyPlatform
    from .operation_approval_policy_type import OperationApprovalPolicyType

@dataclass
class OperationApprovalPolicySet(AdditionalDataHolder, Parsable):
    """
    Contains the pair of OperationApprovalPolicyType and OperationApprovalPolicyPlatform determining the set of applicable OperationApprovalPolicies for a user. The OperationApprovalPolicySet complex type is used to indicate to the UX which policies are enabled for the current logged in user in order to correctly show the expected experience.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # The set of available platforms for the OperationApprovalPolicy. Allows configuration of a policy to specific platform(s) for approval. If no specific platform is required or applicable, the platform is `notApplicable`.
    policy_platform: Optional[OperationApprovalPolicyPlatform] = None
    # The set of available policy types that can be configured for approval. The policy type must always be defined in an OperationApprovalRequest.
    policy_type: Optional[OperationApprovalPolicyType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OperationApprovalPolicySet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OperationApprovalPolicySet
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OperationApprovalPolicySet()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .operation_approval_policy_platform import OperationApprovalPolicyPlatform
        from .operation_approval_policy_type import OperationApprovalPolicyType

        from .operation_approval_policy_platform import OperationApprovalPolicyPlatform
        from .operation_approval_policy_type import OperationApprovalPolicyType

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "policyPlatform": lambda n : setattr(self, 'policy_platform', n.get_collection_of_enum_values(OperationApprovalPolicyPlatform)),
            "policyType": lambda n : setattr(self, 'policy_type', n.get_enum_value(OperationApprovalPolicyType)),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("policyPlatform", self.policy_platform)
        writer.write_enum_value("policyType", self.policy_type)
        writer.write_additional_data_value(self.additional_data)
    

