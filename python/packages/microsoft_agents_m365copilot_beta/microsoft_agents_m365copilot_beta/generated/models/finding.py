from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .aws_external_system_access_finding import AwsExternalSystemAccessFinding
    from .aws_external_system_access_role_finding import AwsExternalSystemAccessRoleFinding
    from .aws_identity_access_management_key_age_finding import AwsIdentityAccessManagementKeyAgeFinding
    from .aws_identity_access_management_key_usage_finding import AwsIdentityAccessManagementKeyUsageFinding
    from .aws_secret_information_access_finding import AwsSecretInformationAccessFinding
    from .aws_security_tool_administration_finding import AwsSecurityToolAdministrationFinding
    from .encrypted_aws_storage_bucket_finding import EncryptedAwsStorageBucketFinding
    from .encrypted_azure_storage_account_finding import EncryptedAzureStorageAccountFinding
    from .encrypted_gcp_storage_bucket_finding import EncryptedGcpStorageBucketFinding
    from .entity import Entity
    from .externally_accessible_aws_storage_bucket_finding import ExternallyAccessibleAwsStorageBucketFinding
    from .externally_accessible_azure_blob_container_finding import ExternallyAccessibleAzureBlobContainerFinding
    from .externally_accessible_gcp_storage_bucket_finding import ExternallyAccessibleGcpStorageBucketFinding
    from .identity_finding import IdentityFinding
    from .inactive_aws_resource_finding import InactiveAwsResourceFinding
    from .inactive_aws_role_finding import InactiveAwsRoleFinding
    from .inactive_azure_service_principal_finding import InactiveAzureServicePrincipalFinding
    from .inactive_gcp_service_account_finding import InactiveGcpServiceAccountFinding
    from .inactive_group_finding import InactiveGroupFinding
    from .inactive_serverless_function_finding import InactiveServerlessFunctionFinding
    from .inactive_user_finding import InactiveUserFinding
    from .open_aws_security_group_finding import OpenAwsSecurityGroupFinding
    from .open_network_azure_security_group_finding import OpenNetworkAzureSecurityGroupFinding
    from .overprovisioned_aws_resource_finding import OverprovisionedAwsResourceFinding
    from .overprovisioned_aws_role_finding import OverprovisionedAwsRoleFinding
    from .overprovisioned_azure_service_principal_finding import OverprovisionedAzureServicePrincipalFinding
    from .overprovisioned_gcp_service_account_finding import OverprovisionedGcpServiceAccountFinding
    from .overprovisioned_serverless_function_finding import OverprovisionedServerlessFunctionFinding
    from .overprovisioned_user_finding import OverprovisionedUserFinding
    from .privilege_escalation_aws_resource_finding import PrivilegeEscalationAwsResourceFinding
    from .privilege_escalation_aws_role_finding import PrivilegeEscalationAwsRoleFinding
    from .privilege_escalation_finding import PrivilegeEscalationFinding
    from .privilege_escalation_gcp_service_account_finding import PrivilegeEscalationGcpServiceAccountFinding
    from .privilege_escalation_user_finding import PrivilegeEscalationUserFinding
    from .secret_information_access_aws_resource_finding import SecretInformationAccessAwsResourceFinding
    from .secret_information_access_aws_role_finding import SecretInformationAccessAwsRoleFinding
    from .secret_information_access_aws_serverless_function_finding import SecretInformationAccessAwsServerlessFunctionFinding
    from .secret_information_access_aws_user_finding import SecretInformationAccessAwsUserFinding
    from .security_tool_aws_resource_administrator_finding import SecurityToolAwsResourceAdministratorFinding
    from .security_tool_aws_role_administrator_finding import SecurityToolAwsRoleAdministratorFinding
    from .security_tool_aws_serverless_function_administrator_finding import SecurityToolAwsServerlessFunctionAdministratorFinding
    from .security_tool_aws_user_administrator_finding import SecurityToolAwsUserAdministratorFinding
    from .super_aws_resource_finding import SuperAwsResourceFinding
    from .super_aws_role_finding import SuperAwsRoleFinding
    from .super_azure_service_principal_finding import SuperAzureServicePrincipalFinding
    from .super_gcp_service_account_finding import SuperGcpServiceAccountFinding
    from .super_serverless_function_finding import SuperServerlessFunctionFinding
    from .super_user_finding import SuperUserFinding
    from .unenforced_mfa_aws_user_finding import UnenforcedMfaAwsUserFinding
    from .virtual_machine_with_aws_storage_bucket_access_finding import VirtualMachineWithAwsStorageBucketAccessFinding

