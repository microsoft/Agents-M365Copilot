from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .connector_health_check import ConnectorHealthCheck
    from .entity import Entity
    from .ndes_connector_health_status import NdesConnectorHealthStatus
    from .ndes_connector_state import NdesConnectorState

from .entity import Entity

@dataclass
class NdesConnector(Entity, Parsable):
    """
    Entity which represents an OnPrem Ndes connector.
    """
    # The build version of the Ndes Connector.
    connector_version: Optional[str] = None
    # The friendly name of the Ndes Connector.
    display_name: Optional[str] = None
    # Timestamp when on-prem certificate connector was enrolled in Intune.
    enrolled_date_time: Optional[datetime.datetime] = None
    # The collection of individual health check results for this connector. Each entry represents an independent health metric with its current status. Empty when the connector is disconnected or when health has not been evaluated yet. Read-only.
    health_checks: Optional[list[ConnectorHealthCheck]] = None
    # The overall health status of the connector, representing the worst status across all individual health checks. This value is pre-computed on each connector upload and may be overridden to disconnected at read time if the connector has not connected recently. Read-only.
    health_status: Optional[NdesConnectorHealthStatus] = None
    # Last connection time for the Ndes Connector
    last_connection_date_time: Optional[datetime.datetime] = None
    # Name of the machine running on-prem certificate connector service.
    machine_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # List of Scope Tags for this Entity instance.
    role_scope_tag_ids: Optional[list[str]] = None
    # The current status of the Ndes Connector.
    state: Optional[NdesConnectorState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> NdesConnector:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: NdesConnector
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return NdesConnector()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .connector_health_check import ConnectorHealthCheck
        from .entity import Entity
        from .ndes_connector_health_status import NdesConnectorHealthStatus
        from .ndes_connector_state import NdesConnectorState

        from .connector_health_check import ConnectorHealthCheck
        from .entity import Entity
        from .ndes_connector_health_status import NdesConnectorHealthStatus
        from .ndes_connector_state import NdesConnectorState

        fields: dict[str, Callable[[Any], None]] = {
            "connectorVersion": lambda n : setattr(self, 'connector_version', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "enrolledDateTime": lambda n : setattr(self, 'enrolled_date_time', n.get_datetime_value()),
            "healthChecks": lambda n : setattr(self, 'health_checks', n.get_collection_of_object_values(ConnectorHealthCheck)),
            "healthStatus": lambda n : setattr(self, 'health_status', n.get_enum_value(NdesConnectorHealthStatus)),
            "lastConnectionDateTime": lambda n : setattr(self, 'last_connection_date_time', n.get_datetime_value()),
            "machineName": lambda n : setattr(self, 'machine_name', n.get_str_value()),
            "roleScopeTagIds": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(NdesConnectorState)),
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
        writer.write_str_value("connectorVersion", self.connector_version)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("enrolledDateTime", self.enrolled_date_time)
        writer.write_datetime_value("lastConnectionDateTime", self.last_connection_date_time)
        writer.write_str_value("machineName", self.machine_name)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
        writer.write_enum_value("state", self.state)
    

