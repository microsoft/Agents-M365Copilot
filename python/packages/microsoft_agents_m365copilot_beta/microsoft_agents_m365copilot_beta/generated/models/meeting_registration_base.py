from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .external_meeting_registration import ExternalMeetingRegistration
    from .meeting_audience import MeetingAudience
    from .meeting_registrant_base import MeetingRegistrantBase
    from .meeting_registration import MeetingRegistration

from .entity import Entity

@dataclass
class MeetingRegistrationBase(Entity, Parsable):
    # Specifies who can register for the meeting.
    allowed_registrant: Optional[MeetingAudience] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Registrants of the online meeting.
    registrants: Optional[list[MeetingRegistrantBase]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MeetingRegistrationBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MeetingRegistrationBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externalMeetingRegistration".casefold():
            from .external_meeting_registration import ExternalMeetingRegistration

            return ExternalMeetingRegistration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.meetingRegistration".casefold():
            from .meeting_registration import MeetingRegistration

            return MeetingRegistration()
        return MeetingRegistrationBase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .external_meeting_registration import ExternalMeetingRegistration
        from .meeting_audience import MeetingAudience
        from .meeting_registrant_base import MeetingRegistrantBase
        from .meeting_registration import MeetingRegistration

        from .entity import Entity
        from .external_meeting_registration import ExternalMeetingRegistration
        from .meeting_audience import MeetingAudience
        from .meeting_registrant_base import MeetingRegistrantBase
        from .meeting_registration import MeetingRegistration

        fields: dict[str, Callable[[Any], None]] = {
            "allowedRegistrant": lambda n : setattr(self, 'allowed_registrant', n.get_enum_value(MeetingAudience)),
            "registrants": lambda n : setattr(self, 'registrants', n.get_collection_of_object_values(MeetingRegistrantBase)),
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
        writer.write_enum_value("allowedRegistrant", self.allowed_registrant)
        writer.write_collection_of_object_values("registrants", self.registrants)
    

