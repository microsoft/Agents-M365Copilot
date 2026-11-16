from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .eap_fast_configuration import EapFastConfiguration
    from .eap_type import EapType
    from .mac_o_s_certificate_profile_base import MacOSCertificateProfileBase
    from .mac_o_s_trusted_root_certificate import MacOSTrustedRootCertificate
    from .mac_o_s_wi_fi_configuration import MacOSWiFiConfiguration
    from .non_eap_authentication_method_for_eap_ttls_type import NonEapAuthenticationMethodForEapTtlsType
    from .wi_fi_authentication_method import WiFiAuthenticationMethod

from .mac_o_s_wi_fi_configuration import MacOSWiFiConfiguration

@dataclass
class MacOSEnterpriseWiFiConfiguration(MacOSWiFiConfiguration, Parsable):
    """
    MacOS Wi-Fi WPA-Enterprise/WPA2-Enterprise configuration profile.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.macOSEnterpriseWiFiConfiguration"
    # Authentication Method when EAP Type is configured to PEAP or EAP-TTLS. Possible values are: certificate, usernameAndPassword, derivedCredential.
    authentication_method: Optional[WiFiAuthenticationMethod] = None
    # EAP-FAST Configuration Option when EAP-FAST is the selected EAP Type. Possible values are: noProtectedAccessCredential, useProtectedAccessCredential, useProtectedAccessCredentialAndProvision, useProtectedAccessCredentialAndProvisionAnonymously.
    eap_fast_configuration: Optional[EapFastConfiguration] = None
    # Extensible Authentication Protocol (EAP) configuration types.
    eap_type: Optional[EapType] = None
    # Identity Certificate for client authentication when EAP Type is configured to EAP-TLS, EAP-TTLS (with Certificate Authentication), or PEAP (with Certificate Authentication).
    identity_certificate_for_client_authentication: Optional[MacOSCertificateProfileBase] = None
    # Non-EAP Method for Authentication (Inner Identity) when EAP Type is EAP-TTLS and Authenticationmethod is Username and Password. Possible values are: unencryptedPassword, challengeHandshakeAuthenticationProtocol, microsoftChap, microsoftChapVersionTwo.
    inner_authentication_protocol_for_eap_ttls: Optional[NonEapAuthenticationMethodForEapTtlsType] = None
    # Enable identity privacy (Outer Identity) when EAP Type is configured to EAP-TTLS, EAP-FAST or PEAP. This property masks usernames with the text you enter. For example, if you use 'anonymous', each user that authenticates with this Wi-Fi connection using their real username is displayed as 'anonymous'.
    outer_identity_privacy_temporary_value: Optional[str] = None
    # Trusted Root Certificate for Server Validation when EAP Type is configured to EAP-TLS/TTLS/FAST or PEAP.
    root_certificate_for_server_validation: Optional[MacOSTrustedRootCertificate] = None
    # Trusted Root Certificates for Server Validation when EAP Type is configured to EAP-TLS/TTLS/FAST or PEAP. If you provide this value you do not need to provide trustedServerCertificateNames, and vice versa. This collection can contain a maximum of 500 elements.
    root_certificates_for_server_validation: Optional[list[MacOSTrustedRootCertificate]] = None
    # Trusted server certificate names when EAP Type is configured to EAP-TLS/TTLS/FAST or PEAP. This is the common name used in the certificates issued by your trusted certificate authority (CA). If you provide this information, you can bypass the dynamic trust dialog that is displayed on end users devices when they connect to this Wi-Fi network.
    trusted_server_certificate_names: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MacOSEnterpriseWiFiConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MacOSEnterpriseWiFiConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MacOSEnterpriseWiFiConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .eap_fast_configuration import EapFastConfiguration
        from .eap_type import EapType
        from .mac_o_s_certificate_profile_base import MacOSCertificateProfileBase
        from .mac_o_s_trusted_root_certificate import MacOSTrustedRootCertificate
        from .mac_o_s_wi_fi_configuration import MacOSWiFiConfiguration
        from .non_eap_authentication_method_for_eap_ttls_type import NonEapAuthenticationMethodForEapTtlsType
        from .wi_fi_authentication_method import WiFiAuthenticationMethod

        from .eap_fast_configuration import EapFastConfiguration
        from .eap_type import EapType
        from .mac_o_s_certificate_profile_base import MacOSCertificateProfileBase
        from .mac_o_s_trusted_root_certificate import MacOSTrustedRootCertificate
        from .mac_o_s_wi_fi_configuration import MacOSWiFiConfiguration
        from .non_eap_authentication_method_for_eap_ttls_type import NonEapAuthenticationMethodForEapTtlsType
        from .wi_fi_authentication_method import WiFiAuthenticationMethod

        fields: dict[str, Callable[[Any], None]] = {
            "authenticationMethod": lambda n : setattr(self, 'authentication_method', n.get_enum_value(WiFiAuthenticationMethod)),
            "eapFastConfiguration": lambda n : setattr(self, 'eap_fast_configuration', n.get_enum_value(EapFastConfiguration)),
            "eapType": lambda n : setattr(self, 'eap_type', n.get_enum_value(EapType)),
            "identityCertificateForClientAuthentication": lambda n : setattr(self, 'identity_certificate_for_client_authentication', n.get_object_value(MacOSCertificateProfileBase)),
            "innerAuthenticationProtocolForEapTtls": lambda n : setattr(self, 'inner_authentication_protocol_for_eap_ttls', n.get_enum_value(NonEapAuthenticationMethodForEapTtlsType)),
            "outerIdentityPrivacyTemporaryValue": lambda n : setattr(self, 'outer_identity_privacy_temporary_value', n.get_str_value()),
            "rootCertificateForServerValidation": lambda n : setattr(self, 'root_certificate_for_server_validation', n.get_object_value(MacOSTrustedRootCertificate)),
            "rootCertificatesForServerValidation": lambda n : setattr(self, 'root_certificates_for_server_validation', n.get_collection_of_object_values(MacOSTrustedRootCertificate)),
            "trustedServerCertificateNames": lambda n : setattr(self, 'trusted_server_certificate_names', n.get_collection_of_primitive_values(str)),
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
        writer.write_enum_value("authenticationMethod", self.authentication_method)
        writer.write_enum_value("eapFastConfiguration", self.eap_fast_configuration)
        writer.write_enum_value("eapType", self.eap_type)
        writer.write_object_value("identityCertificateForClientAuthentication", self.identity_certificate_for_client_authentication)
        writer.write_enum_value("innerAuthenticationProtocolForEapTtls", self.inner_authentication_protocol_for_eap_ttls)
        writer.write_str_value("outerIdentityPrivacyTemporaryValue", self.outer_identity_privacy_temporary_value)
        writer.write_object_value("rootCertificateForServerValidation", self.root_certificate_for_server_validation)
        writer.write_collection_of_object_values("rootCertificatesForServerValidation", self.root_certificates_for_server_validation)
        writer.write_collection_of_primitive_values("trustedServerCertificateNames", self.trusted_server_certificate_names)
    

