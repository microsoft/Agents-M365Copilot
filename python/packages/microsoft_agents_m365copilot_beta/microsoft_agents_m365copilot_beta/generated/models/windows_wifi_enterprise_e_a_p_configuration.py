from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .eap_type import EapType
    from .network_single_sign_on_type import NetworkSingleSignOnType
    from .non_eap_authentication_method_for_eap_ttls_type import NonEapAuthenticationMethodForEapTtlsType
    from .wifi_authentication_type import WifiAuthenticationType
    from .windows81_trusted_root_certificate import Windows81TrustedRootCertificate
    from .windows_certificate_profile_base import WindowsCertificateProfileBase
    from .windows_wifi_configuration import WindowsWifiConfiguration
    from .wi_fi_authentication_method import WiFiAuthenticationMethod

from .windows_wifi_configuration import WindowsWifiConfiguration

@dataclass
class WindowsWifiEnterpriseEAPConfiguration(WindowsWifiConfiguration, Parsable):
    """
    This entity provides descriptions of the declared methods, properties and relationships exposed by the Wifi CSP.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsWifiEnterpriseEAPConfiguration"
    # Specify the authentication method. Possible values are: certificate, usernameAndPassword, derivedCredential.
    authentication_method: Optional[WiFiAuthenticationMethod] = None
    # Specify the number of seconds for the client to wait after an authentication attempt before failing. Valid range 1-3600.
    authentication_period_in_seconds: Optional[int] = None
    # Specify the number of seconds between a failed authentication and the next authentication attempt. Valid range 1-3600.
    authentication_retry_delay_period_in_seconds: Optional[int] = None
    # Specify whether to authenticate the user, the device, either, or to use guest authentication (none). If you’re using certificate authentication, make sure the certificate type matches the authentication type. Possible values are: none, user, machine, machineOrUser, guest.
    authentication_type: Optional[WifiAuthenticationType] = None
    # Specify whether to cache user credentials on the device so that users don’t need to keep entering them each time they connect.
    cache_credentials: Optional[bool] = None
    # Specify whether to prevent the user from being prompted to authorize new servers for trusted certification authorities when EAP type is selected as PEAP.
    disable_user_prompt_for_server_validation: Optional[bool] = None
    # Extensible Authentication Protocol (EAP) configuration types.
    eap_type: Optional[EapType] = None
    # Specify the number of seconds to wait before sending an EAPOL (Extensible Authentication Protocol over LAN) Start message. Valid range 1-3600.
    eapol_start_period_in_seconds: Optional[int] = None
    # Specify whether the wifi connection should enable pairwise master key caching.
    enable_pairwise_master_key_caching: Optional[bool] = None
    # Specify whether pre-authentication should be enabled.
    enable_pre_authentication: Optional[bool] = None
    # Specify identity certificate for client authentication.
    identity_certificate_for_client_authentication: Optional[WindowsCertificateProfileBase] = None
    # Specify inner authentication protocol for EAP TTLS. Possible values are: unencryptedPassword, challengeHandshakeAuthenticationProtocol, microsoftChap, microsoftChapVersionTwo.
    inner_authentication_protocol_for_e_a_p_t_t_l_s: Optional[NonEapAuthenticationMethodForEapTtlsType] = None
    # Specify the maximum authentication failures allowed for a set of credentials. Valid range 1-100.
    maximum_authentication_failures: Optional[int] = None
    # Specify maximum authentication timeout (in seconds).  Valid range: 1-120
    maximum_authentication_timeout_in_seconds: Optional[int] = None
    # Specifiy the maximum number of EAPOL (Extensible Authentication Protocol over LAN) Start messages to be sent before returning failure. Valid range 1-100.
    maximum_e_a_p_o_l_start_messages: Optional[int] = None
    # Specify maximum number of pairwise master keys in cache.  Valid range: 1-255
    maximum_number_of_pairwise_master_keys_in_cache: Optional[int] = None
    # Specify maximum pairwise master key cache time (in minutes).  Valid range: 5-1440
    maximum_pairwise_master_key_cache_time_in_minutes: Optional[int] = None
    # Specify maximum pre-authentication attempts.  Valid range: 1-16
    maximum_pre_authentication_attempts: Optional[int] = None
    # Specify the network single sign on type. Possible values are: disabled, prelogon, postlogon.
    network_single_sign_on: Optional[NetworkSingleSignOnType] = None
    # Specify the string to replace usernames for privacy when using EAP TTLS or PEAP.
    outer_identity_privacy_temporary_value: Optional[str] = None
    # Specify whether to enable verification of server's identity by validating the certificate when EAP type is selected as PEAP.
    perform_server_validation: Optional[bool] = None
    # Specify whether the wifi connection should prompt for additional authentication credentials.
    prompt_for_additional_authentication_credentials: Optional[bool] = None
    # Specify whether to enable cryptographic binding when EAP type is selected as PEAP.
    require_cryptographic_binding: Optional[bool] = None
    # Specify root certificate for client validation.
    root_certificate_for_client_validation: Optional[Windows81TrustedRootCertificate] = None
    # Specify root certificate for server validation. This collection can contain a maximum of 500 elements.
    root_certificates_for_server_validation: Optional[list[Windows81TrustedRootCertificate]] = None
    # Specify trusted server certificate names.
    trusted_server_certificate_names: Optional[list[str]] = None
    # Specifiy whether to change the virtual LAN used by the device based on the user’s credentials. Cannot be used when NetworkSingleSignOnType is set to ​Disabled.
    user_based_virtual_lan: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsWifiEnterpriseEAPConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsWifiEnterpriseEAPConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsWifiEnterpriseEAPConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .eap_type import EapType
        from .network_single_sign_on_type import NetworkSingleSignOnType
        from .non_eap_authentication_method_for_eap_ttls_type import NonEapAuthenticationMethodForEapTtlsType
        from .wifi_authentication_type import WifiAuthenticationType
        from .windows81_trusted_root_certificate import Windows81TrustedRootCertificate
        from .windows_certificate_profile_base import WindowsCertificateProfileBase
        from .windows_wifi_configuration import WindowsWifiConfiguration
        from .wi_fi_authentication_method import WiFiAuthenticationMethod

        from .eap_type import EapType
        from .network_single_sign_on_type import NetworkSingleSignOnType
        from .non_eap_authentication_method_for_eap_ttls_type import NonEapAuthenticationMethodForEapTtlsType
        from .wifi_authentication_type import WifiAuthenticationType
        from .windows81_trusted_root_certificate import Windows81TrustedRootCertificate
        from .windows_certificate_profile_base import WindowsCertificateProfileBase
        from .windows_wifi_configuration import WindowsWifiConfiguration
        from .wi_fi_authentication_method import WiFiAuthenticationMethod

        fields: dict[str, Callable[[Any], None]] = {
            "authenticationMethod": lambda n : setattr(self, 'authentication_method', n.get_enum_value(WiFiAuthenticationMethod)),
            "authenticationPeriodInSeconds": lambda n : setattr(self, 'authentication_period_in_seconds', n.get_int_value()),
            "authenticationRetryDelayPeriodInSeconds": lambda n : setattr(self, 'authentication_retry_delay_period_in_seconds', n.get_int_value()),
            "authenticationType": lambda n : setattr(self, 'authentication_type', n.get_enum_value(WifiAuthenticationType)),
            "cacheCredentials": lambda n : setattr(self, 'cache_credentials', n.get_bool_value()),
            "disableUserPromptForServerValidation": lambda n : setattr(self, 'disable_user_prompt_for_server_validation', n.get_bool_value()),
            "eapType": lambda n : setattr(self, 'eap_type', n.get_enum_value(EapType)),
            "eapolStartPeriodInSeconds": lambda n : setattr(self, 'eapol_start_period_in_seconds', n.get_int_value()),
            "enablePairwiseMasterKeyCaching": lambda n : setattr(self, 'enable_pairwise_master_key_caching', n.get_bool_value()),
            "enablePreAuthentication": lambda n : setattr(self, 'enable_pre_authentication', n.get_bool_value()),
            "identityCertificateForClientAuthentication": lambda n : setattr(self, 'identity_certificate_for_client_authentication', n.get_object_value(WindowsCertificateProfileBase)),
            "innerAuthenticationProtocolForEAPTTLS": lambda n : setattr(self, 'inner_authentication_protocol_for_e_a_p_t_t_l_s', n.get_enum_value(NonEapAuthenticationMethodForEapTtlsType)),
            "maximumAuthenticationFailures": lambda n : setattr(self, 'maximum_authentication_failures', n.get_int_value()),
            "maximumAuthenticationTimeoutInSeconds": lambda n : setattr(self, 'maximum_authentication_timeout_in_seconds', n.get_int_value()),
            "maximumEAPOLStartMessages": lambda n : setattr(self, 'maximum_e_a_p_o_l_start_messages', n.get_int_value()),
            "maximumNumberOfPairwiseMasterKeysInCache": lambda n : setattr(self, 'maximum_number_of_pairwise_master_keys_in_cache', n.get_int_value()),
            "maximumPairwiseMasterKeyCacheTimeInMinutes": lambda n : setattr(self, 'maximum_pairwise_master_key_cache_time_in_minutes', n.get_int_value()),
            "maximumPreAuthenticationAttempts": lambda n : setattr(self, 'maximum_pre_authentication_attempts', n.get_int_value()),
            "networkSingleSignOn": lambda n : setattr(self, 'network_single_sign_on', n.get_enum_value(NetworkSingleSignOnType)),
            "outerIdentityPrivacyTemporaryValue": lambda n : setattr(self, 'outer_identity_privacy_temporary_value', n.get_str_value()),
            "performServerValidation": lambda n : setattr(self, 'perform_server_validation', n.get_bool_value()),
            "promptForAdditionalAuthenticationCredentials": lambda n : setattr(self, 'prompt_for_additional_authentication_credentials', n.get_bool_value()),
            "requireCryptographicBinding": lambda n : setattr(self, 'require_cryptographic_binding', n.get_bool_value()),
            "rootCertificateForClientValidation": lambda n : setattr(self, 'root_certificate_for_client_validation', n.get_object_value(Windows81TrustedRootCertificate)),
            "rootCertificatesForServerValidation": lambda n : setattr(self, 'root_certificates_for_server_validation', n.get_collection_of_object_values(Windows81TrustedRootCertificate)),
            "trustedServerCertificateNames": lambda n : setattr(self, 'trusted_server_certificate_names', n.get_collection_of_primitive_values(str)),
            "userBasedVirtualLan": lambda n : setattr(self, 'user_based_virtual_lan', n.get_bool_value()),
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
        writer.write_int_value("authenticationPeriodInSeconds", self.authentication_period_in_seconds)
        writer.write_int_value("authenticationRetryDelayPeriodInSeconds", self.authentication_retry_delay_period_in_seconds)
        writer.write_enum_value("authenticationType", self.authentication_type)
        writer.write_bool_value("cacheCredentials", self.cache_credentials)
        writer.write_bool_value("disableUserPromptForServerValidation", self.disable_user_prompt_for_server_validation)
        writer.write_enum_value("eapType", self.eap_type)
        writer.write_int_value("eapolStartPeriodInSeconds", self.eapol_start_period_in_seconds)
        writer.write_bool_value("enablePairwiseMasterKeyCaching", self.enable_pairwise_master_key_caching)
        writer.write_bool_value("enablePreAuthentication", self.enable_pre_authentication)
        writer.write_object_value("identityCertificateForClientAuthentication", self.identity_certificate_for_client_authentication)
        writer.write_enum_value("innerAuthenticationProtocolForEAPTTLS", self.inner_authentication_protocol_for_e_a_p_t_t_l_s)
        writer.write_int_value("maximumAuthenticationFailures", self.maximum_authentication_failures)
        writer.write_int_value("maximumAuthenticationTimeoutInSeconds", self.maximum_authentication_timeout_in_seconds)
        writer.write_int_value("maximumEAPOLStartMessages", self.maximum_e_a_p_o_l_start_messages)
        writer.write_int_value("maximumNumberOfPairwiseMasterKeysInCache", self.maximum_number_of_pairwise_master_keys_in_cache)
        writer.write_int_value("maximumPairwiseMasterKeyCacheTimeInMinutes", self.maximum_pairwise_master_key_cache_time_in_minutes)
        writer.write_int_value("maximumPreAuthenticationAttempts", self.maximum_pre_authentication_attempts)
        writer.write_enum_value("networkSingleSignOn", self.network_single_sign_on)
        writer.write_str_value("outerIdentityPrivacyTemporaryValue", self.outer_identity_privacy_temporary_value)
        writer.write_bool_value("performServerValidation", self.perform_server_validation)
        writer.write_bool_value("promptForAdditionalAuthenticationCredentials", self.prompt_for_additional_authentication_credentials)
        writer.write_bool_value("requireCryptographicBinding", self.require_cryptographic_binding)
        writer.write_object_value("rootCertificateForClientValidation", self.root_certificate_for_client_validation)
        writer.write_collection_of_object_values("rootCertificatesForServerValidation", self.root_certificates_for_server_validation)
        writer.write_collection_of_primitive_values("trustedServerCertificateNames", self.trusted_server_certificate_names)
        writer.write_bool_value("userBasedVirtualLan", self.user_based_virtual_lan)
    

