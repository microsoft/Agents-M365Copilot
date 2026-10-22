from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...entity import Entity
    from .admins_mfa_enforced_security_requirement import AdminsMfaEnforcedSecurityRequirement
    from .compliance_status import ComplianceStatus
    from .customers_mfa_enforced_security_requirement import CustomersMfaEnforcedSecurityRequirement
    from .customers_spending_budget_security_requirement import CustomersSpendingBudgetSecurityRequirement
    from .response_time_security_requirement import ResponseTimeSecurityRequirement
    from .security_requirement_state import SecurityRequirementState
    from .security_requirement_type import SecurityRequirementType

from ...entity import Entity

@dataclass
class SecurityRequirement(Entity, Parsable):
    # The link to the site where the admin can take action on the requirement.
    action_url: Optional[str] = None
    # The complianceStatus property
    compliance_status: Optional[ComplianceStatus] = None
    # The link to documentation for the requirement.
    help_url: Optional[str] = None
    # The maximum score possible for the requirement.
    max_score: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The requirementType property
    requirement_type: Optional[SecurityRequirementType] = None
    # The score received for this requirement.
    score: Optional[int] = None
    # The state property
    state: Optional[SecurityRequirementState] = None
    # The date the requirement properties were last updated.
    updated_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SecurityRequirement:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SecurityRequirement
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.partner.security.adminsMfaEnforcedSecurityRequirement".casefold():
            from .admins_mfa_enforced_security_requirement import AdminsMfaEnforcedSecurityRequirement

            return AdminsMfaEnforcedSecurityRequirement()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.partner.security.customersMfaEnforcedSecurityRequirement".casefold():
            from .customers_mfa_enforced_security_requirement import CustomersMfaEnforcedSecurityRequirement

            return CustomersMfaEnforcedSecurityRequirement()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.partner.security.customersSpendingBudgetSecurityRequirement".casefold():
            from .customers_spending_budget_security_requirement import CustomersSpendingBudgetSecurityRequirement

            return CustomersSpendingBudgetSecurityRequirement()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.partner.security.responseTimeSecurityRequirement".casefold():
            from .response_time_security_requirement import ResponseTimeSecurityRequirement

            return ResponseTimeSecurityRequirement()
        return SecurityRequirement()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ...entity import Entity
        from .admins_mfa_enforced_security_requirement import AdminsMfaEnforcedSecurityRequirement
        from .compliance_status import ComplianceStatus
        from .customers_mfa_enforced_security_requirement import CustomersMfaEnforcedSecurityRequirement
        from .customers_spending_budget_security_requirement import CustomersSpendingBudgetSecurityRequirement
        from .response_time_security_requirement import ResponseTimeSecurityRequirement
        from .security_requirement_state import SecurityRequirementState
        from .security_requirement_type import SecurityRequirementType

        from ...entity import Entity
        from .admins_mfa_enforced_security_requirement import AdminsMfaEnforcedSecurityRequirement
        from .compliance_status import ComplianceStatus
        from .customers_mfa_enforced_security_requirement import CustomersMfaEnforcedSecurityRequirement
        from .customers_spending_budget_security_requirement import CustomersSpendingBudgetSecurityRequirement
        from .response_time_security_requirement import ResponseTimeSecurityRequirement
        from .security_requirement_state import SecurityRequirementState
        from .security_requirement_type import SecurityRequirementType

        fields: dict[str, Callable[[Any], None]] = {
            "actionUrl": lambda n : setattr(self, 'action_url', n.get_str_value()),
            "complianceStatus": lambda n : setattr(self, 'compliance_status', n.get_enum_value(ComplianceStatus)),
            "helpUrl": lambda n : setattr(self, 'help_url', n.get_str_value()),
            "maxScore": lambda n : setattr(self, 'max_score', n.get_int_value()),
            "requirementType": lambda n : setattr(self, 'requirement_type', n.get_enum_value(SecurityRequirementType)),
            "score": lambda n : setattr(self, 'score', n.get_int_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(SecurityRequirementState)),
            "updatedDateTime": lambda n : setattr(self, 'updated_date_time', n.get_datetime_value()),
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
        writer.write_str_value("actionUrl", self.action_url)
        writer.write_enum_value("complianceStatus", self.compliance_status)
        writer.write_str_value("helpUrl", self.help_url)
        writer.write_int_value("maxScore", self.max_score)
        writer.write_enum_value("requirementType", self.requirement_type)
        writer.write_int_value("score", self.score)
        writer.write_enum_value("state", self.state)
        writer.write_datetime_value("updatedDateTime", self.updated_date_time)
    

