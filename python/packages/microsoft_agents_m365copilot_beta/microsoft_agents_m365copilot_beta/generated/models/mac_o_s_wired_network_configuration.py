from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .apple_deployment_channel import AppleDeploymentChannel
    from .device_configuration import DeviceConfiguration
    from .eap_fast_configuration import EapFastConfiguration
    from .eap_type import EapType
    from .mac_o_s_certificate_profile_base import MacOSCertificateProfileBase
    from .mac_o_s_trusted_root_certificate import MacOSTrustedRootCertificate
    from .non_eap_authentication_method_for_eap_ttls_type import NonEapAuthenticationMethodForEapTtlsType
    from .wired_network_interface import WiredNetworkInterface
    from .wi_fi_authentication_method import WiFiAuthenticationMethod

from .device_configuration import DeviceConfiguration

@dataclass
class MacOSWiredNetworkConfiguration(DeviceConfiguration, Parsable):
    """
    MacOS wired network configuration profile.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.macOSWiredNetworkConfiguration"
    # Authentication Method when EAP Type is configured to PEAP or EAP-TTLS. Possible values are: certificate, usernameAndPassword, derivedCredential.
    authentication_method: Optional[WiFiAuthenticationMethod] = None
    # Indicates the deployment channel type used to deploy the configuration profile. Possible values are deviceChannel, userChannel. Possible values are: deviceChannel, userChannel, unknownFutureValue.
    deployment_channel: Optional[AppleDeploymentChannel] = None
    # EAP-FAST Configuration Option when EAP-FAST is the selected EAP Type. Possible values are: noProtectedAccessCredential, useProtectedAccessCredential, useProtectedAccessCredentialAndProvision, useProtectedAccessCredentialAndProvisionAnonymously.
    eap_fast_configuration: Optional[EapFastConfiguration] = None
    # Extensible Authentication Protocol (EAP) configuration types.
    eap_type: Optional[EapType] = None
    # Enable identity privacy (Outer Identity) when EAP Type is configured to EAP-TTLS, EAP-FAST or PEAP. This property masks usernames with the text you enter. For example, if you use 'anonymous', each user that authenticates with this wired network using their real username is displayed as 'anonymous'.
    enable_outer_identity_privacy: Optional[str] = None
    # Identity Certificate for client authentication when EAP Type is configured to EAP-TLS, EAP-TTLS (with Certificate Authentication), or PEAP (with Certificate Authentication).
    identity_certificate_for_client_authentication: Optional[MacOSCertificateProfileBase] = None
    # Apple network interface type.
    network_interface: Optional[WiredNetworkInterface] = None
    # Network Name
    network_name: Optional[str] = None
    # Non-EAP Method for Authentication (Inner Identity) when EAP Type is EAP-TTLS and Authenticationmethod is Username and Password. Possible values are: unencryptedPassword, challengeHandshakeAuthenticationProtocol, microsoftChap, microsoftChapVersionTwo.
    non_eap_authentication_method_for_eap_ttls: Optional[NonEapAuthenticationMethodForEapTtlsType] = None
    # Trusted Root Certificate for Server Validation when EAP Type is configured to EAP-TLS/TTLS/FAST or PEAP.
    root_certificate_for_server_validation: Optional[MacOSTrustedRootCertificate] = None
    # Trusted server certificate names when EAP Type is configured to EAP-TLS/TTLS/FAST or PEAP. This is the common name used in the certificates issued by your trusted certificate authority (CA). If you provide this information, you can bypass the dynamic trust dialog that is displayed on end users devices when they connect to this wired network.
    trusted_server_certificate_names: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MacOSWiredNetworkConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MacOSWiredNetworkConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MacOSWiredNetworkConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .apple_deployment_channel import AppleDeploymentChannel
        from .device_configuration import DeviceConfiguration
        from .eap_fast_configuration import EapFastConfiguration
        from .eap_type import EapType
        from .mac_o_s_certificate_profile_base import MacOSCertificateProfileBase
        from .mac_o_s_trusted_root_certificate import MacOSTrustedRootCertificate
        from .non_eap_authentication_method_for_eap_ttls_type import NonEapAuthenticationMethodForEapTtlsType
        from .wired_network_interface import WiredNetworkInterface
        from .wi_fi_authentication_method import WiFiAuthenticationMethod

        from .apple_deployment_channel import AppleDeploymentChannel
        from .device_configuration import DeviceConfiguration
        from .eap_fast_configuration import EapFastConfiguration
        from .eap_type import EapType
        from .mac_o_s_certificate_profile_base import MacOSCertificateProfileBase
        from .mac_o_s_trusted_root_certificate import MacOSTrustedRootCertificate
        from .non_eap_authentication_method_for_eap_ttls_type import NonEapAuthenticationMethodForEapTtlsType
        from .wired_network_interface import WiredNetworkInterface
        from .wi_fi_authentication_method import WiFiAuthenticationMethod

        fields: dict[str, Callable[[Any], None]] = {
            "authenticationMethod": lambda n : setattr(self, 'authentication_method', n.get_enum_value(WiFiAuthenticationMethod)),
            "deploymentChannel": lambda n : setattr(self, 'deployment_channel', n.get_enum_value(AppleDeploymentChannel)),
            "eapFastConfiguration": lambda n : setattr(self, 'eap_fast_configuration', n.get_enum_value(EapFastConfiguration)),
            "eapType": lambda n : setattr(self, 'eap_type', n.get_enum_value(EapType)),
            "enableOuterIdentityPrivacy": lambda n : setattr(self, 'enable_outer_identity_privacy', n.get_str_value()),
            "identityCertificateForClientAuthentication": lambda n : setattr(self, 'identity_certificate_for_client_authentication', n.get_object_value(MacOSCertificateProfileBase)),
            "networkInterface": lambda n : setattr(self, 'network_interface', n.get_enum_value(WiredNetworkInterface)),
            "networkName": lambda n : setattr(self, 'network_name', n.get_str_value()),
            "nonEapAuthenticationMethodForEapTtls": lambda n : setattr(self, 'non_eap_authentication_method_for_eap_ttls', n.get_enum_value(NonEapAuthenticationMethodForEapTtlsType)),
            "rootCertificateForServerValidation": lambda n : setattr(self, 'root_certificate_for_server_validation', n.get_object_value(MacOSTrustedRootCertificate)),
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
        writer.write_enum_value("deploymentChannel", self.deployment_channel)
        writer.write_enum_value("eapFastConfiguration", self.eap_fast_configuration)
        writer.write_enum_value("eapType", self.eap_type)
        writer.write_str_value("enableOuterIdentityPrivacy", self.enable_outer_identity_privacy)
        writer.write_object_value("identityCertificateForClientAuthentication", self.identity_certificate_for_client_authentication)
        writer.write_enum_value("networkInterface", self.network_interface)
        writer.write_str_value("networkName", self.network_name)
        writer.write_enum_value("nonEapAuthenticationMethodForEapTtls", self.non_eap_authentication_method_for_eap_ttls)
        writer.write_object_value("rootCertificateForServerValidation", self.root_certificate_for_server_validation)
        writer.write_collection_of_primitive_values("trustedServerCertificateNames", self.trusted_server_certificate_names)
    

