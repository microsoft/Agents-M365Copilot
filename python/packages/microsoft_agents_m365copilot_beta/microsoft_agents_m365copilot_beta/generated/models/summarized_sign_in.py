from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .agentic.agent_sign_in import AgentSignIn
    from .conditional_access_status import ConditionalAccessStatus
    from .entity import Entity
    from .managed_identity import ManagedIdentity
    from .sign_in_status import SignInStatus
    from .token_issuer_type import TokenIssuerType

from .entity import Entity

@dataclass
class SummarizedSignIn(Entity, Parsable):
    # Represents details about the agentic sign-in. Includes the type of agent as well as parent appId in some cases. Supports $filter (eq) for agentType.
    agent: Optional[AgentSignIn] = None
    # The aggregated day for which the summary applies to. This property always represents the entire day. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    aggregation_date_time: Optional[datetime.datetime] = None
    # The application name displayed in the Microsoft Entra admin center. Supports $filter (eq).
    app_display_name: Optional[str] = None
    # The application identifier (client ID) in Microsoft Entra ID. Supports $filter (eq).
    app_id: Optional[str] = None
    # The status of the conditional access policy triggered. The possible values are: success, failure, notApplied, unknownFutureValue. Supports $filter (eq).
    conditional_access_status: Optional[ConditionalAccessStatus] = None
    # The earliest sign-in event included in this summary. This property always represents the entire day. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    first_sign_in_date_time: Optional[datetime.datetime] = None
    # The IP address a user or autonomous agent used to reach a resource provider, used to determine Conditional Access compliance for some policies. For example, when a user interacts with Exchange Online, the IP address that Microsoft Exchange receives from the user can be recorded here. This value is often null. Supports $filter (eq, startswith).
    ip_address: Optional[str] = None
    # Contains information about the managed identity used for the sign in, including its type, associated Azure Resource Manager resource ID, and federated token information. Supports $filter (eq) for msiType.
    managed_service_identity: Optional[ManagedIdentity] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The name of the resource that the user signed in to. Supports $filter (eq).
    resource_display_name: Optional[str] = None
    # The application identifier of the resource application that the user signed in to. Supports $filter (eq).
    resource_id: Optional[str] = None
    # The rootActorId property
    root_actor_id: Optional[str] = None
    # The application identifier of the specific service principal instance of the application identifier used for sign-in. This field is populated when you're signing in using an application and is different than the appId property. Supports $filter (eq).
    service_principal_id: Optional[str] = None
    # The application name used for sign-in. This field is populated when you're signing in using an application. Supports $filter (eq, startswith).
    service_principal_name: Optional[str] = None
    # The total number of sign-in events included in the summary.
    sign_in_count: Optional[int] = None
    # The sign-in status. Includes the error code and description of the error (for a sign-in failure). Supports $filter (eq) for errorCode.
    status: Optional[SignInStatus] = None
    # The tenant identifier of the user initiating the sign-in. Supports $filter (eq).
    tenant_id: Optional[str] = None
    # The tokenIssuerType property
    token_issuer_type: Optional[TokenIssuerType] = None
    # User principal name of the user that initiated the sign-in. This value is always in lowercase. For guest users whose values in the user object typically contain #EXT# before the domain part, this property stores the value in both lowercase and the 'true' format. For example, while the user object stores AdeleVance_fabrikam.com#EXT#@contoso.com, the sign-in logs store adelevance@fabrikam.com. Supports $filter (eq).
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SummarizedSignIn:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SummarizedSignIn
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SummarizedSignIn()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .agentic.agent_sign_in import AgentSignIn
        from .conditional_access_status import ConditionalAccessStatus
        from .entity import Entity
        from .managed_identity import ManagedIdentity
        from .sign_in_status import SignInStatus
        from .token_issuer_type import TokenIssuerType

        from .agentic.agent_sign_in import AgentSignIn
        from .conditional_access_status import ConditionalAccessStatus
        from .entity import Entity
        from .managed_identity import ManagedIdentity
        from .sign_in_status import SignInStatus
        from .token_issuer_type import TokenIssuerType

        fields: dict[str, Callable[[Any], None]] = {
            "agent": lambda n : setattr(self, 'agent', n.get_object_value(AgentSignIn)),
            "aggregationDateTime": lambda n : setattr(self, 'aggregation_date_time', n.get_datetime_value()),
            "appDisplayName": lambda n : setattr(self, 'app_display_name', n.get_str_value()),
            "appId": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "conditionalAccessStatus": lambda n : setattr(self, 'conditional_access_status', n.get_enum_value(ConditionalAccessStatus)),
            "firstSignInDateTime": lambda n : setattr(self, 'first_sign_in_date_time', n.get_datetime_value()),
            "ipAddress": lambda n : setattr(self, 'ip_address', n.get_str_value()),
            "managedServiceIdentity": lambda n : setattr(self, 'managed_service_identity', n.get_object_value(ManagedIdentity)),
            "resourceDisplayName": lambda n : setattr(self, 'resource_display_name', n.get_str_value()),
            "resourceId": lambda n : setattr(self, 'resource_id', n.get_str_value()),
            "rootActorId": lambda n : setattr(self, 'root_actor_id', n.get_str_value()),
            "servicePrincipalId": lambda n : setattr(self, 'service_principal_id', n.get_str_value()),
            "servicePrincipalName": lambda n : setattr(self, 'service_principal_name', n.get_str_value()),
            "signInCount": lambda n : setattr(self, 'sign_in_count', n.get_int_value()),
            "status": lambda n : setattr(self, 'status', n.get_object_value(SignInStatus)),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "tokenIssuerType": lambda n : setattr(self, 'token_issuer_type', n.get_enum_value(TokenIssuerType)),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
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
        writer.write_datetime_value("aggregationDateTime", self.aggregation_date_time)
        writer.write_str_value("appDisplayName", self.app_display_name)
        writer.write_str_value("appId", self.app_id)
        writer.write_enum_value("conditionalAccessStatus", self.conditional_access_status)
        writer.write_datetime_value("firstSignInDateTime", self.first_sign_in_date_time)
        writer.write_str_value("ipAddress", self.ip_address)
        writer.write_object_value("managedServiceIdentity", self.managed_service_identity)
        writer.write_str_value("resourceDisplayName", self.resource_display_name)
        writer.write_str_value("resourceId", self.resource_id)
        writer.write_str_value("rootActorId", self.root_actor_id)
        writer.write_str_value("servicePrincipalId", self.service_principal_id)
        writer.write_str_value("servicePrincipalName", self.service_principal_name)
        writer.write_int_value("signInCount", self.sign_in_count)
        writer.write_object_value("status", self.status)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_enum_value("tokenIssuerType", self.token_issuer_type)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    

