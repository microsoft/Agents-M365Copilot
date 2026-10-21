from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_domain_join_connector_state import DeviceManagementDomainJoinConnectorState
    from .entity import Entity

from .entity import Entity

@dataclass
class DeviceManagementDomainJoinConnector(Entity, Parsable):
    """
    A Domain Join Connector is a connector that is responsible to allocate (and delete) machine account blobs
    """
    # The connector display name.
    display_name: Optional[str] = None
    # Last time connector contacted Intune.
    last_connection_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The ODJ request states.
    state: Optional[DeviceManagementDomainJoinConnectorState] = None
    # The version of the connector.
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementDomainJoinConnector:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementDomainJoinConnector
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementDomainJoinConnector()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_domain_join_connector_state import DeviceManagementDomainJoinConnectorState
        from .entity import Entity

        from .device_management_domain_join_connector_state import DeviceManagementDomainJoinConnectorState
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastConnectionDateTime": lambda n : setattr(self, 'last_connection_date_time', n.get_datetime_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(DeviceManagementDomainJoinConnectorState)),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastConnectionDateTime", self.last_connection_date_time)
        writer.write_enum_value("state", self.state)
        writer.write_str_value("version", self.version)
    

