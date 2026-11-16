from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .user_experience_analytics_anomaly_correlation_group_feature import UserExperienceAnalyticsAnomalyCorrelationGroupFeature
    from .user_experience_analytics_anomaly_correlation_group_prevalence import UserExperienceAnalyticsAnomalyCorrelationGroupPrevalence

from .entity import Entity

@dataclass
class UserExperienceAnalyticsAnomalyCorrelationGroupOverview(Entity, Parsable):
    """
    The user experience analytics anomaly correlation group overview entity contains the information for each correlation group of an anomaly.
    """
    # Indicates the number of correlation groups in the anomaly. Valid values -2147483648 to 2147483647
    anomaly_correlation_group_count: Optional[int] = None
    # The unique identifier of the anomaly. Anomaly details such as name and type can be found in the UserExperienceAnalyticsAnomalySeverityOverview entity.
    anomaly_id: Optional[str] = None
    # Indicates the total number of devices affected by the anomaly in the correlation group. Valid values -2147483648 to 2147483647
    correlation_group_anomalous_device_count: Optional[int] = None
    # Indicates the total number of devices at risk in the correlation group. Valid values -2147483648 to 2147483647
    correlation_group_at_risk_device_count: Optional[int] = None
    # Indicates the total number of devices in a correlation group. Valid values -2147483648 to 2147483647
    correlation_group_device_count: Optional[int] = None
    # Describes the features of a device that are shared between all devices in a correlation group.
    correlation_group_features: Optional[list[UserExperienceAnalyticsAnomalyCorrelationGroupFeature]] = None
    # The unique identifier for the correlation group which will uniquely identify one of the correlation group within an anomaly. The correlation Id can be mapped to the correlation group name by concatinating the correlation group features. Example of correlation group name which is the indicative of concatenated features names are  for names, Contoso manufacture 4.4.1 and Windows 11.22621.1485.
    correlation_group_id: Optional[str] = None
    # Indicates the level of prevalence of the correlation group features in the anomaly. Possible values are: high, medium or low
    correlation_group_prevalence: Optional[UserExperienceAnalyticsAnomalyCorrelationGroupPrevalence] = None
    # The percentage of the devices in the correlation group that are anomalous. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
    correlation_group_prevalence_percentage: Optional[float] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the total number of devices in the tenant. Valid values -2147483648 to 2147483647
    total_device_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserExperienceAnalyticsAnomalyCorrelationGroupOverview:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsAnomalyCorrelationGroupOverview
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserExperienceAnalyticsAnomalyCorrelationGroupOverview()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .user_experience_analytics_anomaly_correlation_group_feature import UserExperienceAnalyticsAnomalyCorrelationGroupFeature
        from .user_experience_analytics_anomaly_correlation_group_prevalence import UserExperienceAnalyticsAnomalyCorrelationGroupPrevalence

        from .entity import Entity
        from .user_experience_analytics_anomaly_correlation_group_feature import UserExperienceAnalyticsAnomalyCorrelationGroupFeature
        from .user_experience_analytics_anomaly_correlation_group_prevalence import UserExperienceAnalyticsAnomalyCorrelationGroupPrevalence

        fields: dict[str, Callable[[Any], None]] = {
            "anomalyCorrelationGroupCount": lambda n : setattr(self, 'anomaly_correlation_group_count', n.get_int_value()),
            "anomalyId": lambda n : setattr(self, 'anomaly_id', n.get_str_value()),
            "correlationGroupAnomalousDeviceCount": lambda n : setattr(self, 'correlation_group_anomalous_device_count', n.get_int_value()),
            "correlationGroupAtRiskDeviceCount": lambda n : setattr(self, 'correlation_group_at_risk_device_count', n.get_int_value()),
            "correlationGroupDeviceCount": lambda n : setattr(self, 'correlation_group_device_count', n.get_int_value()),
            "correlationGroupFeatures": lambda n : setattr(self, 'correlation_group_features', n.get_collection_of_object_values(UserExperienceAnalyticsAnomalyCorrelationGroupFeature)),
            "correlationGroupId": lambda n : setattr(self, 'correlation_group_id', n.get_str_value()),
            "correlationGroupPrevalence": lambda n : setattr(self, 'correlation_group_prevalence', n.get_enum_value(UserExperienceAnalyticsAnomalyCorrelationGroupPrevalence)),
            "correlationGroupPrevalencePercentage": lambda n : setattr(self, 'correlation_group_prevalence_percentage', n.get_float_value()),
            "totalDeviceCount": lambda n : setattr(self, 'total_device_count', n.get_int_value()),
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
        writer.write_int_value("anomalyCorrelationGroupCount", self.anomaly_correlation_group_count)
        writer.write_str_value("anomalyId", self.anomaly_id)
        writer.write_int_value("correlationGroupAnomalousDeviceCount", self.correlation_group_anomalous_device_count)
        writer.write_int_value("correlationGroupAtRiskDeviceCount", self.correlation_group_at_risk_device_count)
        writer.write_int_value("correlationGroupDeviceCount", self.correlation_group_device_count)
        writer.write_collection_of_object_values("correlationGroupFeatures", self.correlation_group_features)
        writer.write_str_value("correlationGroupId", self.correlation_group_id)
        writer.write_enum_value("correlationGroupPrevalence", self.correlation_group_prevalence)
        writer.write_float_value("correlationGroupPrevalencePercentage", self.correlation_group_prevalence_percentage)
        writer.write_int_value("totalDeviceCount", self.total_device_count)
    

