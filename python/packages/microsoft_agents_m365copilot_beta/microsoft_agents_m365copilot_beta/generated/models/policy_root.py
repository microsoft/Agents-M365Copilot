from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_review_policy import AccessReviewPolicy
    from .activity_based_timeout_policy import ActivityBasedTimeoutPolicy
    from .admin_consent_request_policy import AdminConsentRequestPolicy
    from .app_management_policy import AppManagementPolicy
    from .authentication_flows_policy import AuthenticationFlowsPolicy
    from .authentication_methods_policy import AuthenticationMethodsPolicy
    from .authentication_strength_policy import AuthenticationStrengthPolicy
    from .authorization_policy import AuthorizationPolicy
    from .b2b_management_policy import B2bManagementPolicy
    from .b2c_authentication_methods_policy import B2cAuthenticationMethodsPolicy
    from .claims_mapping_policy import ClaimsMappingPolicy
    from .conditional_access_policy import ConditionalAccessPolicy
    from .cross_tenant_access_policy import CrossTenantAccessPolicy
    from .device_registration_policy import DeviceRegistrationPolicy
    from .directory_role_access_review_policy import DirectoryRoleAccessReviewPolicy
    from .entity import Entity
    from .external_identities_policy import ExternalIdentitiesPolicy
    from .feature_rollout_policy import FeatureRolloutPolicy
    from .federated_token_validation_policy import FederatedTokenValidationPolicy
    from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy
    from .identity_security_defaults_enforcement_policy import IdentitySecurityDefaultsEnforcementPolicy
    from .mobile_app_management_policy import MobileAppManagementPolicy
    from .mobile_device_management_policy import MobileDeviceManagementPolicy
    from .on_prem_authentication_policy import OnPremAuthenticationPolicy
    from .ownerless_group_policy import OwnerlessGroupPolicy
    from .permission_grant_policy import PermissionGrantPolicy
    from .permission_grant_pre_approval_policy import PermissionGrantPreApprovalPolicy
    from .policy_deletable_root import PolicyDeletableRoot
    from .service_principal_creation_policy import ServicePrincipalCreationPolicy
    from .tenant_app_management_policy import TenantAppManagementPolicy
    from .token_issuance_policy import TokenIssuancePolicy
    from .token_lifetime_policy import TokenLifetimePolicy
    from .unified_role_management_policy import UnifiedRoleManagementPolicy
    from .unified_role_management_policy_assignment import UnifiedRoleManagementPolicyAssignment

from .entity import Entity

