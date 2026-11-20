from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .agentic.agent_sign_in import AgentSignIn
    from .applied_authentication_event_listener import AppliedAuthenticationEventListener
    from .applied_conditional_access_policy import AppliedConditionalAccessPolicy
    from .authentication_app_device_details import AuthenticationAppDeviceDetails
    from .authentication_app_policy_details import AuthenticationAppPolicyDetails
    from .authentication_context import AuthenticationContext
    from .authentication_detail import AuthenticationDetail
    from .authentication_requirement_policy import AuthenticationRequirementPolicy
    from .client_credential_type import ClientCredentialType
    from .conditional_access_status import ConditionalAccessStatus
    from .device_detail import DeviceDetail
    from .entity import Entity
    from .incoming_token_type import IncomingTokenType
    from .key_value import KeyValue
    from .managed_identity import ManagedIdentity
    from .mfa_detail import MfaDetail
    from .network_location_detail import NetworkLocationDetail
    from .original_transfer_methods import OriginalTransferMethods
    from .private_link_details import PrivateLinkDetails
    from .protocol_type import ProtocolType
    from .risk_detail import RiskDetail
    from .risk_level import RiskLevel
    from .risk_state import RiskState
    from .session_lifetime_policy import SessionLifetimePolicy
    from .sign_in_access_type import SignInAccessType
    from .sign_in_identifier_type import SignInIdentifierType
    from .sign_in_location import SignInLocation
    from .sign_in_status import SignInStatus
    from .sign_in_user_type import SignInUserType
    from .token_issuer_type import TokenIssuerType
    from .token_protection_status import TokenProtectionStatus
    from .token_protection_status_details import TokenProtectionStatusDetails

from .entity import Entity

