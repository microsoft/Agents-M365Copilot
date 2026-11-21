from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .conditional_access_exclusions import ConditionalAccessExclusions
    from .entity import Entity

from .entity import Entity

@dataclass
class ConditionalAccessSettings(Entity, Parsable):
    # The tenant-wide exclusions configuration.
    exclusions: Optional[ConditionalAccessExclusions] = None
    # The date and time the settings were last modified, in ISO 8601 format and UTC. Nullable. Read-only.
    modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ConditionalAccessSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ConditionalAccessSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .conditional_access_exclusions import ConditionalAccessExclusions
        from .entity import Entity

        from .conditional_access_exclusions import ConditionalAccessExclusions
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "exclusions": lambda n : setattr(self, 'exclusions', n.get_object_value(ConditionalAccessExclusions)),
            "modifiedDateTime": lambda n : setattr(self, 'modified_date_time', n.get_datetime_value()),
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
        writer.write_object_value("exclusions", self.exclusions)
        writer.write_datetime_value("modifiedDateTime", self.modified_date_time)
    

