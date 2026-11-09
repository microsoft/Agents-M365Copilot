from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .delivery_optimization_group_id_options_type import DeliveryOptimizationGroupIdOptionsType
    from .delivery_optimization_group_id_source import DeliveryOptimizationGroupIdSource

from .delivery_optimization_group_id_source import DeliveryOptimizationGroupIdSource

@dataclass
class DeliveryOptimizationGroupIdSourceOptions(DeliveryOptimizationGroupIdSource, Parsable):
    """
    Group id options type
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.deliveryOptimizationGroupIdSourceOptions"
    # Possible values for the DeliveryOptimizationGroupIdOptionsType setting.
    group_id_source_option: Optional[DeliveryOptimizationGroupIdOptionsType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeliveryOptimizationGroupIdSourceOptions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeliveryOptimizationGroupIdSourceOptions
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeliveryOptimizationGroupIdSourceOptions()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .delivery_optimization_group_id_options_type import DeliveryOptimizationGroupIdOptionsType
        from .delivery_optimization_group_id_source import DeliveryOptimizationGroupIdSource

        from .delivery_optimization_group_id_options_type import DeliveryOptimizationGroupIdOptionsType
        from .delivery_optimization_group_id_source import DeliveryOptimizationGroupIdSource

        fields: dict[str, Callable[[Any], None]] = {
            "groupIdSourceOption": lambda n : setattr(self, 'group_id_source_option', n.get_enum_value(DeliveryOptimizationGroupIdOptionsType)),
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
        writer.write_enum_value("groupIdSourceOption", self.group_id_source_option)
    

