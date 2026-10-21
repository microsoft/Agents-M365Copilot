from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .migration_state import MigrationState
    from .sensor_health_status import SensorHealthStatus
    from .sensor_type import SensorType
    from .service_status import ServiceStatus

from ..entity import Entity

@dataclass
class SensorMigration(Entity, Parsable):
    # The date and time the sensor was created.
    created_date_time: Optional[datetime.datetime] = None
    # The display name of the sensor.
    display_name: Optional[str] = None
    # The fully qualified domain name (FQDN) of the domain controller where the sensor is installed.
    domain_name: Optional[str] = None
    # The healthStatus property
    health_status: Optional[SensorHealthStatus] = None
    # The migrationState property
    migration_state: Optional[MigrationState] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The sensorType property
    sensor_type: Optional[SensorType] = None
    # The serviceStatus property
    service_status: Optional[ServiceStatus] = None
    # The version number of the sensor software.
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SensorMigration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SensorMigration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SensorMigration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .migration_state import MigrationState
        from .sensor_health_status import SensorHealthStatus
        from .sensor_type import SensorType
        from .service_status import ServiceStatus

        from ..entity import Entity
        from .migration_state import MigrationState
        from .sensor_health_status import SensorHealthStatus
        from .sensor_type import SensorType
        from .service_status import ServiceStatus

        fields: dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "domainName": lambda n : setattr(self, 'domain_name', n.get_str_value()),
            "healthStatus": lambda n : setattr(self, 'health_status', n.get_enum_value(SensorHealthStatus)),
            "migrationState": lambda n : setattr(self, 'migration_state', n.get_enum_value(MigrationState)),
            "sensorType": lambda n : setattr(self, 'sensor_type', n.get_enum_value(SensorType)),
            "serviceStatus": lambda n : setattr(self, 'service_status', n.get_enum_value(ServiceStatus)),
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("domainName", self.domain_name)
        writer.write_enum_value("healthStatus", self.health_status)
        writer.write_enum_value("migrationState", self.migration_state)
        writer.write_enum_value("sensorType", self.sensor_type)
        writer.write_enum_value("serviceStatus", self.service_status)
        writer.write_str_value("version", self.version)
    