@dataclass
class SignIn(Entity, Parsable):
    # Represents details about the agentic sign-in. Includes the type of agent as well as parentAppID in some cases
    agent: Optional[AgentSignIn] = None
    # The application name displayed in the Microsoft Entra admin center.  Supports $filter (eq, startsWith).
    app_display_name: Optional[str] = None
    # The application identifier in Microsoft Entra ID.  Supports $filter (eq).
    app_id: Optional[str] = None
    # The identifier of the tenant that owns the client application.  Supports $filter (eq).
    app_owner_tenant_id: Optional[str] = None
    # Deprecated. Use tokenProtectionStatusDetails instead. Token protection creates a cryptographically secure tie between the token and the device it's issued to. This field indicates whether the app token was bound to the device.
    app_token_protection_status: Optional[TokenProtectionStatus] = None
    # A list of conditional access policies that the corresponding sign-in activity triggers. Apps need more Conditional Access-related privileges to read the details of this property. For more information, see Permissions for viewing applied conditional access (CA) policies in sign-ins.
    applied_conditional_access_policies: Optional[list[AppliedConditionalAccessPolicy]] = None
    # Detailed information about the listeners, such as Azure Logic Apps and Azure Functions, which the corresponding events in the sign-in event triggered.
    applied_event_listeners: Optional[list[AppliedAuthenticationEventListener]] = None
    # Provides details about the app and device used during a Microsoft Entra authentication step.
    authentication_app_device_details: Optional[AuthenticationAppDeviceDetails] = None
    # Provides details of the Microsoft Entra policies applied to a user and client authentication app during an authentication step.
    authentication_app_policy_evaluation_details: Optional[list[AuthenticationAppPolicyDetails]] = None
    # Contains a collection of values that represent the conditional access authentication contexts applied to the sign-in.
    authentication_context_class_references: Optional[list[AuthenticationContext]] = None
    # The result of the authentication attempt and more details on the authentication method.
    authentication_details: Optional[list[AuthenticationDetail]] = None
    # The authentication methods used. Possible values: SMS, Authenticator App, App Verification code, Password, FIDO, PTA, or PHS.
    authentication_methods_used: Optional[list[str]] = None
    # More authentication processing details, such as the agent name for PTA and PHS, or a server or farm name for federated authentication.
    authentication_processing_details: Optional[list[KeyValue]] = None
    # Lists the protocol type or grant type used in the authentication. The possible values are: none, oAuth2, ropc, wsFederation, saml20, deviceCode, unknownFutureValue, authenticationTransfer, nativeAuth, implicitAccessTokenAndGetResponseMode, implicitIdTokenAndGetResponseMode, implicitAccessTokenAndPostResponseMode, implicitIdTokenAndPostResponseMode, authorizationCodeWithoutPkce, authorizationCodeWithPkce, clientCredentials, refreshTokenGrant, encryptedAuthorizeResponse, directUserGrant, kerberos, prtGrant, seamlessSso, prtBrokerBased, prtNonBrokerBased, onBehalfOf, samlOnBehalfOf. Use the Prefer: include-unknown-enum-members request header to get the following values from this evolvable enum: authenticationTransfer , nativeAuth , implicitAccessTokenAndGetResponseMode , implicitIdTokenAndGetResponseMode , implicitAccessTokenAndPostResponseMode , implicitIdTokenAndPostResponseMode , authorizationCodeWithoutPkce , authorizationCodeWithPkce , clientCredentials , refreshTokenGrant , encryptedAuthorizeResponse , directUserGrant , kerberos , prtGrant , seamlessSso , prtBrokerBased , prtNonBrokerBased , onBehalfOf , samlOnBehalfOf.
    authentication_protocol: Optional[ProtocolType] = None
    # The authentication stage reached during sign-in. It doesn't account for previously satisfied claims. If primary authentication fails, the sign-in attempt is not evaluated by Conditional Access, so the resulting value is singleFactorAuthentication.  Supports $filter (eq, startsWith).
    authentication_requirement: Optional[str] = None
    # Sources of authentication requirement, such as conditional access, per-user MFA, identity protection, and security defaults.
    authentication_requirement_policies: Optional[list[AuthenticationRequirementPolicy]] = None
    # The Autonomous System Number (ASN) of the network used by the actor.
    autonomous_system_number: Optional[int] = None
    # Contains a fully qualified Azure Resource Manager ID of an Azure resource accessed during the sign-in.
    azure_resource_id: Optional[str] = None
    # The legacy client used for sign-in activity. For example: Browser, Exchange ActiveSync, Modern clients, IMAP, MAPI, SMTP, or POP.  Supports $filter (eq).
    client_app_used: Optional[str] = None
    # Describes the credential type that a user client or service principal provided to Microsoft Entra ID to authenticate itself. You can review this property to track and eliminate less secure credential types or to watch for clients and service principals using anomalous credential types. The possible values are: none, clientSecret, clientAssertion, federatedIdentityCredential, managedIdentity, certificate, unknownFutureValue.
    client_credential_type: Optional[ClientCredentialType] = None
    # The clientSessionId property
    client_session_id: Optional[str] = None
    # A list that indicates the audience that Conditional Access evaluated during a sign-in event.  Supports $filter (eq).
    conditional_access_audiences: Optional[list[str]] = None
    # The status of the conditional access policy triggered. Possible values: success, failure, notApplied, or unknownFutureValue.  Supports $filter (eq).
    conditional_access_status: Optional[ConditionalAccessStatus] = None
    # The identifier the client sends when sign-in is initiated. This property is used for troubleshooting the corresponding sign-in activity when calling for support.  Supports $filter (eq).
    correlation_id: Optional[str] = None
    # The date and time the sign-in was initiated. The Timestamp type is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.  Supports $orderby, $filter (eq, le, and ge).
    created_date_time: Optional[datetime.datetime] = None
    # Describes the type of cross-tenant access used by the actor to access the resource. The possible values are: none, b2bCollaboration, b2bDirectConnect, microsoftSupport, serviceProvider, unknownFutureValue, passthrough. Use the Prefer: include-unknown-enum-members request header to get the following value or values in this evolvable enum: passthrough. If the sign in didn't cross tenant boundaries, the value is none.
    cross_tenant_access_type: Optional[SignInAccessType] = None
    # The device information from where the sign-in occurred. Includes information such as deviceId, OS, and browser.  Supports $filter (eq, startsWith) on browser and operatingSystem properties.
    device_detail: Optional[DeviceDetail] = None
    # Contains the identifier of an application's federated identity credential, if a federated identity credential was used to sign in.
    federated_credential_id: Optional[str] = None
    # During a failed sign-in, a user can select a button in the Azure portal to mark the failed event for tenant admins. If a user selects the button to flag the failed sign-in, this value is true.
    flagged_for_review: Optional[bool] = None
    # The Global Secure Access IP address that the sign-in was initiated from.
    global_secure_access_ip_address: Optional[str] = None
    # The tenant identifier of the user initiating the sign-in. Not applicable in Managed Identity or service principal sign ins.
    home_tenant_id: Optional[str] = None
    # For user sign ins, the identifier of the tenant that the user is a member of. Only populated in cases where the home tenant provides affirmative consent to Microsoft Entra ID to show the tenant content.
    home_tenant_name: Optional[str] = None
    # Indicates the token types that were presented to Microsoft Entra ID to authenticate the actor in the sign in. The possible values are: none, primaryRefreshToken, saml11, saml20, unknownFutureValue, remoteDesktopToken, refreshToken.  NOTE Microsoft Entra ID might have also used token types not listed in this enum type to authenticate the actor. Don't infer the lack of a token if it isn't one of the types listed. Use the Prefer: include-unknown-enum-members request header to get the following value or values in this evolvable enum: remoteDesktopToken, refreshToken.
    incoming_token_type: Optional[IncomingTokenType] = None
    # The IP address of the client from where the sign-in occurred.  Supports $filter (eq, startsWith).
    ip_address: Optional[str] = None
    # The IP address a user used to reach a resource provider, used to determine Conditional Access compliance for some policies. For example, when a user interacts with Exchange Online, the IP address that Microsoft Exchange receives from the user can be recorded here. This value is often null.
    ip_address_from_resource_provider: Optional[str] = None
    # Indicates whether a user sign in is interactive. In interactive sign in, the user provides an authentication factor to Microsoft Entra ID. These factors include passwords, responses to MFA challenges, biometric factors, or QR codes that a user provides to Microsoft Entra ID or an associated app. In non-interactive sign in, the user doesn't provide an authentication factor. Instead, the client app uses a token or code to authenticate or access a resource on behalf of a user. Non-interactive sign ins are commonly used for a client to sign in on a user's behalf in a process transparent to the user.
    is_interactive: Optional[bool] = None
    # Shows whether the sign in event was subject to a Microsoft Entra tenant restriction policy.
    is_tenant_restricted: Optional[bool] = None
    # Indicates whether a user came through Global Secure Access service.
    is_through_global_secure_access: Optional[bool] = None
    # The city, state, and two letter country code from where the sign-in occurred.  Supports $filter (eq, startsWith) on city, state, and countryOrRegion properties.
    location: Optional[SignInLocation] = None
    # Contains information about the managed identity used for the sign in, including its type, associated Azure Resource Manager (ARM) resource ID, and federated token information.
    managed_service_identity: Optional[ManagedIdentity] = None
    # This property is deprecated.
    mfa_detail: Optional[MfaDetail] = None
    # The network location details including the type of network used and its names.
    network_location_details: Optional[list[NetworkLocationDetail]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The request identifier of the first request in the authentication sequence.  Supports $filter (eq).
    original_request_id: Optional[str] = None
    # Transfer method used to initiate a session throughout all subsequent request. The possible values are: none, deviceCodeFlow, authenticationTransfer, unknownFutureValue.
    original_transfer_method: Optional[OriginalTransferMethods] = None
    # Contains information about the Microsoft Entra Private Link policy that is associated with the sign in event.
    private_link_details: Optional[PrivateLinkDetails] = None
    # The request processing time in milliseconds in AD STS.
    processing_time_in_milliseconds: Optional[int] = None
    # The name of the resource that the user signed in to.  Supports $filter (eq).
    resource_display_name: Optional[str] = None
    # The identifier of the resource that the user signed in to.  Supports $filter (eq).
    resource_id: Optional[str] = None
    # The identifier of the owner of the resource.  Supports $filter (eq).
    resource_owner_tenant_id: Optional[str] = None
    # The identifier of the service principal representing the target resource in the sign-in event.
    resource_service_principal_id: Optional[str] = None
    # The tenant identifier of the resource referenced in the sign in.
    resource_tenant_id: Optional[str] = None
    # The reason behind a specific state of a risky user, sign-in, or a risk event. The value none means that Microsoft Entra risk detection hasn't flagged the user or the sign-in as a risky event so far.  Supports $filter (eq). Note: Details for this property are only available for Microsoft Entra ID P2 customers. All other customers are returned hidden.
    risk_detail: Optional[RiskDetail] = None
    # The list of risk event types associated with the sign-in. Possible values: unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials, investigationsThreatIntelligence,  generic, or unknownFutureValue.  Supports $filter (eq, startsWith).
    risk_event_types_v2: Optional[list[str]] = None
    # The aggregated risk level. Possible values: none, low, medium, high, hidden, or unknownFutureValue. The value hidden means the user or sign-in wasn't enabled for Microsoft Entra ID Protection.  Supports $filter (eq). Note: Details for this property are only available for Microsoft Entra ID P2 customers. All other customers are returned hidden.
    risk_level_aggregated: Optional[RiskLevel] = None
    # The risk level during sign-in. Possible values: none, low, medium, high, hidden, or unknownFutureValue. The value hidden means the user or sign-in wasn't enabled for Microsoft Entra ID Protection.  Supports $filter (eq). Note: Details for this property are only available for Microsoft Entra ID P2 customers. All other customers are returned hidden.
    risk_level_during_sign_in: Optional[RiskLevel] = None
    # The risk state of a risky user, sign-in, or a risk event. Possible values: none, confirmedSafe, remediated, dismissed, atRisk, confirmedCompromised, or unknownFutureValue.  Supports $filter (eq).
    risk_state: Optional[RiskState] = None
    # The rootActorId property
    root_actor_id: Optional[str] = None
    # The unique identifier of the key credential used by the service principal to authenticate.
    service_principal_credential_key_id: Optional[str] = None
    # The certificate thumbprint of the certificate used by the service principal to authenticate.
    service_principal_credential_thumbprint: Optional[str] = None
    # The application identifier used for sign-in. This field is populated when you're signing in using an application.  Supports $filter (eq, startsWith).
    service_principal_id: Optional[str] = None
    # The application name used for sign-in. This field is populated when you're signing in using an application.  Supports $filter (eq, startsWith).
    service_principal_name: Optional[str] = None
    # Identifier of the session that was generated during the sign-in.
    session_id: Optional[str] = None
    # Any conditional access session management policies that were applied during the sign-in event.
    session_lifetime_policies: Optional[list[SessionLifetimePolicy]] = None
    # Indicates the category of sign in that the event represents. For user sign ins, the category can be interactiveUser or nonInteractiveUser and corresponds to the value for the isInteractive property on the signin resource. For managed identity sign ins, the category is managedIdentity. For service principal sign-ins, the category is servicePrincipal. The possible values are: interactiveUser, nonInteractiveUser, servicePrincipal, managedIdentity, unknownFutureValue.  Supports $filter (eq, ne). NOTE: Only interactive sign-ins are returned unless you set an explicit filter. For example, the filter for getting non-interactive sign-ins is https://graph.microsoft.com/beta/auditLogs/signIns?&$filter=signInEventTypes/any(t: t eq 'nonInteractiveUser'). You can also get both interactive and non-interactive sign-ins using the filter signInEventTypes/any(t: t eq 'interactiveUser' or t eq 'noninteractiveUser'). However, the filter for getting both user and service principal sign-in even types is not supported.
    sign_in_event_types: Optional[list[str]] = None
    # The identification that the user provided to sign in. It can be the userPrincipalName, but is also populated when a user signs in using other identifiers.
    sign_in_identifier: Optional[str] = None
    # The type of sign in identifier. The possible values are: userPrincipalName, phoneNumber, proxyAddress, qrCode, onPremisesUserPrincipalName, unknownFutureValue.
    sign_in_identifier_type: Optional[SignInIdentifierType] = None
    # Deprecated. Use tokenProtectionStatusDetails instead. Token protection creates a cryptographically secure tie between the token and the device it's issued to. This field indicates whether the sign-in token was bound to the device. The possible values are: none, bound, unbound, unknownFutureValue.
    sign_in_token_protection_status: Optional[TokenProtectionStatus] = None
    # The sign-in status. Includes the error code and description of the error (for a sign-in failure).  Supports $filter (eq) on errorCode property.
    status: Optional[SignInStatus] = None
    # The name of the identity provider. For example, sts.microsoft.com.  Supports $filter (eq).
    token_issuer_name: Optional[str] = None
    # The type of identity provider. The possible values are: AzureAD, ADFederationServices, UnknownFutureValue, AzureADBackupAuth, ADFederationServicesMFAAdapter, NPSExtension. Use the Prefer: include-unknown-enum-members request header to get the following values in this evolvable enum: AzureADBackupAuth , ADFederationServicesMFAAdapter , NPSExtension.
    token_issuer_type: Optional[TokenIssuerType] = None
    # The status of the token protection for a request in the sign-in logs. For more information, see Conditional Access: Token Protection.
    token_protection_status_details: Optional[TokenProtectionStatusDetails] = None
    # A unique base64-encoded request identifier used to track tokens issued by Microsoft Entra ID as they're redeemed at resource providers.
    unique_token_identifier: Optional[str] = None
    # The user agent information related to sign-in.  Supports $filter (eq, startsWith).
    user_agent: Optional[str] = None
    # The display name of the user.  Supports $filter (eq, startsWith).
    user_display_name: Optional[str] = None
    # The identifier of the user.  Supports $filter (eq).
    user_id: Optional[str] = None
    # User principal name of the user that initiated the sign-in. This value is always in lowercase. For guest users whose values in the user object typically contain #EXT# before the domain part, this property stores the value in both lowercase and the 'true' format. For example, while the user object stores AdeleVance_fabrikam.com#EXT#@contoso.com, the sign-in logs store adelevance@fabrikam.com. Supports $filter (eq, startsWith).
    user_principal_name: Optional[str] = None
    # Identifies whether the user is a member or guest in the tenant. The possible values are: member, guest, unknownFutureValue.
    user_type: Optional[SignInUserType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SignIn:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SignIn
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SignIn()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .agentic.agent_sign_in import AgentSignIn
        from .applied_authentication_event_listener import AppliedAuthenticationEventListener
        from .applied_conditional_access_policy import AppliedConditionalAccessPolicy
        from .authentication_app_device_details import AuthenticationAppDeviceDetails
        from .authentication_app_policy_details import AuthenticationAppPolicyDetails
        from .authentication_context import AuthenticationContext
        from .authentication_detail import AuthenticationDetail
        from .authentication_requirement_policy import AuthenticationRequirementPolicy
        from .client_credential_type import ClientCredentialType
        from .conditional_access_status import ConditionalAccessStatus
        from .device_detail import DeviceDetail
        from .entity import Entity
        from .incoming_token_type import IncomingTokenType
        from .key_value import KeyValue
        from .managed_identity import ManagedIdentity
        from .mfa_detail import MfaDetail
        from .network_location_detail import NetworkLocationDetail
        from .original_transfer_methods import OriginalTransferMethods
        from .private_link_details import PrivateLinkDetails
        from .protocol_type import ProtocolType
        from .risk_detail import RiskDetail
        from .risk_level import RiskLevel
        from .risk_state import RiskState
        from .session_lifetime_policy import SessionLifetimePolicy
        from .sign_in_access_type import SignInAccessType
        from .sign_in_identifier_type import SignInIdentifierType
        from .sign_in_location import SignInLocation
        from .sign_in_status import SignInStatus
        from .sign_in_user_type import SignInUserType
        from .token_issuer_type import TokenIssuerType
        from .token_protection_status import TokenProtectionStatus
        from .token_protection_status_details import TokenProtectionStatusDetails

        from .agentic.agent_sign_in import AgentSignIn
        from .applied_authentication_event_listener import AppliedAuthenticationEventListener
        from .applied_conditional_access_policy import AppliedConditionalAccessPolicy
        from .authentication_app_device_details import AuthenticationAppDeviceDetails
        from .authentication_app_policy_details import AuthenticationAppPolicyDetails
        from .authentication_context import AuthenticationContext
        from .authentication_detail import AuthenticationDetail
        from .authentication_requirement_policy import AuthenticationRequirementPolicy
        from .client_credential_type import ClientCredentialType
        from .conditional_access_status import ConditionalAccessStatus
        from .device_detail import DeviceDetail
        from .entity import Entity
        from .incoming_token_type import IncomingTokenType
        from .key_value import KeyValue
        from .managed_identity import ManagedIdentity
        from .mfa_detail import MfaDetail
        from .network_location_detail import NetworkLocationDetail
        from .original_transfer_methods import OriginalTransferMethods
        from .private_link_details import PrivateLinkDetails
        from .protocol_type import ProtocolType
        from .risk_detail import RiskDetail
        from .risk_level import RiskLevel
        from .risk_state import RiskState
        from .session_lifetime_policy import SessionLifetimePolicy
        from .sign_in_access_type import SignInAccessType
        from .sign_in_identifier_type import SignInIdentifierType
        from .sign_in_location import SignInLocation
        from .sign_in_status import SignInStatus
        from .sign_in_user_type import SignInUserType
        from .token_issuer_type import TokenIssuerType
        from .token_protection_status import TokenProtectionStatus
        from .token_protection_status_details import TokenProtectionStatusDetails

        fields: dict[str, Callable[[Any], None]] = {
            "agent": lambda n : setattr(self, 'agent', n.get_object_value(AgentSignIn)),
            "appDisplayName": lambda n : setattr(self, 'app_display_name', n.get_str_value()),
            "appId": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "appOwnerTenantId": lambda n : setattr(self, 'app_owner_tenant_id', n.get_str_value()),
            "appTokenProtectionStatus": lambda n : setattr(self, 'app_token_protection_status', n.get_enum_value(TokenProtectionStatus)),
            "appliedConditionalAccessPolicies": lambda n : setattr(self, 'applied_conditional_access_policies', n.get_collection_of_object_values(AppliedConditionalAccessPolicy)),
            "appliedEventListeners": lambda n : setattr(self, 'applied_event_listeners', n.get_collection_of_object_values(AppliedAuthenticationEventListener)),
            "authenticationAppDeviceDetails": lambda n : setattr(self, 'authentication_app_device_details', n.get_object_value(AuthenticationAppDeviceDetails)),
            "authenticationAppPolicyEvaluationDetails": lambda n : setattr(self, 'authentication_app_policy_evaluation_details', n.get_collection_of_object_values(AuthenticationAppPolicyDetails)),
            "authenticationContextClassReferences": lambda n : setattr(self, 'authentication_context_class_references', n.get_collection_of_object_values(AuthenticationContext)),
            "authenticationDetails": lambda n : setattr(self, 'authentication_details', n.get_collection_of_object_values(AuthenticationDetail)),
            "authenticationMethodsUsed": lambda n : setattr(self, 'authentication_methods_used', n.get_collection_of_primitive_values(str)),
            "authenticationProcessingDetails": lambda n : setattr(self, 'authentication_processing_details', n.get_collection_of_object_values(KeyValue)),
            "authenticationProtocol": lambda n : setattr(self, 'authentication_protocol', n.get_collection_of_enum_values(ProtocolType)),
            "authenticationRequirement": lambda n : setattr(self, 'authentication_requirement', n.get_str_value()),
            "authenticationRequirementPolicies": lambda n : setattr(self, 'authentication_requirement_policies', n.get_collection_of_object_values(AuthenticationRequirementPolicy)),
            "autonomousSystemNumber": lambda n : setattr(self, 'autonomous_system_number', n.get_int_value()),
            "azureResourceId": lambda n : setattr(self, 'azure_resource_id', n.get_str_value()),
            "clientAppUsed": lambda n : setattr(self, 'client_app_used', n.get_str_value()),
            "clientCredentialType": lambda n : setattr(self, 'client_credential_type', n.get_enum_value(ClientCredentialType)),
            "clientSessionId": lambda n : setattr(self, 'client_session_id', n.get_str_value()),
            "conditionalAccessAudiences": lambda n : setattr(self, 'conditional_access_audiences', n.get_collection_of_primitive_values(str)),
            "conditionalAccessStatus": lambda n : setattr(self, 'conditional_access_status', n.get_enum_value(ConditionalAccessStatus)),
            "correlationId": lambda n : setattr(self, 'correlation_id', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "crossTenantAccessType": lambda n : setattr(self, 'cross_tenant_access_type', n.get_collection_of_enum_values(SignInAccessType)),
            "deviceDetail": lambda n : setattr(self, 'device_detail', n.get_object_value(DeviceDetail)),
            "federatedCredentialId": lambda n : setattr(self, 'federated_credential_id', n.get_str_value()),
            "flaggedForReview": lambda n : setattr(self, 'flagged_for_review', n.get_bool_value()),
            "globalSecureAccessIpAddress": lambda n : setattr(self, 'global_secure_access_ip_address', n.get_str_value()),
            "homeTenantId": lambda n : setattr(self, 'home_tenant_id', n.get_str_value()),
            "homeTenantName": lambda n : setattr(self, 'home_tenant_name', n.get_str_value()),
            "incomingTokenType": lambda n : setattr(self, 'incoming_token_type', n.get_collection_of_enum_values(IncomingTokenType)),
            "ipAddress": lambda n : setattr(self, 'ip_address', n.get_str_value()),
            "ipAddressFromResourceProvider": lambda n : setattr(self, 'ip_address_from_resource_provider', n.get_str_value()),
            "isInteractive": lambda n : setattr(self, 'is_interactive', n.get_bool_value()),
            "isTenantRestricted": lambda n : setattr(self, 'is_tenant_restricted', n.get_bool_value()),
            "isThroughGlobalSecureAccess": lambda n : setattr(self, 'is_through_global_secure_access', n.get_bool_value()),
            "location": lambda n : setattr(self, 'location', n.get_object_value(SignInLocation)),
            "managedServiceIdentity": lambda n : setattr(self, 'managed_service_identity', n.get_object_value(ManagedIdentity)),
            "mfaDetail": lambda n : setattr(self, 'mfa_detail', n.get_object_value(MfaDetail)),
            "networkLocationDetails": lambda n : setattr(self, 'network_location_details', n.get_collection_of_object_values(NetworkLocationDetail)),
            "originalRequestId": lambda n : setattr(self, 'original_request_id', n.get_str_value()),
            "originalTransferMethod": lambda n : setattr(self, 'original_transfer_method', n.get_enum_value(OriginalTransferMethods)),
            "privateLinkDetails": lambda n : setattr(self, 'private_link_details', n.get_object_value(PrivateLinkDetails)),
            "processingTimeInMilliseconds": lambda n : setattr(self, 'processing_time_in_milliseconds', n.get_int_value()),
            "resourceDisplayName": lambda n : setattr(self, 'resource_display_name', n.get_str_value()),
            "resourceId": lambda n : setattr(self, 'resource_id', n.get_str_value()),
            "resourceOwnerTenantId": lambda n : setattr(self, 'resource_owner_tenant_id', n.get_str_value()),
            "resourceServicePrincipalId": lambda n : setattr(self, 'resource_service_principal_id', n.get_str_value()),
            "resourceTenantId": lambda n : setattr(self, 'resource_tenant_id', n.get_str_value()),
            "riskDetail": lambda n : setattr(self, 'risk_detail', n.get_enum_value(RiskDetail)),
            "riskEventTypes_v2": lambda n : setattr(self, 'risk_event_types_v2', n.get_collection_of_primitive_values(str)),
            "riskLevelAggregated": lambda n : setattr(self, 'risk_level_aggregated', n.get_enum_value(RiskLevel)),
            "riskLevelDuringSignIn": lambda n : setattr(self, 'risk_level_during_sign_in', n.get_enum_value(RiskLevel)),
            "riskState": lambda n : setattr(self, 'risk_state', n.get_enum_value(RiskState)),
            "rootActorId": lambda n : setattr(self, 'root_actor_id', n.get_str_value()),
            "servicePrincipalCredentialKeyId": lambda n : setattr(self, 'service_principal_credential_key_id', n.get_str_value()),
            "servicePrincipalCredentialThumbprint": lambda n : setattr(self, 'service_principal_credential_thumbprint', n.get_str_value()),
            "servicePrincipalId": lambda n : setattr(self, 'service_principal_id', n.get_str_value()),
            "servicePrincipalName": lambda n : setattr(self, 'service_principal_name', n.get_str_value()),
            "sessionId": lambda n : setattr(self, 'session_id', n.get_str_value()),
            "sessionLifetimePolicies": lambda n : setattr(self, 'session_lifetime_policies', n.get_collection_of_object_values(SessionLifetimePolicy)),
            "signInEventTypes": lambda n : setattr(self, 'sign_in_event_types', n.get_collection_of_primitive_values(str)),
            "signInIdentifier": lambda n : setattr(self, 'sign_in_identifier', n.get_str_value()),
            "signInIdentifierType": lambda n : setattr(self, 'sign_in_identifier_type', n.get_enum_value(SignInIdentifierType)),
            "signInTokenProtectionStatus": lambda n : setattr(self, 'sign_in_token_protection_status', n.get_enum_value(TokenProtectionStatus)),
            "status": lambda n : setattr(self, 'status', n.get_object_value(SignInStatus)),
            "tokenIssuerName": lambda n : setattr(self, 'token_issuer_name', n.get_str_value()),
            "tokenIssuerType": lambda n : setattr(self, 'token_issuer_type', n.get_enum_value(TokenIssuerType)),
            "tokenProtectionStatusDetails": lambda n : setattr(self, 'token_protection_status_details', n.get_object_value(TokenProtectionStatusDetails)),
            "uniqueTokenIdentifier": lambda n : setattr(self, 'unique_token_identifier', n.get_str_value()),
            "userAgent": lambda n : setattr(self, 'user_agent', n.get_str_value()),
            "userDisplayName": lambda n : setattr(self, 'user_display_name', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
            "userType": lambda n : setattr(self, 'user_type', n.get_enum_value(SignInUserType)),
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
        writer.write_object_value("agent", self.agent)
        writer.write_str_value("appDisplayName", self.app_display_name)
        writer.write_str_value("appId", self.app_id)
        writer.write_str_value("appOwnerTenantId", self.app_owner_tenant_id)
        writer.write_enum_value("appTokenProtectionStatus", self.app_token_protection_status)
        writer.write_collection_of_object_values("appliedConditionalAccessPolicies", self.applied_conditional_access_policies)
        writer.write_collection_of_object_values("appliedEventListeners", self.applied_event_listeners)
        writer.write_object_value("authenticationAppDeviceDetails", self.authentication_app_device_details)
        writer.write_collection_of_object_values("authenticationAppPolicyEvaluationDetails", self.authentication_app_policy_evaluation_details)
        writer.write_collection_of_object_values("authenticationContextClassReferences", self.authentication_context_class_references)
        writer.write_collection_of_object_values("authenticationDetails", self.authentication_details)
        writer.write_collection_of_primitive_values("authenticationMethodsUsed", self.authentication_methods_used)
        writer.write_collection_of_object_values("authenticationProcessingDetails", self.authentication_processing_details)
        writer.write_enum_value("authenticationProtocol", self.authentication_protocol)
        writer.write_str_value("authenticationRequirement", self.authentication_requirement)
        writer.write_collection_of_object_values("authenticationRequirementPolicies", self.authentication_requirement_policies)
        writer.write_int_value("autonomousSystemNumber", self.autonomous_system_number)
        writer.write_str_value("azureResourceId", self.azure_resource_id)
        writer.write_str_value("clientAppUsed", self.client_app_used)
        writer.write_enum_value("clientCredentialType", self.client_credential_type)
        writer.write_str_value("clientSessionId", self.client_session_id)
        writer.write_collection_of_primitive_values("conditionalAccessAudiences", self.conditional_access_audiences)
        writer.write_enum_value("conditionalAccessStatus", self.conditional_access_status)
        writer.write_str_value("correlationId", self.correlation_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_enum_value("crossTenantAccessType", self.cross_tenant_access_type)
        writer.write_object_value("deviceDetail", self.device_detail)
        writer.write_str_value("federatedCredentialId", self.federated_credential_id)
        writer.write_bool_value("flaggedForReview", self.flagged_for_review)
        writer.write_str_value("globalSecureAccessIpAddress", self.global_secure_access_ip_address)
        writer.write_str_value("homeTenantId", self.home_tenant_id)
        writer.write_str_value("homeTenantName", self.home_tenant_name)
        writer.write_enum_value("incomingTokenType", self.incoming_token_type)
        writer.write_str_value("ipAddress", self.ip_address)
        writer.write_str_value("ipAddressFromResourceProvider", self.ip_address_from_resource_provider)
        writer.write_bool_value("isInteractive", self.is_interactive)
        writer.write_bool_value("isTenantRestricted", self.is_tenant_restricted)
        writer.write_bool_value("isThroughGlobalSecureAccess", self.is_through_global_secure_access)
        writer.write_object_value("location", self.location)
        writer.write_object_value("managedServiceIdentity", self.managed_service_identity)
        writer.write_object_value("mfaDetail", self.mfa_detail)
        writer.write_collection_of_object_values("networkLocationDetails", self.network_location_details)
        writer.write_str_value("originalRequestId", self.original_request_id)
        writer.write_enum_value("originalTransferMethod", self.original_transfer_method)
        writer.write_object_value("privateLinkDetails", self.private_link_details)
        writer.write_int_value("processingTimeInMilliseconds", self.processing_time_in_milliseconds)
        writer.write_str_value("resourceDisplayName", self.resource_display_name)
        writer.write_str_value("resourceId", self.resource_id)
        writer.write_str_value("resourceOwnerTenantId", self.resource_owner_tenant_id)
        writer.write_str_value("resourceServicePrincipalId", self.resource_service_principal_id)
        writer.write_str_value("resourceTenantId", self.resource_tenant_id)
        writer.write_enum_value("riskDetail", self.risk_detail)
        writer.write_collection_of_primitive_values("riskEventTypes_v2", self.risk_event_types_v2)
        writer.write_enum_value("riskLevelAggregated", self.risk_level_aggregated)
        writer.write_enum_value("riskLevelDuringSignIn", self.risk_level_during_sign_in)
        writer.write_enum_value("riskState", self.risk_state)
        writer.write_str_value("rootActorId", self.root_actor_id)
        writer.write_str_value("servicePrincipalCredentialKeyId", self.service_principal_credential_key_id)
        writer.write_str_value("servicePrincipalCredentialThumbprint", self.service_principal_credential_thumbprint)
        writer.write_str_value("servicePrincipalId", self.service_principal_id)
        writer.write_str_value("servicePrincipalName", self.service_principal_name)
        writer.write_str_value("sessionId", self.session_id)
        writer.write_collection_of_object_values("sessionLifetimePolicies", self.session_lifetime_policies)
        writer.write_collection_of_primitive_values("signInEventTypes", self.sign_in_event_types)
        writer.write_str_value("signInIdentifier", self.sign_in_identifier)
        writer.write_enum_value("signInIdentifierType", self.sign_in_identifier_type)
        writer.write_enum_value("signInTokenProtectionStatus", self.sign_in_token_protection_status)
        writer.write_object_value("status", self.status)
        writer.write_str_value("tokenIssuerName", self.token_issuer_name)
        writer.write_enum_value("tokenIssuerType", self.token_issuer_type)
        writer.write_object_value("tokenProtectionStatusDetails", self.token_protection_status_details)
        writer.write_str_value("uniqueTokenIdentifier", self.unique_token_identifier)
        writer.write_str_value("userAgent", self.user_agent)
        writer.write_str_value("userDisplayName", self.user_display_name)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_enum_value("userType", self.user_type)
    

