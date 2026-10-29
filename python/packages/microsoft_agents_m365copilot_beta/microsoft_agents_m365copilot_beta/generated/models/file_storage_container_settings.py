from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class FileStorageContainerSettings(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Indicates whether versioning is enabled for items in the container. Optional. Read-write.
    is_item_versioning_enabled: Optional[bool] = None
    # Indicates whether Optical Character Recognition (OCR) is enabled for the container. The default value is false. When set to true, OCR extraction is performed for new and updated documents of supported document types, and the extracted fields in the metadata of the document enable end-user search and search-driven solutions. When set to false, existing OCR metadata is not impacted. Optional. Read-write.
    is_ocr_enabled: Optional[bool] = None
    # The ID of the default sensitivity label for items in the container. Optional. Read-write.
    item_default_sensitivity_label_id: Optional[str] = None
    # The maximum major versions allowed for items in the container. Optional. Read-write.
    item_major_version_limit: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FileStorageContainerSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FileStorageContainerSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FileStorageContainerSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "isItemVersioningEnabled": lambda n : setattr(self, 'is_item_versioning_enabled', n.get_bool_value()),
            "isOcrEnabled": lambda n : setattr(self, 'is_ocr_enabled', n.get_bool_value()),
            "itemDefaultSensitivityLabelId": lambda n : setattr(self, 'item_default_sensitivity_label_id', n.get_str_value()),
            "itemMajorVersionLimit": lambda n : setattr(self, 'item_major_version_limit', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_bool_value("isItemVersioningEnabled", self.is_item_versioning_enabled)
        writer.write_bool_value("isOcrEnabled", self.is_ocr_enabled)
        writer.write_str_value("itemDefaultSensitivityLabelId", self.item_default_sensitivity_label_id)
        writer.write_int_value("itemMajorVersionLimit", self.item_major_version_limit)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

