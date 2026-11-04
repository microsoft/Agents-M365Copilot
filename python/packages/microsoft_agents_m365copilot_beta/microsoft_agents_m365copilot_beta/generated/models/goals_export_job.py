from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .long_running_operation import LongRunningOperation

from .long_running_operation import LongRunningOperation

@dataclass
class GoalsExportJob(LongRunningOperation, Parsable):
    """
    The status of a long-running operation.
    """
    # The content of the goalsExportJob.
    content: Optional[bytes] = None
    # The date and time of expiry of the result of the operation.
    expiration_date_time: Optional[datetime.datetime] = None
    # The unique identifier of the explorer view to be exported.
    explorer_view_id: Optional[str] = None
    # The unique identifier of the viva goals organization.
    goals_organization_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GoalsExportJob:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GoalsExportJob
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GoalsExportJob()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .long_running_operation import LongRunningOperation

        from .long_running_operation import LongRunningOperation

        fields: dict[str, Callable[[Any], None]] = {
            "content": lambda n : setattr(self, 'content', n.get_bytes_value()),
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "explorerViewId": lambda n : setattr(self, 'explorer_view_id', n.get_str_value()),
            "goalsOrganizationId": lambda n : setattr(self, 'goals_organization_id', n.get_str_value()),
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
        writer.write_bytes_value("content", self.content)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_str_value("explorerViewId", self.explorer_view_id)
        writer.write_str_value("goalsOrganizationId", self.goals_organization_id)
    

