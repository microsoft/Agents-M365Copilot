from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .vpn_encryption_algorithm_type import VpnEncryptionAlgorithmType
    from .vpn_integrity_algorithm_type import VpnIntegrityAlgorithmType

@dataclass
class IosVpnSecurityAssociationParameters(AdditionalDataHolder, Parsable):
    """
    VPN Security Association Parameters
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Lifetime (minutes)
    lifetime_in_minutes: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Diffie-Hellman Group
    security_diffie_hellman_group: Optional[int] = None
    # Encryption algorithm. Possible values are: aes256, des, tripleDes, aes128, aes128Gcm, aes256Gcm, aes192, aes192Gcm, chaCha20Poly1305.
    security_encryption_algorithm: Optional[VpnEncryptionAlgorithmType] = None
    # Integrity algorithm. Possible values are: sha2256, sha196, sha1160, sha2384, sha2_512, md5.
    security_integrity_algorithm: Optional[VpnIntegrityAlgorithmType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IosVpnSecurityAssociationParameters:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IosVpnSecurityAssociationParameters
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IosVpnSecurityAssociationParameters()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .vpn_encryption_algorithm_type import VpnEncryptionAlgorithmType
        from .vpn_integrity_algorithm_type import VpnIntegrityAlgorithmType

        from .vpn_encryption_algorithm_type import VpnEncryptionAlgorithmType
        from .vpn_integrity_algorithm_type import VpnIntegrityAlgorithmType

        fields: dict[str, Callable[[Any], None]] = {
            "lifetimeInMinutes": lambda n : setattr(self, 'lifetime_in_minutes', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "securityDiffieHellmanGroup": lambda n : setattr(self, 'security_diffie_hellman_group', n.get_int_value()),
            "securityEncryptionAlgorithm": lambda n : setattr(self, 'security_encryption_algorithm', n.get_enum_value(VpnEncryptionAlgorithmType)),
            "securityIntegrityAlgorithm": lambda n : setattr(self, 'security_integrity_algorithm', n.get_enum_value(VpnIntegrityAlgorithmType)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_int_value("lifetimeInMinutes", self.lifetime_in_minutes)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("securityDiffieHellmanGroup", self.security_diffie_hellman_group)
        writer.write_enum_value("securityEncryptionAlgorithm", self.security_encryption_algorithm)
        writer.write_enum_value("securityIntegrityAlgorithm", self.security_integrity_algorithm)
        writer.write_additional_data_value(self.additional_data)
    

