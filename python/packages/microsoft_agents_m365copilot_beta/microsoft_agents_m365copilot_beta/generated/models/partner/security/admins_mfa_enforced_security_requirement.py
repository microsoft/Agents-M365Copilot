from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .policy_status import PolicyStatus
    from .security_requirement import SecurityRequirement

from .security_requirement import SecurityRequirement

@dataclass
class AdminsMfaEnforcedSecurityRequirement(SecurityRequirement, Parsable):
    # The number of admins who are required to use MFA, but haven't completed registration.
    admins_required_not_using_mfa_count: Optional[int] = None
    # The legacyPerUserMfaStatus property
    legacy_per_user_mfa_status: Optional[PolicyStatus] = None
    # The mfaConditionalAccessPolicyStatus property
    mfa_conditional_access_policy_status: Optional[PolicyStatus] = None
    # The number of admins who are using MFA.
    mfa_enabled_admins_count: Optional[int] = None
    # The number of users who are using MFA.
    mfa_enabled_users_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The securityDefaultsStatus property
    security_defaults_status: Optional[PolicyStatus] = None
    # The total number of admins in the partner's tenant.
    total_admins_count: Optional[int] = None
    # The total number of users in the partner's tenant.
    total_users_count: Optional[int] = None
    # The number of users who are required to use MFA, but haven't completed registration.
    users_required_not_using_mfa_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AdminsMfaEnforcedSecurityRequirement:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AdminsMfaEnforcedSecurityRequirement
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AdminsMfaEnforcedSecurityRequirement()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .policy_status import PolicyStatus
        from .security_requirement import SecurityRequirement

        from .policy_status import PolicyStatus
        from .security_requirement import SecurityRequirement

        fields: dict[str, Callable[[Any], None]] = {
            "adminsRequiredNotUsingMfaCount": lambda n : setattr(self, 'admins_required_not_using_mfa_count', n.get_int_value()),
            "legacyPerUserMfaStatus": lambda n : setattr(self, 'legacy_per_user_mfa_status', n.get_enum_value(PolicyStatus)),
            "mfaConditionalAccessPolicyStatus": lambda n : setattr(self, 'mfa_conditional_access_policy_status', n.get_enum_value(PolicyStatus)),
            "mfaEnabledAdminsCount": lambda n : setattr(self, 'mfa_enabled_admins_count', n.get_int_value()),
            "mfaEnabledUsersCount": lambda n : setattr(self, 'mfa_enabled_users_count', n.get_int_value()),
            "securityDefaultsStatus": lambda n : setattr(self, 'security_defaults_status', n.get_enum_value(PolicyStatus)),
            "totalAdminsCount": lambda n : setattr(self, 'total_admins_count', n.get_int_value()),
            "totalUsersCount": lambda n : setattr(self, 'total_users_count', n.get_int_value()),
            "usersRequiredNotUsingMfaCount": lambda n : setattr(self, 'users_required_not_using_mfa_count', n.get_int_value()),
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
        writer.write_int_value("adminsRequiredNotUsingMfaCount", self.admins_required_not_using_mfa_count)
        writer.write_enum_value("legacyPerUserMfaStatus", self.legacy_per_user_mfa_status)
        writer.write_enum_value("mfaConditionalAccessPolicyStatus", self.mfa_conditional_access_policy_status)
        writer.write_int_value("mfaEnabledAdminsCount", self.mfa_enabled_admins_count)
        writer.write_int_value("mfaEnabledUsersCount", self.mfa_enabled_users_count)
        writer.write_enum_value("securityDefaultsStatus", self.security_defaults_status)
        writer.write_int_value("totalAdminsCount", self.total_admins_count)
        writer.write_int_value("totalUsersCount", self.total_users_count)
        writer.write_int_value("usersRequiredNotUsingMfaCount", self.users_required_not_using_mfa_count)
    

