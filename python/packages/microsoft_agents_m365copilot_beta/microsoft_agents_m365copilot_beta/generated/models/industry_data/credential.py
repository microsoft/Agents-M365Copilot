from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .o_auth1_client_credential import OAuth1ClientCredential
    from .o_auth2_client_credential import OAuth2ClientCredential
    from .o_auth_client_credential import OAuthClientCredential

@dataclass
class Credential(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The name of the credential.
    display_name: Optional[str] = None
    # Indicates whether the credential provided is valid based on the last data connector validate operation.
    is_valid: Optional[bool] = None
    # The time that the credential was last successfully validated by the data connector validate operation.
    last_valid_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Credential:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Credential
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
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.oAuthClientCredential".casefold():
            from .o_auth_client_credential import OAuthClientCredential

            return OAuthClientCredential()
        return Credential()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .o_auth1_client_credential import OAuth1ClientCredential
        from .o_auth2_client_credential import OAuth2ClientCredential
        from .o_auth_client_credential import OAuthClientCredential

        from .o_auth1_client_credential import OAuth1ClientCredential
        from .o_auth2_client_credential import OAuth2ClientCredential
        from .o_auth_client_credential import OAuthClientCredential

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isValid": lambda n : setattr(self, 'is_valid', n.get_bool_value()),
            "lastValidDateTime": lambda n : setattr(self, 'last_valid_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

