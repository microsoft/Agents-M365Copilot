from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .apple_vpn_always_on_configuration import AppleVpnAlwaysOnConfiguration
    from .ios_vpn_configuration import IosVpnConfiguration
    from .ios_vpn_security_association_parameters import IosVpnSecurityAssociationParameters
    from .vpn_client_authentication_type import VpnClientAuthenticationType
    from .vpn_dead_peer_detection_rate import VpnDeadPeerDetectionRate
    from .vpn_local_identifier import VpnLocalIdentifier
    from .vpn_server_certificate_type import VpnServerCertificateType

from .ios_vpn_configuration import IosVpnConfiguration

@dataclass
class IosikEv2VpnConfiguration(IosVpnConfiguration, Parsable):
    """
    By providing the configurations in this profile you can instruct the iOS device to connect to desired IKEv2 VPN endpoint.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.iosikEv2VpnConfiguration"
    # Allows the use of child security association parameters by setting all parameters to the device's default unless explicitly specified.
    allow_default_child_security_association_parameters: Optional[bool] = None
    # Allows the use of security association parameters by setting all parameters to the device's default unless explicitly specified.
    allow_default_security_association_parameters: Optional[bool] = None
    # AlwaysOn Configuration
    always_on_configuration: Optional[AppleVpnAlwaysOnConfiguration] = None
    # Child Security Association Parameters
    child_security_association_parameters: Optional[IosVpnSecurityAssociationParameters] = None
    # The type of VPN client authentication type
    client_authentication_type: Optional[VpnClientAuthenticationType] = None
    # Determine how often to check if a peer connection is still active. . Possible values are: medium, none, low, high.
    dead_peer_detection_rate: Optional[VpnDeadPeerDetectionRate] = None
    # Disable MOBIKE
    disable_mobility_and_multihoming: Optional[bool] = None
    # Disable Redirect
    disable_redirect: Optional[bool] = None
    # Determines if Always on VPN is enabled
    enable_always_on_configuration: Optional[bool] = None
    # Enables a best-effort revocation check; server response timeouts will not cause it to fail
    enable_certificate_revocation_check: Optional[bool] = None
    # Enables EAP only authentication
    enable_e_a_p: Optional[bool] = None
    # Enable Perfect Forward Secrecy (PFS).
    enable_perfect_forward_secrecy: Optional[bool] = None
    # Enable Use Internal Subnet Attributes.
    enable_use_internal_subnet_attributes: Optional[bool] = None
    # The type of VPN local identifier
    local_identifier: Optional[VpnLocalIdentifier] = None
    # Maximum transmission unit. Valid values 1280 to 1400
    mtu_size_in_bytes: Optional[int] = None
    # Address of the IKEv2 server. Must be a FQDN, UserFQDN, network address, or ASN1DN
    remote_identifier: Optional[str] = None
    # Security Association Parameters
    security_association_parameters: Optional[IosVpnSecurityAssociationParameters] = None
    # Common name of the IKEv2 Server Certificate used in Server Authentication
    server_certificate_common_name: Optional[str] = None
    # Issuer Common name of the IKEv2 Server Certificate issuer used in Authentication
    server_certificate_issuer_common_name: Optional[str] = None
    # The type of certificate the VPN server will present to the VPN client for authentication. Possible values are: rsa, ecdsa256, ecdsa384, ecdsa521.
    server_certificate_type: Optional[VpnServerCertificateType] = None
    # Used when Shared Secret Authentication is selected
    shared_secret: Optional[str] = None
    # The maximum TLS version to be used with EAP-TLS authentication
    tls_maximum_version: Optional[str] = None
    # The minimum TLS version to be used with EAP-TLS authentication
    tls_minimum_version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IosikEv2VpnConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IosikEv2VpnConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IosikEv2VpnConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .apple_vpn_always_on_configuration import AppleVpnAlwaysOnConfiguration
        from .ios_vpn_configuration import IosVpnConfiguration
        from .ios_vpn_security_association_parameters import IosVpnSecurityAssociationParameters
        from .vpn_client_authentication_type import VpnClientAuthenticationType
        from .vpn_dead_peer_detection_rate import VpnDeadPeerDetectionRate
        from .vpn_local_identifier import VpnLocalIdentifier
        from .vpn_server_certificate_type import VpnServerCertificateType

        from .apple_vpn_always_on_configuration import AppleVpnAlwaysOnConfiguration
        from .ios_vpn_configuration import IosVpnConfiguration
        from .ios_vpn_security_association_parameters import IosVpnSecurityAssociationParameters
        from .vpn_client_authentication_type import VpnClientAuthenticationType
        from .vpn_dead_peer_detection_rate import VpnDeadPeerDetectionRate
        from .vpn_local_identifier import VpnLocalIdentifier
        from .vpn_server_certificate_type import VpnServerCertificateType

        fields: dict[str, Callable[[Any], None]] = {
            "allowDefaultChildSecurityAssociationParameters": lambda n : setattr(self, 'allow_default_child_security_association_parameters', n.get_bool_value()),
            "allowDefaultSecurityAssociationParameters": lambda n : setattr(self, 'allow_default_security_association_parameters', n.get_bool_value()),
            "alwaysOnConfiguration": lambda n : setattr(self, 'always_on_configuration', n.get_object_value(AppleVpnAlwaysOnConfiguration)),
            "childSecurityAssociationParameters": lambda n : setattr(self, 'child_security_association_parameters', n.get_object_value(IosVpnSecurityAssociationParameters)),
            "clientAuthenticationType": lambda n : setattr(self, 'client_authentication_type', n.get_enum_value(VpnClientAuthenticationType)),
            "deadPeerDetectionRate": lambda n : setattr(self, 'dead_peer_detection_rate', n.get_enum_value(VpnDeadPeerDetectionRate)),
            "disableMobilityAndMultihoming": lambda n : setattr(self, 'disable_mobility_and_multihoming', n.get_bool_value()),
            "disableRedirect": lambda n : setattr(self, 'disable_redirect', n.get_bool_value()),
            "enableAlwaysOnConfiguration": lambda n : setattr(self, 'enable_always_on_configuration', n.get_bool_value()),
            "enableCertificateRevocationCheck": lambda n : setattr(self, 'enable_certificate_revocation_check', n.get_bool_value()),
            "enableEAP": lambda n : setattr(self, 'enable_e_a_p', n.get_bool_value()),
            "enablePerfectForwardSecrecy": lambda n : setattr(self, 'enable_perfect_forward_secrecy', n.get_bool_value()),
            "enableUseInternalSubnetAttributes": lambda n : setattr(self, 'enable_use_internal_subnet_attributes', n.get_bool_value()),
            "localIdentifier": lambda n : setattr(self, 'local_identifier', n.get_enum_value(VpnLocalIdentifier)),
            "mtuSizeInBytes": lambda n : setattr(self, 'mtu_size_in_bytes', n.get_int_value()),
            "remoteIdentifier": lambda n : setattr(self, 'remote_identifier', n.get_str_value()),
            "securityAssociationParameters": lambda n : setattr(self, 'security_association_parameters', n.get_object_value(IosVpnSecurityAssociationParameters)),
            "serverCertificateCommonName": lambda n : setattr(self, 'server_certificate_common_name', n.get_str_value()),
            "serverCertificateIssuerCommonName": lambda n : setattr(self, 'server_certificate_issuer_common_name', n.get_str_value()),
            "serverCertificateType": lambda n : setattr(self, 'server_certificate_type', n.get_enum_value(VpnServerCertificateType)),
            "sharedSecret": lambda n : setattr(self, 'shared_secret', n.get_str_value()),
            "tlsMaximumVersion": lambda n : setattr(self, 'tls_maximum_version', n.get_str_value()),
            "tlsMinimumVersion": lambda n : setattr(self, 'tls_minimum_version', n.get_str_value()),
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
        writer.write_bool_value("allowDefaultChildSecurityAssociationParameters", self.allow_default_child_security_association_parameters)
        writer.write_bool_value("allowDefaultSecurityAssociationParameters", self.allow_default_security_association_parameters)
        writer.write_object_value("alwaysOnConfiguration", self.always_on_configuration)
        writer.write_object_value("childSecurityAssociationParameters", self.child_security_association_parameters)
        writer.write_enum_value("clientAuthenticationType", self.client_authentication_type)
        writer.write_enum_value("deadPeerDetectionRate", self.dead_peer_detection_rate)
        writer.write_bool_value("disableMobilityAndMultihoming", self.disable_mobility_and_multihoming)
        writer.write_bool_value("disableRedirect", self.disable_redirect)
        writer.write_bool_value("enableAlwaysOnConfiguration", self.enable_always_on_configuration)
        writer.write_bool_value("enableCertificateRevocationCheck", self.enable_certificate_revocation_check)
        writer.write_bool_value("enableEAP", self.enable_e_a_p)
        writer.write_bool_value("enablePerfectForwardSecrecy", self.enable_perfect_forward_secrecy)
        writer.write_bool_value("enableUseInternalSubnetAttributes", self.enable_use_internal_subnet_attributes)
        writer.write_enum_value("localIdentifier", self.local_identifier)
        writer.write_int_value("mtuSizeInBytes", self.mtu_size_in_bytes)
        writer.write_str_value("remoteIdentifier", self.remote_identifier)
        writer.write_object_value("securityAssociationParameters", self.security_association_parameters)
        writer.write_str_value("serverCertificateCommonName", self.server_certificate_common_name)
        writer.write_str_value("serverCertificateIssuerCommonName", self.server_certificate_issuer_common_name)
        writer.write_enum_value("serverCertificateType", self.server_certificate_type)
        writer.write_str_value("sharedSecret", self.shared_secret)
        writer.write_str_value("tlsMaximumVersion", self.tls_maximum_version)
        writer.write_str_value("tlsMinimumVersion", self.tls_minimum_version)
    

