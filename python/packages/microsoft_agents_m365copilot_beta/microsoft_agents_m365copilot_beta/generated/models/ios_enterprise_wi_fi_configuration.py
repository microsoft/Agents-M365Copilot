from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_derived_credential_settings import DeviceManagementDerivedCredentialSettings
    from .eap_fast_configuration import EapFastConfiguration
    from .eap_type import EapType
    from .ios_certificate_profile_base import IosCertificateProfileBase
    from .ios_trusted_root_certificate import IosTrustedRootCertificate
    from .ios_wi_fi_configuration import IosWiFiConfiguration
    from .non_eap_authentication_method_for_eap_ttls_type import NonEapAuthenticationMethodForEapTtlsType
    from .wi_fi_authentication_method import WiFiAuthenticationMethod

from .ios_wi_fi_configuration import IosWiFiConfiguration

@dataclass
class IosEnterpriseWiFiConfiguration(IosWiFiConfiguration, Parsable):
    """
    By providing the configurations in this profile you can instruct the iOS device to connect to desired Wi-Fi endpoint. By specifying the authentication method and security types expected by Wi-Fi endpoint you can make the Wi-Fi connection seamless for end user.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.iosEnterpriseWiFiConfiguration"
    # Authentication Method when EAP Type is configured to PEAP or EAP-TTLS. Possible values are: certificate, usernameAndPassword, derivedCredential.
    authentication_method: Optional[WiFiAuthenticationMethod] = None
    # Tenant level settings for the Derived Credentials to be used for authentication.
    derived_credential_settings: Optional[DeviceManagementDerivedCredentialSettings] = None
    # EAP-FAST Configuration Option when EAP-FAST is the selected EAP Type. Possible values are: noProtectedAccessCredential, useProtectedAccessCredential, useProtectedAccessCredentialAndProvision, useProtectedAccessCredentialAndProvisionAnonymously.
    eap_fast_configuration: Optional[EapFastConfiguration] = None
    # Extensible Authentication Protocol (EAP) configuration types.
    eap_type: Optional[EapType] = None
    # Identity Certificate for client authentication when EAP Type is configured to EAP-TLS, EAP-TTLS (with Certificate Authentication), or PEAP (with Certificate Authentication).
    identity_certificate_for_client_authentication: Optional[IosCertificateProfileBase] = None
    # Non-EAP Method for Authentication when EAP Type is EAP-TTLS and Authenticationmethod is Username and Password. Possible values are: unencryptedPassword, challengeHandshakeAuthenticationProtocol, microsoftChap, microsoftChapVersionTwo.
    inner_authentication_protocol_for_eap_ttls: Optional[NonEapAuthenticationMethodForEapTtlsType] = None
    # Enable identity privacy (Outer Identity) when EAP Type is configured to EAP - TTLS, EAP - FAST or PEAP. This property masks usernames with the text you enter. For example, if you use 'anonymous', each user that authenticates with this Wi-Fi connection using their real username is displayed as 'anonymous'.
    outer_identity_privacy_temporary_value: Optional[str] = None
    # Password format string used to build the password to connect to wifi
    password_format_string: Optional[str] = None
    # Trusted Root Certificates for Server Validation when EAP Type is configured to EAP-TLS/TTLS/FAST or PEAP. If you provide this value you do not need to provide trustedServerCertificateNames, and vice versa. This collection can contain a maximum of 500 elements.
    root_certificates_for_server_validation: Optional[list[IosTrustedRootCertificate]] = None
    # Trusted server certificate names when EAP Type is configured to EAP-TLS/TTLS/FAST or PEAP. This is the common name used in the certificates issued by your trusted certificate authority (CA). If you provide this information, you can bypass the dynamic trust dialog that is displayed on end users' devices when they connect to this Wi-Fi network.
    trusted_server_certificate_names: Optional[list[str]] = None
    # Username format string used to build the username to connect to wifi
    username_format_string: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IosEnterpriseWiFiConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IosEnterpriseWiFiConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IosEnterpriseWiFiConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_derived_credential_settings import DeviceManagementDerivedCredentialSettings
        from .eap_fast_configuration import EapFastConfiguration
        from .eap_type import EapType
        from .ios_certificate_profile_base import IosCertificateProfileBase
        from .ios_trusted_root_certificate import IosTrustedRootCertificate
        from .ios_wi_fi_configuration import IosWiFiConfiguration
        from .non_eap_authentication_method_for_eap_ttls_type import NonEapAuthenticationMethodForEapTtlsType
        from .wi_fi_authentication_method import WiFiAuthenticationMethod

        from .device_management_derived_credential_settings import DeviceManagementDerivedCredentialSettings
        from .eap_fast_configuration import EapFastConfiguration
        from .eap_type import EapType
        from .ios_certificate_profile_base import IosCertificateProfileBase
        from .ios_trusted_root_certificate import IosTrustedRootCertificate
        from .ios_wi_fi_configuration import IosWiFiConfiguration
        from .non_eap_authentication_method_for_eap_ttls_type import NonEapAuthenticationMethodForEapTtlsType
        from .wi_fi_authentication_method import WiFiAuthenticationMethod

        fields: dict[str, Callable[[Any], None]] = {
            "authenticationMethod": lambda n : setattr(self, 'authentication_method', n.get_enum_value(WiFiAuthenticationMethod)),
            "derivedCredentialSettings": lambda n : setattr(self, 'derived_credential_settings', n.get_object_value(DeviceManagementDerivedCredentialSettings)),
            "eapFastConfiguration": lambda n : setattr(self, 'eap_fast_configuration', n.get_enum_value(EapFastConfiguration)),
            "eapType": lambda n : setattr(self, 'eap_type', n.get_enum_value(EapType)),
            "identityCertificateForClientAuthentication": lambda n : setattr(self, 'identity_certificate_for_client_authentication', n.get_object_value(IosCertificateProfileBase)),
            "innerAuthenticationProtocolForEapTtls": lambda n : setattr(self, 'inner_authentication_protocol_for_eap_ttls', n.get_enum_value(NonEapAuthenticationMethodForEapTtlsType)),
            "outerIdentityPrivacyTemporaryValue": lambda n : setattr(self, 'outer_identity_privacy_temporary_value', n.get_str_value()),
            "passwordFormatString": lambda n : setattr(self, 'password_format_string', n.get_str_value()),
            "rootCertificatesForServerValidation": lambda n : setattr(self, 'root_certificates_for_server_validation', n.get_collection_of_object_values(IosTrustedRootCertificate)),
            "trustedServerCertificateNames": lambda n : setattr(self, 'trusted_server_certificate_names', n.get_collection_of_primitive_values(str)),
            "usernameFormatString": lambda n : setattr(self, 'username_format_string', n.get_str_value()),
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
        writer.write_object_value("derivedCredentialSettings", self.derived_credential_settings)
        writer.write_enum_value("eapFastConfiguration", self.eap_fast_configuration)
        writer.write_enum_value("eapType", self.eap_type)
        writer.write_object_value("identityCertificateForClientAuthentication", self.identity_certificate_for_client_authentication)
        writer.write_enum_value("innerAuthenticationProtocolForEapTtls", self.inner_authentication_protocol_for_eap_ttls)
        writer.write_str_value("outerIdentityPrivacyTemporaryValue", self.outer_identity_privacy_temporary_value)
        writer.write_str_value("passwordFormatString", self.password_format_string)
        writer.write_collection_of_object_values("rootCertificatesForServerValidation", self.root_certificates_for_server_validation)
        writer.write_collection_of_primitive_values("trustedServerCertificateNames", self.trusted_server_certificate_names)
        writer.write_str_value("usernameFormatString", self.username_format_string)
    

