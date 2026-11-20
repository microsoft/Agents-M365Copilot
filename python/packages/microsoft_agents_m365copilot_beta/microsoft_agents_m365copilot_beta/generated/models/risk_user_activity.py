from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .risk_detail import RiskDetail
    from .risk_event_type import RiskEventType

@dataclass
class RiskUserActivity(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # For more information, see riskDetail.
    detail: Optional[RiskDetail] = None
    # List of risk event types. Deprecated. Use riskEventType instead.
    event_types: Optional[list[RiskEventType]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The type of risk event detected. The possible values are: anonymizedIPAddress, investigationsThreatIntelligence, investigationsThreatIntelligenceSigninLinked,leakedCredentials, maliciousIPAddress, maliciousIPAddressValidCredentialsBlockedIP, malwareInfectedIPAddress, mcasImpossibleTravel, mcasSuspiciousInboxManipulationRules, suspiciousAPITraffic, suspiciousIPAddress,   unfamiliarFeatures, unlikelyTravel. For more information about each value, see Risk types and detection.
    risk_event_types: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RiskUserActivity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RiskUserActivity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RiskUserActivity()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .risk_detail import RiskDetail
        from .risk_event_type import RiskEventType

        from .risk_detail import RiskDetail
        from .risk_event_type import RiskEventType

        fields: dict[str, Callable[[Any], None]] = {
            "detail": lambda n : setattr(self, 'detail', n.get_enum_value(RiskDetail)),
            "eventTypes": lambda n : setattr(self, 'event_types', n.get_collection_of_enum_values(RiskEventType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "riskEventTypes": lambda n : setattr(self, 'risk_event_types', n.get_collection_of_primitive_values(str)),
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
        writer.write_enum_value("detail", self.detail)
        writer.write_collection_of_enum_values("eventTypes", self.event_types)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_primitive_values("riskEventTypes", self.risk_event_types)
        writer.write_additional_data_value(self.additional_data)
    

