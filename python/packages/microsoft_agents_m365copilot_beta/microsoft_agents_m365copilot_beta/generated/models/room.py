from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .booking_type import BookingType
    from .place import Place
    from .place_feature_enablement import PlaceFeatureEnablement

from .place import Place

@dataclass
class Room(Place, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.room"
    # The name of the audio device that is available in the room.
    audio_device_name: Optional[str] = None
    # Specifies how the room can be booked. The possible values are:unknown - Unspecified booking behavior. We don't recommend that you use this value.standard - Available for general booking.reserved - Reserved for specific users or purposes.
    booking_type: Optional[BookingType] = None
    # The name or identifier of the building where the room is located.
    building: Optional[str] = None
    # The maximum number of people the room can accommodate.
    capacity: Optional[int] = None
    # The name of the display device (for example, monitor or projector) that is available in the room.
    display_device_name: Optional[str] = None
    # The email address associated with the room. This email address is used for booking.
    email_address: Optional[str] = None
    # A human-readable label for the floor; for example, Ground Floor.
    floor_label: Optional[str] = None
    # The numeric floor level within the building. For example, 1 for first floor, 2 for second floor, and so on.
    floor_number: Optional[int] = None
    # Indicates whether the room is configured with the Microsoft Teams Rooms system.
    is_teams_enabled: Optional[bool] = None
    # A short, friendly name for the room, often used for easier identification or display in UI.
    nickname: Optional[str] = None
    # The teamsEnabledState property
    teams_enabled_state: Optional[PlaceFeatureEnablement] = None
    # The name of the video device that is available in the room.
    video_device_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Room:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Room
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Room()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .booking_type import BookingType
        from .place import Place
        from .place_feature_enablement import PlaceFeatureEnablement

        from .booking_type import BookingType
        from .place import Place
        from .place_feature_enablement import PlaceFeatureEnablement

        fields: dict[str, Callable[[Any], None]] = {
            "audioDeviceName": lambda n : setattr(self, 'audio_device_name', n.get_str_value()),
            "bookingType": lambda n : setattr(self, 'booking_type', n.get_enum_value(BookingType)),
            "building": lambda n : setattr(self, 'building', n.get_str_value()),
            "capacity": lambda n : setattr(self, 'capacity', n.get_int_value()),
            "displayDeviceName": lambda n : setattr(self, 'display_device_name', n.get_str_value()),
            "emailAddress": lambda n : setattr(self, 'email_address', n.get_str_value()),
            "floorLabel": lambda n : setattr(self, 'floor_label', n.get_str_value()),
            "floorNumber": lambda n : setattr(self, 'floor_number', n.get_int_value()),
            "isTeamsEnabled": lambda n : setattr(self, 'is_teams_enabled', n.get_bool_value()),
            "nickname": lambda n : setattr(self, 'nickname', n.get_str_value()),
            "teamsEnabledState": lambda n : setattr(self, 'teams_enabled_state', n.get_enum_value(PlaceFeatureEnablement)),
            "videoDeviceName": lambda n : setattr(self, 'video_device_name', n.get_str_value()),
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
        writer.write_str_value("audioDeviceName", self.audio_device_name)
        writer.write_enum_value("bookingType", self.booking_type)
        writer.write_str_value("building", self.building)
        writer.write_int_value("capacity", self.capacity)
        writer.write_str_value("displayDeviceName", self.display_device_name)
        writer.write_str_value("emailAddress", self.email_address)
        writer.write_str_value("floorLabel", self.floor_label)
        writer.write_int_value("floorNumber", self.floor_number)
        writer.write_bool_value("isTeamsEnabled", self.is_teams_enabled)
        writer.write_str_value("nickname", self.nickname)
        writer.write_enum_value("teamsEnabledState", self.teams_enabled_state)
        writer.write_str_value("videoDeviceName", self.video_device_name)
    

