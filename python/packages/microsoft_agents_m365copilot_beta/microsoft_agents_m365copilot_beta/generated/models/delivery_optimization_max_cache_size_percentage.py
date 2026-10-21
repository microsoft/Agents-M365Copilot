from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .delivery_optimization_max_cache_size import DeliveryOptimizationMaxCacheSize

from .delivery_optimization_max_cache_size import DeliveryOptimizationMaxCacheSize

@dataclass
class DeliveryOptimizationMaxCacheSizePercentage(DeliveryOptimizationMaxCacheSize, Parsable):
    """
    Delivery Optimization Max cache size percentage types.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.deliveryOptimizationMaxCacheSizePercentage"
    # Specifies the maximum cache size that Delivery Optimization can utilize, as a percentage of disk size (1-100). Valid values 1 to 100
    maximum_cache_size_percentage: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeliveryOptimizationMaxCacheSizePercentage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeliveryOptimizationMaxCacheSizePercentage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeliveryOptimizationMaxCacheSizePercentage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .delivery_optimization_max_cache_size import DeliveryOptimizationMaxCacheSize

        from .delivery_optimization_max_cache_size import DeliveryOptimizationMaxCacheSize

        fields: dict[str, Callable[[Any], None]] = {
            "maximumCacheSizePercentage": lambda n : setattr(self, 'maximum_cache_size_percentage', n.get_int_value()),
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
        writer.write_int_value("maximumCacheSizePercentage", self.maximum_cache_size_percentage)
    

