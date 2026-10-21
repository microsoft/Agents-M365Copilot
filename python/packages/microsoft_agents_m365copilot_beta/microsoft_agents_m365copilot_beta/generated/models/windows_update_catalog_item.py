from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .windows_feature_update_catalog_item import WindowsFeatureUpdateCatalogItem
    from .windows_quality_update_catalog_item import WindowsQualityUpdateCatalogItem

from .entity import Entity

@dataclass
class WindowsUpdateCatalogItem(Entity, Parsable):
    """
    Windows update catalog item entity
    """
    # The display name for the catalog item.
    display_name: Optional[str] = None
    # The last supported date for a catalog item
    end_of_support_date: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The date the catalog item was released
    release_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsUpdateCatalogItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsUpdateCatalogItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsFeatureUpdateCatalogItem".casefold():
            from .windows_feature_update_catalog_item import WindowsFeatureUpdateCatalogItem

            return WindowsFeatureUpdateCatalogItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsQualityUpdateCatalogItem".casefold():
            from .windows_quality_update_catalog_item import WindowsQualityUpdateCatalogItem

            return WindowsQualityUpdateCatalogItem()
        return WindowsUpdateCatalogItem()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .windows_feature_update_catalog_item import WindowsFeatureUpdateCatalogItem
        from .windows_quality_update_catalog_item import WindowsQualityUpdateCatalogItem

        from .entity import Entity
        from .windows_feature_update_catalog_item import WindowsFeatureUpdateCatalogItem
        from .windows_quality_update_catalog_item import WindowsQualityUpdateCatalogItem

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "endOfSupportDate": lambda n : setattr(self, 'end_of_support_date', n.get_datetime_value()),
            "releaseDateTime": lambda n : setattr(self, 'release_date_time', n.get_datetime_value()),
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
        writer.write_datetime_value("endOfSupportDate", self.end_of_support_date)
        writer.write_datetime_value("releaseDateTime", self.release_date_time)
    

