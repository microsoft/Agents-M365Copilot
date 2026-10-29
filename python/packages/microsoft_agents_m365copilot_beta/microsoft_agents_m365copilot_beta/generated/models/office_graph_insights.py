from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .item_insights import ItemInsights
    from .shared_insight import SharedInsight
    from .trending import Trending
    from .used_insight import UsedInsight

from .entity import Entity

@dataclass
class OfficeGraphInsights(Entity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    # Access this property from the derived type itemInsights.
    shared: Optional[list[SharedInsight]] = None
    # Access this property from the derived type itemInsights.
    trending: Optional[list[Trending]] = None
    # Access this property from the derived type itemInsights.
    used: Optional[list[UsedInsight]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OfficeGraphInsights:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OfficeGraphInsights
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.itemInsights".casefold():
            from .item_insights import ItemInsights

            return ItemInsights()
        return OfficeGraphInsights()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .item_insights import ItemInsights
        from .shared_insight import SharedInsight
        from .trending import Trending
        from .used_insight import UsedInsight

        from .entity import Entity
        from .item_insights import ItemInsights
        from .shared_insight import SharedInsight
        from .trending import Trending
        from .used_insight import UsedInsight

        fields: dict[str, Callable[[Any], None]] = {
            "shared": lambda n : setattr(self, 'shared', n.get_collection_of_object_values(SharedInsight)),
            "trending": lambda n : setattr(self, 'trending', n.get_collection_of_object_values(Trending)),
            "used": lambda n : setattr(self, 'used', n.get_collection_of_object_values(UsedInsight)),
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
        writer.write_collection_of_object_values("shared", self.shared)
        writer.write_collection_of_object_values("trending", self.trending)
        writer.write_collection_of_object_values("used", self.used)
    

