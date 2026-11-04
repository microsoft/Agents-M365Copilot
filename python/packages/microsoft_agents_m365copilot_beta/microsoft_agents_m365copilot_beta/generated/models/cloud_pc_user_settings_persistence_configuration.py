from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_user_settings_persistence_storage_size_category import CloudPcUserSettingsPersistenceStorageSizeCategory

@dataclass
class CloudPcUserSettingsPersistenceConfiguration(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates whether user application settings are persisted between Cloud PC sessions. The default value is false. When true, user settings persistence is enabled, and Windows 365 automatically saves any user-specific application data in a central cloud storage location. Anytime the user connects to a Cloud PC within this provisioning policy, Windows 365 reconnects the user to that persisted storage. When false, this feature isn't used. The persistent storage can only be accessed by Cloud PC; IT admins can't access it.
    user_settings_persistence_enabled: Optional[bool] = None
    # Indicates the storage size for persisting user application settings. The possible values are: fourGB, eightGB, sixteenGB, thirtyTwoGB, sixtyFourGB, unknownFutureValue. The default value is fourGB.
    user_settings_persistence_storage_size_category: Optional[CloudPcUserSettingsPersistenceStorageSizeCategory] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcUserSettingsPersistenceConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcUserSettingsPersistenceConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcUserSettingsPersistenceConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_user_settings_persistence_storage_size_category import CloudPcUserSettingsPersistenceStorageSizeCategory

        from .cloud_pc_user_settings_persistence_storage_size_category import CloudPcUserSettingsPersistenceStorageSizeCategory

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "userSettingsPersistenceEnabled": lambda n : setattr(self, 'user_settings_persistence_enabled', n.get_bool_value()),
            "userSettingsPersistenceStorageSizeCategory": lambda n : setattr(self, 'user_settings_persistence_storage_size_category', n.get_enum_value(CloudPcUserSettingsPersistenceStorageSizeCategory)),
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
        writer.write_bool_value("userSettingsPersistenceEnabled", self.user_settings_persistence_enabled)
        writer.write_enum_value("userSettingsPersistenceStorageSizeCategory", self.user_settings_persistence_storage_size_category)
        writer.write_additional_data_value(self.additional_data)
    

