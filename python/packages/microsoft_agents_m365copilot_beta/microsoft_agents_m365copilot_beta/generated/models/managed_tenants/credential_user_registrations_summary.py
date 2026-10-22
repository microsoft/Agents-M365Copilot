from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity

from ..entity import Entity

@dataclass
class CredentialUserRegistrationsSummary(Entity, Parsable):
    # Date and time the entity was last updated in the multi-tenant management platform. Optional. Read-only.
    last_refreshed_date_time: Optional[datetime.datetime] = None
    # The number of users that are capable of performing multi-factor authentication or self service password reset. Optional. Read-only.
    mfa_and_sspr_capable_user_count: Optional[int] = None
    # The state of a conditional access policy that enforces multi-factor authentication. Optional. Read-only.
    mfa_conditional_access_policy_state: Optional[str] = None
    # The number of users in the multi-factor authentication exclusion security group (Microsoft 365 Lighthouse - MFA exclusions). Optional. Read-only.
    mfa_excluded_user_count: Optional[int] = None
    # The number of users registered for multi-factor authentication. Optional. Read-only.
    mfa_registered_user_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A flag indicating whether Identity Security Defaults is enabled. Optional. Read-only.
    security_defaults_enabled: Optional[bool] = None
    # The number of users enabled for self service password reset. Optional. Read-only.
    sspr_enabled_user_count: Optional[int] = None
    # The number of users registered for self service password reset. Optional. Read-only.
    sspr_registered_user_count: Optional[int] = None
    # The display name for the managed tenant. Required. Read-only.
    tenant_display_name: Optional[str] = None
    # The Microsoft Entra tenant identifier for the managed tenant. Required. Read-only.
    tenant_id: Optional[str] = None
    # The license type associated with the tenant; for example, AADFree, AADPremium1, AADPremium2.
    tenant_license_type: Optional[str] = None
    # The total number of users in the given managed tenant. Optional. Read-only.
    total_user_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CredentialUserRegistrationsSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CredentialUserRegistrationsSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CredentialUserRegistrationsSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity

        from ..entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "lastRefreshedDateTime": lambda n : setattr(self, 'last_refreshed_date_time', n.get_datetime_value()),
            "mfaAndSsprCapableUserCount": lambda n : setattr(self, 'mfa_and_sspr_capable_user_count', n.get_int_value()),
            "mfaConditionalAccessPolicyState": lambda n : setattr(self, 'mfa_conditional_access_policy_state', n.get_str_value()),
            "mfaExcludedUserCount": lambda n : setattr(self, 'mfa_excluded_user_count', n.get_int_value()),
            "mfaRegisteredUserCount": lambda n : setattr(self, 'mfa_registered_user_count', n.get_int_value()),
            "securityDefaultsEnabled": lambda n : setattr(self, 'security_defaults_enabled', n.get_bool_value()),
            "ssprEnabledUserCount": lambda n : setattr(self, 'sspr_enabled_user_count', n.get_int_value()),
            "ssprRegisteredUserCount": lambda n : setattr(self, 'sspr_registered_user_count', n.get_int_value()),
            "tenantDisplayName": lambda n : setattr(self, 'tenant_display_name', n.get_str_value()),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "tenantLicenseType": lambda n : setattr(self, 'tenant_license_type', n.get_str_value()),
            "totalUserCount": lambda n : setattr(self, 'total_user_count', n.get_int_value()),
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
        writer.write_datetime_value("lastRefreshedDateTime", self.last_refreshed_date_time)
        writer.write_int_value("mfaAndSsprCapableUserCount", self.mfa_and_sspr_capable_user_count)
        writer.write_str_value("mfaConditionalAccessPolicyState", self.mfa_conditional_access_policy_state)
        writer.write_int_value("mfaExcludedUserCount", self.mfa_excluded_user_count)
        writer.write_int_value("mfaRegisteredUserCount", self.mfa_registered_user_count)
        writer.write_bool_value("securityDefaultsEnabled", self.security_defaults_enabled)
        writer.write_int_value("ssprEnabledUserCount", self.sspr_enabled_user_count)
        writer.write_int_value("ssprRegisteredUserCount", self.sspr_registered_user_count)
        writer.write_str_value("tenantDisplayName", self.tenant_display_name)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_str_value("tenantLicenseType", self.tenant_license_type)
        writer.write_int_value("totalUserCount", self.total_user_count)
    

