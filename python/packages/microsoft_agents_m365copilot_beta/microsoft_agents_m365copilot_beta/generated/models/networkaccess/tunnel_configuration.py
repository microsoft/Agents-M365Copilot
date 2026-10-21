from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tunnel_configuration_i_k_ev2_custom import TunnelConfigurationIKEv2Custom
    from .tunnel_configuration_i_k_ev2_default import TunnelConfigurationIKEv2Default

@dataclass
class TunnelConfiguration(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # A key to establish secure connection between the link and VPN tunnel on the edge.
    pre_shared_key: Optional[str] = None
    # Another key for zone redundant tunnel. Required only when you select zoneRedundancy redindancyTier when creating a deviceLink.
    zone_redundancy_pre_shared_key: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TunnelConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TunnelConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.tunnelConfigurationIKEv2Custom".casefold():
            from .tunnel_configuration_i_k_ev2_custom import TunnelConfigurationIKEv2Custom

            return TunnelConfigurationIKEv2Custom()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.tunnelConfigurationIKEv2Default".casefold():
            from .tunnel_configuration_i_k_ev2_default import TunnelConfigurationIKEv2Default

            return TunnelConfigurationIKEv2Default()
        return TunnelConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tunnel_configuration_i_k_ev2_custom import TunnelConfigurationIKEv2Custom
        from .tunnel_configuration_i_k_ev2_default import TunnelConfigurationIKEv2Default

        from .tunnel_configuration_i_k_ev2_custom import TunnelConfigurationIKEv2Custom
        from .tunnel_configuration_i_k_ev2_default import TunnelConfigurationIKEv2Default

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "preSharedKey": lambda n : setattr(self, 'pre_shared_key', n.get_str_value()),
            "zoneRedundancyPreSharedKey": lambda n : setattr(self, 'zone_redundancy_pre_shared_key', n.get_str_value()),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("preSharedKey", self.pre_shared_key)
        writer.write_str_value("zoneRedundancyPreSharedKey", self.zone_redundancy_pre_shared_key)
        writer.write_additional_data_value(self.additional_data)
    

