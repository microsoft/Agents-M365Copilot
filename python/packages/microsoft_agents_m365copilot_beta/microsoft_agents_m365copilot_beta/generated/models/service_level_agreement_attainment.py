from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ServiceLevelAgreementAttainment(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The end date for the calendar month for which SLA attainment is measured.
    end_date: Optional[datetime.date] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The level of SLA attainment achieved by the tenant for the calendar month identified, as described in Microsoft Entra SLA performance. Values are truncated, not rounded, so the actual value is always equal to or higher than the displayed value. Values are expressed as a percentage of availability for the tenant.
    score: Optional[float] = None
    # The start date for the calendar month for which SLA attainment is measured.
    start_date: Optional[datetime.date] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ServiceLevelAgreementAttainment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ServiceLevelAgreementAttainment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ServiceLevelAgreementAttainment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "endDate": lambda n : setattr(self, 'end_date', n.get_date_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "score": lambda n : setattr(self, 'score', n.get_float_value()),
            "startDate": lambda n : setattr(self, 'start_date', n.get_date_value()),
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
        writer.write_date_value("endDate", self.end_date)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_float_value("score", self.score)
        writer.write_date_value("startDate", self.start_date)
        writer.write_additional_data_value(self.additional_data)
    

