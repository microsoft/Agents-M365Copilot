from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TicketInfo(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # ID for the request approver.
    ticket_approver_identity_id: Optional[str] = None
    # The ticket number.
    ticket_number: Optional[str] = None
    # ID for the request submitter.
    ticket_submitter_identity_id: Optional[str] = None
    # The description of the ticket system.
    ticket_system: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TicketInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TicketInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TicketInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "ticketApproverIdentityId": lambda n : setattr(self, 'ticket_approver_identity_id', n.get_str_value()),
            "ticketNumber": lambda n : setattr(self, 'ticket_number', n.get_str_value()),
            "ticketSubmitterIdentityId": lambda n : setattr(self, 'ticket_submitter_identity_id', n.get_str_value()),
            "ticketSystem": lambda n : setattr(self, 'ticket_system', n.get_str_value()),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("ticketApproverIdentityId", self.ticket_approver_identity_id)
        writer.write_str_value("ticketNumber", self.ticket_number)
        writer.write_str_value("ticketSubmitterIdentityId", self.ticket_submitter_identity_id)
        writer.write_str_value("ticketSystem", self.ticket_system)
        writer.write_additional_data_value(self.additional_data)
    

