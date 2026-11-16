from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .delivery_optimization_bandwidth import DeliveryOptimizationBandwidth
    from .delivery_optimization_bandwidth_business_hours_limit import DeliveryOptimizationBandwidthBusinessHoursLimit

from .delivery_optimization_bandwidth import DeliveryOptimizationBandwidth

@dataclass
class DeliveryOptimizationBandwidthHoursWithPercentage(DeliveryOptimizationBandwidth, Parsable):
    """
    Bandwidth limit as a percentage with business hours.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.deliveryOptimizationBandwidthHoursWithPercentage"
    # Background download percentage hours.
    bandwidth_background_percentage_hours: Optional[DeliveryOptimizationBandwidthBusinessHoursLimit] = None
    # Foreground download percentage hours.
    bandwidth_foreground_percentage_hours: Optional[DeliveryOptimizationBandwidthBusinessHoursLimit] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeliveryOptimizationBandwidthHoursWithPercentage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeliveryOptimizationBandwidthHoursWithPercentage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeliveryOptimizationBandwidthHoursWithPercentage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .delivery_optimization_bandwidth import DeliveryOptimizationBandwidth
        from .delivery_optimization_bandwidth_business_hours_limit import DeliveryOptimizationBandwidthBusinessHoursLimit

        from .delivery_optimization_bandwidth import DeliveryOptimizationBandwidth
        from .delivery_optimization_bandwidth_business_hours_limit import DeliveryOptimizationBandwidthBusinessHoursLimit

        fields: dict[str, Callable[[Any], None]] = {
            "bandwidthBackgroundPercentageHours": lambda n : setattr(self, 'bandwidth_background_percentage_hours', n.get_object_value(DeliveryOptimizationBandwidthBusinessHoursLimit)),
            "bandwidthForegroundPercentageHours": lambda n : setattr(self, 'bandwidth_foreground_percentage_hours', n.get_object_value(DeliveryOptimizationBandwidthBusinessHoursLimit)),
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
        writer.write_object_value("bandwidthBackgroundPercentageHours", self.bandwidth_background_percentage_hours)
        writer.write_object_value("bandwidthForegroundPercentageHours", self.bandwidth_foreground_percentage_hours)
    

