from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .operation_approval_policy_platform import OperationApprovalPolicyPlatform
    from .operation_approval_policy_set import OperationApprovalPolicySet
    from .operation_approval_policy_type import OperationApprovalPolicyType

from .entity import Entity

@dataclass
class OperationApprovalPolicy(Entity, Parsable):
    """
    The OperationApprovalPolicy entity allows an administrator to configure which operations require admin approval and the set of admins who can perform that approval. Creating a policy enables the multiple admin approval service to catch requests which are targeted by the specific policy type defined.
    """
    # The Microsoft Entra ID (Azure AD) security group IDs for the approvers for the policy. This property is required when the policy is created, and is defined by the IT Admins to define the possible approvers for the policy.
    approver_group_ids: Optional[list[str]] = None
    # Indicates the description of the policy. Maximum length of the description is 1024 characters. This property is not required, but can be used by the IT Admin to describe the policy.
    description: Optional[str] = None
    # Indicates the display name of the policy. Maximum length of the display name is 128 characters. This property is required when the policy is created, and is defined by the IT Admins to identify the policy.
    display_name: Optional[str] = None
    # Indicates the last DateTime that the policy was modified. The value cannot be modified and is automatically populated whenever values in the request are updated. For example, when the 'policyType' property changes from apps to scripts. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-only. This property is read-only.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The set of available platforms for the OperationApprovalPolicy. Allows configuration of a policy to specific platform(s) for approval. If no specific platform is required or applicable, the platform is `notApplicable`.
    policy_platform: Optional[OperationApprovalPolicyPlatform] = None
    # Indicates areas of the Intune UX that could support MAA UX for the current logged in IT Admin. This property is required, and is defined by the IT Admins in order to correctly show the expected experience.
    policy_set: Optional[OperationApprovalPolicySet] = None
    # The set of available policy types that can be configured for approval. The policy type must always be defined in an OperationApprovalRequest.
    policy_type: Optional[OperationApprovalPolicyType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OperationApprovalPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OperationApprovalPolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OperationApprovalPolicy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .operation_approval_policy_platform import OperationApprovalPolicyPlatform
        from .operation_approval_policy_set import OperationApprovalPolicySet
        from .operation_approval_policy_type import OperationApprovalPolicyType

        from .entity import Entity
        from .operation_approval_policy_platform import OperationApprovalPolicyPlatform
        from .operation_approval_policy_set import OperationApprovalPolicySet
        from .operation_approval_policy_type import OperationApprovalPolicyType

        fields: dict[str, Callable[[Any], None]] = {
            "approverGroupIds": lambda n : setattr(self, 'approver_group_ids', n.get_collection_of_primitive_values(str)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "policyPlatform": lambda n : setattr(self, 'policy_platform', n.get_collection_of_enum_values(OperationApprovalPolicyPlatform)),
            "policySet": lambda n : setattr(self, 'policy_set', n.get_object_value(OperationApprovalPolicySet)),
            "policyType": lambda n : setattr(self, 'policy_type', n.get_enum_value(OperationApprovalPolicyType)),
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
        writer.write_collection_of_primitive_values("approverGroupIds", self.approver_group_ids)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("policyPlatform", self.policy_platform)
        writer.write_object_value("policySet", self.policy_set)
        writer.write_enum_value("policyType", self.policy_type)
    

