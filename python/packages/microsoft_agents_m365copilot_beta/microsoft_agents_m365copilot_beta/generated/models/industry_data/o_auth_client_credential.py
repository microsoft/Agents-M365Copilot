from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .credential import Credential
    from .o_auth1_client_credential import OAuth1ClientCredential
    from .o_auth2_client_credential import OAuth2ClientCredential

from .credential import Credential

@dataclass
class OAuthClientCredential(Credential, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.industryData.oAuthClientCredential"
    # The client identifier of the application that is authenticating.
    client_id: Optional[str] = None
    # The client secret that is used to authenticate (write-only).
    client_secret: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OAuthClientCredential:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OAuthClientCredential
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.oAuth1ClientCredential".casefold():
            from .o_auth1_client_credential import OAuth1ClientCredential

            return OAuth1ClientCredential()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.oAuth2ClientCredential".casefold():
            from .o_auth2_client_credential import OAuth2ClientCredential

            return OAuth2ClientCredential()
        return OAuthClientCredential()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .credential import Credential
        from .o_auth1_client_credential import OAuth1ClientCredential
        from .o_auth2_client_credential import OAuth2ClientCredential

        from .credential import Credential
        from .o_auth1_client_credential import OAuth1ClientCredential
        from .o_auth2_client_credential import OAuth2ClientCredential

        fields: dict[str, Callable[[Any], None]] = {
            "clientId": lambda n : setattr(self, 'client_id', n.get_str_value()),
            "clientSecret": lambda n : setattr(self, 'client_secret', n.get_str_value()),
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
        writer.write_str_value("clientId", self.client_id)
        writer.write_str_value("clientSecret", self.client_secret)
    

