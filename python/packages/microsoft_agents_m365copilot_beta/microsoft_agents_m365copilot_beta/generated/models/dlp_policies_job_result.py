from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .matching_dlp_rule import MatchingDlpRule

@dataclass
class DlpPoliciesJobResult(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The auditCorrelationId property
    audit_correlation_id: Optional[str] = None
    # The evaluationDateTime property
    evaluation_date_time: Optional[datetime.datetime] = None
    # The matchingRules property
    matching_rules: Optional[list[MatchingDlpRule]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DlpPoliciesJobResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DlpPoliciesJobResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DlpPoliciesJobResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .matching_dlp_rule import MatchingDlpRule

        from .matching_dlp_rule import MatchingDlpRule

        fields: dict[str, Callable[[Any], None]] = {
            "auditCorrelationId": lambda n : setattr(self, 'audit_correlation_id', n.get_str_value()),
            "evaluationDateTime": lambda n : setattr(self, 'evaluation_date_time', n.get_datetime_value()),
            "matchingRules": lambda n : setattr(self, 'matching_rules', n.get_collection_of_object_values(MatchingDlpRule)),
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
        writer.write_str_value("auditCorrelationId", self.audit_correlation_id)
        writer.write_datetime_value("evaluationDateTime", self.evaluation_date_time)
        writer.write_collection_of_object_values("matchingRules", self.matching_rules)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

