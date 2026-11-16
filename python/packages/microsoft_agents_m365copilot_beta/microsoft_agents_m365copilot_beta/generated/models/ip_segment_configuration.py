from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ip_application_segment import IpApplicationSegment
    from .segment_configuration import SegmentConfiguration

from .segment_configuration import SegmentConfiguration

@dataclass
class IpSegmentConfiguration(SegmentConfiguration, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.ipSegmentConfiguration"
    # The applicationSegments property
    application_segments: Optional[list[IpApplicationSegment]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IpSegmentConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IpSegmentConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IpSegmentConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .ip_application_segment import IpApplicationSegment
        from .segment_configuration import SegmentConfiguration

        from .ip_application_segment import IpApplicationSegment
        from .segment_configuration import SegmentConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "applicationSegments": lambda n : setattr(self, 'application_segments', n.get_collection_of_object_values(IpApplicationSegment)),
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
        writer.write_collection_of_object_values("applicationSegments", self.application_segments)
    

