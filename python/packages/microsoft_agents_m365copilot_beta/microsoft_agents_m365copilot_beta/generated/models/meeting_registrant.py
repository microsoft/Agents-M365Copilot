from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .custom_question_answer import CustomQuestionAnswer
    from .meeting_registrant_base import MeetingRegistrantBase
    from .meeting_registrant_status import MeetingRegistrantStatus

from .meeting_registrant_base import MeetingRegistrantBase

@dataclass
class MeetingRegistrant(MeetingRegistrantBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.meetingRegistrant"
    # The registrant's answer to custom questions.
    custom_question_answers: Optional[list[CustomQuestionAnswer]] = None
    # The email address of the registrant.
    email: Optional[str] = None
    # The first name of the registrant.
    first_name: Optional[str] = None
    # The family name of the registrant.
    last_name: Optional[str] = None
    # Time in UTC when the registrant registers for the meeting. Read-only.
    registration_date_time: Optional[datetime.datetime] = None
    # The registration status of the registrant. Read-only.
    status: Optional[MeetingRegistrantStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MeetingRegistrant:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MeetingRegistrant
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MeetingRegistrant()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .custom_question_answer import CustomQuestionAnswer
        from .meeting_registrant_base import MeetingRegistrantBase
        from .meeting_registrant_status import MeetingRegistrantStatus

        from .custom_question_answer import CustomQuestionAnswer
        from .meeting_registrant_base import MeetingRegistrantBase
        from .meeting_registrant_status import MeetingRegistrantStatus

        fields: dict[str, Callable[[Any], None]] = {
            "customQuestionAnswers": lambda n : setattr(self, 'custom_question_answers', n.get_collection_of_object_values(CustomQuestionAnswer)),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "firstName": lambda n : setattr(self, 'first_name', n.get_str_value()),
            "lastName": lambda n : setattr(self, 'last_name', n.get_str_value()),
            "registrationDateTime": lambda n : setattr(self, 'registration_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(MeetingRegistrantStatus)),
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
        writer.write_collection_of_object_values("customQuestionAnswers", self.custom_question_answers)
        writer.write_str_value("email", self.email)
        writer.write_str_value("firstName", self.first_name)
        writer.write_str_value("lastName", self.last_name)
        writer.write_datetime_value("registrationDateTime", self.registration_date_time)
        writer.write_enum_value("status", self.status)
    

