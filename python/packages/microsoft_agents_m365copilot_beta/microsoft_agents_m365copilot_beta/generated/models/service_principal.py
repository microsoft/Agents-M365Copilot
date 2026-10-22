from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .add_in import AddIn
    from .agent_identity import AgentIdentity
    from .agent_identity_blueprint_principal import AgentIdentityBlueprintPrincipal
    from .app_management_policy import AppManagementPolicy
    from .app_role import AppRole
    from .app_role_assignment import AppRoleAssignment
    from .claims_mapping_policy import ClaimsMappingPolicy
    from .custom_claims_policy import CustomClaimsPolicy
    from .custom_security_attribute_value import CustomSecurityAttributeValue
    from .delegated_permission_classification import DelegatedPermissionClassification
    from .directory_object import DirectoryObject
    from .endpoint import Endpoint
    from .federated_identity_credential import FederatedIdentityCredential
    from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy
    from .identity_governance.identity_lifecycle import IdentityLifecycle
    from .informational_url import InformationalUrl
    from .key_credential import KeyCredential
    from .license_details import LicenseDetails
    from .o_auth2_permission_grant import OAuth2PermissionGrant
    from .password_credential import PasswordCredential
    from .password_single_sign_on_settings import PasswordSingleSignOnSettings
    from .permission_grant_pre_approval_policy import PermissionGrantPreApprovalPolicy
    from .permission_scope import PermissionScope
    from .remote_desktop_security_configuration import RemoteDesktopSecurityConfiguration
    from .saml_single_sign_on_settings import SamlSingleSignOnSettings
    from .synchronization import Synchronization
    from .token_issuance_policy import TokenIssuancePolicy
    from .token_lifetime_policy import TokenLifetimePolicy
    from .verified_publisher import VerifiedPublisher

from .directory_object import DirectoryObject

