from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .meeting_engagement_type import MeetingEngagementType

@dataclass
class MeetingEngagement(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The UTC date and time when the engagement event occurred, in ISO 8601 format.
    date_time: Optional[datetime.datetime] = None
    # The specific engagement action within the type (e.g., like, love, applause, laugh, surprised for reactions; raiseHand for hand; cameraOn for camera; unmute, mute for microphone).
    engagement_sub_type: Optional[str] = None
    # The category of the engagement event. Required, non-nullable.
    engagement_type: Optional[MeetingEngagementType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MeetingEngagement:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MeetingEngagement
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MeetingEngagement()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .meeting_engagement_type import MeetingEngagementType

        from .meeting_engagement_type import MeetingEngagementType

        fields: dict[str, Callable[[Any], None]] = {
            "dateTime": lambda n : setattr(self, 'date_time', n.get_datetime_value()),
            "engagementSubType": lambda n : setattr(self, 'engagement_sub_type', n.get_str_value()),
            "engagementType": lambda n : setattr(self, 'engagement_type', n.get_enum_value(MeetingEngagementType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_datetime_value("dateTime", self.date_time)
        writer.write_str_value("engagementSubType", self.engagement_sub_type)
        writer.write_enum_value("engagementType", self.engagement_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

