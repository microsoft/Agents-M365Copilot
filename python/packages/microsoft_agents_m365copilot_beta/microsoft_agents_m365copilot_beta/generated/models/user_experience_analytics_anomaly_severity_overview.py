from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class UserExperienceAnalyticsAnomalySeverityOverview(AdditionalDataHolder, Parsable):
    """
    The user experience analytics anomaly severity overview entity contains the count information for each severity of anomaly.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Indicates count of high severity anomalies which have been detected. Valid values -2147483648 to 2147483647
    high_severity_anomaly_count: Optional[int] = None
    # Indicates count of informational severity anomalies which have been detected. Valid values -2147483648 to 2147483647
    informational_severity_anomaly_count: Optional[int] = None
    # Indicates count of low severity anomalies which have been detected. Valid values -2147483648 to 2147483647
    low_severity_anomaly_count: Optional[int] = None
    # Indicates count of medium severity anomalies which have been detected. Valid values -2147483648 to 2147483647
    medium_severity_anomaly_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserExperienceAnalyticsAnomalySeverityOverview:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsAnomalySeverityOverview
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserExperienceAnalyticsAnomalySeverityOverview()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "highSeverityAnomalyCount": lambda n : setattr(self, 'high_severity_anomaly_count', n.get_int_value()),
            "informationalSeverityAnomalyCount": lambda n : setattr(self, 'informational_severity_anomaly_count', n.get_int_value()),
            "lowSeverityAnomalyCount": lambda n : setattr(self, 'low_severity_anomaly_count', n.get_int_value()),
            "mediumSeverityAnomalyCount": lambda n : setattr(self, 'medium_severity_anomaly_count', n.get_int_value()),
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
        writer.write_int_value("highSeverityAnomalyCount", self.high_severity_anomaly_count)
        writer.write_int_value("informationalSeverityAnomalyCount", self.informational_severity_anomaly_count)
        writer.write_int_value("lowSeverityAnomalyCount", self.low_severity_anomaly_count)
        writer.write_int_value("mediumSeverityAnomalyCount", self.medium_severity_anomaly_count)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

