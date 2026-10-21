from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .action_summary import ActionSummary
    from .authorization_system_identity import AuthorizationSystemIdentity
    from .finding import Finding
    from .identity_details import IdentityDetails
    from .inactive_aws_resource_finding import InactiveAwsResourceFinding
    from .inactive_aws_role_finding import InactiveAwsRoleFinding
    from .inactive_azure_service_principal_finding import InactiveAzureServicePrincipalFinding
    from .inactive_gcp_service_account_finding import InactiveGcpServiceAccountFinding
    from .inactive_serverless_function_finding import InactiveServerlessFunctionFinding
    from .inactive_user_finding import InactiveUserFinding
    from .overprovisioned_aws_resource_finding import OverprovisionedAwsResourceFinding
    from .overprovisioned_aws_role_finding import OverprovisionedAwsRoleFinding
    from .overprovisioned_azure_service_principal_finding import OverprovisionedAzureServicePrincipalFinding
    from .overprovisioned_gcp_service_account_finding import OverprovisionedGcpServiceAccountFinding
    from .overprovisioned_serverless_function_finding import OverprovisionedServerlessFunctionFinding
    from .overprovisioned_user_finding import OverprovisionedUserFinding
    from .permissions_creep_index import PermissionsCreepIndex
    from .super_aws_resource_finding import SuperAwsResourceFinding
    from .super_aws_role_finding import SuperAwsRoleFinding
    from .super_azure_service_principal_finding import SuperAzureServicePrincipalFinding
    from .super_gcp_service_account_finding import SuperGcpServiceAccountFinding
    from .super_serverless_function_finding import SuperServerlessFunctionFinding
    from .super_user_finding import SuperUserFinding
    from .unenforced_mfa_aws_user_finding import UnenforcedMfaAwsUserFinding

from .finding import Finding

