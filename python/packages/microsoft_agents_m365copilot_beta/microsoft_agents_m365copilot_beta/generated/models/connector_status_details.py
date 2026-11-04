from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .connector_health_state import ConnectorHealthState
    from .connector_name import ConnectorName

@dataclass
class ConnectorStatusDetails(AdditionalDataHolder, Parsable):
    """
    Represent connector status
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Connector Instance Id
    connector_instance_id: Optional[str] = None
    # Connectors name for connector status
    connector_name: Optional[ConnectorName] = None
    # Event datetime
    event_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Connector health state for connector status
    status: Optional[ConnectorHealthState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ConnectorStatusDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConnectorStatusDetails
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ConnectorStatusDetails()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .connector_health_state import ConnectorHealthState
        from .connector_name import ConnectorName

        from .connector_health_state import ConnectorHealthState
        from .connector_name import ConnectorName

        fields: dict[str, Callable[[Any], None]] = {
            "connectorInstanceId": lambda n : setattr(self, 'connector_instance_id', n.get_str_value()),
            "connectorName": lambda n : setattr(self, 'connector_name', n.get_enum_value(ConnectorName)),
            "eventDateTime": lambda n : setattr(self, 'event_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(ConnectorHealthState)),
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
        writer.write_str_value("connectorInstanceId", self.connector_instance_id)
        writer.write_enum_value("connectorName", self.connector_name)
        writer.write_datetime_value("eventDateTime", self.event_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

