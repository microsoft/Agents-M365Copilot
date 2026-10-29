from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cost_management_alert_threshold import CostManagementAlertThreshold

from .cost_management_alert_threshold import CostManagementAlertThreshold

@dataclass
class PercentageCostManagementAlertThreshold(CostManagementAlertThreshold, Parsable):
    """
    A threshold expressed as a percentage of the policy's period limit. The value is aninteger from 1 to 100 and carries no unit.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.percentageCostManagementAlertThreshold"
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PercentageCostManagementAlertThreshold:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PercentageCostManagementAlertThreshold
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PercentageCostManagementAlertThreshold()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cost_management_alert_threshold import CostManagementAlertThreshold

        from .cost_management_alert_threshold import CostManagementAlertThreshold

        fields: dict[str, Callable[[Any], None]] = {
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
    

