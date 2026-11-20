from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .identity_set import IdentitySet
    from .participant_info import ParticipantInfo
    from .recording_status import RecordingStatus

@dataclass
class RecordingInfo(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The participant who initiated the recording.
    initiated_by: Optional[ParticipantInfo] = None
    # The identities of recording initiator.
    initiator: Optional[IdentitySet] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The recordingStatus property
    recording_status: Optional[RecordingStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RecordingInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RecordingInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RecordingInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .identity_set import IdentitySet
        from .participant_info import ParticipantInfo
        from .recording_status import RecordingStatus

        from .identity_set import IdentitySet
        from .participant_info import ParticipantInfo
        from .recording_status import RecordingStatus

        fields: dict[str, Callable[[Any], None]] = {
            "initiatedBy": lambda n : setattr(self, 'initiated_by', n.get_object_value(ParticipantInfo)),
            "initiator": lambda n : setattr(self, 'initiator', n.get_object_value(IdentitySet)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recordingStatus": lambda n : setattr(self, 'recording_status', n.get_enum_value(RecordingStatus)),
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
        writer.write_object_value("initiatedBy", self.initiated_by)
        writer.write_object_value("initiator", self.initiator)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("recordingStatus", self.recording_status)
        writer.write_additional_data_value(self.additional_data)
    

