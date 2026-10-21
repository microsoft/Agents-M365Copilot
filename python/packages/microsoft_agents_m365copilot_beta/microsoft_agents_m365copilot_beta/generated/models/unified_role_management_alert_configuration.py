from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .invalid_license_alert_configuration import InvalidLicenseAlertConfiguration
    from .no_mfa_on_role_activation_alert_configuration import NoMfaOnRoleActivationAlertConfiguration
    from .redundant_assignment_alert_configuration import RedundantAssignmentAlertConfiguration
    from .roles_assigned_outside_privileged_identity_management_alert_configuration import RolesAssignedOutsidePrivilegedIdentityManagementAlertConfiguration
    from .sequential_activation_renewals_alert_configuration import SequentialActivationRenewalsAlertConfiguration
    from .stale_sign_in_alert_configuration import StaleSignInAlertConfiguration
    from .too_many_global_admins_assigned_to_tenant_alert_configuration import TooManyGlobalAdminsAssignedToTenantAlertConfiguration
    from .unified_role_management_alert_definition import UnifiedRoleManagementAlertDefinition

from .entity import Entity

@dataclass
class UnifiedRoleManagementAlertConfiguration(Entity, Parsable):
    # The definition of the alert that contains its description, impact, and measures to mitigate or prevent it. Supports $expand.
    alert_definition: Optional[UnifiedRoleManagementAlertDefinition] = None
    # The identifier of an alert definition. Supports $filter (eq, ne).
    alert_definition_id: Optional[str] = None
    # true if the alert is enabled. Setting it to false disables PIM scanning the tenant to identify instances that trigger the alert.
    is_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The identifier of the scope to which the alert is related. Only / is supported to represent the tenant scope. Supports $filter (eq, ne).
    scope_id: Optional[str] = None
    # The type of scope where the alert is created. DirectoryRole is the only currently supported scope type for Microsoft Entra roles.
    scope_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UnifiedRoleManagementAlertConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleManagementAlertConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.invalidLicenseAlertConfiguration".casefold():
            from .invalid_license_alert_configuration import InvalidLicenseAlertConfiguration

            return InvalidLicenseAlertConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.noMfaOnRoleActivationAlertConfiguration".casefold():
            from .no_mfa_on_role_activation_alert_configuration import NoMfaOnRoleActivationAlertConfiguration

            return NoMfaOnRoleActivationAlertConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.redundantAssignmentAlertConfiguration".casefold():
            from .redundant_assignment_alert_configuration import RedundantAssignmentAlertConfiguration

            return RedundantAssignmentAlertConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.rolesAssignedOutsidePrivilegedIdentityManagementAlertConfiguration".casefold():
            from .roles_assigned_outside_privileged_identity_management_alert_configuration import RolesAssignedOutsidePrivilegedIdentityManagementAlertConfiguration

            return RolesAssignedOutsidePrivilegedIdentityManagementAlertConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sequentialActivationRenewalsAlertConfiguration".casefold():
            from .sequential_activation_renewals_alert_configuration import SequentialActivationRenewalsAlertConfiguration

            return SequentialActivationRenewalsAlertConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.staleSignInAlertConfiguration".casefold():
            from .stale_sign_in_alert_configuration import StaleSignInAlertConfiguration

            return StaleSignInAlertConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.tooManyGlobalAdminsAssignedToTenantAlertConfiguration".casefold():
            from .too_many_global_admins_assigned_to_tenant_alert_configuration import TooManyGlobalAdminsAssignedToTenantAlertConfiguration

            return TooManyGlobalAdminsAssignedToTenantAlertConfiguration()
        return UnifiedRoleManagementAlertConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .invalid_license_alert_configuration import InvalidLicenseAlertConfiguration
        from .no_mfa_on_role_activation_alert_configuration import NoMfaOnRoleActivationAlertConfiguration
        from .redundant_assignment_alert_configuration import RedundantAssignmentAlertConfiguration
        from .roles_assigned_outside_privileged_identity_management_alert_configuration import RolesAssignedOutsidePrivilegedIdentityManagementAlertConfiguration
        from .sequential_activation_renewals_alert_configuration import SequentialActivationRenewalsAlertConfiguration
        from .stale_sign_in_alert_configuration import StaleSignInAlertConfiguration
        from .too_many_global_admins_assigned_to_tenant_alert_configuration import TooManyGlobalAdminsAssignedToTenantAlertConfiguration
        from .unified_role_management_alert_definition import UnifiedRoleManagementAlertDefinition

        from .entity import Entity
        from .invalid_license_alert_configuration import InvalidLicenseAlertConfiguration
        from .no_mfa_on_role_activation_alert_configuration import NoMfaOnRoleActivationAlertConfiguration
        from .redundant_assignment_alert_configuration import RedundantAssignmentAlertConfiguration
        from .roles_assigned_outside_privileged_identity_management_alert_configuration import RolesAssignedOutsidePrivilegedIdentityManagementAlertConfiguration
        from .sequential_activation_renewals_alert_configuration import SequentialActivationRenewalsAlertConfiguration
        from .stale_sign_in_alert_configuration import StaleSignInAlertConfiguration
        from .too_many_global_admins_assigned_to_tenant_alert_configuration import TooManyGlobalAdminsAssignedToTenantAlertConfiguration
        from .unified_role_management_alert_definition import UnifiedRoleManagementAlertDefinition

        fields: dict[str, Callable[[Any], None]] = {
            "alertDefinition": lambda n : setattr(self, 'alert_definition', n.get_object_value(UnifiedRoleManagementAlertDefinition)),
            "alertDefinitionId": lambda n : setattr(self, 'alert_definition_id', n.get_str_value()),
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "scopeId": lambda n : setattr(self, 'scope_id', n.get_str_value()),
            "scopeType": lambda n : setattr(self, 'scope_type', n.get_str_value()),
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
        writer.write_object_value("alertDefinition", self.alert_definition)
        writer.write_str_value("alertDefinitionId", self.alert_definition_id)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_str_value("scopeId", self.scope_id)
        writer.write_str_value("scopeType", self.scope_type)
    

