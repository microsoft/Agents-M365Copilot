from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_configuration import DeviceConfiguration
    from .eap_type import EapType
    from .non_eap_authentication_method_for_eap_ttls_type import NonEapAuthenticationMethodForEapTtlsType
    from .windows81_trusted_root_certificate import Windows81TrustedRootCertificate
    from .windows_certificate_profile_base import WindowsCertificateProfileBase
    from .wired_network_authentication_method import WiredNetworkAuthenticationMethod
    from .wired_network_authentication_type import WiredNetworkAuthenticationType

from .device_configuration import DeviceConfiguration

@dataclass
class WindowsWiredNetworkConfiguration(DeviceConfiguration, Parsable):
    """
    This entity provides descriptions of the declared methods, properties and relationships exposed by the Wired Network CSP.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsWiredNetworkConfiguration"
    # Specify the duration for which automatic authentication attempts will be blocked from occuring after a failed authentication attempt.
    authentication_block_period_in_minutes: Optional[int] = None
    # Specify the authentication method. Possible values are: certificate, usernameAndPassword, derivedCredential. Possible values are: certificate, usernameAndPassword, derivedCredential, unknownFutureValue.
    authentication_method: Optional[WiredNetworkAuthenticationMethod] = None
    # Specify the number of seconds for the client to wait after an authentication attempt before failing. Valid range 1-3600.
    authentication_period_in_seconds: Optional[int] = None
    # Specify the number of seconds between a failed authentication and the next authentication attempt. Valid range 1-3600.
    authentication_retry_delay_period_in_seconds: Optional[int] = None
    # Specify whether to authenticate the user, the device, either, or to use guest authentication (none). If you're using certificate authentication, make sure the certificate type matches the authentication type. Possible values are: none, user, machine, machineOrUser, guest. Possible values are: none, user, machine, machineOrUser, guest, unknownFutureValue.
    authentication_type: Optional[WiredNetworkAuthenticationType] = None
    # When TRUE, caches user credentials on the device so that users don't need to keep entering them each time they connect. When FALSE, do not cache credentials. Default value is FALSE.
    cache_credentials: Optional[bool] = None
    # When TRUE, prevents the user from being prompted to authorize new servers for trusted certification authorities when EAP type is selected as PEAP. When FALSE, does not prevent the user from being prompted. Default value is FALSE.
    disable_user_prompt_for_server_validation: Optional[bool] = None
    # Extensible Authentication Protocol (EAP) configuration types.
    eap_type: Optional[EapType] = None
    # Specify the number of seconds to wait before sending an EAPOL (Extensible Authentication Protocol over LAN) Start message. Valid range 1-3600.
    eapol_start_period_in_seconds: Optional[int] = None
    # When TRUE, the automatic configuration service for wired networks requires the use of 802.1X for port authentication. When FALSE, 802.1X is not required. Default value is FALSE.
    enforce8021_x: Optional[bool] = None
    # When TRUE, forces FIPS compliance. When FALSE, does not enable FIPS compliance. Default value is FALSE.
    force_f_i_p_s_compliance: Optional[bool] = None
    # Specify identity certificate for client authentication.
    identity_certificate_for_client_authentication: Optional[WindowsCertificateProfileBase] = None
    # Specify inner authentication protocol for EAP TTLS. Possible values are: unencryptedPassword, challengeHandshakeAuthenticationProtocol, microsoftChap, microsoftChapVersionTwo. Possible values are: unencryptedPassword, challengeHandshakeAuthenticationProtocol, microsoftChap, microsoftChapVersionTwo.
    inner_authentication_protocol_for_e_a_p_t_t_l_s: Optional[NonEapAuthenticationMethodForEapTtlsType] = None
    # Specify the maximum authentication failures allowed for a set of credentials. Valid range 1-100.
    maximum_authentication_failures: Optional[int] = None
    # Specify the maximum number of EAPOL (Extensible Authentication Protocol over LAN) Start messages to be sent before returning failure. Valid range 1-100.
    maximum_e_a_p_o_l_start_messages: Optional[int] = None
    # Specify the string to replace usernames for privacy when using EAP TTLS or PEAP.
    outer_identity_privacy_temporary_value: Optional[str] = None
    # When TRUE, enables verification of server's identity by validating the certificate when EAP type is selected as PEAP. When FALSE, the certificate is not validated. Default value is TRUE.
    perform_server_validation: Optional[bool] = None
    # When TRUE, enables cryptographic binding when EAP type is selected as PEAP. When FALSE, does not enable cryptogrpahic binding. Default value is TRUE.
    require_cryptographic_binding: Optional[bool] = None
    # Specify root certificate for client validation.
    root_certificate_for_client_validation: Optional[Windows81TrustedRootCertificate] = None
    # Specify root certificates for server validation. This collection can contain a maximum of 500 elements.
    root_certificates_for_server_validation: Optional[list[Windows81TrustedRootCertificate]] = None
    # Specify the secondary authentication method. Possible values are: certificate, usernameAndPassword, derivedCredential. Possible values are: certificate, usernameAndPassword, derivedCredential, unknownFutureValue.
    secondary_authentication_method: Optional[WiredNetworkAuthenticationMethod] = None
    # Specify secondary identity certificate for client authentication.
    secondary_identity_certificate_for_client_authentication: Optional[WindowsCertificateProfileBase] = None
    # Specify secondary root certificate for client validation.
    secondary_root_certificate_for_client_validation: Optional[Windows81TrustedRootCertificate] = None
    # Specify trusted server certificate names.
    trusted_server_certificate_names: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsWiredNetworkConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsWiredNetworkConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsWiredNetworkConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_configuration import DeviceConfiguration
        from .eap_type import EapType
        from .non_eap_authentication_method_for_eap_ttls_type import NonEapAuthenticationMethodForEapTtlsType
        from .windows81_trusted_root_certificate import Windows81TrustedRootCertificate
        from .windows_certificate_profile_base import WindowsCertificateProfileBase
        from .wired_network_authentication_method import WiredNetworkAuthenticationMethod
        from .wired_network_authentication_type import WiredNetworkAuthenticationType

        from .device_configuration import DeviceConfiguration
        from .eap_type import EapType
        from .non_eap_authentication_method_for_eap_ttls_type import NonEapAuthenticationMethodForEapTtlsType
        from .windows81_trusted_root_certificate import Windows81TrustedRootCertificate
        from .windows_certificate_profile_base import WindowsCertificateProfileBase
        from .wired_network_authentication_method import WiredNetworkAuthenticationMethod
        from .wired_network_authentication_type import WiredNetworkAuthenticationType

        fields: dict[str, Callable[[Any], None]] = {
            "authenticationBlockPeriodInMinutes": lambda n : setattr(self, 'authentication_block_period_in_minutes', n.get_int_value()),
            "authenticationMethod": lambda n : setattr(self, 'authentication_method', n.get_enum_value(WiredNetworkAuthenticationMethod)),
            "authenticationPeriodInSeconds": lambda n : setattr(self, 'authentication_period_in_seconds', n.get_int_value()),
            "authenticationRetryDelayPeriodInSeconds": lambda n : setattr(self, 'authentication_retry_delay_period_in_seconds', n.get_int_value()),
            "authenticationType": lambda n : setattr(self, 'authentication_type', n.get_enum_value(WiredNetworkAuthenticationType)),
            "cacheCredentials": lambda n : setattr(self, 'cache_credentials', n.get_bool_value()),
            "disableUserPromptForServerValidation": lambda n : setattr(self, 'disable_user_prompt_for_server_validation', n.get_bool_value()),
            "eapType": lambda n : setattr(self, 'eap_type', n.get_enum_value(EapType)),
            "eapolStartPeriodInSeconds": lambda n : setattr(self, 'eapol_start_period_in_seconds', n.get_int_value()),
            "enforce8021X": lambda n : setattr(self, 'enforce8021_x', n.get_bool_value()),
            "forceFIPSCompliance": lambda n : setattr(self, 'force_f_i_p_s_compliance', n.get_bool_value()),
            "identityCertificateForClientAuthentication": lambda n : setattr(self, 'identity_certificate_for_client_authentication', n.get_object_value(WindowsCertificateProfileBase)),
            "innerAuthenticationProtocolForEAPTTLS": lambda n : setattr(self, 'inner_authentication_protocol_for_e_a_p_t_t_l_s', n.get_enum_value(NonEapAuthenticationMethodForEapTtlsType)),
            "maximumAuthenticationFailures": lambda n : setattr(self, 'maximum_authentication_failures', n.get_int_value()),
            "maximumEAPOLStartMessages": lambda n : setattr(self, 'maximum_e_a_p_o_l_start_messages', n.get_int_value()),
            "outerIdentityPrivacyTemporaryValue": lambda n : setattr(self, 'outer_identity_privacy_temporary_value', n.get_str_value()),
            "performServerValidation": lambda n : setattr(self, 'perform_server_validation', n.get_bool_value()),
            "requireCryptographicBinding": lambda n : setattr(self, 'require_cryptographic_binding', n.get_bool_value()),
            "rootCertificateForClientValidation": lambda n : setattr(self, 'root_certificate_for_client_validation', n.get_object_value(Windows81TrustedRootCertificate)),
            "rootCertificatesForServerValidation": lambda n : setattr(self, 'root_certificates_for_server_validation', n.get_collection_of_object_values(Windows81TrustedRootCertificate)),
            "secondaryAuthenticationMethod": lambda n : setattr(self, 'secondary_authentication_method', n.get_enum_value(WiredNetworkAuthenticationMethod)),
            "secondaryIdentityCertificateForClientAuthentication": lambda n : setattr(self, 'secondary_identity_certificate_for_client_authentication', n.get_object_value(WindowsCertificateProfileBase)),
            "secondaryRootCertificateForClientValidation": lambda n : setattr(self, 'secondary_root_certificate_for_client_validation', n.get_object_value(Windows81TrustedRootCertificate)),
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
        writer.write_int_value("authenticationBlockPeriodInMinutes", self.authentication_block_period_in_minutes)
        writer.write_enum_value("authenticationMethod", self.authentication_method)
        writer.write_int_value("authenticationPeriodInSeconds", self.authentication_period_in_seconds)
        writer.write_int_value("authenticationRetryDelayPeriodInSeconds", self.authentication_retry_delay_period_in_seconds)
        writer.write_enum_value("authenticationType", self.authentication_type)
        writer.write_bool_value("cacheCredentials", self.cache_credentials)
        writer.write_bool_value("disableUserPromptForServerValidation", self.disable_user_prompt_for_server_validation)
        writer.write_enum_value("eapType", self.eap_type)
        writer.write_int_value("eapolStartPeriodInSeconds", self.eapol_start_period_in_seconds)
        writer.write_bool_value("enforce8021X", self.enforce8021_x)
        writer.write_bool_value("forceFIPSCompliance", self.force_f_i_p_s_compliance)
        writer.write_object_value("identityCertificateForClientAuthentication", self.identity_certificate_for_client_authentication)
        writer.write_enum_value("innerAuthenticationProtocolForEAPTTLS", self.inner_authentication_protocol_for_e_a_p_t_t_l_s)
        writer.write_int_value("maximumAuthenticationFailures", self.maximum_authentication_failures)
        writer.write_int_value("maximumEAPOLStartMessages", self.maximum_e_a_p_o_l_start_messages)
        writer.write_str_value("outerIdentityPrivacyTemporaryValue", self.outer_identity_privacy_temporary_value)
        writer.write_bool_value("performServerValidation", self.perform_server_validation)
        writer.write_bool_value("requireCryptographicBinding", self.require_cryptographic_binding)
        writer.write_object_value("rootCertificateForClientValidation", self.root_certificate_for_client_validation)
        writer.write_collection_of_object_values("rootCertificatesForServerValidation", self.root_certificates_for_server_validation)
        writer.write_enum_value("secondaryAuthenticationMethod", self.secondary_authentication_method)
        writer.write_object_value("secondaryIdentityCertificateForClientAuthentication", self.secondary_identity_certificate_for_client_authentication)
        writer.write_object_value("secondaryRootCertificateForClientValidation", self.secondary_root_certificate_for_client_validation)
        writer.write_collection_of_primitive_values("trustedServerCertificateNames", self.trusted_server_certificate_names)
    

