from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class RecommendationConfiguration(Entity, Parsable):
    # Indicates whether notifications for recommendations are enabled.
    is_notification_enabled: Optional[bool] = None
    # The date and time of the most recent refresh cycle in which every pipeline that populates Microsoft Entra recommendations completed successfully for the tenant's region. The value advances only when all contributing pipelines succeed and remains at the last fully successful cycle if any contributing pipeline is unhealthy. A successful refresh doesn't imply that any individual recommendation changed. Is null when no fully successful refresh has been recorded yet. Read-only.
    last_refreshed_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RecommendationConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RecommendationConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RecommendationConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "isNotificationEnabled": lambda n : setattr(self, 'is_notification_enabled', n.get_bool_value()),
            "lastRefreshedDateTime": lambda n : setattr(self, 'last_refreshed_date_time', n.get_datetime_value()),
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
        writer.write_bool_value("isNotificationEnabled", self.is_notification_enabled)
    

