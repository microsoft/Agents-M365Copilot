from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .microsoft_apps_file_storage_container_geo_usage import MicrosoftAppsFileStorageContainerGeoUsage

from .entity import Entity

@dataclass
class MicrosoftAppsFileStorageContainerUsage(Entity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    # The total number of active file storage containers across the tenant.
    total_active_container_count: Optional[int] = None
    # The total storage used in bytes across all active file storage containers in the tenant.
    total_active_storage_used_in_bytes: Optional[int] = None
    # Storage usage data broken down by geographic location. Expandable using $expand=usageByDataLocation.
    usage_by_data_location: Optional[list[MicrosoftAppsFileStorageContainerGeoUsage]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MicrosoftAppsFileStorageContainerUsage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MicrosoftAppsFileStorageContainerUsage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MicrosoftAppsFileStorageContainerUsage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .microsoft_apps_file_storage_container_geo_usage import MicrosoftAppsFileStorageContainerGeoUsage

        from .entity import Entity
        from .microsoft_apps_file_storage_container_geo_usage import MicrosoftAppsFileStorageContainerGeoUsage

        fields: dict[str, Callable[[Any], None]] = {
            "totalActiveContainerCount": lambda n : setattr(self, 'total_active_container_count', n.get_int_value()),
            "totalActiveStorageUsedInBytes": lambda n : setattr(self, 'total_active_storage_used_in_bytes', n.get_int_value()),
            "usageByDataLocation": lambda n : setattr(self, 'usage_by_data_location', n.get_collection_of_object_values(MicrosoftAppsFileStorageContainerGeoUsage)),
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
        writer.write_collection_of_object_values("usageByDataLocation", self.usage_by_data_location)
    

