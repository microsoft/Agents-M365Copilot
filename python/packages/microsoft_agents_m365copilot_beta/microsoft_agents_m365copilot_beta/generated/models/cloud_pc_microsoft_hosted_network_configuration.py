from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_geographic_location_type import CloudPcGeographicLocationType
    from .cloud_pc_network_configuration import CloudPcNetworkConfiguration
    from .cloud_pc_region_group_configuration import CloudPcRegionGroupConfiguration

from .cloud_pc_network_configuration import CloudPcNetworkConfiguration

@dataclass
class CloudPcMicrosoftHostedNetworkConfiguration(CloudPcNetworkConfiguration, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.cloudPcMicrosoftHostedNetworkConfiguration"
    # The geographicLocationType property
    geographic_location_type: Optional[CloudPcGeographicLocationType] = None
    # The region group configurations for the network.
    region_groups: Optional[list[CloudPcRegionGroupConfiguration]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcMicrosoftHostedNetworkConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcMicrosoftHostedNetworkConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcMicrosoftHostedNetworkConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_geographic_location_type import CloudPcGeographicLocationType
        from .cloud_pc_network_configuration import CloudPcNetworkConfiguration
        from .cloud_pc_region_group_configuration import CloudPcRegionGroupConfiguration

        from .cloud_pc_geographic_location_type import CloudPcGeographicLocationType
        from .cloud_pc_network_configuration import CloudPcNetworkConfiguration
        from .cloud_pc_region_group_configuration import CloudPcRegionGroupConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "geographicLocationType": lambda n : setattr(self, 'geographic_location_type', n.get_enum_value(CloudPcGeographicLocationType)),
            "regionGroups": lambda n : setattr(self, 'region_groups', n.get_collection_of_object_values(CloudPcRegionGroupConfiguration)),
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
        writer.write_enum_value("geographicLocationType", self.geographic_location_type)
        writer.write_collection_of_object_values("regionGroups", self.region_groups)
    

