from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_storage_sizing_type import CloudPcStorageSizingType
    from .cloud_pc_user_settings_persistence_storage_size_category import CloudPcUserSettingsPersistenceStorageSizeCategory

@dataclass
class CloudPcStorageConfiguration(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The allocatedStorageSizeCategory property
    allocated_storage_size_category: Optional[CloudPcUserSettingsPersistenceStorageSizeCategory] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The storageSizingType property
    storage_sizing_type: Optional[CloudPcStorageSizingType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcStorageConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcStorageConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcStorageConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_storage_sizing_type import CloudPcStorageSizingType
        from .cloud_pc_user_settings_persistence_storage_size_category import CloudPcUserSettingsPersistenceStorageSizeCategory

        from .cloud_pc_storage_sizing_type import CloudPcStorageSizingType
        from .cloud_pc_user_settings_persistence_storage_size_category import CloudPcUserSettingsPersistenceStorageSizeCategory

        fields: dict[str, Callable[[Any], None]] = {
            "allocatedStorageSizeCategory": lambda n : setattr(self, 'allocated_storage_size_category', n.get_enum_value(CloudPcUserSettingsPersistenceStorageSizeCategory)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "storageSizingType": lambda n : setattr(self, 'storage_sizing_type', n.get_enum_value(CloudPcStorageSizingType)),
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
        writer.write_enum_value("allocatedStorageSizeCategory", self.allocated_storage_size_category)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("storageSizingType", self.storage_sizing_type)
        writer.write_additional_data_value(self.additional_data)
    

