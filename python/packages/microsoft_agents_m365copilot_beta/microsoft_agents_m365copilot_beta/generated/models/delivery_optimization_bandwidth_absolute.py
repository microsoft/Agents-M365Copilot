from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .delivery_optimization_bandwidth import DeliveryOptimizationBandwidth

from .delivery_optimization_bandwidth import DeliveryOptimizationBandwidth

@dataclass
class DeliveryOptimizationBandwidthAbsolute(DeliveryOptimizationBandwidth, Parsable):
    """
    Bandwidth limits in kilobytes per second.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.deliveryOptimizationBandwidthAbsolute"
    # Specifies the maximum download bandwidth in KiloBytes/second that the device can use across all concurrent download activities using Delivery Optimization. Valid values 0 to 4294967295
    maximum_download_bandwidth_in_kilobytes_per_second: Optional[int] = None
    # Specifies the maximum upload bandwidth in KiloBytes/second that a device will use across all concurrent upload activity using Delivery Optimization (0-4000000). Valid values 0 to 4000000
    maximum_upload_bandwidth_in_kilobytes_per_second: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeliveryOptimizationBandwidthAbsolute:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeliveryOptimizationBandwidthAbsolute
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeliveryOptimizationBandwidthAbsolute()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .delivery_optimization_bandwidth import DeliveryOptimizationBandwidth

        from .delivery_optimization_bandwidth import DeliveryOptimizationBandwidth

        fields: dict[str, Callable[[Any], None]] = {
            "maximumDownloadBandwidthInKilobytesPerSecond": lambda n : setattr(self, 'maximum_download_bandwidth_in_kilobytes_per_second', n.get_int_value()),
            "maximumUploadBandwidthInKilobytesPerSecond": lambda n : setattr(self, 'maximum_upload_bandwidth_in_kilobytes_per_second', n.get_int_value()),
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
        writer.write_int_value("maximumDownloadBandwidthInKilobytesPerSecond", self.maximum_download_bandwidth_in_kilobytes_per_second)
        writer.write_int_value("maximumUploadBandwidthInKilobytesPerSecond", self.maximum_upload_bandwidth_in_kilobytes_per_second)
    

