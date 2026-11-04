from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .claims_mapping import ClaimsMapping
    from .identity_provider import IdentityProvider
    from .open_id_connect_response_mode import OpenIdConnectResponseMode
    from .open_id_connect_response_types import OpenIdConnectResponseTypes

from .identity_provider import IdentityProvider

@dataclass
class OpenIdConnectProvider(IdentityProvider, Parsable):
    # After the OIDC provider sends an ID token back to Microsoft Entra ID, Microsoft Entra ID needs to be able to map the claims from the received token to the claims that Microsoft Entra ID recognizes and uses. This complex type captures that mapping. It's a required property.
    claims_mapping: Optional[ClaimsMapping] = None
    # The domain hint can be used to skip directly to the sign-in page of the specified identity provider, instead of having the user make a selection among the list of available identity providers.
    domain_hint: Optional[str] = None
    # The URL for the metadata document of the OpenID Connect identity provider. Every OpenID Connect identity provider describes a metadata document that contains most of the information required to perform sign-in. This includes information such as the URLs to use and the location of the service's public signing keys. The OpenID Connect metadata document is always located at an endpoint that ends in a well-known/openid-configuration. For the OpenID Connect identity provider you're looking to add, you need to provide the metadata URL. It's a required property and is read only after creation.
    metadata_url: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The responseMode property
    response_mode: Optional[OpenIdConnectResponseMode] = None
    # The responseType property
    response_type: Optional[OpenIdConnectResponseTypes] = None
    # Scope defines the information and permissions you're looking to gather from your custom identity provider. OpenID Connect requests must contain the openid scope value in order to receive the ID token from the identity provider. Without the ID token, users aren't able to sign in to Azure AD B2C using the custom identity provider. Other scopes can be appended separated by space. For more information about the scope limitations, see RFC6749 Section 3.3. It's a required property.
    scope: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OpenIdConnectProvider:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OpenIdConnectProvider
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OpenIdConnectProvider()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .claims_mapping import ClaimsMapping
        from .identity_provider import IdentityProvider
        from .open_id_connect_response_mode import OpenIdConnectResponseMode
        from .open_id_connect_response_types import OpenIdConnectResponseTypes

        from .claims_mapping import ClaimsMapping
        from .identity_provider import IdentityProvider
        from .open_id_connect_response_mode import OpenIdConnectResponseMode
        from .open_id_connect_response_types import OpenIdConnectResponseTypes

        fields: dict[str, Callable[[Any], None]] = {
            "claimsMapping": lambda n : setattr(self, 'claims_mapping', n.get_object_value(ClaimsMapping)),
            "domainHint": lambda n : setattr(self, 'domain_hint', n.get_str_value()),
            "metadataUrl": lambda n : setattr(self, 'metadata_url', n.get_str_value()),
            "responseMode": lambda n : setattr(self, 'response_mode', n.get_enum_value(OpenIdConnectResponseMode)),
            "responseType": lambda n : setattr(self, 'response_type', n.get_collection_of_enum_values(OpenIdConnectResponseTypes)),
            "scope": lambda n : setattr(self, 'scope', n.get_str_value()),
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
        writer.write_object_value("claimsMapping", self.claims_mapping)
        writer.write_str_value("domainHint", self.domain_hint)
        writer.write_str_value("metadataUrl", self.metadata_url)
        writer.write_enum_value("responseMode", self.response_mode)
        writer.write_enum_value("responseType", self.response_type)
        writer.write_str_value("scope", self.scope)
    

