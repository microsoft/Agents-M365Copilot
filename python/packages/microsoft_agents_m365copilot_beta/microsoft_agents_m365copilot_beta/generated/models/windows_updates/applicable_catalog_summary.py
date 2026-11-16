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
class ApplicableCatalogSummary(Entity, Parsable):
    # The number of devices included in the summary. Read-only.
    aggregated_device_count: Optional[int] = None
    # The devices included in the applicability summary.
    aggregated_devices: Optional[list[ApplicableDevice]] = None
    # The associated Windows update catalog entry.
    catalog_entry: Optional[CatalogEntry] = None
    # Indicates whether the catalog entry is recommended for at least one device in the summary. Read-only.
    has_recommended_device: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The identifiers of Windows Autopatch policies for which the catalog entry is applicable. Read-only.
    policies: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ApplicableCatalogSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ApplicableCatalogSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ApplicableCatalogSummary()
    
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
            "aggregatedDeviceCount": lambda n : setattr(self, 'aggregated_device_count', n.get_int_value()),
            "aggregatedDevices": lambda n : setattr(self, 'aggregated_devices', n.get_collection_of_object_values(ApplicableDevice)),
            "catalogEntry": lambda n : setattr(self, 'catalog_entry', n.get_object_value(CatalogEntry)),
            "hasRecommendedDevice": lambda n : setattr(self, 'has_recommended_device', n.get_bool_value()),
            "policies": lambda n : setattr(self, 'policies', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_object_values("aggregatedDevices", self.aggregated_devices)
        writer.write_object_value("catalogEntry", self.catalog_entry)
    

