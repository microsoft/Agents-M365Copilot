from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_device_owner_certificate_profile_base import AndroidDeviceOwnerCertificateProfileBase
    from .android_device_owner_trusted_root_certificate import AndroidDeviceOwnerTrustedRootCertificate
    from .android_device_owner_wi_fi_configuration import AndroidDeviceOwnerWiFiConfiguration
    from .android_eap_type import AndroidEapType
    from .device_management_derived_credential_settings import DeviceManagementDerivedCredentialSettings
    from .non_eap_authentication_method_for_eap_ttls_type import NonEapAuthenticationMethodForEapTtlsType
    from .non_eap_authentication_method_for_peap import NonEapAuthenticationMethodForPeap
    from .wi_fi_authentication_method import WiFiAuthenticationMethod

from .android_device_owner_wi_fi_configuration import AndroidDeviceOwnerWiFiConfiguration

@dataclass
class AndroidDeviceOwnerEnterpriseWiFiConfiguration(AndroidDeviceOwnerWiFiConfiguration, Parsable):
    """
    By providing the configurations in this profile you can instruct the Android Device Owner device to connect to desired Wi-Fi endpoint. By specifying the authentication method and security types expected by Wi-Fi endpoint you can make the Wi-Fi connection seamless for end user.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.androidDeviceOwnerEnterpriseWiFiConfiguration"
    # Indicates the Authentication Method the client (device) needs to use when the EAP Type is configured to PEAP or EAP-TTLS. Possible values are: certificate, usernameAndPassword, derivedCredential.
    authentication_method: Optional[WiFiAuthenticationMethod] = None
    # Tenant level settings for the Derived Credentials to be used for authentication.
    derived_credential_settings: Optional[DeviceManagementDerivedCredentialSettings] = None
    # Extensible Authentication Protocol (EAP) Configuration Types.
    eap_type: Optional[AndroidEapType] = None
    # Identity Certificate for client authentication when EAP Type is configured to EAP-TLS, EAP-TTLS (with Certificate Authentication), or PEAP (with Certificate Authentication). This is the certificate presented by client to the Wi-Fi endpoint. The authentication server sitting behind the Wi-Fi endpoint must accept this certificate to successfully establish a Wi-Fi connection.
    identity_certificate_for_client_authentication: Optional[AndroidDeviceOwnerCertificateProfileBase] = None
    # Non-EAP Method for Authentication (Inner Identity) when EAP Type is EAP-TTLS and Authenticationmethod is Username and Password. Possible values are: unencryptedPassword, challengeHandshakeAuthenticationProtocol, microsoftChap, microsoftChapVersionTwo.
    inner_authentication_protocol_for_eap_ttls: Optional[NonEapAuthenticationMethodForEapTtlsType] = None
    # Non-EAP Method for Authentication (Inner Identity) when EAP Type is PEAP and Authenticationmethod is Username and Password. Possible values are: none, microsoftChapVersionTwo.
    inner_authentication_protocol_for_peap: Optional[NonEapAuthenticationMethodForPeap] = None
    # Enable identity privacy (Outer Identity) when EAP Type is configured to EAP-TTLS or PEAP. The String provided here is used to mask the username of individual users when they attempt to connect to Wi-Fi network.
    outer_identity_privacy_temporary_value: Optional[str] = None
    # Trusted Root Certificate for Server Validation when EAP Type is configured to EAP-TLS, EAP-TTLS or PEAP. This is the certificate presented by the Wi-Fi endpoint when the device attempts to connect to Wi-Fi endpoint. The device (or user) must accept this certificate to continue the connection attempt.
    root_certificate_for_server_validation: Optional[AndroidDeviceOwnerTrustedRootCertificate] = None
    # Trusted Root Certificates for Server Validation when EAP Type is configured to EAP-TLS, EAP-TTLS or PEAP. This is the certificate presented by the Wi-Fi endpoint when the device attempts to connect to Wi-Fi endpoint. The device (or user) must accept this certificate to continue the connection attempt. This collection can contain a maximum of 500 elements.
    root_certificates_for_server_validation: Optional[list[AndroidDeviceOwnerTrustedRootCertificate]] = None
    # Trusted server certificate names when EAP Type is configured to EAP-TLS/TTLS/FAST or PEAP. This is the common name used in the certificates issued by your trusted certificate authority (CA). If you provide this information, you can bypass the dynamic trust dialog that is displayed on end users' devices when they connect to this Wi-Fi network.
    trusted_server_certificate_names: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AndroidDeviceOwnerEnterpriseWiFiConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidDeviceOwnerEnterpriseWiFiConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AndroidDeviceOwnerEnterpriseWiFiConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .android_device_owner_certificate_profile_base import AndroidDeviceOwnerCertificateProfileBase
        from .android_device_owner_trusted_root_certificate import AndroidDeviceOwnerTrustedRootCertificate
        from .android_device_owner_wi_fi_configuration import AndroidDeviceOwnerWiFiConfiguration
        from .android_eap_type import AndroidEapType
        from .device_management_derived_credential_settings import DeviceManagementDerivedCredentialSettings
        from .non_eap_authentication_method_for_eap_ttls_type import NonEapAuthenticationMethodForEapTtlsType
        from .non_eap_authentication_method_for_peap import NonEapAuthenticationMethodForPeap
        from .wi_fi_authentication_method import WiFiAuthenticationMethod

        from .android_device_owner_certificate_profile_base import AndroidDeviceOwnerCertificateProfileBase
        from .android_device_owner_trusted_root_certificate import AndroidDeviceOwnerTrustedRootCertificate
        from .android_device_owner_wi_fi_configuration import AndroidDeviceOwnerWiFiConfiguration
        from .android_eap_type import AndroidEapType
        from .device_management_derived_credential_settings import DeviceManagementDerivedCredentialSettings
        from .non_eap_authentication_method_for_eap_ttls_type import NonEapAuthenticationMethodForEapTtlsType
        from .non_eap_authentication_method_for_peap import NonEapAuthenticationMethodForPeap
        from .wi_fi_authentication_method import WiFiAuthenticationMethod

        fields: dict[str, Callable[[Any], None]] = {
            "authenticationMethod": lambda n : setattr(self, 'authentication_method', n.get_enum_value(WiFiAuthenticationMethod)),
            "derivedCredentialSettings": lambda n : setattr(self, 'derived_credential_settings', n.get_object_value(DeviceManagementDerivedCredentialSettings)),
            "eapType": lambda n : setattr(self, 'eap_type', n.get_enum_value(AndroidEapType)),
            "identityCertificateForClientAuthentication": lambda n : setattr(self, 'identity_certificate_for_client_authentication', n.get_object_value(AndroidDeviceOwnerCertificateProfileBase)),
            "innerAuthenticationProtocolForEapTtls": lambda n : setattr(self, 'inner_authentication_protocol_for_eap_ttls', n.get_enum_value(NonEapAuthenticationMethodForEapTtlsType)),
            "innerAuthenticationProtocolForPeap": lambda n : setattr(self, 'inner_authentication_protocol_for_peap', n.get_enum_value(NonEapAuthenticationMethodForPeap)),
            "outerIdentityPrivacyTemporaryValue": lambda n : setattr(self, 'outer_identity_privacy_temporary_value', n.get_str_value()),
            "rootCertificateForServerValidation": lambda n : setattr(self, 'root_certificate_for_server_validation', n.get_object_value(AndroidDeviceOwnerTrustedRootCertificate)),
            "rootCertificatesForServerValidation": lambda n : setattr(self, 'root_certificates_for_server_validation', n.get_collection_of_object_values(AndroidDeviceOwnerTrustedRootCertificate)),
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
        writer.write_object_value("derivedCredentialSettings", self.derived_credential_settings)
        writer.write_enum_value("eapType", self.eap_type)
        writer.write_object_value("identityCertificateForClientAuthentication", self.identity_certificate_for_client_authentication)
        writer.write_enum_value("innerAuthenticationProtocolForEapTtls", self.inner_authentication_protocol_for_eap_ttls)
        writer.write_enum_value("innerAuthenticationProtocolForPeap", self.inner_authentication_protocol_for_peap)
        writer.write_str_value("outerIdentityPrivacyTemporaryValue", self.outer_identity_privacy_temporary_value)
        writer.write_object_value("rootCertificateForServerValidation", self.root_certificate_for_server_validation)
        writer.write_collection_of_object_values("rootCertificatesForServerValidation", self.root_certificates_for_server_validation)
        writer.write_collection_of_primitive_values("trustedServerCertificateNames", self.trusted_server_certificate_names)
    

