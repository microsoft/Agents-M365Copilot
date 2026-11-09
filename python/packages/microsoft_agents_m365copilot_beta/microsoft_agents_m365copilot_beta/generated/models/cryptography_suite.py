from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_transform_constant import AuthenticationTransformConstant
    from .diffie_hellman_group import DiffieHellmanGroup
    from .perfect_forward_secrecy_group import PerfectForwardSecrecyGroup
    from .vpn_encryption_algorithm_type import VpnEncryptionAlgorithmType
    from .vpn_integrity_algorithm_type import VpnIntegrityAlgorithmType

@dataclass
class CryptographySuite(AdditionalDataHolder, Parsable):
    """
    VPN Security Association Parameters
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Authentication Transform Constants. Possible values are: md596, sha196, sha256128, aes128Gcm, aes192Gcm, aes256Gcm.
    authentication_transform_constants: Optional[AuthenticationTransformConstant] = None
    # Cipher Transform Constants. Possible values are: aes256, des, tripleDes, aes128, aes128Gcm, aes256Gcm, aes192, aes192Gcm, chaCha20Poly1305.
    cipher_transform_constants: Optional[VpnEncryptionAlgorithmType] = None
    # Diffie Hellman Group. Possible values are: group1, group2, group14, ecp256, ecp384, group24.
    dh_group: Optional[DiffieHellmanGroup] = None
    # Encryption Method. Possible values are: aes256, des, tripleDes, aes128, aes128Gcm, aes256Gcm, aes192, aes192Gcm, chaCha20Poly1305.
    encryption_method: Optional[VpnEncryptionAlgorithmType] = None
    # Integrity Check Method. Possible values are: sha2256, sha196, sha1160, sha2384, sha2_512, md5.
    integrity_check_method: Optional[VpnIntegrityAlgorithmType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Perfect Forward Secrecy Group. Possible values are: pfs1, pfs2, pfs2048, ecp256, ecp384, pfsMM, pfs24.
    pfs_group: Optional[PerfectForwardSecrecyGroup] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CryptographySuite:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CryptographySuite
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CryptographySuite()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_transform_constant import AuthenticationTransformConstant
        from .diffie_hellman_group import DiffieHellmanGroup
        from .perfect_forward_secrecy_group import PerfectForwardSecrecyGroup
        from .vpn_encryption_algorithm_type import VpnEncryptionAlgorithmType
        from .vpn_integrity_algorithm_type import VpnIntegrityAlgorithmType

        from .authentication_transform_constant import AuthenticationTransformConstant
        from .diffie_hellman_group import DiffieHellmanGroup
        from .perfect_forward_secrecy_group import PerfectForwardSecrecyGroup
        from .vpn_encryption_algorithm_type import VpnEncryptionAlgorithmType
        from .vpn_integrity_algorithm_type import VpnIntegrityAlgorithmType

        fields: dict[str, Callable[[Any], None]] = {
            "authenticationTransformConstants": lambda n : setattr(self, 'authentication_transform_constants', n.get_enum_value(AuthenticationTransformConstant)),
            "cipherTransformConstants": lambda n : setattr(self, 'cipher_transform_constants', n.get_enum_value(VpnEncryptionAlgorithmType)),
            "dhGroup": lambda n : setattr(self, 'dh_group', n.get_enum_value(DiffieHellmanGroup)),
            "encryptionMethod": lambda n : setattr(self, 'encryption_method', n.get_enum_value(VpnEncryptionAlgorithmType)),
            "integrityCheckMethod": lambda n : setattr(self, 'integrity_check_method', n.get_enum_value(VpnIntegrityAlgorithmType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "pfsGroup": lambda n : setattr(self, 'pfs_group', n.get_enum_value(PerfectForwardSecrecyGroup)),
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
        writer.write_enum_value("authenticationTransformConstants", self.authentication_transform_constants)
        writer.write_enum_value("cipherTransformConstants", self.cipher_transform_constants)
        writer.write_enum_value("dhGroup", self.dh_group)
        writer.write_enum_value("encryptionMethod", self.encryption_method)
        writer.write_enum_value("integrityCheckMethod", self.integrity_check_method)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("pfsGroup", self.pfs_group)
        writer.write_additional_data_value(self.additional_data)
    

