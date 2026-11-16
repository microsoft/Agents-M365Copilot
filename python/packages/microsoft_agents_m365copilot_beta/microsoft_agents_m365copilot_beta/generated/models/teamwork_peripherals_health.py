from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .teamwork_peripheral_health import TeamworkPeripheralHealth

@dataclass
class TeamworkPeripheralsHealth(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The health details about the communication speaker.
    communication_speaker_health: Optional[TeamworkPeripheralHealth] = None
    # The health details about the content camera.
    content_camera_health: Optional[TeamworkPeripheralHealth] = None
    # The health details about displays.
    display_health_collection: Optional[list[TeamworkPeripheralHealth]] = None
    # The health details about the microphone.
    microphone_health: Optional[TeamworkPeripheralHealth] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The health details about the room camera.
    room_camera_health: Optional[TeamworkPeripheralHealth] = None
    # The health details about the speaker.
    speaker_health: Optional[TeamworkPeripheralHealth] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamworkPeripheralsHealth:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkPeripheralsHealth
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TeamworkPeripheralsHealth()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .teamwork_peripheral_health import TeamworkPeripheralHealth

        from .teamwork_peripheral_health import TeamworkPeripheralHealth

        fields: dict[str, Callable[[Any], None]] = {
            "communicationSpeakerHealth": lambda n : setattr(self, 'communication_speaker_health', n.get_object_value(TeamworkPeripheralHealth)),
            "contentCameraHealth": lambda n : setattr(self, 'content_camera_health', n.get_object_value(TeamworkPeripheralHealth)),
            "displayHealthCollection": lambda n : setattr(self, 'display_health_collection', n.get_collection_of_object_values(TeamworkPeripheralHealth)),
            "microphoneHealth": lambda n : setattr(self, 'microphone_health', n.get_object_value(TeamworkPeripheralHealth)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "roomCameraHealth": lambda n : setattr(self, 'room_camera_health', n.get_object_value(TeamworkPeripheralHealth)),
            "speakerHealth": lambda n : setattr(self, 'speaker_health', n.get_object_value(TeamworkPeripheralHealth)),
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
        writer.write_object_value("communicationSpeakerHealth", self.communication_speaker_health)
        writer.write_object_value("contentCameraHealth", self.content_camera_health)
        writer.write_collection_of_object_values("displayHealthCollection", self.display_health_collection)
        writer.write_object_value("microphoneHealth", self.microphone_health)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("roomCameraHealth", self.room_camera_health)
        writer.write_object_value("speakerHealth", self.speaker_health)
        writer.write_additional_data_value(self.additional_data)
    

