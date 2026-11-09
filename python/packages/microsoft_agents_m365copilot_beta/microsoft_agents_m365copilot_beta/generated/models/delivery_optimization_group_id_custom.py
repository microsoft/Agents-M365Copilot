from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .delivery_optimization_group_id_source import DeliveryOptimizationGroupIdSource

from .delivery_optimization_group_id_source import DeliveryOptimizationGroupIdSource

@dataclass
class DeliveryOptimizationGroupIdCustom(DeliveryOptimizationGroupIdSource, Parsable):
    """
    Custom group id type
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.deliveryOptimizationGroupIdCustom"
    # Specifies an arbitrary group ID that the device belongs to
    group_id_custom: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeliveryOptimizationGroupIdCustom:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeliveryOptimizationGroupIdCustom
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeliveryOptimizationGroupIdCustom()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .delivery_optimization_group_id_source import DeliveryOptimizationGroupIdSource

        from .delivery_optimization_group_id_source import DeliveryOptimizationGroupIdSource

        fields: dict[str, Callable[[Any], None]] = {
            "groupIdCustom": lambda n : setattr(self, 'group_id_custom', n.get_str_value()),
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
        writer.write_str_value("groupIdCustom", self.group_id_custom)
    

