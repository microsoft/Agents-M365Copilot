from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .risk_level import RiskLevel
    from .risk_recommendation import RiskRecommendation

@dataclass
class ExposureRisk(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # The riskIndicators property
    risk_indicators: Optional[list[str]] = None
    # The riskLevel property
    risk_level: Optional[RiskLevel] = None
    # The riskRecommendations property
    risk_recommendations: Optional[list[RiskRecommendation]] = None
    # The riskUrl property
    risk_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ExposureRisk:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExposureRisk
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ExposureRisk()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .risk_level import RiskLevel
        from .risk_recommendation import RiskRecommendation

        from .risk_level import RiskLevel
        from .risk_recommendation import RiskRecommendation

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "riskIndicators": lambda n : setattr(self, 'risk_indicators', n.get_collection_of_primitive_values(str)),
            "riskLevel": lambda n : setattr(self, 'risk_level', n.get_enum_value(RiskLevel)),
            "riskRecommendations": lambda n : setattr(self, 'risk_recommendations', n.get_collection_of_object_values(RiskRecommendation)),
            "riskUrl": lambda n : setattr(self, 'risk_url', n.get_str_value()),
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
        writer.write_collection_of_primitive_values("riskIndicators", self.risk_indicators)
        writer.write_enum_value("riskLevel", self.risk_level)
        writer.write_collection_of_object_values("riskRecommendations", self.risk_recommendations)
        writer.write_str_value("riskUrl", self.risk_url)
        writer.write_additional_data_value(self.additional_data)
    

