from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .o_auth_client_credential import OAuthClientCredential

from .o_auth_client_credential import OAuthClientCredential

@dataclass
class OAuth2ClientCredential(OAuthClientCredential, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.industryData.oAuth2ClientCredential"
    # The OAuth scope that is provided to the authentication process.
    scope: Optional[str] = None
    # The URL with which to retrieve the token after authentication happens.
    token_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OAuth2ClientCredential:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OAuth2ClientCredential
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OAuth2ClientCredential()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .o_auth_client_credential import OAuthClientCredential

        from .o_auth_client_credential import OAuthClientCredential

        fields: dict[str, Callable[[Any], None]] = {
            "scope": lambda n : setattr(self, 'scope', n.get_str_value()),
            "tokenUrl": lambda n : setattr(self, 'token_url', n.get_str_value()),
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
        writer.write_str_value("scope", self.scope)
        writer.write_str_value("tokenUrl", self.token_url)
    

