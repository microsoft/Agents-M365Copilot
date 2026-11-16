from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_configuration import DeviceConfiguration
    from .enablement import Enablement
    from .windows_health_monitoring_scope import WindowsHealthMonitoringScope

from .device_configuration import DeviceConfiguration

@dataclass
class WindowsHealthMonitoringConfiguration(DeviceConfiguration, Parsable):
    """
    Windows device health monitoring configuration
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsHealthMonitoringConfiguration"
    # Possible values of a property
    allow_device_health_monitoring: Optional[Enablement] = None
    # Specifies custom set of events collected from the device where health monitoring is enabled
    config_device_health_monitoring_custom_scope: Optional[str] = None
    # Device health monitoring scope
    config_device_health_monitoring_scope: Optional[WindowsHealthMonitoringScope] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsHealthMonitoringConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsHealthMonitoringConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsHealthMonitoringConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_configuration import DeviceConfiguration
        from .enablement import Enablement
        from .windows_health_monitoring_scope import WindowsHealthMonitoringScope

        from .device_configuration import DeviceConfiguration
        from .enablement import Enablement
        from .windows_health_monitoring_scope import WindowsHealthMonitoringScope

        fields: dict[str, Callable[[Any], None]] = {
            "allowDeviceHealthMonitoring": lambda n : setattr(self, 'allow_device_health_monitoring', n.get_enum_value(Enablement)),
            "configDeviceHealthMonitoringCustomScope": lambda n : setattr(self, 'config_device_health_monitoring_custom_scope', n.get_str_value()),
            "configDeviceHealthMonitoringScope": lambda n : setattr(self, 'config_device_health_monitoring_scope', n.get_collection_of_enum_values(WindowsHealthMonitoringScope)),
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
        writer.write_enum_value("allowDeviceHealthMonitoring", self.allow_device_health_monitoring)
        writer.write_str_value("configDeviceHealthMonitoringCustomScope", self.config_device_health_monitoring_custom_scope)
        writer.write_enum_value("configDeviceHealthMonitoringScope", self.config_device_health_monitoring_scope)
    

