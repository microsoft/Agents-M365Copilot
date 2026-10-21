from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .absolute_cost_management_alert_threshold import AbsoluteCostManagementAlertThreshold
    from .percentage_cost_management_alert_threshold import PercentageCostManagementAlertThreshold

@dataclass
class CostManagementAlertThreshold(AdditionalDataHolder, Parsable):
    """
    A single notify-only alert threshold. Every threshold is one of its derived types,identified by @odata.type on create.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # The threshold value. Its permitted range is set by the derived type.
    value: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CostManagementAlertThreshold:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CostManagementAlertThreshold
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.absoluteCostManagementAlertThreshold".casefold():
            from .absolute_cost_management_alert_threshold import AbsoluteCostManagementAlertThreshold

            return AbsoluteCostManagementAlertThreshold()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.percentageCostManagementAlertThreshold".casefold():
            from .percentage_cost_management_alert_threshold import PercentageCostManagementAlertThreshold

            return PercentageCostManagementAlertThreshold()
        return CostManagementAlertThreshold()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .absolute_cost_management_alert_threshold import AbsoluteCostManagementAlertThreshold
        from .percentage_cost_management_alert_threshold import PercentageCostManagementAlertThreshold

        from .absolute_cost_management_alert_threshold import AbsoluteCostManagementAlertThreshold
        from .percentage_cost_management_alert_threshold import PercentageCostManagementAlertThreshold

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "value": lambda n : setattr(self, 'value', n.get_float_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_float_value("value", self.value)
        writer.write_additional_data_value(self.additional_data)
    

