from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .gradual_rollout_settings import GradualRolloutSettings

@dataclass
class ScheduleSettings(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Settings for governing how to rollout content to devices. One of: microsoft.graph.windowsUpdates.dateDrivenRolloutSettings, microsoft.graph.windowsUpdates.durationDrivenRolloutSettings, or microsoft.graph.windowsUpdates.rateDrivenRolloutSettings.
    gradual_rollout: Optional[GradualRolloutSettings] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The date on which devices in the deployment start receiving the update. When not set, the deployment starts as soon as devices are assigned. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    start_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ScheduleSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ScheduleSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ScheduleSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .gradual_rollout_settings import GradualRolloutSettings

        from .gradual_rollout_settings import GradualRolloutSettings

        fields: dict[str, Callable[[Any], None]] = {
            "gradualRollout": lambda n : setattr(self, 'gradual_rollout', n.get_object_value(GradualRolloutSettings)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
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
        writer.write_object_value("gradualRollout", self.gradual_rollout)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_additional_data_value(self.additional_data)
    

