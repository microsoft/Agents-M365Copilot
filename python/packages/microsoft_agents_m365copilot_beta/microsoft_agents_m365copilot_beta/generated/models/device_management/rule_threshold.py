from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .aggregation_type import AggregationType
    from .operator_type import OperatorType

@dataclass
class RuleThreshold(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Indicates the built-in aggregation methods. The possible values are: count, percentage, affectedCloudPcCount, affectedCloudPcPercentage, unknownFutureValue.
    aggregation: Optional[AggregationType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the built-in operator. The possible values are: greaterOrEqual, equal, greater, less, lessOrEqual, notEqual, unknownFutureValue.
    operator: Optional[OperatorType] = None
    # The target threshold value.
    target: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RuleThreshold:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RuleThreshold
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RuleThreshold()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .aggregation_type import AggregationType
        from .operator_type import OperatorType

        from .aggregation_type import AggregationType
        from .operator_type import OperatorType

        fields: dict[str, Callable[[Any], None]] = {
            "aggregation": lambda n : setattr(self, 'aggregation', n.get_enum_value(AggregationType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "operator": lambda n : setattr(self, 'operator', n.get_enum_value(OperatorType)),
            "target": lambda n : setattr(self, 'target', n.get_int_value()),
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
        writer.write_enum_value("aggregation", self.aggregation)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("operator", self.operator)
        writer.write_int_value("target", self.target)
        writer.write_additional_data_value(self.additional_data)
    

