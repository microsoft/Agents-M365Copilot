from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .severity import Severity

@dataclass
class RiskAlert(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The displayName property
    display_name: Optional[str] = None
    # The mitreTechniques property
    mitre_techniques: Optional[list[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The providerAlertId property
    provider_alert_id: Optional[str] = None
    # The severity property
    severity: Optional[Severity] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RiskAlert:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RiskAlert
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RiskAlert()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .severity import Severity

        from .severity import Severity

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "mitreTechniques": lambda n : setattr(self, 'mitre_techniques', n.get_collection_of_primitive_values(str)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "providerAlertId": lambda n : setattr(self, 'provider_alert_id', n.get_str_value()),
            "severity": lambda n : setattr(self, 'severity', n.get_enum_value(Severity)),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_primitive_values("mitreTechniques", self.mitre_techniques)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("providerAlertId", self.provider_alert_id)
        writer.write_enum_value("severity", self.severity)
        writer.write_additional_data_value(self.additional_data)
    

