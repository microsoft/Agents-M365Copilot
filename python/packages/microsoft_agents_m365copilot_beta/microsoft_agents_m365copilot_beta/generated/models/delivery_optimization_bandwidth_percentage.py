from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .delivery_optimization_bandwidth import DeliveryOptimizationBandwidth

from .delivery_optimization_bandwidth import DeliveryOptimizationBandwidth

@dataclass
class DeliveryOptimizationBandwidthPercentage(DeliveryOptimizationBandwidth, Parsable):
    """
    Bandwidth limits specified as a percentage.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.deliveryOptimizationBandwidthPercentage"
    # Specifies the maximum background download bandwidth that Delivery Optimization uses across all concurrent download activities as a percentage of available download bandwidth (0-100). Valid values 0 to 100
    maximum_background_bandwidth_percentage: Optional[int] = None
    # Specifies the maximum foreground download bandwidth that Delivery Optimization uses across all concurrent download activities as a percentage of available download bandwidth (0-100). Valid values 0 to 100
    maximum_foreground_bandwidth_percentage: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeliveryOptimizationBandwidthPercentage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeliveryOptimizationBandwidthPercentage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeliveryOptimizationBandwidthPercentage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .delivery_optimization_bandwidth import DeliveryOptimizationBandwidth

        from .delivery_optimization_bandwidth import DeliveryOptimizationBandwidth

        fields: dict[str, Callable[[Any], None]] = {
            "maximumBackgroundBandwidthPercentage": lambda n : setattr(self, 'maximum_background_bandwidth_percentage', n.get_int_value()),
            "maximumForegroundBandwidthPercentage": lambda n : setattr(self, 'maximum_foreground_bandwidth_percentage', n.get_int_value()),
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
        writer.write_int_value("maximumBackgroundBandwidthPercentage", self.maximum_background_bandwidth_percentage)
        writer.write_int_value("maximumForegroundBandwidthPercentage", self.maximum_foreground_bandwidth_percentage)
    

