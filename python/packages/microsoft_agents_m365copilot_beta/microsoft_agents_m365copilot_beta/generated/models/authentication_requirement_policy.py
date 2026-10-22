from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .requirement_provider import RequirementProvider

@dataclass
class AuthenticationRequirementPolicy(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Provides additional detail on the feature identified in requirementProvider.
    detail: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Identifies what Microsoft Entra feature requires MFA in this policy. The possible values are: user, request, servicePrincipal, v1ConditionalAccess, multiConditionalAccess, tenantSessionRiskPolicy, accountCompromisePolicies, v1ConditionalAccessDependency, v1ConditionalAccessPolicyIdRequested, mfaRegistrationRequiredByIdentityProtectionPolicy, baselineProtection, mfaRegistrationRequiredByBaselineProtection, mfaRegistrationRequiredByMultiConditionalAccess, enforcedForCspAdmins, securityDefaults, mfaRegistrationRequiredBySecurityDefaults, proofUpCodeRequest, crossTenantOutboundRule, gpsLocationCondition, riskBasedPolicy, unknownFutureValue, scopeBasedAuthRequirementPolicy, authenticationStrengths . Use the Prefer: include-unknown-enum-members request header to get the following value or values in this evolvable enum: scopeBasedAuthRequirementPolicy, authenticationStrengths.
    requirement_provider: Optional[RequirementProvider] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuthenticationRequirementPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationRequirementPolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AuthenticationRequirementPolicy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .requirement_provider import RequirementProvider

        from .requirement_provider import RequirementProvider

        fields: dict[str, Callable[[Any], None]] = {
            "detail": lambda n : setattr(self, 'detail', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "requirementProvider": lambda n : setattr(self, 'requirement_provider', n.get_enum_value(RequirementProvider)),
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
        writer.write_str_value("detail", self.detail)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("requirementProvider", self.requirement_provider)
        writer.write_additional_data_value(self.additional_data)
    

