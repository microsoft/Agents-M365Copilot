from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .policy_status import PolicyStatus

@dataclass
class CustomerMfaInsight(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The number of admins that are compliant with the MFA requirements
    compliant_admins_count: Optional[int] = None
    # The number of users that are compliant with the MFA requirements
    compliant_non_admins_count: Optional[int] = None
    # The legacyPerUserMfaStatus property
    legacy_per_user_mfa_status: Optional[PolicyStatus] = None
    # The mfaConditionalAccessPolicyStatus property
    mfa_conditional_access_policy_status: Optional[PolicyStatus] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The securityDefaultsStatus property
    security_defaults_status: Optional[PolicyStatus] = None
    # The total number of users in the tenant
    total_users_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomerMfaInsight:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomerMfaInsight
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomerMfaInsight()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .policy_status import PolicyStatus

        from .policy_status import PolicyStatus

        fields: dict[str, Callable[[Any], None]] = {
            "compliantAdminsCount": lambda n : setattr(self, 'compliant_admins_count', n.get_int_value()),
            "compliantNonAdminsCount": lambda n : setattr(self, 'compliant_non_admins_count', n.get_int_value()),
            "legacyPerUserMfaStatus": lambda n : setattr(self, 'legacy_per_user_mfa_status', n.get_enum_value(PolicyStatus)),
            "mfaConditionalAccessPolicyStatus": lambda n : setattr(self, 'mfa_conditional_access_policy_status', n.get_enum_value(PolicyStatus)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "securityDefaultsStatus": lambda n : setattr(self, 'security_defaults_status', n.get_enum_value(PolicyStatus)),
            "totalUsersCount": lambda n : setattr(self, 'total_users_count', n.get_int_value()),
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
        writer.write_int_value("compliantAdminsCount", self.compliant_admins_count)
        writer.write_int_value("compliantNonAdminsCount", self.compliant_non_admins_count)
        writer.write_enum_value("legacyPerUserMfaStatus", self.legacy_per_user_mfa_status)
        writer.write_enum_value("mfaConditionalAccessPolicyStatus", self.mfa_conditional_access_policy_status)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("securityDefaultsStatus", self.security_defaults_status)
        writer.write_int_value("totalUsersCount", self.total_users_count)
        writer.write_additional_data_value(self.additional_data)
    

