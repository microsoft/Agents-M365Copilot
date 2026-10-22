from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .information_barrier_mode import InformationBarrierMode

@dataclass
class InformationBarrier(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The mode property
    mode: Optional[InformationBarrierMode] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The list of segment IDs associated with the container.
    segment_ids: Optional[list[UUID]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> InformationBarrier:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InformationBarrier
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return InformationBarrier()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .information_barrier_mode import InformationBarrierMode

        from .information_barrier_mode import InformationBarrierMode

        fields: dict[str, Callable[[Any], None]] = {
            "mode": lambda n : setattr(self, 'mode', n.get_enum_value(InformationBarrierMode)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "segmentIds": lambda n : setattr(self, 'segment_ids', n.get_collection_of_primitive_values(UUID)),
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
        writer.write_enum_value("mode", self.mode)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_primitive_values("segmentIds", self.segment_ids)
        writer.write_additional_data_value(self.additional_data)
    

