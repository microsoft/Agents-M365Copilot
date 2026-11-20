from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .microsoft_tunnel_log_collection_status import MicrosoftTunnelLogCollectionStatus

from .entity import Entity

@dataclass
class MicrosoftTunnelServerLogCollectionResponse(Entity, Parsable):
    """
    Entity that stores the server log collection status.
    """
    # The end time of the logs collected
    end_date_time: Optional[datetime.datetime] = None
    # The time when the log collection is expired
    expiry_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The time when the log collection was requested
    request_date_time: Optional[datetime.datetime] = None
    # ID of the server the log collection is requested upon
    server_id: Optional[str] = None
    # The size of the logs in bytes
    size_in_bytes: Optional[int] = None
    # The start time of the logs collected
    start_date_time: Optional[datetime.datetime] = None
    # Enum type that represent the status of log collection
    status: Optional[MicrosoftTunnelLogCollectionStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MicrosoftTunnelServerLogCollectionResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MicrosoftTunnelServerLogCollectionResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MicrosoftTunnelServerLogCollectionResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .microsoft_tunnel_log_collection_status import MicrosoftTunnelLogCollectionStatus

        from .entity import Entity
        from .microsoft_tunnel_log_collection_status import MicrosoftTunnelLogCollectionStatus

        fields: dict[str, Callable[[Any], None]] = {
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "expiryDateTime": lambda n : setattr(self, 'expiry_date_time', n.get_datetime_value()),
            "requestDateTime": lambda n : setattr(self, 'request_date_time', n.get_datetime_value()),
            "serverId": lambda n : setattr(self, 'server_id', n.get_str_value()),
            "sizeInBytes": lambda n : setattr(self, 'size_in_bytes', n.get_int_value()),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(MicrosoftTunnelLogCollectionStatus)),
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
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_datetime_value("expiryDateTime", self.expiry_date_time)
        writer.write_datetime_value("requestDateTime", self.request_date_time)
        writer.write_str_value("serverId", self.server_id)
        writer.write_int_value("sizeInBytes", self.size_in_bytes)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_enum_value("status", self.status)
    

