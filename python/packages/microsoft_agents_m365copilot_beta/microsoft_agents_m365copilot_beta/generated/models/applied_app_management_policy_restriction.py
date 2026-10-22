from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .app_management_audit_log_audit_result import AppManagementAuditLogAuditResult
    from .app_management_audit_log_policy_type import AppManagementAuditLogPolicyType
    from .app_management_audit_log_restriction_result import AppManagementAuditLogRestrictionResult
    from .app_management_audit_log_restriction_state import AppManagementAuditLogRestrictionState
    from .dictionary import Dictionary

@dataclass
class AppliedAppManagementPolicyRestriction(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The attemptedChanges property
    attempted_changes: Optional[Dictionary] = None
    # The auditResult property
    audit_result: Optional[AppManagementAuditLogAuditResult] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The policyId property
    policy_id: Optional[str] = None
    # The policyType property
    policy_type: Optional[AppManagementAuditLogPolicyType] = None
    # The restrictionDetails property
    restriction_details: Optional[Dictionary] = None
    # The restrictionResult property
    restriction_result: Optional[AppManagementAuditLogRestrictionResult] = None
    # The restrictionState property
    restriction_state: Optional[AppManagementAuditLogRestrictionState] = None
    # The restrictionType property
    restriction_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AppliedAppManagementPolicyRestriction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AppliedAppManagementPolicyRestriction
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AppliedAppManagementPolicyRestriction()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .app_management_audit_log_audit_result import AppManagementAuditLogAuditResult
        from .app_management_audit_log_policy_type import AppManagementAuditLogPolicyType
        from .app_management_audit_log_restriction_result import AppManagementAuditLogRestrictionResult
        from .app_management_audit_log_restriction_state import AppManagementAuditLogRestrictionState
        from .dictionary import Dictionary

        from .app_management_audit_log_audit_result import AppManagementAuditLogAuditResult
        from .app_management_audit_log_policy_type import AppManagementAuditLogPolicyType
        from .app_management_audit_log_restriction_result import AppManagementAuditLogRestrictionResult
        from .app_management_audit_log_restriction_state import AppManagementAuditLogRestrictionState
        from .dictionary import Dictionary

        fields: dict[str, Callable[[Any], None]] = {
            "attemptedChanges": lambda n : setattr(self, 'attempted_changes', n.get_object_value(Dictionary)),
            "auditResult": lambda n : setattr(self, 'audit_result', n.get_enum_value(AppManagementAuditLogAuditResult)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "policyId": lambda n : setattr(self, 'policy_id', n.get_str_value()),
            "policyType": lambda n : setattr(self, 'policy_type', n.get_enum_value(AppManagementAuditLogPolicyType)),
            "restrictionDetails": lambda n : setattr(self, 'restriction_details', n.get_object_value(Dictionary)),
            "restrictionResult": lambda n : setattr(self, 'restriction_result', n.get_enum_value(AppManagementAuditLogRestrictionResult)),
            "restrictionState": lambda n : setattr(self, 'restriction_state', n.get_enum_value(AppManagementAuditLogRestrictionState)),
            "restrictionType": lambda n : setattr(self, 'restriction_type', n.get_str_value()),
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
        writer.write_object_value("attemptedChanges", self.attempted_changes)
        writer.write_enum_value("auditResult", self.audit_result)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("policyId", self.policy_id)
        writer.write_enum_value("policyType", self.policy_type)
        writer.write_object_value("restrictionDetails", self.restriction_details)
        writer.write_enum_value("restrictionResult", self.restriction_result)
        writer.write_enum_value("restrictionState", self.restriction_state)
        writer.write_str_value("restrictionType", self.restriction_type)
        writer.write_additional_data_value(self.additional_data)
    

