from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_method_configuration import AuthenticationMethodConfiguration
    from .authentication_method_target import AuthenticationMethodTarget
    from .x509_certificate_authentication_mode_configuration import X509CertificateAuthenticationModeConfiguration
    from .x509_certificate_authority_scope import X509CertificateAuthorityScope
    from .x509_certificate_issuer_hints_configuration import X509CertificateIssuerHintsConfiguration
    from .x509_certificate_user_binding import X509CertificateUserBinding

from .authentication_method_configuration import AuthenticationMethodConfiguration

@dataclass
class X509CertificateAuthenticationMethodConfiguration(AuthenticationMethodConfiguration, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.x509CertificateAuthenticationMethodConfiguration"
    # Defines strong authentication configurations. This configuration includes the default authentication mode and the different rules for strong authentication bindings.
    authentication_mode_configuration: Optional[X509CertificateAuthenticationModeConfiguration] = None
    # Defines configuration to allow a group of users to use certificates from specific issuing certificate authorities to successfully authenticate.
    certificate_authority_scopes: Optional[list[X509CertificateAuthorityScope]] = None
    # Defines fields in the X.509 certificate that map to attributes of the Microsoft Entra user object in order to bind the certificate to the user. The priority of the object determines the order in which the binding is carried out. The first binding that matches will be used and the rest ignored.
    certificate_user_bindings: Optional[list[X509CertificateUserBinding]] = None
    # A collection of groups that are enabled to use the authentication method.
    include_targets: Optional[list[AuthenticationMethodTarget]] = None
    # Determines whether issuer(CA) hints are sent back to the client side to filter the certificates shown in certificate picker.
    issuer_hints_configuration: Optional[X509CertificateIssuerHintsConfiguration] = None
    # When set to true, Microsoft Entra ID matches the SID in the Security Identifier (SID) extension or the SAN URI SID value from the user's X.509 certificate to the user's on-premises SID attribute for hybrid users and cloud SID for cloud-only users. Certificate-based authentication fails if the values don't match. The value can't be null. The default value is false.
    require_certificate_sid_alignment: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> X509CertificateAuthenticationMethodConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: X509CertificateAuthenticationMethodConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return X509CertificateAuthenticationMethodConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_method_configuration import AuthenticationMethodConfiguration
        from .authentication_method_target import AuthenticationMethodTarget
        from .x509_certificate_authentication_mode_configuration import X509CertificateAuthenticationModeConfiguration
        from .x509_certificate_authority_scope import X509CertificateAuthorityScope
        from .x509_certificate_issuer_hints_configuration import X509CertificateIssuerHintsConfiguration
        from .x509_certificate_user_binding import X509CertificateUserBinding

        from .authentication_method_configuration import AuthenticationMethodConfiguration
        from .authentication_method_target import AuthenticationMethodTarget
        from .x509_certificate_authentication_mode_configuration import X509CertificateAuthenticationModeConfiguration
        from .x509_certificate_authority_scope import X509CertificateAuthorityScope
        from .x509_certificate_issuer_hints_configuration import X509CertificateIssuerHintsConfiguration
        from .x509_certificate_user_binding import X509CertificateUserBinding

        fields: dict[str, Callable[[Any], None]] = {
            "authenticationModeConfiguration": lambda n : setattr(self, 'authentication_mode_configuration', n.get_object_value(X509CertificateAuthenticationModeConfiguration)),
            "certificateAuthorityScopes": lambda n : setattr(self, 'certificate_authority_scopes', n.get_collection_of_object_values(X509CertificateAuthorityScope)),
            "certificateUserBindings": lambda n : setattr(self, 'certificate_user_bindings', n.get_collection_of_object_values(X509CertificateUserBinding)),
            "includeTargets": lambda n : setattr(self, 'include_targets', n.get_collection_of_object_values(AuthenticationMethodTarget)),
            "issuerHintsConfiguration": lambda n : setattr(self, 'issuer_hints_configuration', n.get_object_value(X509CertificateIssuerHintsConfiguration)),
            "requireCertificateSidAlignment": lambda n : setattr(self, 'require_certificate_sid_alignment', n.get_bool_value()),
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
        writer.write_object_value("authenticationModeConfiguration", self.authentication_mode_configuration)
        writer.write_collection_of_object_values("certificateAuthorityScopes", self.certificate_authority_scopes)
        writer.write_collection_of_object_values("certificateUserBindings", self.certificate_user_bindings)
        writer.write_collection_of_object_values("includeTargets", self.include_targets)
        writer.write_object_value("issuerHintsConfiguration", self.issuer_hints_configuration)
        writer.write_bool_value("requireCertificateSidAlignment", self.require_certificate_sid_alignment)
    