@dataclass
class PolicyRoot(Entity, Parsable):
    # The policy that contains directory-level access review settings.
    access_review_policy: Optional[AccessReviewPolicy] = None
    # The policy that controls the idle time-out for web sessions for applications.
    activity_based_timeout_policies: Optional[list[ActivityBasedTimeoutPolicy]] = None
    # The policy by which consent requests are created and managed for the entire tenant.
    admin_consent_request_policy: Optional[AdminConsentRequestPolicy] = None
    # The policies that enforce app management restrictions for specific applications and service principals, overriding the defaultAppManagementPolicy.
    app_management_policies: Optional[list[AppManagementPolicy]] = None
    # The policy configuration of the self-service sign-up experience of guests.
    authentication_flows_policy: Optional[AuthenticationFlowsPolicy] = None
    # The authentication methods and the users that are allowed to use them to sign in and perform multifactor authentication (MFA) in Microsoft Entra ID.
    authentication_methods_policy: Optional[AuthenticationMethodsPolicy] = None
    # The authentication method combinations that are to be used in scenarios defined by Microsoft Entra Conditional Access.
    authentication_strength_policies: Optional[list[AuthenticationStrengthPolicy]] = None
    # The policy that controls Microsoft Entra authorization settings.
    authorization_policy: Optional[list[AuthorizationPolicy]] = None
    # The policy to manage Microsoft Entra B2B features in Microsoft Entra External ID for workforce tenants.
    b2b_management_policies: Optional[list[B2bManagementPolicy]] = None
    # The Azure AD B2C policies that define how end users register via local accounts.
    b2c_authentication_methods_policy: Optional[B2cAuthenticationMethodsPolicy] = None
    # The claim-mapping policies for WS-Fed, SAML, OAuth 2.0, and OpenID Connect protocols, for tokens issued to a specific application.
    claims_mapping_policies: Optional[list[ClaimsMappingPolicy]] = None
    # The custom rules that define an access scenario.
    conditional_access_policies: Optional[list[ConditionalAccessPolicy]] = None
    # The custom rules that define an access scenario when interacting with external Microsoft Entra tenants.
    cross_tenant_access_policy: Optional[CrossTenantAccessPolicy] = None
    # The tenant-wide policy that enforces app management restrictions for all applications and service principals.
    default_app_management_policy: Optional[TenantAppManagementPolicy] = None
    # Policies that support soft-delete functionality and can be restored within 30 days.
    deleted_items: Optional[PolicyDeletableRoot] = None
    # Represents the policy scope that controls quota restrictions, additional authentication, and authorization policies to register device identities to your organization.
    device_registration_policy: Optional[DeviceRegistrationPolicy] = None
    # The directoryRoleAccessReviewPolicy property
    directory_role_access_review_policy: Optional[DirectoryRoleAccessReviewPolicy] = None
    # Represents the tenant-wide policy that controls whether guests can leave a Microsoft Entra tenant via self-service controls.
    external_identities_policy: Optional[ExternalIdentitiesPolicy] = None
    # The feature rollout policy associated with a directory object.
    feature_rollout_policies: Optional[list[FeatureRolloutPolicy]] = None
    # Represents a policy to control enabling or disabling validation of federation authentication tokens.
    federated_token_validation_policy: Optional[FederatedTokenValidationPolicy] = None
    # The policy to control Microsoft Entra authentication behavior for federated users.
    home_realm_discovery_policies: Optional[list[HomeRealmDiscoveryPolicy]] = None
    # The policy that represents the security defaults that protect against common attacks.
    identity_security_defaults_enforcement_policy: Optional[IdentitySecurityDefaultsEnforcementPolicy] = None
    # The policy that defines autoenrollment configuration for a mobility management (MDM or MAM) application.
    mobile_app_management_policies: Optional[list[MobileAppManagementPolicy]] = None
    # The mobileDeviceManagementPolicies property
    mobile_device_management_policies: Optional[list[MobileDeviceManagementPolicy]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The policy that controls how authentication requests from on-premises environments are managed.
    on_prem_authentication_policies: Optional[list[OnPremAuthenticationPolicy]] = None
    # The policy configuration for managing groups that have lost their sole owner.
    ownerless_group_policy: Optional[OwnerlessGroupPolicy] = None
    # The policy that specifies the conditions under which consent can be granted.
    permission_grant_policies: Optional[list[PermissionGrantPolicy]] = None
    # Policies that specify the conditions under which consent can be granted to a specific application.
    permission_grant_pre_approval_policies: Optional[list[PermissionGrantPreApprovalPolicy]] = None
    # Represents the role management policies.
    role_management_policies: Optional[list[UnifiedRoleManagementPolicy]] = None
    # Represents the role management policy assignments.
    role_management_policy_assignments: Optional[list[UnifiedRoleManagementPolicyAssignment]] = None
    # The servicePrincipalCreationPolicies property
    service_principal_creation_policies: Optional[list[ServicePrincipalCreationPolicy]] = None
    # The policy that specifies the characteristics of SAML tokens issued by Microsoft Entra ID.
    token_issuance_policies: Optional[list[TokenIssuancePolicy]] = None
    # The policy that controls the lifetime of a JWT access token, an ID token, or a SAML 1.1/2.0 token issued by Microsoft Entra ID.
    token_lifetime_policies: Optional[list[TokenLifetimePolicy]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PolicyRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PolicyRoot
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PolicyRoot()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_review_policy import AccessReviewPolicy
        from .activity_based_timeout_policy import ActivityBasedTimeoutPolicy
        from .admin_consent_request_policy import AdminConsentRequestPolicy
        from .app_management_policy import AppManagementPolicy
        from .authentication_flows_policy import AuthenticationFlowsPolicy
        from .authentication_methods_policy import AuthenticationMethodsPolicy
        from .authentication_strength_policy import AuthenticationStrengthPolicy
        from .authorization_policy import AuthorizationPolicy
        from .b2b_management_policy import B2bManagementPolicy
        from .b2c_authentication_methods_policy import B2cAuthenticationMethodsPolicy
        from .claims_mapping_policy import ClaimsMappingPolicy
        from .conditional_access_policy import ConditionalAccessPolicy
        from .cross_tenant_access_policy import CrossTenantAccessPolicy
        from .device_registration_policy import DeviceRegistrationPolicy
        from .directory_role_access_review_policy import DirectoryRoleAccessReviewPolicy
        from .entity import Entity
        from .external_identities_policy import ExternalIdentitiesPolicy
        from .feature_rollout_policy import FeatureRolloutPolicy
        from .federated_token_validation_policy import FederatedTokenValidationPolicy
        from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy
        from .identity_security_defaults_enforcement_policy import IdentitySecurityDefaultsEnforcementPolicy
        from .mobile_app_management_policy import MobileAppManagementPolicy
        from .mobile_device_management_policy import MobileDeviceManagementPolicy
        from .on_prem_authentication_policy import OnPremAuthenticationPolicy
        from .ownerless_group_policy import OwnerlessGroupPolicy
        from .permission_grant_policy import PermissionGrantPolicy
        from .permission_grant_pre_approval_policy import PermissionGrantPreApprovalPolicy
        from .policy_deletable_root import PolicyDeletableRoot
        from .service_principal_creation_policy import ServicePrincipalCreationPolicy
        from .tenant_app_management_policy import TenantAppManagementPolicy
        from .token_issuance_policy import TokenIssuancePolicy
        from .token_lifetime_policy import TokenLifetimePolicy
        from .unified_role_management_policy import UnifiedRoleManagementPolicy
        from .unified_role_management_policy_assignment import UnifiedRoleManagementPolicyAssignment

        from .access_review_policy import AccessReviewPolicy
        from .activity_based_timeout_policy import ActivityBasedTimeoutPolicy
        from .admin_consent_request_policy import AdminConsentRequestPolicy
        from .app_management_policy import AppManagementPolicy
        from .authentication_flows_policy import AuthenticationFlowsPolicy
        from .authentication_methods_policy import AuthenticationMethodsPolicy
        from .authentication_strength_policy import AuthenticationStrengthPolicy
        from .authorization_policy import AuthorizationPolicy
        from .b2b_management_policy import B2bManagementPolicy
        from .b2c_authentication_methods_policy import B2cAuthenticationMethodsPolicy
        from .claims_mapping_policy import ClaimsMappingPolicy
        from .conditional_access_policy import ConditionalAccessPolicy
        from .cross_tenant_access_policy import CrossTenantAccessPolicy
        from .device_registration_policy import DeviceRegistrationPolicy
        from .directory_role_access_review_policy import DirectoryRoleAccessReviewPolicy
        from .entity import Entity
        from .external_identities_policy import ExternalIdentitiesPolicy
        from .feature_rollout_policy import FeatureRolloutPolicy
        from .federated_token_validation_policy import FederatedTokenValidationPolicy
        from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy
        from .identity_security_defaults_enforcement_policy import IdentitySecurityDefaultsEnforcementPolicy
        from .mobile_app_management_policy import MobileAppManagementPolicy
        from .mobile_device_management_policy import MobileDeviceManagementPolicy
        from .on_prem_authentication_policy import OnPremAuthenticationPolicy
        from .ownerless_group_policy import OwnerlessGroupPolicy
        from .permission_grant_policy import PermissionGrantPolicy
        from .permission_grant_pre_approval_policy import PermissionGrantPreApprovalPolicy
        from .policy_deletable_root import PolicyDeletableRoot
        from .service_principal_creation_policy import ServicePrincipalCreationPolicy
        from .tenant_app_management_policy import TenantAppManagementPolicy
        from .token_issuance_policy import TokenIssuancePolicy
        from .token_lifetime_policy import TokenLifetimePolicy
        from .unified_role_management_policy import UnifiedRoleManagementPolicy
        from .unified_role_management_policy_assignment import UnifiedRoleManagementPolicyAssignment

        fields: dict[str, Callable[[Any], None]] = {
            "accessReviewPolicy": lambda n : setattr(self, 'access_review_policy', n.get_object_value(AccessReviewPolicy)),
            "activityBasedTimeoutPolicies": lambda n : setattr(self, 'activity_based_timeout_policies', n.get_collection_of_object_values(ActivityBasedTimeoutPolicy)),
            "adminConsentRequestPolicy": lambda n : setattr(self, 'admin_consent_request_policy', n.get_object_value(AdminConsentRequestPolicy)),
            "appManagementPolicies": lambda n : setattr(self, 'app_management_policies', n.get_collection_of_object_values(AppManagementPolicy)),
            "authenticationFlowsPolicy": lambda n : setattr(self, 'authentication_flows_policy', n.get_object_value(AuthenticationFlowsPolicy)),
            "authenticationMethodsPolicy": lambda n : setattr(self, 'authentication_methods_policy', n.get_object_value(AuthenticationMethodsPolicy)),
            "authenticationStrengthPolicies": lambda n : setattr(self, 'authentication_strength_policies', n.get_collection_of_object_values(AuthenticationStrengthPolicy)),
            "authorizationPolicy": lambda n : setattr(self, 'authorization_policy', n.get_collection_of_object_values(AuthorizationPolicy)),
            "b2bManagementPolicies": lambda n : setattr(self, 'b2b_management_policies', n.get_collection_of_object_values(B2bManagementPolicy)),
            "b2cAuthenticationMethodsPolicy": lambda n : setattr(self, 'b2c_authentication_methods_policy', n.get_object_value(B2cAuthenticationMethodsPolicy)),
            "claimsMappingPolicies": lambda n : setattr(self, 'claims_mapping_policies', n.get_collection_of_object_values(ClaimsMappingPolicy)),
            "conditionalAccessPolicies": lambda n : setattr(self, 'conditional_access_policies', n.get_collection_of_object_values(ConditionalAccessPolicy)),
            "crossTenantAccessPolicy": lambda n : setattr(self, 'cross_tenant_access_policy', n.get_object_value(CrossTenantAccessPolicy)),
            "defaultAppManagementPolicy": lambda n : setattr(self, 'default_app_management_policy', n.get_object_value(TenantAppManagementPolicy)),
            "deletedItems": lambda n : setattr(self, 'deleted_items', n.get_object_value(PolicyDeletableRoot)),
            "deviceRegistrationPolicy": lambda n : setattr(self, 'device_registration_policy', n.get_object_value(DeviceRegistrationPolicy)),
            "directoryRoleAccessReviewPolicy": lambda n : setattr(self, 'directory_role_access_review_policy', n.get_object_value(DirectoryRoleAccessReviewPolicy)),
            "externalIdentitiesPolicy": lambda n : setattr(self, 'external_identities_policy', n.get_object_value(ExternalIdentitiesPolicy)),
            "featureRolloutPolicies": lambda n : setattr(self, 'feature_rollout_policies', n.get_collection_of_object_values(FeatureRolloutPolicy)),
            "federatedTokenValidationPolicy": lambda n : setattr(self, 'federated_token_validation_policy', n.get_object_value(FederatedTokenValidationPolicy)),
            "homeRealmDiscoveryPolicies": lambda n : setattr(self, 'home_realm_discovery_policies', n.get_collection_of_object_values(HomeRealmDiscoveryPolicy)),
            "identitySecurityDefaultsEnforcementPolicy": lambda n : setattr(self, 'identity_security_defaults_enforcement_policy', n.get_object_value(IdentitySecurityDefaultsEnforcementPolicy)),
            "mobileAppManagementPolicies": lambda n : setattr(self, 'mobile_app_management_policies', n.get_collection_of_object_values(MobileAppManagementPolicy)),
            "mobileDeviceManagementPolicies": lambda n : setattr(self, 'mobile_device_management_policies', n.get_collection_of_object_values(MobileDeviceManagementPolicy)),
            "onPremAuthenticationPolicies": lambda n : setattr(self, 'on_prem_authentication_policies', n.get_collection_of_object_values(OnPremAuthenticationPolicy)),
            "ownerlessGroupPolicy": lambda n : setattr(self, 'ownerless_group_policy', n.get_object_value(OwnerlessGroupPolicy)),
            "permissionGrantPolicies": lambda n : setattr(self, 'permission_grant_policies', n.get_collection_of_object_values(PermissionGrantPolicy)),
            "permissionGrantPreApprovalPolicies": lambda n : setattr(self, 'permission_grant_pre_approval_policies', n.get_collection_of_object_values(PermissionGrantPreApprovalPolicy)),
            "roleManagementPolicies": lambda n : setattr(self, 'role_management_policies', n.get_collection_of_object_values(UnifiedRoleManagementPolicy)),
            "roleManagementPolicyAssignments": lambda n : setattr(self, 'role_management_policy_assignments', n.get_collection_of_object_values(UnifiedRoleManagementPolicyAssignment)),
            "servicePrincipalCreationPolicies": lambda n : setattr(self, 'service_principal_creation_policies', n.get_collection_of_object_values(ServicePrincipalCreationPolicy)),
            "tokenIssuancePolicies": lambda n : setattr(self, 'token_issuance_policies', n.get_collection_of_object_values(TokenIssuancePolicy)),
            "tokenLifetimePolicies": lambda n : setattr(self, 'token_lifetime_policies', n.get_collection_of_object_values(TokenLifetimePolicy)),
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
        writer.write_object_value("accessReviewPolicy", self.access_review_policy)
        writer.write_collection_of_object_values("activityBasedTimeoutPolicies", self.activity_based_timeout_policies)
        writer.write_object_value("adminConsentRequestPolicy", self.admin_consent_request_policy)
        writer.write_collection_of_object_values("appManagementPolicies", self.app_management_policies)
        writer.write_object_value("authenticationFlowsPolicy", self.authentication_flows_policy)
        writer.write_object_value("authenticationMethodsPolicy", self.authentication_methods_policy)
        writer.write_collection_of_object_values("authenticationStrengthPolicies", self.authentication_strength_policies)
        writer.write_collection_of_object_values("authorizationPolicy", self.authorization_policy)
        writer.write_collection_of_object_values("b2bManagementPolicies", self.b2b_management_policies)
        writer.write_object_value("b2cAuthenticationMethodsPolicy", self.b2c_authentication_methods_policy)
        writer.write_collection_of_object_values("claimsMappingPolicies", self.claims_mapping_policies)
        writer.write_collection_of_object_values("conditionalAccessPolicies", self.conditional_access_policies)
        writer.write_object_value("crossTenantAccessPolicy", self.cross_tenant_access_policy)
        writer.write_object_value("defaultAppManagementPolicy", self.default_app_management_policy)
        writer.write_object_value("deletedItems", self.deleted_items)
        writer.write_object_value("deviceRegistrationPolicy", self.device_registration_policy)
        writer.write_object_value("directoryRoleAccessReviewPolicy", self.directory_role_access_review_policy)
        writer.write_object_value("externalIdentitiesPolicy", self.external_identities_policy)
        writer.write_collection_of_object_values("featureRolloutPolicies", self.feature_rollout_policies)
        writer.write_object_value("federatedTokenValidationPolicy", self.federated_token_validation_policy)
        writer.write_collection_of_object_values("homeRealmDiscoveryPolicies", self.home_realm_discovery_policies)
        writer.write_object_value("identitySecurityDefaultsEnforcementPolicy", self.identity_security_defaults_enforcement_policy)
        writer.write_collection_of_object_values("mobileAppManagementPolicies", self.mobile_app_management_policies)
        writer.write_collection_of_object_values("mobileDeviceManagementPolicies", self.mobile_device_management_policies)
        writer.write_collection_of_object_values("onPremAuthenticationPolicies", self.on_prem_authentication_policies)
        writer.write_object_value("ownerlessGroupPolicy", self.ownerless_group_policy)
        writer.write_collection_of_object_values("permissionGrantPolicies", self.permission_grant_policies)
        writer.write_collection_of_object_values("permissionGrantPreApprovalPolicies", self.permission_grant_pre_approval_policies)
        writer.write_collection_of_object_values("roleManagementPolicies", self.role_management_policies)
        writer.write_collection_of_object_values("roleManagementPolicyAssignments", self.role_management_policy_assignments)
        writer.write_collection_of_object_values("servicePrincipalCreationPolicies", self.service_principal_creation_policies)
        writer.write_collection_of_object_values("tokenIssuancePolicies", self.token_issuance_policies)
        writer.write_collection_of_object_values("tokenLifetimePolicies", self.token_lifetime_policies)
    

