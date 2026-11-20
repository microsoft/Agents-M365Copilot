from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_method_configuration import AuthenticationMethodConfiguration
    from .identity_verification_events_configuration import IdentityVerificationEventsConfiguration
    from .verifiable_credential_authentication_method_target import VerifiableCredentialAuthenticationMethodTarget

from .authentication_method_configuration import AuthenticationMethodConfiguration

@dataclass
class VerifiableCredentialsAuthenticationMethodConfiguration(AuthenticationMethodConfiguration, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.verifiableCredentialsAuthenticationMethodConfiguration"
    # The optional tenant-level configuration that controls whether identity verification events and credential provenance information are collected and exposed for Verified ID verification. This setting isn't scoped to individual Verified ID profiles. If no configuration is stored or the stored value is null, event collection and exposure are disabled. Omitting this property from a PATCH request leaves its existing value unchanged.
    identity_verification_events_configuration: Optional[IdentityVerificationEventsConfiguration] = None
    # A collection of groups that are enabled to use the authentication method.
    include_targets: Optional[list[VerifiableCredentialAuthenticationMethodTarget]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VerifiableCredentialsAuthenticationMethodConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VerifiableCredentialsAuthenticationMethodConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return VerifiableCredentialsAuthenticationMethodConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_method_configuration import AuthenticationMethodConfiguration
        from .identity_verification_events_configuration import IdentityVerificationEventsConfiguration
        from .verifiable_credential_authentication_method_target import VerifiableCredentialAuthenticationMethodTarget

        from .authentication_method_configuration import AuthenticationMethodConfiguration
        from .identity_verification_events_configuration import IdentityVerificationEventsConfiguration
        from .verifiable_credential_authentication_method_target import VerifiableCredentialAuthenticationMethodTarget

        fields: dict[str, Callable[[Any], None]] = {
            "identityVerificationEventsConfiguration": lambda n : setattr(self, 'identity_verification_events_configuration', n.get_object_value(IdentityVerificationEventsConfiguration)),
            "includeTargets": lambda n : setattr(self, 'include_targets', n.get_collection_of_object_values(VerifiableCredentialAuthenticationMethodTarget)),
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
        writer.write_object_value("identityVerificationEventsConfiguration", self.identity_verification_events_configuration)
        writer.write_collection_of_object_values("includeTargets", self.include_targets)
    

