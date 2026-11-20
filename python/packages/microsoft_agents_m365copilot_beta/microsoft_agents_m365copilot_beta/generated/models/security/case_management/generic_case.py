from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .case import Case

from .case import Case

@dataclass
class GenericCase(Case, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.caseManagement.genericCase"
    # The user assigned to the generic case. Supports $filter and $orderby.
    assigned_to: Optional[str] = None
    # Notes recorded when the generic case is closed. Supports $filter.
    closing_notes: Optional[str] = None
    # The description of the generic case. Supports $filter.
    description: Optional[str] = None
    # The target completion date and time for the generic case. Supports $filter.
    due_date_time: Optional[datetime.datetime] = None
    # The priority assigned to the generic case. Possible values are: veryLow, low, medium, high, and critical. Supports $filter.
    priority: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GenericCase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GenericCase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GenericCase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .case import Case

        from .case import Case

        fields: dict[str, Callable[[Any], None]] = {
            "assignedTo": lambda n : setattr(self, 'assigned_to', n.get_str_value()),
            "closingNotes": lambda n : setattr(self, 'closing_notes', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "dueDateTime": lambda n : setattr(self, 'due_date_time', n.get_datetime_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_str_value()),
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
        writer.write_str_value("assignedTo", self.assigned_to)
        writer.write_str_value("closingNotes", self.closing_notes)
        writer.write_str_value("description", self.description)
        writer.write_datetime_value("dueDateTime", self.due_date_time)
        writer.write_str_value("priority", self.priority)
    

