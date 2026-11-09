from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_domain_join_type import CloudPcDomainJoinType
    from .cloud_pc_geographic_location_type import CloudPcGeographicLocationType
    from .cloud_pc_region_group import CloudPcRegionGroup

@dataclass
class CloudPcDomainJoinConfiguration(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Specifies the method by which the provisioned Cloud PC joins Microsoft Entra ID. If you choose the hybridAzureADJoin type, only provide a value for the onPremisesConnectionId property and leave the regionName property empty. If you choose the azureADJoin type, provide a value for either the onPremisesConnectionId or the regionName property. The possible values are: azureADJoin, hybridAzureADJoin, unknownFutureValue.
    domain_join_type: Optional[CloudPcDomainJoinType] = None
    # The geographic location where the region is located. Read-only.
    geographic_location_type: Optional[CloudPcGeographicLocationType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The Azure network connection ID that matches the virtual network IT admins want the provisioning policy to use when they create Cloud PCs. You can use this property in both domain join types: Azure AD joined or Hybrid Microsoft Entra joined. If you enter an onPremisesConnectionId, leave the regionName property empty.
    on_premises_connection_id: Optional[str] = None
    # The logical geographic group this region belongs to. Multiple regions can belong to one region group. A customer can select a regionGroup when they provision a Cloud PC, and the Cloud PC is put in one of the regions in the group based on resource status. For example, the Europe region group contains the Northern Europe and Western Europe regions. Read-only.
    region_group: Optional[CloudPcRegionGroup] = None
    # The supported Azure region where the IT admin wants the provisioning policy to create Cloud PCs. The underlying virtual network is created and managed by the Windows 365 service. This can only be entered if the IT admin chooses Microsoft Entra joined as the domain join type. If you enter a regionName, leave the onPremisesConnectionId property empty.
    region_name: Optional[str] = None
    # Specifies the method by which the provisioned Cloud PC joins Microsoft Entra ID. If you choose the hybridAzureADJoin type, only provide a value for the onPremisesConnectionId property and leave regionName as empty. If you choose the azureADJoin type, provide a value for either onPremisesConnectionId or regionName. The possible values are: azureADJoin, hybridAzureADJoin, unknownFutureValue. The type property is deprecated and will stop returning data on January 31, 2024. Going forward, use the domainJoinType property.
    type: Optional[CloudPcDomainJoinType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcDomainJoinConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcDomainJoinConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcDomainJoinConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_domain_join_type import CloudPcDomainJoinType
        from .cloud_pc_geographic_location_type import CloudPcGeographicLocationType
        from .cloud_pc_region_group import CloudPcRegionGroup

        from .cloud_pc_domain_join_type import CloudPcDomainJoinType
        from .cloud_pc_geographic_location_type import CloudPcGeographicLocationType
        from .cloud_pc_region_group import CloudPcRegionGroup

        fields: dict[str, Callable[[Any], None]] = {
            "domainJoinType": lambda n : setattr(self, 'domain_join_type', n.get_enum_value(CloudPcDomainJoinType)),
            "geographicLocationType": lambda n : setattr(self, 'geographic_location_type', n.get_enum_value(CloudPcGeographicLocationType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "onPremisesConnectionId": lambda n : setattr(self, 'on_premises_connection_id', n.get_str_value()),
            "regionGroup": lambda n : setattr(self, 'region_group', n.get_enum_value(CloudPcRegionGroup)),
            "regionName": lambda n : setattr(self, 'region_name', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(CloudPcDomainJoinType)),
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
        writer.write_enum_value("domainJoinType", self.domain_join_type)
        writer.write_enum_value("geographicLocationType", self.geographic_location_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("onPremisesConnectionId", self.on_premises_connection_id)
        writer.write_enum_value("regionGroup", self.region_group)
        writer.write_str_value("regionName", self.region_name)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

