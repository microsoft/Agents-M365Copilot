from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .sensor_status import SensorStatus

from .entity import Entity

@dataclass
class PrivateAccessSensor(Entity, Parsable):
    # External IP of sensor.
    external_ip: Optional[str] = None
    # Not Implementated.
    is_audit_mode: Optional[bool] = None
    # Not Implemented.
    is_breakglass_enabled: Optional[bool] = None
    # Machine name of sensor.
    machine_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status property
    status: Optional[SensorStatus] = None
    # Version of sensor.
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PrivateAccessSensor:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PrivateAccessSensor
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PrivateAccessSensor()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .sensor_status import SensorStatus

        from .entity import Entity
        from .sensor_status import SensorStatus

        fields: dict[str, Callable[[Any], None]] = {
            "externalIp": lambda n : setattr(self, 'external_ip', n.get_str_value()),
            "isAuditMode": lambda n : setattr(self, 'is_audit_mode', n.get_bool_value()),
            "isBreakglassEnabled": lambda n : setattr(self, 'is_breakglass_enabled', n.get_bool_value()),
            "machineName": lambda n : setattr(self, 'machine_name', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(SensorStatus)),
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
        writer.write_str_value("externalIp", self.external_ip)
        writer.write_bool_value("isAuditMode", self.is_audit_mode)
        writer.write_bool_value("isBreakglassEnabled", self.is_breakglass_enabled)
        writer.write_str_value("machineName", self.machine_name)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("version", self.version)
    

