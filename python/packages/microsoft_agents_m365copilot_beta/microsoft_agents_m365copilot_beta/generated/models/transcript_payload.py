from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .transcript_speaker import TranscriptSpeaker

@dataclass
class TranscriptPayload(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The audioCaptureDateTime property
    audio_capture_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The speaker property
    speaker: Optional[TranscriptSpeaker] = None
    # The spokenLanguage property
    spoken_language: Optional[str] = None
    # The text property
    text: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TranscriptPayload:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TranscriptPayload
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TranscriptPayload()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .transcript_speaker import TranscriptSpeaker

        from .transcript_speaker import TranscriptSpeaker

        fields: dict[str, Callable[[Any], None]] = {
            "audioCaptureDateTime": lambda n : setattr(self, 'audio_capture_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "speaker": lambda n : setattr(self, 'speaker', n.get_object_value(TranscriptSpeaker)),
            "spokenLanguage": lambda n : setattr(self, 'spoken_language', n.get_str_value()),
            "text": lambda n : setattr(self, 'text', n.get_str_value()),
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
        writer.write_datetime_value("audioCaptureDateTime", self.audio_capture_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("speaker", self.speaker)
        writer.write_str_value("spokenLanguage", self.spoken_language)
        writer.write_str_value("text", self.text)
        writer.write_additional_data_value(self.additional_data)
    

