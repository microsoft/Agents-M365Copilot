from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class IncidentSeverityCounts(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The number of alerts with high severity.
    high: Optional[int] = None
    # The number of alerts with informational severity.
    informational: Optional[int] = None
    # The number of alerts with low severity.
    low: Optional[int] = None
    # The number of alerts with medium severity.
    medium: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The number of alerts with unknown severity.
    unknown: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IncidentSeverityCounts:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IncidentSeverityCounts
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IncidentSeverityCounts()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "high": lambda n : setattr(self, 'high', n.get_int_value()),
            "informational": lambda n : setattr(self, 'informational', n.get_int_value()),
            "low": lambda n : setattr(self, 'low', n.get_int_value()),
            "medium": lambda n : setattr(self, 'medium', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "unknown": lambda n : setattr(self, 'unknown', n.get_int_value()),
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
        writer.write_int_value("high", self.high)
        writer.write_int_value("informational", self.informational)
        writer.write_int_value("low", self.low)
        writer.write_int_value("medium", self.medium)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("unknown", self.unknown)
        writer.write_additional_data_value(self.additional_data)
    

