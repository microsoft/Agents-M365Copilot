from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .applicable_device import ApplicableDevice
    from .catalog_entry import CatalogEntry

from ..entity import Entity

@dataclass
class ApplicableCatalog(Entity, Parsable):
    # The associated Windows update catalog entry.
    catalog_entry: Optional[CatalogEntry] = None
    # The number of devices for which the catalog entry is applicable. Read-only.
    device_count: Optional[int] = None
    # The devices for which the catalog entry is applicable.
    devices: Optional[list[ApplicableDevice]] = None
    # Indicates whether the catalog entry is recommended for at least one applicable device. Read-only.
    has_recommended_device: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ApplicableCatalog:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ApplicableCatalog
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ApplicableCatalog()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .applicable_device import ApplicableDevice
        from .catalog_entry import CatalogEntry

        from ..entity import Entity
        from .applicable_device import ApplicableDevice
        from .catalog_entry import CatalogEntry

        fields: dict[str, Callable[[Any], None]] = {
            "catalogEntry": lambda n : setattr(self, 'catalog_entry', n.get_object_value(CatalogEntry)),
            "deviceCount": lambda n : setattr(self, 'device_count', n.get_int_value()),
            "devices": lambda n : setattr(self, 'devices', n.get_collection_of_object_values(ApplicableDevice)),
            "hasRecommendedDevice": lambda n : setattr(self, 'has_recommended_device', n.get_bool_value()),
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
        writer.write_object_value("catalogEntry", self.catalog_entry)
        writer.write_collection_of_object_values("devices", self.devices)
    

