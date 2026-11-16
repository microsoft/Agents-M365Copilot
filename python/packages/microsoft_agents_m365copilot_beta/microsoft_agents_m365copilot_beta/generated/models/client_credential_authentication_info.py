from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_info import AuthenticationInfo

from .authentication_info import AuthenticationInfo

@dataclass
class ClientCredentialAuthenticationInfo(AuthenticationInfo, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.clientCredentialAuthenticationInfo"
    # The URL endpoint used to obtain access tokens for authentication with the external system.
    access_token_url: Optional[str] = None
    # The client identifier used for authentication with the external system.
    client_id: Optional[str] = None
    # The name of the secret in Azure Key Vault that contains the client secret.
    secret_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ClientCredentialAuthenticationInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ClientCredentialAuthenticationInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ClientCredentialAuthenticationInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_info import AuthenticationInfo

        from .authentication_info import AuthenticationInfo

        fields: dict[str, Callable[[Any], None]] = {
            "accessTokenUrl": lambda n : setattr(self, 'access_token_url', n.get_str_value()),
            "clientId": lambda n : setattr(self, 'client_id', n.get_str_value()),
            "secretName": lambda n : setattr(self, 'secret_name', n.get_str_value()),
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
        writer.write_str_value("accessTokenUrl", self.access_token_url)
        writer.write_str_value("clientId", self.client_id)
        writer.write_str_value("secretName", self.secret_name)
    