@dataclass
class ServicePrincipal(DirectoryObject, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.servicePrincipal"
    # true if the service principal account is enabled; otherwise, false. If set to false, then no users are able to sign in to this app, even if they're assigned to it. Supports $filter (eq, ne, not, in).
    account_enabled: Optional[bool] = None
    # Defines custom behavior that a consuming service can use to call an app in specific contexts. For example, applications that can render file streams may set the addIns property for its 'FileHandler' functionality. This lets services like Microsoft 365 call the application in the context of a document the user is working on.
    add_ins: Optional[list[AddIn]] = None
    # Used to retrieve service principals by subscription, identify resource group and full resource IDs for managed identities. Supports $filter (eq, not, ge, le, startsWith).
    alternative_names: Optional[list[str]] = None
    # The description exposed by the associated application.
    app_description: Optional[str] = None
    # The display name exposed by the associated application. Maximum length is 256 characters.
    app_display_name: Optional[str] = None
    # The unique identifier for the associated application (its appId property). Alternate key. Supports $filter (eq, ne, not, in, startsWith).
    app_id: Optional[str] = None
    # The appManagementPolicy applied to this service principal.
    app_management_policies: Optional[list[AppManagementPolicy]] = None
    # Contains the tenant ID where the application is registered. This is applicable only to service principals backed by applications. Supports $filter (eq, ne, NOT, ge, le).
    app_owner_organization_id: Optional[UUID] = None
    # App role assignments for this app or service, granted to users, groups, and other service principals.Supports $expand.
    app_role_assigned_to: Optional[list[AppRoleAssignment]] = None
    # Specifies whether users or other service principals need to be granted an app role assignment for this service principal before users can sign in or apps can get tokens. The default value is false. Not nullable. Supports $filter (eq, ne, NOT).
    app_role_assignment_required: Optional[bool] = None
    # App role assignment for another app or service, granted to this service principal. Supports $expand.
    app_role_assignments: Optional[list[AppRoleAssignment]] = None
    # The roles exposed by the application, which this service principal represents. For more information, see the appRoles property definition on the application entity. Not nullable. App roles and exposed delegated permission scopes (publishedPermissionScopes) share a default limit of 700 permission definitions per service principal, including definitions inherited from the application and definitions added directly to the service principal. Enabled and disabled definitions both count. This limit counts definitions, not app role assignments. For counting rules, behavior for existing objects above the limit, and design guidance, see App role limits.
    app_roles: Optional[list[AppRole]] = None
    # Unique identifier of the applicationTemplate. Supports $filter (eq, not, ne). Read-only. null if the app wasn't created from an application template.
    application_template_id: Optional[str] = None
    # The claimsMappingPolicies assigned to this service principal. Supports $expand.
    claims_mapping_policies: Optional[list[ClaimsMappingPolicy]] = None
    # A claims policy that allows application admins to customize the claims that will be emitted in tokens affected by this policy.
    claims_policy: Optional[CustomClaimsPolicy] = None
    # The appId of the application that created this service principal. Set internally by Microsoft Entra ID. Read-only.
    created_by_app_id: Optional[str] = None
    # Directory objects created by this service principal. Read-only. Nullable.
    created_objects: Optional[list[DirectoryObject]] = None
    # An open complex type that holds the value of a custom security attribute that is assigned to a directory object. Nullable. Requires $select to retrieve. Supports $filter (eq, ne, not, startsWith). Filter value is case sensitive.To read this property, the calling app must be assigned the CustomSecAttributeAssignment.Read.All permission. To write this property, the calling app must be assigned the CustomSecAttributeAssignment.ReadWrite.All permissions. To read or write this property in delegated scenarios, the admin must be assigned the Attribute Assignment Administrator role.
    custom_security_attributes: Optional[CustomSecurityAttributeValue] = None
    # The permission classifications for delegated permissions exposed by the app that this service principal represents. Supports $expand.
    delegated_permission_classifications: Optional[list[DelegatedPermissionClassification]] = None
    # Free text field to provide an internal end-user facing description of the service principal. End-user portals such MyApps displays the application description in this field. The maximum allowed size is 1,024 characters. Supports $filter (eq, ne, not, ge, le, startsWith) and $search.
    description: Optional[str] = None
    # Specifies whether Microsoft has disabled the registered application. The possible values are: null (default value), NotDisabled, and DisabledDueToViolationOfServicesAgreement (reasons may include suspicious, abusive, or malicious activity, or a violation of the Microsoft Services Agreement).  Supports $filter (eq, ne, not).
    disabled_by_microsoft_status: Optional[str] = None
    # The display name for the service principal. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values), $search, and $orderby.
    display_name: Optional[str] = None
    # Endpoints available for discovery. Services like Sharepoint populate this property with a tenant specific SharePoint endpoints that other applications can discover and use in their experiences.
    endpoints: Optional[list[Endpoint]] = None
    # Deprecated. Don't use.
    error_url: Optional[str] = None
    # The federatedIdentityCredentials property
    federated_identity_credentials: Optional[list[FederatedIdentityCredential]] = None
    # The homeRealmDiscoveryPolicies assigned to this service principal. Supports $expand.
    home_realm_discovery_policies: Optional[list[HomeRealmDiscoveryPolicy]] = None
    # Home page or landing page of the application.
    homepage: Optional[str] = None
    # Basic profile information of the acquired application such as app's marketing, support, terms of service and privacy statement URLs. The terms of service and privacy statement are surfaced to users through the user consent experience. For more info, see How to: Add Terms of service and privacy statement for registered Microsoft Entra apps. Supports $filter (eq, ne, not, ge, le, and eq on null values).
    info: Optional[InformationalUrl] = None
    # Specifies whether the service principal of the app in a tenant or across tenants for multi-tenant apps can obtain new access tokens or access protected resources. When set to true, existing tokens remain valid until they expire based on their configured lifetimes, and the app stays visible in the Enterprise apps list but users cannot sign in.true if the application is deactivated (disabled); otherwise false.
    is_disabled: Optional[bool] = None
    # The collection of key credentials associated with the service principal. Not nullable. Supports $filter (eq, not, ge, le).
    key_credentials: Optional[list[KeyCredential]] = None
    # The licenseDetails property
    license_details: Optional[list[LicenseDetails]] = None
    # The lifecycle governance state of the agent identity backed by this service principal.
    lifecycle: Optional[IdentityLifecycle] = None
    # Specifies the URL where the service provider redirects the user to Microsoft Entra ID to authenticate. Microsoft Entra ID uses the URL to launch the application from Microsoft 365 or the Microsoft Entra My Apps. When blank, Microsoft Entra ID performs IdP-initiated sign-on for applications configured with SAML-based single sign-on. The user launches the application from Microsoft 365, the Microsoft Entra My Apps, or the Microsoft Entra SSO URL.
    login_url: Optional[str] = None
    # Specifies the URL that the Microsoft's authorization service uses to sign out a user using OpenId Connect front-channel, back-channel, or SAML sign out protocols.
    logout_url: Optional[str] = None
    # Roles that this service principal is a member of. HTTP Methods: GET Read-only. Nullable. Supports $expand.
    member_of: Optional[list[DirectoryObject]] = None
    # Free text field to capture information about the service principal, typically used for operational purposes. Maximum allowed size is 1,024 characters.
    notes: Optional[str] = None
    # Specifies the list of email addresses where Microsoft Entra ID sends a notification when the active certificate is near the expiration date. This is only for the certificates used to sign the SAML token issued for Microsoft Entra Gallery applications.
    notification_email_addresses: Optional[list[str]] = None
    # Delegated permission grants authorizing this service principal to access an API on behalf of a signed-in user. Read-only. Nullable.
    oauth2_permission_grants: Optional[list[OAuth2PermissionGrant]] = None
    # Directory objects that are owned by this service principal. Read-only. Nullable. Supports $expand and $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1).
    owned_objects: Optional[list[DirectoryObject]] = None
    # Directory objects that are owners of this servicePrincipal. The owners are a set of nonadmin users or servicePrincipals who are allowed to modify this object. Supports $expand and $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1).
    owners: Optional[list[DirectoryObject]] = None
    # The collection of password credentials associated with the service principal. Not nullable.
    password_credentials: Optional[list[PasswordCredential]] = None
    # The collection for settings related to password single sign-on. Use $select=passwordSingleSignOnSettings to read the property. Read-only for applicationTemplates except for custom applicationTemplates.
    password_single_sign_on_settings: Optional[PasswordSingleSignOnSettings] = None
    # The permissionGrantPreApprovalPolicies property
    permission_grant_pre_approval_policies: Optional[list[PermissionGrantPreApprovalPolicy]] = None
    # Specifies the single sign-on mode configured for this application. Microsoft Entra ID uses the preferred single sign-on mode to launch the application from Microsoft 365 or the Microsoft Entra My Apps. The supported values are password, saml, notSupported, and oidc. Note: This field might be null for older SAML apps and for OIDC applications where it isn't set automatically.
    preferred_single_sign_on_mode: Optional[str] = None
    # Specifies the expiration date of the keyCredential used for token signing, marked by preferredTokenSigningKeyThumbprint. Updating this attribute isn't currently supported. For details, see ServicePrincipal property differences.
    preferred_token_signing_key_end_date_time: Optional[datetime.datetime] = None
    # This property can be used on SAML applications (apps that have preferredSingleSignOnMode set to saml) to control which certificate is used to sign the SAML responses. For applications that aren't SAML, don't write or otherwise rely on this property.
    preferred_token_signing_key_thumbprint: Optional[str] = None
    # The delegated permissions exposed by the application. For more information, see the oauth2PermissionScopes property on the application entity's api property. Not nullable. Note: This property is named oauth2PermissionScopes in v1.0. These scopes and appRoles share a default limit of 700 permission definitions per service principal. Enabled and disabled definitions both count. For counting rules, behavior for existing objects above the limit, and design guidance, see App role limits.
    published_permission_scopes: Optional[list[PermissionScope]] = None
    # The name of the Microsoft Entra tenant that published the application.
    publisher_name: Optional[str] = None
    # The remoteDesktopSecurityConfiguration object applied to this service principal. Supports $filter (eq) for isRemoteDesktopProtocolEnabled property.
    remote_desktop_security_configuration: Optional[RemoteDesktopSecurityConfiguration] = None
    # The URLs that user tokens are sent to for sign in with the associated application, or the redirect URIs that OAuth 2.0 authorization codes and access tokens are sent to for the associated application. Not nullable.
    reply_urls: Optional[list[str]] = None
    # The url where the service exposes SAML metadata for federation.
    saml_metadata_url: Optional[str] = None
    # The collection for settings related to saml single sign-on.
    saml_single_sign_on_settings: Optional[SamlSingleSignOnSettings] = None
    # Contains the list of identifiersUris, copied over from the associated application. More values can be added to hybrid applications. These values can be used to identify the permissions exposed by this app within Microsoft Entra ID. For example,Client apps can specify a resource URI that is based on the values of this property to acquire an access token, which is the URI returned in the 'aud' claim.The any operator is required for filter expressions on multi-valued properties. Not nullable.  Supports $filter (eq, not, ge, le, startsWith).
    service_principal_names: Optional[list[str]] = None
    # Identifies if the service principal represents an application or a managed identity. This property is set by Microsoft Entra ID internally. For a service principal that represents an application this is set as Application. For a service principal that represents a managed identity this is set as ManagedIdentity.For a service principal that represents an agent identity, this is set to ServiceIdentity. The SocialIdp type is for internal use.
    service_principal_type: Optional[str] = None
    # Specifies the Microsoft accounts that are supported for the current application. Read-only. Supported values are:AzureADMyOrg: Users with a Microsoft work or school account in my organization's Microsoft Entra tenant (single-tenant).AzureADMultipleOrgs: Users with a Microsoft work or school account in any organization's Microsoft Entra tenant (multitenant).AzureADandPersonalMicrosoftAccount: Users with a personal Microsoft account, or a work or school account in any organization's Microsoft Entra tenant.PersonalMicrosoftAccount: Users with a personal Microsoft account only.
    sign_in_audience: Optional[str] = None
    # Represents the capability for Microsoft Entra identity synchronization through the Microsoft Graph API.
    synchronization: Optional[Synchronization] = None
    # Custom strings that can be used to categorize and identify the service principal. Not nullable. The value is the union of strings set here and on the associated application entity's tags property.Supports $filter (eq, not, ge, le, startsWith).
    tags: Optional[list[str]] = None
    # Specifies the keyId of a public key from the keyCredentials collection. When configured, Microsoft Entra ID issues tokens for this application encrypted using the key specified by this property. The application code that receives the encrypted token must use the matching private key to decrypt the token before it can be used for the signed-in user.
    token_encryption_key_id: Optional[UUID] = None
    # The tokenIssuancePolicies assigned to this service principal. Supports $expand.
    token_issuance_policies: Optional[list[TokenIssuancePolicy]] = None
    # The tokenLifetimePolicies assigned to this service principal. Supports $expand.
    token_lifetime_policies: Optional[list[TokenLifetimePolicy]] = None
    # The transitiveMemberOf property
    transitive_member_of: Optional[list[DirectoryObject]] = None
    # Specifies the verified publisher of the application that's linked to this service principal.
    verified_publisher: Optional[VerifiedPublisher] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ServicePrincipal:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ServicePrincipal
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.agentIdentity".casefold():
            from .agent_identity import AgentIdentity

            return AgentIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.agentIdentityBlueprintPrincipal".casefold():
            from .agent_identity_blueprint_principal import AgentIdentityBlueprintPrincipal

            return AgentIdentityBlueprintPrincipal()
        return ServicePrincipal()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .add_in import AddIn
        from .agent_identity import AgentIdentity
        from .agent_identity_blueprint_principal import AgentIdentityBlueprintPrincipal
        from .app_management_policy import AppManagementPolicy
        from .app_role import AppRole
        from .app_role_assignment import AppRoleAssignment
        from .claims_mapping_policy import ClaimsMappingPolicy
        from .custom_claims_policy import CustomClaimsPolicy
        from .custom_security_attribute_value import CustomSecurityAttributeValue
        from .delegated_permission_classification import DelegatedPermissionClassification
        from .directory_object import DirectoryObject
        from .endpoint import Endpoint
        from .federated_identity_credential import FederatedIdentityCredential
        from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy
        from .identity_governance.identity_lifecycle import IdentityLifecycle
        from .informational_url import InformationalUrl
        from .key_credential import KeyCredential
        from .license_details import LicenseDetails
        from .o_auth2_permission_grant import OAuth2PermissionGrant
        from .password_credential import PasswordCredential
        from .password_single_sign_on_settings import PasswordSingleSignOnSettings
        from .permission_grant_pre_approval_policy import PermissionGrantPreApprovalPolicy
        from .permission_scope import PermissionScope
        from .remote_desktop_security_configuration import RemoteDesktopSecurityConfiguration
        from .saml_single_sign_on_settings import SamlSingleSignOnSettings
        from .synchronization import Synchronization
        from .token_issuance_policy import TokenIssuancePolicy
        from .token_lifetime_policy import TokenLifetimePolicy
        from .verified_publisher import VerifiedPublisher

        from .add_in import AddIn
        from .agent_identity import AgentIdentity
        from .agent_identity_blueprint_principal import AgentIdentityBlueprintPrincipal
        from .app_management_policy import AppManagementPolicy
        from .app_role import AppRole
        from .app_role_assignment import AppRoleAssignment
        from .claims_mapping_policy import ClaimsMappingPolicy
        from .custom_claims_policy import CustomClaimsPolicy
        from .custom_security_attribute_value import CustomSecurityAttributeValue
        from .delegated_permission_classification import DelegatedPermissionClassification
        from .directory_object import DirectoryObject
        from .endpoint import Endpoint
        from .federated_identity_credential import FederatedIdentityCredential
        from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy
        from .identity_governance.identity_lifecycle import IdentityLifecycle
        from .informational_url import InformationalUrl
        from .key_credential import KeyCredential
        from .license_details import LicenseDetails
        from .o_auth2_permission_grant import OAuth2PermissionGrant
        from .password_credential import PasswordCredential
        from .password_single_sign_on_settings import PasswordSingleSignOnSettings
        from .permission_grant_pre_approval_policy import PermissionGrantPreApprovalPolicy
        from .permission_scope import PermissionScope
        from .remote_desktop_security_configuration import RemoteDesktopSecurityConfiguration
        from .saml_single_sign_on_settings import SamlSingleSignOnSettings
        from .synchronization import Synchronization
        from .token_issuance_policy import TokenIssuancePolicy
        from .token_lifetime_policy import TokenLifetimePolicy
        from .verified_publisher import VerifiedPublisher

        fields: dict[str, Callable[[Any], None]] = {
            "accountEnabled": lambda n : setattr(self, 'account_enabled', n.get_bool_value()),
            "addIns": lambda n : setattr(self, 'add_ins', n.get_collection_of_object_values(AddIn)),
            "alternativeNames": lambda n : setattr(self, 'alternative_names', n.get_collection_of_primitive_values(str)),
            "appDescription": lambda n : setattr(self, 'app_description', n.get_str_value()),
            "appDisplayName": lambda n : setattr(self, 'app_display_name', n.get_str_value()),
            "appId": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "appManagementPolicies": lambda n : setattr(self, 'app_management_policies', n.get_collection_of_object_values(AppManagementPolicy)),
            "appOwnerOrganizationId": lambda n : setattr(self, 'app_owner_organization_id', n.get_uuid_value()),
            "appRoleAssignedTo": lambda n : setattr(self, 'app_role_assigned_to', n.get_collection_of_object_values(AppRoleAssignment)),
            "appRoleAssignmentRequired": lambda n : setattr(self, 'app_role_assignment_required', n.get_bool_value()),
            "appRoleAssignments": lambda n : setattr(self, 'app_role_assignments', n.get_collection_of_object_values(AppRoleAssignment)),
            "appRoles": lambda n : setattr(self, 'app_roles', n.get_collection_of_object_values(AppRole)),
            "applicationTemplateId": lambda n : setattr(self, 'application_template_id', n.get_str_value()),
            "claimsMappingPolicies": lambda n : setattr(self, 'claims_mapping_policies', n.get_collection_of_object_values(ClaimsMappingPolicy)),
            "claimsPolicy": lambda n : setattr(self, 'claims_policy', n.get_object_value(CustomClaimsPolicy)),
            "createdByAppId": lambda n : setattr(self, 'created_by_app_id', n.get_str_value()),
            "createdObjects": lambda n : setattr(self, 'created_objects', n.get_collection_of_object_values(DirectoryObject)),
            "customSecurityAttributes": lambda n : setattr(self, 'custom_security_attributes', n.get_object_value(CustomSecurityAttributeValue)),
            "delegatedPermissionClassifications": lambda n : setattr(self, 'delegated_permission_classifications', n.get_collection_of_object_values(DelegatedPermissionClassification)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "disabledByMicrosoftStatus": lambda n : setattr(self, 'disabled_by_microsoft_status', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "endpoints": lambda n : setattr(self, 'endpoints', n.get_collection_of_object_values(Endpoint)),
            "errorUrl": lambda n : setattr(self, 'error_url', n.get_str_value()),
            "federatedIdentityCredentials": lambda n : setattr(self, 'federated_identity_credentials', n.get_collection_of_object_values(FederatedIdentityCredential)),
            "homeRealmDiscoveryPolicies": lambda n : setattr(self, 'home_realm_discovery_policies', n.get_collection_of_object_values(HomeRealmDiscoveryPolicy)),
            "homepage": lambda n : setattr(self, 'homepage', n.get_str_value()),
            "info": lambda n : setattr(self, 'info', n.get_object_value(InformationalUrl)),
            "isDisabled": lambda n : setattr(self, 'is_disabled', n.get_bool_value()),
            "keyCredentials": lambda n : setattr(self, 'key_credentials', n.get_collection_of_object_values(KeyCredential)),
            "licenseDetails": lambda n : setattr(self, 'license_details', n.get_collection_of_object_values(LicenseDetails)),
            "lifecycle": lambda n : setattr(self, 'lifecycle', n.get_object_value(IdentityLifecycle)),
            "loginUrl": lambda n : setattr(self, 'login_url', n.get_str_value()),
            "logoutUrl": lambda n : setattr(self, 'logout_url', n.get_str_value()),
            "memberOf": lambda n : setattr(self, 'member_of', n.get_collection_of_object_values(DirectoryObject)),
            "notes": lambda n : setattr(self, 'notes', n.get_str_value()),
            "notificationEmailAddresses": lambda n : setattr(self, 'notification_email_addresses', n.get_collection_of_primitive_values(str)),
            "oauth2PermissionGrants": lambda n : setattr(self, 'oauth2_permission_grants', n.get_collection_of_object_values(OAuth2PermissionGrant)),
            "ownedObjects": lambda n : setattr(self, 'owned_objects', n.get_collection_of_object_values(DirectoryObject)),
            "owners": lambda n : setattr(self, 'owners', n.get_collection_of_object_values(DirectoryObject)),
            "passwordCredentials": lambda n : setattr(self, 'password_credentials', n.get_collection_of_object_values(PasswordCredential)),
            "passwordSingleSignOnSettings": lambda n : setattr(self, 'password_single_sign_on_settings', n.get_object_value(PasswordSingleSignOnSettings)),
            "permissionGrantPreApprovalPolicies": lambda n : setattr(self, 'permission_grant_pre_approval_policies', n.get_collection_of_object_values(PermissionGrantPreApprovalPolicy)),
            "preferredSingleSignOnMode": lambda n : setattr(self, 'preferred_single_sign_on_mode', n.get_str_value()),
            "preferredTokenSigningKeyEndDateTime": lambda n : setattr(self, 'preferred_token_signing_key_end_date_time', n.get_datetime_value()),
            "preferredTokenSigningKeyThumbprint": lambda n : setattr(self, 'preferred_token_signing_key_thumbprint', n.get_str_value()),
            "publishedPermissionScopes": lambda n : setattr(self, 'published_permission_scopes', n.get_collection_of_object_values(PermissionScope)),
            "publisherName": lambda n : setattr(self, 'publisher_name', n.get_str_value()),
            "remoteDesktopSecurityConfiguration": lambda n : setattr(self, 'remote_desktop_security_configuration', n.get_object_value(RemoteDesktopSecurityConfiguration)),
            "replyUrls": lambda n : setattr(self, 'reply_urls', n.get_collection_of_primitive_values(str)),
            "samlMetadataUrl": lambda n : setattr(self, 'saml_metadata_url', n.get_str_value()),
            "samlSingleSignOnSettings": lambda n : setattr(self, 'saml_single_sign_on_settings', n.get_object_value(SamlSingleSignOnSettings)),
            "servicePrincipalNames": lambda n : setattr(self, 'service_principal_names', n.get_collection_of_primitive_values(str)),
            "servicePrincipalType": lambda n : setattr(self, 'service_principal_type', n.get_str_value()),
            "signInAudience": lambda n : setattr(self, 'sign_in_audience', n.get_str_value()),
            "synchronization": lambda n : setattr(self, 'synchronization', n.get_object_value(Synchronization)),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_primitive_values(str)),
            "tokenEncryptionKeyId": lambda n : setattr(self, 'token_encryption_key_id', n.get_uuid_value()),
            "tokenIssuancePolicies": lambda n : setattr(self, 'token_issuance_policies', n.get_collection_of_object_values(TokenIssuancePolicy)),
            "tokenLifetimePolicies": lambda n : setattr(self, 'token_lifetime_policies', n.get_collection_of_object_values(TokenLifetimePolicy)),
            "transitiveMemberOf": lambda n : setattr(self, 'transitive_member_of', n.get_collection_of_object_values(DirectoryObject)),
            "verifiedPublisher": lambda n : setattr(self, 'verified_publisher', n.get_object_value(VerifiedPublisher)),
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
        writer.write_bool_value("accountEnabled", self.account_enabled)
        writer.write_collection_of_object_values("addIns", self.add_ins)
        writer.write_collection_of_primitive_values("alternativeNames", self.alternative_names)
        writer.write_str_value("appDescription", self.app_description)
        writer.write_str_value("appDisplayName", self.app_display_name)
        writer.write_str_value("appId", self.app_id)
        writer.write_collection_of_object_values("appManagementPolicies", self.app_management_policies)
        writer.write_uuid_value("appOwnerOrganizationId", self.app_owner_organization_id)
        writer.write_collection_of_object_values("appRoleAssignedTo", self.app_role_assigned_to)
        writer.write_bool_value("appRoleAssignmentRequired", self.app_role_assignment_required)
        writer.write_collection_of_object_values("appRoleAssignments", self.app_role_assignments)
        writer.write_collection_of_object_values("appRoles", self.app_roles)
        writer.write_str_value("applicationTemplateId", self.application_template_id)
        writer.write_collection_of_object_values("claimsMappingPolicies", self.claims_mapping_policies)
        writer.write_object_value("claimsPolicy", self.claims_policy)
        writer.write_str_value("createdByAppId", self.created_by_app_id)
        writer.write_collection_of_object_values("createdObjects", self.created_objects)
        writer.write_object_value("customSecurityAttributes", self.custom_security_attributes)
        writer.write_collection_of_object_values("delegatedPermissionClassifications", self.delegated_permission_classifications)
        writer.write_str_value("description", self.description)
        writer.write_str_value("disabledByMicrosoftStatus", self.disabled_by_microsoft_status)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("endpoints", self.endpoints)
        writer.write_str_value("errorUrl", self.error_url)
        writer.write_collection_of_object_values("federatedIdentityCredentials", self.federated_identity_credentials)
        writer.write_collection_of_object_values("homeRealmDiscoveryPolicies", self.home_realm_discovery_policies)
        writer.write_str_value("homepage", self.homepage)
        writer.write_object_value("info", self.info)
        writer.write_bool_value("isDisabled", self.is_disabled)
        writer.write_collection_of_object_values("keyCredentials", self.key_credentials)
        writer.write_collection_of_object_values("licenseDetails", self.license_details)
        writer.write_object_value("lifecycle", self.lifecycle)
        writer.write_str_value("loginUrl", self.login_url)
        writer.write_str_value("logoutUrl", self.logout_url)
        writer.write_collection_of_object_values("memberOf", self.member_of)
        writer.write_str_value("notes", self.notes)
        writer.write_collection_of_primitive_values("notificationEmailAddresses", self.notification_email_addresses)
        writer.write_collection_of_object_values("oauth2PermissionGrants", self.oauth2_permission_grants)
        writer.write_collection_of_object_values("ownedObjects", self.owned_objects)
        writer.write_collection_of_object_values("owners", self.owners)
        writer.write_collection_of_object_values("passwordCredentials", self.password_credentials)
        writer.write_object_value("passwordSingleSignOnSettings", self.password_single_sign_on_settings)
        writer.write_collection_of_object_values("permissionGrantPreApprovalPolicies", self.permission_grant_pre_approval_policies)
        writer.write_str_value("preferredSingleSignOnMode", self.preferred_single_sign_on_mode)
        writer.write_datetime_value("preferredTokenSigningKeyEndDateTime", self.preferred_token_signing_key_end_date_time)
        writer.write_str_value("preferredTokenSigningKeyThumbprint", self.preferred_token_signing_key_thumbprint)
        writer.write_collection_of_object_values("publishedPermissionScopes", self.published_permission_scopes)
        writer.write_str_value("publisherName", self.publisher_name)
        writer.write_object_value("remoteDesktopSecurityConfiguration", self.remote_desktop_security_configuration)
        writer.write_collection_of_primitive_values("replyUrls", self.reply_urls)
        writer.write_str_value("samlMetadataUrl", self.saml_metadata_url)
        writer.write_object_value("samlSingleSignOnSettings", self.saml_single_sign_on_settings)
        writer.write_collection_of_primitive_values("servicePrincipalNames", self.service_principal_names)
        writer.write_str_value("servicePrincipalType", self.service_principal_type)
        writer.write_str_value("signInAudience", self.sign_in_audience)
        writer.write_object_value("synchronization", self.synchronization)
        writer.write_collection_of_primitive_values("tags", self.tags)
        writer.write_uuid_value("tokenEncryptionKeyId", self.token_encryption_key_id)
        writer.write_collection_of_object_values("tokenIssuancePolicies", self.token_issuance_policies)
        writer.write_collection_of_object_values("tokenLifetimePolicies", self.token_lifetime_policies)
        writer.write_collection_of_object_values("transitiveMemberOf", self.transitive_member_of)
        writer.write_object_value("verifiedPublisher", self.verified_publisher)
    

