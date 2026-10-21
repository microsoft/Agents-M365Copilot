from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .request_schedule import RequestSchedule
    from .user_set import UserSet

@dataclass
class ApproverDelegate(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The identity that receives the approval delegation. Only singleUser and groupMembers are currently supported.
    delegate: Optional[UserSet] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The schedule for the delegation, including start date and expiration pattern (duration, end date, or no expiration).
    schedule: Optional[RequestSchedule] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ApproverDelegate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ApproverDelegate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ApproverDelegate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .request_schedule import RequestSchedule
        from .user_set import UserSet

        from .request_schedule import RequestSchedule
        from .user_set import UserSet

        fields: dict[str, Callable[[Any], None]] = {
            "delegate": lambda n : setattr(self, 'delegate', n.get_object_value(UserSet)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "schedule": lambda n : setattr(self, 'schedule', n.get_object_value(RequestSchedule)),
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
        writer.write_object_value("delegate", self.delegate)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("schedule", self.schedule)
        writer.write_additional_data_value(self.additional_data)
    

