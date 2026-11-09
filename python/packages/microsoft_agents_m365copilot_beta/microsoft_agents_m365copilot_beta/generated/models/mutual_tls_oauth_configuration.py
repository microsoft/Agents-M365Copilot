from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tls_client_registration_metadata import TlsClientRegistrationMetadata
    from .trusted_certificate_authority_base import TrustedCertificateAuthorityBase

from .trusted_certificate_authority_base import TrustedCertificateAuthorityBase

@dataclass
class MutualTlsOauthConfiguration(TrustedCertificateAuthorityBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.mutualTlsOauthConfiguration"
    # Friendly name. Supports $filter (eq, in).
    display_name: Optional[str] = None
    # The tlsClientAuthParameter property
    tls_client_auth_parameter: Optional[TlsClientRegistrationMetadata] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MutualTlsOauthConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MutualTlsOauthConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MutualTlsOauthConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tls_client_registration_metadata import TlsClientRegistrationMetadata
        from .trusted_certificate_authority_base import TrustedCertificateAuthorityBase

        from .tls_client_registration_metadata import TlsClientRegistrationMetadata
        from .trusted_certificate_authority_base import TrustedCertificateAuthorityBase

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "tlsClientAuthParameter": lambda n : setattr(self, 'tls_client_auth_parameter', n.get_enum_value(TlsClientRegistrationMetadata)),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("tlsClientAuthParameter", self.tls_client_auth_parameter)
    

