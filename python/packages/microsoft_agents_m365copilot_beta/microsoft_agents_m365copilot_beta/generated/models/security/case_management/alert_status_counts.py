from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class AlertStatusCounts(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The number of alerts that are in progress.
    in_progress: Optional[int] = None
    # The number of new alerts.
    new: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The number of resolved alerts.
    resolved: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AlertStatusCounts:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AlertStatusCounts
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AlertStatusCounts()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "inProgress": lambda n : setattr(self, 'in_progress', n.get_int_value()),
            "new": lambda n : setattr(self, 'new', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "resolved": lambda n : setattr(self, 'resolved', n.get_int_value()),
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
        writer.write_int_value("inProgress", self.in_progress)
        writer.write_int_value("new", self.new)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("resolved", self.resolved)
        writer.write_additional_data_value(self.additional_data)
    

