from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .application_activity import ApplicationActivity

@dataclass
class GenerativeAIInsight(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The activity property
    activity: Optional[ApplicationActivity] = None
    # The prompt text or content captured for this insight. Supports $filter (eq) and $orderby.
    content: Optional[str] = None
    # The date and time when the insight was created. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2024, is 2024-01-01T00:00:00Z. Supports $filter (eq) and $orderby.
    created_date_time: Optional[datetime.datetime] = None
    # The destination URL associated with this insight. Supports $filter (eq) and $orderby.
    destination_url: Optional[str] = None
    # The unique identifier for the event. Supports $filter (eq) and $orderby.
    event_id: Optional[str] = None
    # The event type that classifies the insight event. Supports $filter (eq) and $orderby.
    event_type: Optional[str] = None
    # The MCP client name when the activity is related to MCP interactions. Supports $filter (eq) and $orderby.
    mcp_client_name: Optional[str] = None
    # The MCP server name when the activity is related to MCP interactions. Supports $filter (eq) and $orderby.
    mcp_server_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The session identifier used to correlate related events. Supports $filter (eq) and $orderby.
    session_id: Optional[str] = None
    # A finer-grained classification of activity, such as chat-interaction, tools/call, or data-analysis. Supports $filter (eq) and $orderby.
    subactivity: Optional[str] = None
    # A unique identifier assigned to a specific transaction or operation. Key. Supports $filter (eq) and $orderby.
    transaction_id: Optional[str] = None
    # The UPN of the user associated with this insight. Supports $filter (eq) and $orderby.
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GenerativeAIInsight:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GenerativeAIInsight
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GenerativeAIInsight()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .application_activity import ApplicationActivity

        from .application_activity import ApplicationActivity

        fields: dict[str, Callable[[Any], None]] = {
            "activity": lambda n : setattr(self, 'activity', n.get_enum_value(ApplicationActivity)),
            "content": lambda n : setattr(self, 'content', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "destinationUrl": lambda n : setattr(self, 'destination_url', n.get_str_value()),
            "eventId": lambda n : setattr(self, 'event_id', n.get_str_value()),
            "eventType": lambda n : setattr(self, 'event_type', n.get_str_value()),
            "mcpClientName": lambda n : setattr(self, 'mcp_client_name', n.get_str_value()),
            "mcpServerName": lambda n : setattr(self, 'mcp_server_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sessionId": lambda n : setattr(self, 'session_id', n.get_str_value()),
            "subactivity": lambda n : setattr(self, 'subactivity', n.get_str_value()),
            "transactionId": lambda n : setattr(self, 'transaction_id', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
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
        writer.write_enum_value("activity", self.activity)
        writer.write_str_value("content", self.content)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("destinationUrl", self.destination_url)
        writer.write_str_value("eventId", self.event_id)
        writer.write_str_value("eventType", self.event_type)
        writer.write_str_value("mcpClientName", self.mcp_client_name)
        writer.write_str_value("mcpServerName", self.mcp_server_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("sessionId", self.session_id)
        writer.write_str_value("subactivity", self.subactivity)
        writer.write_str_value("transactionId", self.transaction_id)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_additional_data_value(self.additional_data)
    

