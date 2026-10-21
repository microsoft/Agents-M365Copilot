from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_geographic_location_type import CloudPcGeographicLocationType
    from .cloud_pc_management_service import CloudPcManagementService
    from .cloud_pc_region_group import CloudPcRegionGroup
    from .cloud_pc_supported_region_restriction_detail import CloudPcSupportedRegionRestrictionDetail
    from .cloud_pc_supported_region_status import CloudPcSupportedRegionStatus
    from .entity import Entity

from .entity import Entity

@dataclass
class CloudPcSupportedRegion(Entity, Parsable):
    # The name for the supported region. Read-only.
    display_name: Optional[str] = None
    # The geographic location where the region is located. Read-only.
    geographic_location_type: Optional[CloudPcGeographicLocationType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The regionGroup property
    region_group: Optional[CloudPcRegionGroup] = None
    # When the region isn't available, all region restrictions are set to true. These restrictions apply to four properties: cPURestricted, gPURestricted, nestedVirtualizationRestricted and availabilityZoneRestricted. cPURestricted indicates whether the region is available for CPU, gPURestricted indicates whether the region is available for GPU, nestedVirtualizationRestricted indicates whether the region is available for nested virtualization, and availabilityZoneRestricted indicates whether the region is available for availability zone support. Read-only.
    region_restriction_detail: Optional[CloudPcSupportedRegionRestrictionDetail] = None
    # The status of the supported region. The possible values are: available, restricted, unavailable, unknownFutureValue. Read-only.
    region_status: Optional[CloudPcSupportedRegionStatus] = None
    # The supportedSolution property
    supported_solution: Optional[CloudPcManagementService] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcSupportedRegion:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcSupportedRegion
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcSupportedRegion()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_geographic_location_type import CloudPcGeographicLocationType
        from .cloud_pc_management_service import CloudPcManagementService
        from .cloud_pc_region_group import CloudPcRegionGroup
        from .cloud_pc_supported_region_restriction_detail import CloudPcSupportedRegionRestrictionDetail
        from .cloud_pc_supported_region_status import CloudPcSupportedRegionStatus
        from .entity import Entity

        from .cloud_pc_geographic_location_type import CloudPcGeographicLocationType
        from .cloud_pc_management_service import CloudPcManagementService
        from .cloud_pc_region_group import CloudPcRegionGroup
        from .cloud_pc_supported_region_restriction_detail import CloudPcSupportedRegionRestrictionDetail
        from .cloud_pc_supported_region_status import CloudPcSupportedRegionStatus
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "geographicLocationType": lambda n : setattr(self, 'geographic_location_type', n.get_enum_value(CloudPcGeographicLocationType)),
            "regionGroup": lambda n : setattr(self, 'region_group', n.get_enum_value(CloudPcRegionGroup)),
            "regionRestrictionDetail": lambda n : setattr(self, 'region_restriction_detail', n.get_object_value(CloudPcSupportedRegionRestrictionDetail)),
            "regionStatus": lambda n : setattr(self, 'region_status', n.get_enum_value(CloudPcSupportedRegionStatus)),
            "supportedSolution": lambda n : setattr(self, 'supported_solution', n.get_collection_of_enum_values(CloudPcManagementService)),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("geographicLocationType", self.geographic_location_type)
        writer.write_enum_value("regionGroup", self.region_group)
        writer.write_object_value("regionRestrictionDetail", self.region_restriction_detail)
        writer.write_enum_value("regionStatus", self.region_status)
        writer.write_enum_value("supportedSolution", self.supported_solution)
    

