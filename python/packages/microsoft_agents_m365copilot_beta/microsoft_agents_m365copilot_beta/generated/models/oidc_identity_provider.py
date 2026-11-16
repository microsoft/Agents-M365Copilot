from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .identity_provider_base import IdentityProviderBase
    from .oidc_client_authentication import OidcClientAuthentication
    from .oidc_inbound_claim_mapping_override import OidcInboundClaimMappingOverride
    from .oidc_response_type import OidcResponseType

from .identity_provider_base import IdentityProviderBase

@dataclass
class OidcIdentityProvider(IdentityProviderBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.oidcIdentityProvider"
    # The clientAuthentication property
    client_authentication: Optional[OidcClientAuthentication] = None
    # The client ID for the application obtained when registering the application with the identity provider.
    client_id: Optional[str] = None
    # After the OIDC provider sends an ID token back to Microsoft Entra External ID, Microsoft Entra External ID needs to be able to map the claims from the received token to the claims that Microsoft Entra ID recognizes and uses. This complex type captures that mapping.
    inbound_claim_mapping: Optional[OidcInboundClaimMappingOverride] = None
    # The issuer URI. Issuer URI is a case-sensitive URL using https scheme contains scheme, host, and optionally, port number and path components and no query or fragment components. Note: Configuring other Microsoft Entra tenants as an external identity provider is currently not supported. As a result, the microsoftonline.com domain in the issuer URI is not accepted.
    issuer: Optional[str] = None
    # The responseType property
    response_type: Optional[OidcResponseType] = None
    # Scope defines the information and permissions you are looking to gather from your custom identity provider.
    scope: Optional[str] = None
    # The URL for the metadata document of the OpenID Connect identity provider. Every OpenID Connect identity provider describes a metadata document that contains most of the information required to perform sign-in. This includes information such as the URLs to use and the location of the service's public signing keys. The OpenID Connect metadata document is always located at an endpoint that ends in .well-known/openid-configuration. Note: The metadata document should, at minimum, contain the following properties: issuer, authorizationendpoint, tokenendpoint, tokenendpointauthmethodssupported, responsetypessupported, subjecttypessupported and jwks_uri. Visit OpenID Connect Discovery specifications for more details.
    well_known_endpoint: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OidcIdentityProvider:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OidcIdentityProvider
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OidcIdentityProvider()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .identity_provider_base import IdentityProviderBase
        from .oidc_client_authentication import OidcClientAuthentication
        from .oidc_inbound_claim_mapping_override import OidcInboundClaimMappingOverride
        from .oidc_response_type import OidcResponseType

        from .identity_provider_base import IdentityProviderBase
        from .oidc_client_authentication import OidcClientAuthentication
        from .oidc_inbound_claim_mapping_override import OidcInboundClaimMappingOverride
        from .oidc_response_type import OidcResponseType

        fields: dict[str, Callable[[Any], None]] = {
            "clientAuthentication": lambda n : setattr(self, 'client_authentication', n.get_object_value(OidcClientAuthentication)),
            "clientId": lambda n : setattr(self, 'client_id', n.get_str_value()),
            "inboundClaimMapping": lambda n : setattr(self, 'inbound_claim_mapping', n.get_object_value(OidcInboundClaimMappingOverride)),
            "issuer": lambda n : setattr(self, 'issuer', n.get_str_value()),
            "responseType": lambda n : setattr(self, 'response_type', n.get_collection_of_enum_values(OidcResponseType)),
            "scope": lambda n : setattr(self, 'scope', n.get_str_value()),
            "wellKnownEndpoint": lambda n : setattr(self, 'well_known_endpoint', n.get_str_value()),
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
        writer.write_object_value("clientAuthentication", self.client_authentication)
        writer.write_str_value("clientId", self.client_id)
        writer.write_object_value("inboundClaimMapping", self.inbound_claim_mapping)
        writer.write_str_value("issuer", self.issuer)
        writer.write_enum_value("responseType", self.response_type)
        writer.write_str_value("scope", self.scope)
        writer.write_str_value("wellKnownEndpoint", self.well_known_endpoint)
    

