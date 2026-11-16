from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .membership_rule_processing_status_details import MembershipRuleProcessingStatusDetails

@dataclass
class MembershipRuleProcessingStatus(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Detailed error message if dynamic group processing ran into an error.  Optional. Read-only.
    error_message: Optional[str] = None
    # Most recent date and time when membership of a dynamic group was updated.  Optional. Read-only.
    last_membership_updated: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Current status of a dynamic group processing. The possible values are: NotStarted, Running, Succeeded, Failed, and UnknownFutureValue.  Required. Read-only.
    status: Optional[MembershipRuleProcessingStatusDetails] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MembershipRuleProcessingStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MembershipRuleProcessingStatus
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MembershipRuleProcessingStatus()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .membership_rule_processing_status_details import MembershipRuleProcessingStatusDetails

        from .membership_rule_processing_status_details import MembershipRuleProcessingStatusDetails

        fields: dict[str, Callable[[Any], None]] = {
            "errorMessage": lambda n : setattr(self, 'error_message', n.get_str_value()),
            "lastMembershipUpdated": lambda n : setattr(self, 'last_membership_updated', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(MembershipRuleProcessingStatusDetails)),
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
        writer.write_str_value("errorMessage", self.error_message)
        writer.write_datetime_value("lastMembershipUpdated", self.last_membership_updated)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

