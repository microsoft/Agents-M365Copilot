from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .content_applicability_settings import ContentApplicabilitySettings
    from .expedite_settings import ExpediteSettings
    from .monitoring_settings import MonitoringSettings
    from .schedule_settings import ScheduleSettings
    from .user_experience_settings import UserExperienceSettings

@dataclass
class DeploymentSettings(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Settings for governing whether content is applicable to a device.
    content_applicability: Optional[ContentApplicabilitySettings] = None
    # Settings for governing whether updates should be expedited.
    expedite: Optional[ExpediteSettings] = None
    # Settings for governing conditions to monitor and automated actions to take.
    monitoring: Optional[MonitoringSettings] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Settings for governing how and when the content is rolled out.
    schedule: Optional[ScheduleSettings] = None
    # Settings for governing end user update experience.
    user_experience: Optional[UserExperienceSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeploymentSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeploymentSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeploymentSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .content_applicability_settings import ContentApplicabilitySettings
        from .expedite_settings import ExpediteSettings
        from .monitoring_settings import MonitoringSettings
        from .schedule_settings import ScheduleSettings
        from .user_experience_settings import UserExperienceSettings

        from .content_applicability_settings import ContentApplicabilitySettings
        from .expedite_settings import ExpediteSettings
        from .monitoring_settings import MonitoringSettings
        from .schedule_settings import ScheduleSettings
        from .user_experience_settings import UserExperienceSettings

        fields: dict[str, Callable[[Any], None]] = {
            "contentApplicability": lambda n : setattr(self, 'content_applicability', n.get_object_value(ContentApplicabilitySettings)),
            "expedite": lambda n : setattr(self, 'expedite', n.get_object_value(ExpediteSettings)),
            "monitoring": lambda n : setattr(self, 'monitoring', n.get_object_value(MonitoringSettings)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "schedule": lambda n : setattr(self, 'schedule', n.get_object_value(ScheduleSettings)),
            "userExperience": lambda n : setattr(self, 'user_experience', n.get_object_value(UserExperienceSettings)),
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
        writer.write_object_value("contentApplicability", self.content_applicability)
        writer.write_object_value("expedite", self.expedite)
        writer.write_object_value("monitoring", self.monitoring)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("schedule", self.schedule)
        writer.write_object_value("userExperience", self.user_experience)
        writer.write_additional_data_value(self.additional_data)
    

