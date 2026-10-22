from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .threat_intelligence_action import ThreatIntelligenceAction

@dataclass
class ThreatIntelligencePolicySettings(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The defaultAction property
    default_action: Optional[ThreatIntelligenceAction] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ThreatIntelligencePolicySettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ThreatIntelligencePolicySettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ThreatIntelligencePolicySettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .threat_intelligence_action import ThreatIntelligenceAction

        from .threat_intelligence_action import ThreatIntelligenceAction

        fields: dict[str, Callable[[Any], None]] = {
            "defaultAction": lambda n : setattr(self, 'default_action', n.get_enum_value(ThreatIntelligenceAction)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_enum_value("defaultAction", self.default_action)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

