from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .dh_group import DhGroup
    from .ike_encryption import IkeEncryption
    from .ike_integrity import IkeIntegrity
    from .ip_sec_encryption import IpSecEncryption
    from .ip_sec_integrity import IpSecIntegrity
    from .pfs_group import PfsGroup
    from .tunnel_configuration import TunnelConfiguration

from .tunnel_configuration import TunnelConfiguration

@dataclass
class TunnelConfigurationIKEv2Custom(TunnelConfiguration, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.networkaccess.tunnelConfigurationIKEv2Custom"
    # The dhGroup property
    dh_group: Optional[DhGroup] = None
    # The ikeEncryption property
    ike_encryption: Optional[IkeEncryption] = None
    # The ikeIntegrity property
    ike_integrity: Optional[IkeIntegrity] = None
    # The ipSecEncryption property
    ip_sec_encryption: Optional[IpSecEncryption] = None
    # The ipSecIntegrity property
    ip_sec_integrity: Optional[IpSecIntegrity] = None
    # The pfsGroup property
    pfs_group: Optional[PfsGroup] = None
    # a standard specifiying Security Association lifetime with recommended values from an RFC standard.
    sa_life_time_seconds: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TunnelConfigurationIKEv2Custom:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TunnelConfigurationIKEv2Custom
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TunnelConfigurationIKEv2Custom()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .dh_group import DhGroup
        from .ike_encryption import IkeEncryption
        from .ike_integrity import IkeIntegrity
        from .ip_sec_encryption import IpSecEncryption
        from .ip_sec_integrity import IpSecIntegrity
        from .pfs_group import PfsGroup
        from .tunnel_configuration import TunnelConfiguration

        from .dh_group import DhGroup
        from .ike_encryption import IkeEncryption
        from .ike_integrity import IkeIntegrity
        from .ip_sec_encryption import IpSecEncryption
        from .ip_sec_integrity import IpSecIntegrity
        from .pfs_group import PfsGroup
        from .tunnel_configuration import TunnelConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "dhGroup": lambda n : setattr(self, 'dh_group', n.get_enum_value(DhGroup)),
            "ikeEncryption": lambda n : setattr(self, 'ike_encryption', n.get_enum_value(IkeEncryption)),
            "ikeIntegrity": lambda n : setattr(self, 'ike_integrity', n.get_enum_value(IkeIntegrity)),
            "ipSecEncryption": lambda n : setattr(self, 'ip_sec_encryption', n.get_enum_value(IpSecEncryption)),
            "ipSecIntegrity": lambda n : setattr(self, 'ip_sec_integrity', n.get_enum_value(IpSecIntegrity)),
            "pfsGroup": lambda n : setattr(self, 'pfs_group', n.get_enum_value(PfsGroup)),
            "saLifeTimeSeconds": lambda n : setattr(self, 'sa_life_time_seconds', n.get_int_value()),
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
        writer.write_enum_value("dhGroup", self.dh_group)
        writer.write_enum_value("ikeEncryption", self.ike_encryption)
        writer.write_enum_value("ikeIntegrity", self.ike_integrity)
        writer.write_enum_value("ipSecEncryption", self.ip_sec_encryption)
        writer.write_enum_value("ipSecIntegrity", self.ip_sec_integrity)
        writer.write_enum_value("pfsGroup", self.pfs_group)
        writer.write_int_value("saLifeTimeSeconds", self.sa_life_time_seconds)
    

