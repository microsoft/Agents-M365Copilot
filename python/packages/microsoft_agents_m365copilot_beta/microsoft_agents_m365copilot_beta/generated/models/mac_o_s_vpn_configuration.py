from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .apple_deployment_channel import AppleDeploymentChannel
    from .apple_vpn_configuration import AppleVpnConfiguration
    from .mac_o_s_certificate_profile_base import MacOSCertificateProfileBase

from .apple_vpn_configuration import AppleVpnConfiguration

@dataclass
class MacOSVpnConfiguration(AppleVpnConfiguration, Parsable):
    """
    By providing the configurations in this profile you can instruct the Mac device to connect to desired VPN endpoint. By specifying the authentication method and security types expected by VPN endpoint you can make the VPN connection seamless for end user.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.macOSVpnConfiguration"
    # Indicates the deployment channel type used to deploy the configuration profile. Possible values are deviceChannel, userChannel. Possible values are: deviceChannel, userChannel, unknownFutureValue.
    deployment_channel: Optional[AppleDeploymentChannel] = None
    # Identity certificate for client authentication when authentication method is certificate.
    identity_certificate: Optional[MacOSCertificateProfileBase] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MacOSVpnConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MacOSVpnConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MacOSVpnConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .apple_deployment_channel import AppleDeploymentChannel
        from .apple_vpn_configuration import AppleVpnConfiguration
        from .mac_o_s_certificate_profile_base import MacOSCertificateProfileBase

        from .apple_deployment_channel import AppleDeploymentChannel
        from .apple_vpn_configuration import AppleVpnConfiguration
        from .mac_o_s_certificate_profile_base import MacOSCertificateProfileBase

        fields: dict[str, Callable[[Any], None]] = {
            "deploymentChannel": lambda n : setattr(self, 'deployment_channel', n.get_enum_value(AppleDeploymentChannel)),
            "identityCertificate": lambda n : setattr(self, 'identity_certificate', n.get_object_value(MacOSCertificateProfileBase)),
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
        writer.write_enum_value("deploymentChannel", self.deployment_channel)
        writer.write_object_value("identityCertificate", self.identity_certificate)
    

