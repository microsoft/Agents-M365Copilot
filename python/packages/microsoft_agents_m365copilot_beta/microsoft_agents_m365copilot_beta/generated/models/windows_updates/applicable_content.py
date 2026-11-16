from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .applicable_content_device_match import ApplicableContentDeviceMatch
    from .catalog_entry import CatalogEntry

@dataclass
class ApplicableContent(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Catalog entry for the update or content.
    catalog_entry: Optional[CatalogEntry] = None
    # ID of the catalog entry for the applicable content.
    catalog_entry_id: Optional[str] = None
    # Collection of devices and recommendations for applicable catalog content.
    matched_devices: Optional[list[ApplicableContentDeviceMatch]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ApplicableContent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ApplicableContent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ApplicableContent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .applicable_content_device_match import ApplicableContentDeviceMatch
        from .catalog_entry import CatalogEntry

        from .applicable_content_device_match import ApplicableContentDeviceMatch
        from .catalog_entry import CatalogEntry

        fields: dict[str, Callable[[Any], None]] = {
            "catalogEntry": lambda n : setattr(self, 'catalog_entry', n.get_object_value(CatalogEntry)),
            "catalogEntryId": lambda n : setattr(self, 'catalog_entry_id', n.get_str_value()),
            "matchedDevices": lambda n : setattr(self, 'matched_devices', n.get_collection_of_object_values(ApplicableContentDeviceMatch)),
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
        writer.write_object_value("catalogEntry", self.catalog_entry)
        writer.write_str_value("catalogEntryId", self.catalog_entry_id)
        writer.write_collection_of_object_values("matchedDevices", self.matched_devices)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

