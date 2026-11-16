from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .media_stream import MediaStream
    from .online_meeting_restricted import OnlineMeetingRestricted
    from .participant_info import ParticipantInfo
    from .recording_info import RecordingInfo
    from .removed_state import RemovedState
    from .synthetic_media_detection_info import SyntheticMediaDetectionInfo

from .entity import Entity

@dataclass
class Participant(Entity, Parsable):
    # The info property
    info: Optional[ParticipantInfo] = None
    # The isIdentityAnonymized property
    is_identity_anonymized: Optional[bool] = None
    # true if the participant is in lobby.
    is_in_lobby: Optional[bool] = None
    # true if the participant is muted (client or server muted).
    is_muted: Optional[bool] = None
    # The list of media streams.
    media_streams: Optional[list[MediaStream]] = None
    # A blob of data provided by the participant in the roster.
    metadata: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The participant's preferred display name that overrides the original display name.
    preferred_display_name: Optional[str] = None
    # Information on whether the participant has recording capability.
    recording_info: Optional[RecordingInfo] = None
    # Indicates the reason why the participant was removed from the roster.
    removed_state: Optional[RemovedState] = None
    # Indicates the reason or reasons why media content from this participant is restricted.
    restricted_experience: Optional[OnlineMeetingRestricted] = None
    # Indicates the roster sequence number the participant was last updated in.
    roster_sequence_number: Optional[int] = None
    # The latest synthetic media detection result reported for this participant by an in-call detection bot. Nullable. Set to null when no detection is reported. Populated asynchronously after a successful call to reportSyntheticMedia.
    synthetic_media_detection: Optional[SyntheticMediaDetectionInfo] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Participant:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Participant
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Participant()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .media_stream import MediaStream
        from .online_meeting_restricted import OnlineMeetingRestricted
        from .participant_info import ParticipantInfo
        from .recording_info import RecordingInfo
        from .removed_state import RemovedState
        from .synthetic_media_detection_info import SyntheticMediaDetectionInfo

        from .entity import Entity
        from .media_stream import MediaStream
        from .online_meeting_restricted import OnlineMeetingRestricted
        from .participant_info import ParticipantInfo
        from .recording_info import RecordingInfo
        from .removed_state import RemovedState
        from .synthetic_media_detection_info import SyntheticMediaDetectionInfo

        fields: dict[str, Callable[[Any], None]] = {
            "info": lambda n : setattr(self, 'info', n.get_object_value(ParticipantInfo)),
            "isIdentityAnonymized": lambda n : setattr(self, 'is_identity_anonymized', n.get_bool_value()),
            "isInLobby": lambda n : setattr(self, 'is_in_lobby', n.get_bool_value()),
            "isMuted": lambda n : setattr(self, 'is_muted', n.get_bool_value()),
            "mediaStreams": lambda n : setattr(self, 'media_streams', n.get_collection_of_object_values(MediaStream)),
            "metadata": lambda n : setattr(self, 'metadata', n.get_str_value()),
            "preferredDisplayName": lambda n : setattr(self, 'preferred_display_name', n.get_str_value()),
            "recordingInfo": lambda n : setattr(self, 'recording_info', n.get_object_value(RecordingInfo)),
            "removedState": lambda n : setattr(self, 'removed_state', n.get_object_value(RemovedState)),
            "restrictedExperience": lambda n : setattr(self, 'restricted_experience', n.get_object_value(OnlineMeetingRestricted)),
            "rosterSequenceNumber": lambda n : setattr(self, 'roster_sequence_number', n.get_int_value()),
            "syntheticMediaDetection": lambda n : setattr(self, 'synthetic_media_detection', n.get_object_value(SyntheticMediaDetectionInfo)),
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
        writer.write_object_value("info", self.info)
        writer.write_bool_value("isIdentityAnonymized", self.is_identity_anonymized)
        writer.write_bool_value("isInLobby", self.is_in_lobby)
        writer.write_bool_value("isMuted", self.is_muted)
        writer.write_collection_of_object_values("mediaStreams", self.media_streams)
        writer.write_str_value("metadata", self.metadata)
        writer.write_str_value("preferredDisplayName", self.preferred_display_name)
        writer.write_object_value("recordingInfo", self.recording_info)
        writer.write_object_value("removedState", self.removed_state)
        writer.write_object_value("restrictedExperience", self.restricted_experience)
        writer.write_int_value("rosterSequenceNumber", self.roster_sequence_number)
        writer.write_object_value("syntheticMediaDetection", self.synthetic_media_detection)
    

