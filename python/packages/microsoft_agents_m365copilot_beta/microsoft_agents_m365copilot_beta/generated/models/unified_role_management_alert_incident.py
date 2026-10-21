from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .invalid_license_alert_incident import InvalidLicenseAlertIncident
    from .no_mfa_on_role_activation_alert_incident import NoMfaOnRoleActivationAlertIncident
    from .redundant_assignment_alert_incident import RedundantAssignmentAlertIncident
    from .roles_assigned_outside_privileged_identity_management_alert_incident import RolesAssignedOutsidePrivilegedIdentityManagementAlertIncident
    from .sequential_activation_renewals_alert_incident import SequentialActivationRenewalsAlertIncident
    from .stale_sign_in_alert_incident import StaleSignInAlertIncident
    from .too_many_global_admins_assigned_to_tenant_alert_incident import TooManyGlobalAdminsAssignedToTenantAlertIncident

from .entity import Entity

@dataclass
class UnifiedRoleManagementAlertIncident(Entity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UnifiedRoleManagementAlertIncident:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleManagementAlertIncident
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.invalidLicenseAlertIncident".casefold():
            from .invalid_license_alert_incident import InvalidLicenseAlertIncident

            return InvalidLicenseAlertIncident()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.noMfaOnRoleActivationAlertIncident".casefold():
            from .no_mfa_on_role_activation_alert_incident import NoMfaOnRoleActivationAlertIncident

            return NoMfaOnRoleActivationAlertIncident()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.redundantAssignmentAlertIncident".casefold():
            from .redundant_assignment_alert_incident import RedundantAssignmentAlertIncident

            return RedundantAssignmentAlertIncident()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.rolesAssignedOutsidePrivilegedIdentityManagementAlertIncident".casefold():
            from .roles_assigned_outside_privileged_identity_management_alert_incident import RolesAssignedOutsidePrivilegedIdentityManagementAlertIncident

            return RolesAssignedOutsidePrivilegedIdentityManagementAlertIncident()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sequentialActivationRenewalsAlertIncident".casefold():
            from .sequential_activation_renewals_alert_incident import SequentialActivationRenewalsAlertIncident

            return SequentialActivationRenewalsAlertIncident()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.staleSignInAlertIncident".casefold():
            from .stale_sign_in_alert_incident import StaleSignInAlertIncident

            return StaleSignInAlertIncident()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.tooManyGlobalAdminsAssignedToTenantAlertIncident".casefold():
            from .too_many_global_admins_assigned_to_tenant_alert_incident import TooManyGlobalAdminsAssignedToTenantAlertIncident

            return TooManyGlobalAdminsAssignedToTenantAlertIncident()
        return UnifiedRoleManagementAlertIncident()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .invalid_license_alert_incident import InvalidLicenseAlertIncident
        from .no_mfa_on_role_activation_alert_incident import NoMfaOnRoleActivationAlertIncident
        from .redundant_assignment_alert_incident import RedundantAssignmentAlertIncident
        from .roles_assigned_outside_privileged_identity_management_alert_incident import RolesAssignedOutsidePrivilegedIdentityManagementAlertIncident
        from .sequential_activation_renewals_alert_incident import SequentialActivationRenewalsAlertIncident
        from .stale_sign_in_alert_incident import StaleSignInAlertIncident
        from .too_many_global_admins_assigned_to_tenant_alert_incident import TooManyGlobalAdminsAssignedToTenantAlertIncident

        from .entity import Entity
        from .invalid_license_alert_incident import InvalidLicenseAlertIncident
        from .no_mfa_on_role_activation_alert_incident import NoMfaOnRoleActivationAlertIncident
        from .redundant_assignment_alert_incident import RedundantAssignmentAlertIncident
        from .roles_assigned_outside_privileged_identity_management_alert_incident import RolesAssignedOutsidePrivilegedIdentityManagementAlertIncident
        from .sequential_activation_renewals_alert_incident import SequentialActivationRenewalsAlertIncident
        from .stale_sign_in_alert_incident import StaleSignInAlertIncident
        from .too_many_global_admins_assigned_to_tenant_alert_incident import TooManyGlobalAdminsAssignedToTenantAlertIncident

        fields: dict[str, Callable[[Any], None]] = {
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
    

