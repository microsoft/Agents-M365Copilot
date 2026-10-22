from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...entity import Entity
    from .customer_insight import CustomerInsight
    from .security_requirement import SecurityRequirement
    from .security_score_history import SecurityScoreHistory

from ...entity import Entity

@dataclass
class PartnerSecurityScore(Entity, Parsable):
    # The current security score for the partner.
    current_score: Optional[float] = None
    # Contains customer-specific information for certain requirements.
    customer_insights: Optional[list[CustomerInsight]] = None
    # Contains a list of recent score changes.
    history: Optional[list[SecurityScoreHistory]] = None
    # The last time the data was checked.
    last_refresh_date_time: Optional[datetime.datetime] = None
    # The maximum score possible.
    max_score: Optional[float] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Contains the list of security requirements that make up the score.
    requirements: Optional[list[SecurityRequirement]] = None
    # The last time the security score or related properties changed.
    updated_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PartnerSecurityScore:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PartnerSecurityScore
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PartnerSecurityScore()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ...entity import Entity
        from .customer_insight import CustomerInsight
        from .security_requirement import SecurityRequirement
        from .security_score_history import SecurityScoreHistory

        from ...entity import Entity
        from .customer_insight import CustomerInsight
        from .security_requirement import SecurityRequirement
        from .security_score_history import SecurityScoreHistory

        fields: dict[str, Callable[[Any], None]] = {
            "currentScore": lambda n : setattr(self, 'current_score', n.get_float_value()),
            "customerInsights": lambda n : setattr(self, 'customer_insights', n.get_collection_of_object_values(CustomerInsight)),
            "history": lambda n : setattr(self, 'history', n.get_collection_of_object_values(SecurityScoreHistory)),
            "lastRefreshDateTime": lambda n : setattr(self, 'last_refresh_date_time', n.get_datetime_value()),
            "maxScore": lambda n : setattr(self, 'max_score', n.get_float_value()),
            "requirements": lambda n : setattr(self, 'requirements', n.get_collection_of_object_values(SecurityRequirement)),
            "updatedDateTime": lambda n : setattr(self, 'updated_date_time', n.get_datetime_value()),
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
        writer.write_float_value("currentScore", self.current_score)
        writer.write_collection_of_object_values("customerInsights", self.customer_insights)
        writer.write_collection_of_object_values("history", self.history)
        writer.write_datetime_value("lastRefreshDateTime", self.last_refresh_date_time)
        writer.write_float_value("maxScore", self.max_score)
        writer.write_collection_of_object_values("requirements", self.requirements)
        writer.write_datetime_value("updatedDateTime", self.updated_date_time)
    

