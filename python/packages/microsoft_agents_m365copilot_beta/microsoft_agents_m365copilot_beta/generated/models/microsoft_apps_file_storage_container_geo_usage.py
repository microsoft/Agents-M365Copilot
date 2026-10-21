from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .microsoft_apps_file_storage_container_app_usage import MicrosoftAppsFileStorageContainerAppUsage

@dataclass
class MicrosoftAppsFileStorageContainerGeoUsage(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The number of active file storage containers in this geographic location.
    active_container_count: Optional[int] = None
    # The storage used in bytes for active file storage containers in this geographic location.
    active_storage_used_in_bytes: Optional[int] = None
    # The geographic location code (for example, NAM for North America, EUR for Europe).
    data_location_code: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Storage usage data broken down by application within this geographic location. Expandable using $expand=usageByApp.
    usage_by_app: Optional[list[MicrosoftAppsFileStorageContainerAppUsage]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MicrosoftAppsFileStorageContainerGeoUsage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MicrosoftAppsFileStorageContainerGeoUsage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MicrosoftAppsFileStorageContainerGeoUsage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .microsoft_apps_file_storage_container_app_usage import MicrosoftAppsFileStorageContainerAppUsage

        from .microsoft_apps_file_storage_container_app_usage import MicrosoftAppsFileStorageContainerAppUsage

        fields: dict[str, Callable[[Any], None]] = {
            "activeContainerCount": lambda n : setattr(self, 'active_container_count', n.get_int_value()),
            "activeStorageUsedInBytes": lambda n : setattr(self, 'active_storage_used_in_bytes', n.get_int_value()),
            "dataLocationCode": lambda n : setattr(self, 'data_location_code', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "usageByApp": lambda n : setattr(self, 'usage_by_app', n.get_collection_of_object_values(MicrosoftAppsFileStorageContainerAppUsage)),
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
        writer.write_collection_of_object_values("usageByApp", self.usage_by_app)
        writer.write_additional_data_value(self.additional_data)
    

