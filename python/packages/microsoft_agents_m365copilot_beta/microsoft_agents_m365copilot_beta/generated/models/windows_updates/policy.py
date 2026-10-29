from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .applicable_content import ApplicableContent
    from .approval_rule import ApprovalRule
    from .policy_approval import PolicyApproval
    from .quality_update_policy import QualityUpdatePolicy
    from .ring import Ring

from ..entity import Entity

@dataclass
class Policy(Entity, Parsable):
    # Represents content applicable for offering to the related collection of devices.
    applicable_content: Optional[list[ApplicableContent]] = None
    # The approved rule of the policy that determines which published content matches the rule on an ongoing basis.
    approval_rules: Optional[list[ApprovalRule]] = None
    # Represents a set of quality updates policy approval types.
    approvals: Optional[list[PolicyApproval]] = None
    # The date and time when the policy is created. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    # The policy description. The maximum length is 1,500 characters.
    description: Optional[str] = None
    # The policy display name. The maximum length is 200 characters.
    display_name: Optional[str] = None
    # The date and time when the policy was last modified. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents a set of deployment rings that contains update deployment settings.
    rings: Optional[list[Ring]] = None
    
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
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdates.qualityUpdatePolicy".casefold():
            from .quality_update_policy import QualityUpdatePolicy

            return QualityUpdatePolicy()
        return Policy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .applicable_content import ApplicableContent
        from .approval_rule import ApprovalRule
        from .policy_approval import PolicyApproval
        from .quality_update_policy import QualityUpdatePolicy
        from .ring import Ring

        from ..entity import Entity
        from .applicable_content import ApplicableContent
        from .approval_rule import ApprovalRule
        from .policy_approval import PolicyApproval
        from .quality_update_policy import QualityUpdatePolicy
        from .ring import Ring

        fields: dict[str, Callable[[Any], None]] = {
            "applicableContent": lambda n : setattr(self, 'applicable_content', n.get_collection_of_object_values(ApplicableContent)),
            "approvalRules": lambda n : setattr(self, 'approval_rules', n.get_collection_of_object_values(ApprovalRule)),
            "approvals": lambda n : setattr(self, 'approvals', n.get_collection_of_object_values(PolicyApproval)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "rings": lambda n : setattr(self, 'rings', n.get_collection_of_object_values(Ring)),
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
        writer.write_collection_of_object_values("applicableContent", self.applicable_content)
        writer.write_collection_of_object_values("approvalRules", self.approval_rules)
        writer.write_collection_of_object_values("approvals", self.approvals)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_object_values("rings", self.rings)
    