@dataclass
class IdentityFinding(Finding, Parsable):
    # The actionSummary property
    action_summary: Optional[ActionSummary] = None
    # The identity property
    identity: Optional[AuthorizationSystemIdentity] = None
    # An identity's information details.
    identity_details: Optional[IdentityDetails] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The permissionsCreepIndex property
    permissions_creep_index: Optional[PermissionsCreepIndex] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IdentityFinding:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IdentityFinding
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.inactiveAwsResourceFinding".casefold():
            from .inactive_aws_resource_finding import InactiveAwsResourceFinding

            return InactiveAwsResourceFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.inactiveAwsRoleFinding".casefold():
            from .inactive_aws_role_finding import InactiveAwsRoleFinding

            return InactiveAwsRoleFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.inactiveAzureServicePrincipalFinding".casefold():
            from .inactive_azure_service_principal_finding import InactiveAzureServicePrincipalFinding

            return InactiveAzureServicePrincipalFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.inactiveGcpServiceAccountFinding".casefold():
            from .inactive_gcp_service_account_finding import InactiveGcpServiceAccountFinding

            return InactiveGcpServiceAccountFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.inactiveServerlessFunctionFinding".casefold():
            from .inactive_serverless_function_finding import InactiveServerlessFunctionFinding

            return InactiveServerlessFunctionFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.inactiveUserFinding".casefold():
            from .inactive_user_finding import InactiveUserFinding

            return InactiveUserFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.overprovisionedAwsResourceFinding".casefold():
            from .overprovisioned_aws_resource_finding import OverprovisionedAwsResourceFinding

            return OverprovisionedAwsResourceFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.overprovisionedAwsRoleFinding".casefold():
            from .overprovisioned_aws_role_finding import OverprovisionedAwsRoleFinding

            return OverprovisionedAwsRoleFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.overprovisionedAzureServicePrincipalFinding".casefold():
            from .overprovisioned_azure_service_principal_finding import OverprovisionedAzureServicePrincipalFinding

            return OverprovisionedAzureServicePrincipalFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.overprovisionedGcpServiceAccountFinding".casefold():
            from .overprovisioned_gcp_service_account_finding import OverprovisionedGcpServiceAccountFinding

            return OverprovisionedGcpServiceAccountFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.overprovisionedServerlessFunctionFinding".casefold():
            from .overprovisioned_serverless_function_finding import OverprovisionedServerlessFunctionFinding

            return OverprovisionedServerlessFunctionFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.overprovisionedUserFinding".casefold():
            from .overprovisioned_user_finding import OverprovisionedUserFinding

            return OverprovisionedUserFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.superAwsResourceFinding".casefold():
            from .super_aws_resource_finding import SuperAwsResourceFinding

            return SuperAwsResourceFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.superAwsRoleFinding".casefold():
            from .super_aws_role_finding import SuperAwsRoleFinding

            return SuperAwsRoleFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.superAzureServicePrincipalFinding".casefold():
            from .super_azure_service_principal_finding import SuperAzureServicePrincipalFinding

            return SuperAzureServicePrincipalFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.superGcpServiceAccountFinding".casefold():
            from .super_gcp_service_account_finding import SuperGcpServiceAccountFinding

            return SuperGcpServiceAccountFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.superServerlessFunctionFinding".casefold():
            from .super_serverless_function_finding import SuperServerlessFunctionFinding

            return SuperServerlessFunctionFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.superUserFinding".casefold():
            from .super_user_finding import SuperUserFinding

            return SuperUserFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unenforcedMfaAwsUserFinding".casefold():
            from .unenforced_mfa_aws_user_finding import UnenforcedMfaAwsUserFinding

            return UnenforcedMfaAwsUserFinding()
        return IdentityFinding()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .action_summary import ActionSummary
        from .authorization_system_identity import AuthorizationSystemIdentity
        from .finding import Finding
        from .identity_details import IdentityDetails
        from .inactive_aws_resource_finding import InactiveAwsResourceFinding
        from .inactive_aws_role_finding import InactiveAwsRoleFinding
        from .inactive_azure_service_principal_finding import InactiveAzureServicePrincipalFinding
        from .inactive_gcp_service_account_finding import InactiveGcpServiceAccountFinding
        from .inactive_serverless_function_finding import InactiveServerlessFunctionFinding
        from .inactive_user_finding import InactiveUserFinding
        from .overprovisioned_aws_resource_finding import OverprovisionedAwsResourceFinding
        from .overprovisioned_aws_role_finding import OverprovisionedAwsRoleFinding
        from .overprovisioned_azure_service_principal_finding import OverprovisionedAzureServicePrincipalFinding
        from .overprovisioned_gcp_service_account_finding import OverprovisionedGcpServiceAccountFinding
        from .overprovisioned_serverless_function_finding import OverprovisionedServerlessFunctionFinding
        from .overprovisioned_user_finding import OverprovisionedUserFinding
        from .permissions_creep_index import PermissionsCreepIndex
        from .super_aws_resource_finding import SuperAwsResourceFinding
        from .super_aws_role_finding import SuperAwsRoleFinding
        from .super_azure_service_principal_finding import SuperAzureServicePrincipalFinding
        from .super_gcp_service_account_finding import SuperGcpServiceAccountFinding
        from .super_serverless_function_finding import SuperServerlessFunctionFinding
        from .super_user_finding import SuperUserFinding
        from .unenforced_mfa_aws_user_finding import UnenforcedMfaAwsUserFinding

        from .action_summary import ActionSummary
        from .authorization_system_identity import AuthorizationSystemIdentity
        from .finding import Finding
        from .identity_details import IdentityDetails
        from .inactive_aws_resource_finding import InactiveAwsResourceFinding
        from .inactive_aws_role_finding import InactiveAwsRoleFinding
        from .inactive_azure_service_principal_finding import InactiveAzureServicePrincipalFinding
        from .inactive_gcp_service_account_finding import InactiveGcpServiceAccountFinding
        from .inactive_serverless_function_finding import InactiveServerlessFunctionFinding
        from .inactive_user_finding import InactiveUserFinding
        from .overprovisioned_aws_resource_finding import OverprovisionedAwsResourceFinding
        from .overprovisioned_aws_role_finding import OverprovisionedAwsRoleFinding
        from .overprovisioned_azure_service_principal_finding import OverprovisionedAzureServicePrincipalFinding
        from .overprovisioned_gcp_service_account_finding import OverprovisionedGcpServiceAccountFinding
        from .overprovisioned_serverless_function_finding import OverprovisionedServerlessFunctionFinding
        from .overprovisioned_user_finding import OverprovisionedUserFinding
        from .permissions_creep_index import PermissionsCreepIndex
        from .super_aws_resource_finding import SuperAwsResourceFinding
        from .super_aws_role_finding import SuperAwsRoleFinding
        from .super_azure_service_principal_finding import SuperAzureServicePrincipalFinding
        from .super_gcp_service_account_finding import SuperGcpServiceAccountFinding
        from .super_serverless_function_finding import SuperServerlessFunctionFinding
        from .super_user_finding import SuperUserFinding
        from .unenforced_mfa_aws_user_finding import UnenforcedMfaAwsUserFinding

        fields: dict[str, Callable[[Any], None]] = {
            "actionSummary": lambda n : setattr(self, 'action_summary', n.get_object_value(ActionSummary)),
            "identity": lambda n : setattr(self, 'identity', n.get_object_value(AuthorizationSystemIdentity)),
            "identityDetails": lambda n : setattr(self, 'identity_details', n.get_object_value(IdentityDetails)),
            "permissionsCreepIndex": lambda n : setattr(self, 'permissions_creep_index', n.get_object_value(PermissionsCreepIndex)),
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
        writer.write_object_value("actionSummary", self.action_summary)
        writer.write_object_value("identity", self.identity)
        writer.write_object_value("identityDetails", self.identity_details)
        writer.write_object_value("permissionsCreepIndex", self.permissions_creep_index)
    

