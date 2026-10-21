from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class SyntheticMediaDetectionInfo(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Unique identifier for the detection event. This property correlates with the id parameter that the detection bot passed to reportSyntheticMedia.
    detection_id: Optional[UUID] = None
    # Identifier of the detection bot that produced this result.
    detector_bot: Optional[str] = None
    # Set to true if the participant is classified as trusted or reliable (for example, a known internal user); otherwise, false.
    is_participant_trusted: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Confidence score (0.0 to 1.0) that the participant's media is synthetic.
    synthetic_confidence: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SyntheticMediaDetectionInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SyntheticMediaDetectionInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SyntheticMediaDetectionInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "detectionId": lambda n : setattr(self, 'detection_id', n.get_uuid_value()),
            "detectorBot": lambda n : setattr(self, 'detector_bot', n.get_str_value()),
            "isParticipantTrusted": lambda n : setattr(self, 'is_participant_trusted', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "syntheticConfidence": lambda n : setattr(self, 'synthetic_confidence', n.get_float_value()),
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
        writer.write_uuid_value("detectionId", self.detection_id)
        writer.write_str_value("detectorBot", self.detector_bot)
        writer.write_bool_value("isParticipantTrusted", self.is_participant_trusted)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_float_value("syntheticConfidence", self.synthetic_confidence)
        writer.write_additional_data_value(self.additional_data)
    

