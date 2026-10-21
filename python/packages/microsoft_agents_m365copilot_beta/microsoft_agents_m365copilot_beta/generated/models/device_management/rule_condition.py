from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .aggregation_type import AggregationType
    from .condition_category import ConditionCategory
    from .operator_type import OperatorType
    from .relationship_type import RelationshipType

@dataclass
class RuleCondition(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The built-in aggregation method for the rule condition. The possible values are: count, percentage, affectedCloudPcCount, affectedCloudPcPercentage, unknownFutureValue.
    aggregation: Optional[AggregationType] = None
    # The property that the rule condition monitors. The possible values are: provisionFailures, imageUploadFailures, azureNetworkConnectionCheckFailures, cloudPcInGracePeriod, frontlineInsufficientLicenses, cloudPcConnectionErrors, cloudPcHostHealthCheckFailures, cloudPcZoneOutage, unknownFutureValue, frontlineBufferUsageDuration, frontlineBufferUsageThreshold, cloudPcUserSettingsPersistenceUsageThreshold, cloudPcDeprovisionedThreshold, cloudPcReserveDeprovisionFailedThreshold. Use the Prefer: include-unknown-enum-members request header to get the following values from this evolvable enum: frontlineBufferUsageDuration, frontlineBufferUsageThreshold, cloudPcUserSettingsPersistenceUsageThreshold, cloudPcDeprovisionedThreshold, cloudPcReserveDeprovisionFailedThreshold.
    condition_category: Optional[ConditionCategory] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The built-in operator for the rule condition. The possible values are: greaterOrEqual, equal, greater, less, lessOrEqual, notEqual, unknownFutureValue.
    operator: Optional[OperatorType] = None
    # The relationship type.  The possible values are: and, or.
    relationship_type: Optional[RelationshipType] = None
    # The threshold value of the alert condition. The threshold value can be a number in string form or string like 'WestUS'.
    threshold_value: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RuleCondition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RuleCondition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RuleCondition()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .aggregation_type import AggregationType
        from .condition_category import ConditionCategory
        from .operator_type import OperatorType
        from .relationship_type import RelationshipType

        from .aggregation_type import AggregationType
        from .condition_category import ConditionCategory
        from .operator_type import OperatorType
        from .relationship_type import RelationshipType

        fields: dict[str, Callable[[Any], None]] = {
            "aggregation": lambda n : setattr(self, 'aggregation', n.get_enum_value(AggregationType)),
            "conditionCategory": lambda n : setattr(self, 'condition_category', n.get_enum_value(ConditionCategory)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "operator": lambda n : setattr(self, 'operator', n.get_enum_value(OperatorType)),
            "relationshipType": lambda n : setattr(self, 'relationship_type', n.get_enum_value(RelationshipType)),
            "thresholdValue": lambda n : setattr(self, 'threshold_value', n.get_str_value()),
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
        writer.write_enum_value("conditionCategory", self.condition_category)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("operator", self.operator)
        writer.write_enum_value("relationshipType", self.relationship_type)
        writer.write_str_value("thresholdValue", self.threshold_value)
        writer.write_additional_data_value(self.additional_data)
    