from .entity import Entity

@dataclass
class Finding(Entity, Parsable):
    # Defines when the finding was created.
    created_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Finding:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Finding
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.awsExternalSystemAccessFinding".casefold():
            from .aws_external_system_access_finding import AwsExternalSystemAccessFinding

            return AwsExternalSystemAccessFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.awsExternalSystemAccessRoleFinding".casefold():
            from .aws_external_system_access_role_finding import AwsExternalSystemAccessRoleFinding

            return AwsExternalSystemAccessRoleFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.awsIdentityAccessManagementKeyAgeFinding".casefold():
            from .aws_identity_access_management_key_age_finding import AwsIdentityAccessManagementKeyAgeFinding

            return AwsIdentityAccessManagementKeyAgeFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.awsIdentityAccessManagementKeyUsageFinding".casefold():
            from .aws_identity_access_management_key_usage_finding import AwsIdentityAccessManagementKeyUsageFinding

            return AwsIdentityAccessManagementKeyUsageFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.awsSecretInformationAccessFinding".casefold():
            from .aws_secret_information_access_finding import AwsSecretInformationAccessFinding

            return AwsSecretInformationAccessFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.awsSecurityToolAdministrationFinding".casefold():
            from .aws_security_tool_administration_finding import AwsSecurityToolAdministrationFinding

            return AwsSecurityToolAdministrationFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.encryptedAwsStorageBucketFinding".casefold():
            from .encrypted_aws_storage_bucket_finding import EncryptedAwsStorageBucketFinding

            return EncryptedAwsStorageBucketFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.encryptedAzureStorageAccountFinding".casefold():
            from .encrypted_azure_storage_account_finding import EncryptedAzureStorageAccountFinding

            return EncryptedAzureStorageAccountFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.encryptedGcpStorageBucketFinding".casefold():
            from .encrypted_gcp_storage_bucket_finding import EncryptedGcpStorageBucketFinding

            return EncryptedGcpStorageBucketFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externallyAccessibleAwsStorageBucketFinding".casefold():
            from .externally_accessible_aws_storage_bucket_finding import ExternallyAccessibleAwsStorageBucketFinding

            return ExternallyAccessibleAwsStorageBucketFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externallyAccessibleAzureBlobContainerFinding".casefold():
            from .externally_accessible_azure_blob_container_finding import ExternallyAccessibleAzureBlobContainerFinding

            return ExternallyAccessibleAzureBlobContainerFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externallyAccessibleGcpStorageBucketFinding".casefold():
            from .externally_accessible_gcp_storage_bucket_finding import ExternallyAccessibleGcpStorageBucketFinding

            return ExternallyAccessibleGcpStorageBucketFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityFinding".casefold():
            from .identity_finding import IdentityFinding

            return IdentityFinding()
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
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.inactiveGroupFinding".casefold():
            from .inactive_group_finding import InactiveGroupFinding

            return InactiveGroupFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.inactiveServerlessFunctionFinding".casefold():
            from .inactive_serverless_function_finding import InactiveServerlessFunctionFinding

            return InactiveServerlessFunctionFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.inactiveUserFinding".casefold():
            from .inactive_user_finding import InactiveUserFinding

            return InactiveUserFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.openAwsSecurityGroupFinding".casefold():
            from .open_aws_security_group_finding import OpenAwsSecurityGroupFinding

            return OpenAwsSecurityGroupFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.openNetworkAzureSecurityGroupFinding".casefold():
            from .open_network_azure_security_group_finding import OpenNetworkAzureSecurityGroupFinding

            return OpenNetworkAzureSecurityGroupFinding()
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
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegeEscalationAwsResourceFinding".casefold():
            from .privilege_escalation_aws_resource_finding import PrivilegeEscalationAwsResourceFinding

            return PrivilegeEscalationAwsResourceFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegeEscalationAwsRoleFinding".casefold():
            from .privilege_escalation_aws_role_finding import PrivilegeEscalationAwsRoleFinding

            return PrivilegeEscalationAwsRoleFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegeEscalationFinding".casefold():
            from .privilege_escalation_finding import PrivilegeEscalationFinding

            return PrivilegeEscalationFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegeEscalationGcpServiceAccountFinding".casefold():
            from .privilege_escalation_gcp_service_account_finding import PrivilegeEscalationGcpServiceAccountFinding

            return PrivilegeEscalationGcpServiceAccountFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegeEscalationUserFinding".casefold():
            from .privilege_escalation_user_finding import PrivilegeEscalationUserFinding

            return PrivilegeEscalationUserFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.secretInformationAccessAwsResourceFinding".casefold():
            from .secret_information_access_aws_resource_finding import SecretInformationAccessAwsResourceFinding

            return SecretInformationAccessAwsResourceFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.secretInformationAccessAwsRoleFinding".casefold():
            from .secret_information_access_aws_role_finding import SecretInformationAccessAwsRoleFinding

            return SecretInformationAccessAwsRoleFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.secretInformationAccessAwsServerlessFunctionFinding".casefold():
            from .secret_information_access_aws_serverless_function_finding import SecretInformationAccessAwsServerlessFunctionFinding

            return SecretInformationAccessAwsServerlessFunctionFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.secretInformationAccessAwsUserFinding".casefold():
            from .secret_information_access_aws_user_finding import SecretInformationAccessAwsUserFinding

            return SecretInformationAccessAwsUserFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.securityToolAwsResourceAdministratorFinding".casefold():
            from .security_tool_aws_resource_administrator_finding import SecurityToolAwsResourceAdministratorFinding

            return SecurityToolAwsResourceAdministratorFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.securityToolAwsRoleAdministratorFinding".casefold():
            from .security_tool_aws_role_administrator_finding import SecurityToolAwsRoleAdministratorFinding

            return SecurityToolAwsRoleAdministratorFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.securityToolAwsServerlessFunctionAdministratorFinding".casefold():
            from .security_tool_aws_serverless_function_administrator_finding import SecurityToolAwsServerlessFunctionAdministratorFinding

            return SecurityToolAwsServerlessFunctionAdministratorFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.securityToolAwsUserAdministratorFinding".casefold():
            from .security_tool_aws_user_administrator_finding import SecurityToolAwsUserAdministratorFinding

            return SecurityToolAwsUserAdministratorFinding()
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
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.virtualMachineWithAwsStorageBucketAccessFinding".casefold():
            from .virtual_machine_with_aws_storage_bucket_access_finding import VirtualMachineWithAwsStorageBucketAccessFinding

            return VirtualMachineWithAwsStorageBucketAccessFinding()
        return Finding()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .aws_external_system_access_finding import AwsExternalSystemAccessFinding
        from .aws_external_system_access_role_finding import AwsExternalSystemAccessRoleFinding
        from .aws_identity_access_management_key_age_finding import AwsIdentityAccessManagementKeyAgeFinding
        from .aws_identity_access_management_key_usage_finding import AwsIdentityAccessManagementKeyUsageFinding
        from .aws_secret_information_access_finding import AwsSecretInformationAccessFinding
        from .aws_security_tool_administration_finding import AwsSecurityToolAdministrationFinding
        from .encrypted_aws_storage_bucket_finding import EncryptedAwsStorageBucketFinding
        from .encrypted_azure_storage_account_finding import EncryptedAzureStorageAccountFinding
        from .encrypted_gcp_storage_bucket_finding import EncryptedGcpStorageBucketFinding
        from .entity import Entity
        from .externally_accessible_aws_storage_bucket_finding import ExternallyAccessibleAwsStorageBucketFinding
        from .externally_accessible_azure_blob_container_finding import ExternallyAccessibleAzureBlobContainerFinding
        from .externally_accessible_gcp_storage_bucket_finding import ExternallyAccessibleGcpStorageBucketFinding
        from .identity_finding import IdentityFinding
        from .inactive_aws_resource_finding import InactiveAwsResourceFinding
        from .inactive_aws_role_finding import InactiveAwsRoleFinding
        from .inactive_azure_service_principal_finding import InactiveAzureServicePrincipalFinding
        from .inactive_gcp_service_account_finding import InactiveGcpServiceAccountFinding
        from .inactive_group_finding import InactiveGroupFinding
        from .inactive_serverless_function_finding import InactiveServerlessFunctionFinding
        from .inactive_user_finding import InactiveUserFinding
        from .open_aws_security_group_finding import OpenAwsSecurityGroupFinding
        from .open_network_azure_security_group_finding import OpenNetworkAzureSecurityGroupFinding
        from .overprovisioned_aws_resource_finding import OverprovisionedAwsResourceFinding
        from .overprovisioned_aws_role_finding import OverprovisionedAwsRoleFinding
        from .overprovisioned_azure_service_principal_finding import OverprovisionedAzureServicePrincipalFinding
        from .overprovisioned_gcp_service_account_finding import OverprovisionedGcpServiceAccountFinding
        from .overprovisioned_serverless_function_finding import OverprovisionedServerlessFunctionFinding
        from .overprovisioned_user_finding import OverprovisionedUserFinding
        from .privilege_escalation_aws_resource_finding import PrivilegeEscalationAwsResourceFinding
        from .privilege_escalation_aws_role_finding import PrivilegeEscalationAwsRoleFinding
        from .privilege_escalation_finding import PrivilegeEscalationFinding
        from .privilege_escalation_gcp_service_account_finding import PrivilegeEscalationGcpServiceAccountFinding
        from .privilege_escalation_user_finding import PrivilegeEscalationUserFinding
        from .secret_information_access_aws_resource_finding import SecretInformationAccessAwsResourceFinding
        from .secret_information_access_aws_role_finding import SecretInformationAccessAwsRoleFinding
        from .secret_information_access_aws_serverless_function_finding import SecretInformationAccessAwsServerlessFunctionFinding
        from .secret_information_access_aws_user_finding import SecretInformationAccessAwsUserFinding
        from .security_tool_aws_resource_administrator_finding import SecurityToolAwsResourceAdministratorFinding
        from .security_tool_aws_role_administrator_finding import SecurityToolAwsRoleAdministratorFinding
        from .security_tool_aws_serverless_function_administrator_finding import SecurityToolAwsServerlessFunctionAdministratorFinding
        from .security_tool_aws_user_administrator_finding import SecurityToolAwsUserAdministratorFinding
        from .super_aws_resource_finding import SuperAwsResourceFinding
        from .super_aws_role_finding import SuperAwsRoleFinding
        from .super_azure_service_principal_finding import SuperAzureServicePrincipalFinding
        from .super_gcp_service_account_finding import SuperGcpServiceAccountFinding
        from .super_serverless_function_finding import SuperServerlessFunctionFinding
        from .super_user_finding import SuperUserFinding
        from .unenforced_mfa_aws_user_finding import UnenforcedMfaAwsUserFinding
        from .virtual_machine_with_aws_storage_bucket_access_finding import VirtualMachineWithAwsStorageBucketAccessFinding

        from .aws_external_system_access_finding import AwsExternalSystemAccessFinding
        from .aws_external_system_access_role_finding import AwsExternalSystemAccessRoleFinding
        from .aws_identity_access_management_key_age_finding import AwsIdentityAccessManagementKeyAgeFinding
        from .aws_identity_access_management_key_usage_finding import AwsIdentityAccessManagementKeyUsageFinding
        from .aws_secret_information_access_finding import AwsSecretInformationAccessFinding
        from .aws_security_tool_administration_finding import AwsSecurityToolAdministrationFinding
        from .encrypted_aws_storage_bucket_finding import EncryptedAwsStorageBucketFinding
        from .encrypted_azure_storage_account_finding import EncryptedAzureStorageAccountFinding
        from .encrypted_gcp_storage_bucket_finding import EncryptedGcpStorageBucketFinding
        from .entity import Entity
        from .externally_accessible_aws_storage_bucket_finding import ExternallyAccessibleAwsStorageBucketFinding
        from .externally_accessible_azure_blob_container_finding import ExternallyAccessibleAzureBlobContainerFinding
        from .externally_accessible_gcp_storage_bucket_finding import ExternallyAccessibleGcpStorageBucketFinding
        from .identity_finding import IdentityFinding
        from .inactive_aws_resource_finding import InactiveAwsResourceFinding
        from .inactive_aws_role_finding import InactiveAwsRoleFinding
        from .inactive_azure_service_principal_finding import InactiveAzureServicePrincipalFinding
        from .inactive_gcp_service_account_finding import InactiveGcpServiceAccountFinding
        from .inactive_group_finding import InactiveGroupFinding
        from .inactive_serverless_function_finding import InactiveServerlessFunctionFinding
        from .inactive_user_finding import InactiveUserFinding
        from .open_aws_security_group_finding import OpenAwsSecurityGroupFinding
        from .open_network_azure_security_group_finding import OpenNetworkAzureSecurityGroupFinding
        from .overprovisioned_aws_resource_finding import OverprovisionedAwsResourceFinding
        from .overprovisioned_aws_role_finding import OverprovisionedAwsRoleFinding
        from .overprovisioned_azure_service_principal_finding import OverprovisionedAzureServicePrincipalFinding
        from .overprovisioned_gcp_service_account_finding import OverprovisionedGcpServiceAccountFinding
        from .overprovisioned_serverless_function_finding import OverprovisionedServerlessFunctionFinding
        from .overprovisioned_user_finding import OverprovisionedUserFinding
        from .privilege_escalation_aws_resource_finding import PrivilegeEscalationAwsResourceFinding
        from .privilege_escalation_aws_role_finding import PrivilegeEscalationAwsRoleFinding
        from .privilege_escalation_finding import PrivilegeEscalationFinding
        from .privilege_escalation_gcp_service_account_finding import PrivilegeEscalationGcpServiceAccountFinding
        from .privilege_escalation_user_finding import PrivilegeEscalationUserFinding
        from .secret_information_access_aws_resource_finding import SecretInformationAccessAwsResourceFinding
        from .secret_information_access_aws_role_finding import SecretInformationAccessAwsRoleFinding
        from .secret_information_access_aws_serverless_function_finding import SecretInformationAccessAwsServerlessFunctionFinding
        from .secret_information_access_aws_user_finding import SecretInformationAccessAwsUserFinding
        from .security_tool_aws_resource_administrator_finding import SecurityToolAwsResourceAdministratorFinding
        from .security_tool_aws_role_administrator_finding import SecurityToolAwsRoleAdministratorFinding
        from .security_tool_aws_serverless_function_administrator_finding import SecurityToolAwsServerlessFunctionAdministratorFinding
        from .security_tool_aws_user_administrator_finding import SecurityToolAwsUserAdministratorFinding
        from .super_aws_resource_finding import SuperAwsResourceFinding
        from .super_aws_role_finding import SuperAwsRoleFinding
        from .super_azure_service_principal_finding import SuperAzureServicePrincipalFinding
        from .super_gcp_service_account_finding import SuperGcpServiceAccountFinding
        from .super_serverless_function_finding import SuperServerlessFunctionFinding
        from .super_user_finding import SuperUserFinding
        from .unenforced_mfa_aws_user_finding import UnenforcedMfaAwsUserFinding
        from .virtual_machine_with_aws_storage_bucket_access_finding import VirtualMachineWithAwsStorageBucketAccessFinding

        fields: dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
    

