from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .threat_intelligence_destination import ThreatIntelligenceDestination
    from .threat_intelligence_severity import ThreatIntelligenceSeverity

@dataclass
class ThreatIntelligenceMatchingConditions(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # A collection of destinations that are considered potential threats for network access evaluation.
    destinations: Optional[list[ThreatIntelligenceDestination]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The severity level of the threat associated with the destinations. Higher severity levels typically result in stricter security controls. The possible values are: low, medium, high, unknownFutureValue.
    severity: Optional[ThreatIntelligenceSeverity] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ThreatIntelligenceMatchingConditions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ThreatIntelligenceMatchingConditions
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ThreatIntelligenceMatchingConditions()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .threat_intelligence_destination import ThreatIntelligenceDestination
        from .threat_intelligence_severity import ThreatIntelligenceSeverity

        from .threat_intelligence_destination import ThreatIntelligenceDestination
        from .threat_intelligence_severity import ThreatIntelligenceSeverity

        fields: dict[str, Callable[[Any], None]] = {
            "destinations": lambda n : setattr(self, 'destinations', n.get_collection_of_object_values(ThreatIntelligenceDestination)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "severity": lambda n : setattr(self, 'severity', n.get_enum_value(ThreatIntelligenceSeverity)),
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
        writer.write_collection_of_object_values("destinations", self.destinations)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("severity", self.severity)
        writer.write_additional_data_value(self.additional_data)
    

