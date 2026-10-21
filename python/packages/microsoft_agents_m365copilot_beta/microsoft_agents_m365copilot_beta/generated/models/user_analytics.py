from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .activity_statistics import ActivityStatistics
    from .entity import Entity
    from .settings import Settings

from .entity import Entity

@dataclass
class UserAnalytics(Entity, Parsable):
    # The collection of work activities that a user spent time on during and outside of working hours. Read-only. Nullable.
    activity_statistics: Optional[list[ActivityStatistics]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The current settings for a user to use the analytics API.
    settings: Optional[Settings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserAnalytics:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserAnalytics
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserAnalytics()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .activity_statistics import ActivityStatistics
        from .entity import Entity
        from .settings import Settings

        from .activity_statistics import ActivityStatistics
        from .entity import Entity
        from .settings import Settings

        fields: dict[str, Callable[[Any], None]] = {
            "activityStatistics": lambda n : setattr(self, 'activity_statistics', n.get_collection_of_object_values(ActivityStatistics)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(Settings)),
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
        writer.write_collection_of_object_values("activityStatistics", self.activity_statistics)
        writer.write_object_value("settings", self.settings)
    

