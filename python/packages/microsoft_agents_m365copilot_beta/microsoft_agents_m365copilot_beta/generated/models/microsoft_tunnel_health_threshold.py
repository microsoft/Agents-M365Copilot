from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class MicrosoftTunnelHealthThreshold(Entity, Parsable):
    """
    Entity that represents the health thresholds of a health metric
    """
    # The threshold for being healthy based on default health status metrics: CPU usage healthy < 50%, Memory usage healthy < 50%, Disk space healthy > 5GB, Latency healthy < 10ms, health metrics can be customized. Read-only.
    default_healthy_threshold: Optional[int] = None
    # The threshold for being unhealthy based on default health status metrics: CPU usage unhealthy > 75%, Memory usage unhealthy > 75%, Disk space < 3GB, Latency unhealthy > 20ms, health metrics can be customized. Read-only.
    default_unhealthy_threshold: Optional[int] = None
    # The threshold for being healthy based on default health status metrics: CPU usage healthy < 50%, Memory usage healthy < 50%, Disk space healthy > 5GB, Latency healthy < 10ms, health metrics can be customized.
    healthy_threshold: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The threshold for being unhealthy based on default health status metrics: CPU usage unhealthy > 75%, Memory usage unhealthy > 75%, Disk space < 3GB, Latency Unhealthy > 20ms, health metrics can be customized.
    unhealthy_threshold: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MicrosoftTunnelHealthThreshold:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MicrosoftTunnelHealthThreshold
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MicrosoftTunnelHealthThreshold()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "defaultHealthyThreshold": lambda n : setattr(self, 'default_healthy_threshold', n.get_int_value()),
            "defaultUnhealthyThreshold": lambda n : setattr(self, 'default_unhealthy_threshold', n.get_int_value()),
            "healthyThreshold": lambda n : setattr(self, 'healthy_threshold', n.get_int_value()),
            "unhealthyThreshold": lambda n : setattr(self, 'unhealthy_threshold', n.get_int_value()),
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
        writer.write_int_value("defaultHealthyThreshold", self.default_healthy_threshold)
        writer.write_int_value("defaultUnhealthyThreshold", self.default_unhealthy_threshold)
        writer.write_int_value("healthyThreshold", self.healthy_threshold)
        writer.write_int_value("unhealthyThreshold", self.unhealthy_threshold)
    

