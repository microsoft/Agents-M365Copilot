from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .activity_log_base import ActivityLogBase
    from .destination_type import DestinationType
    from .restore_artifact_details import RestoreArtifactDetails
    from .restore_point_tags import RestorePointTags
    from .restore_session_status import RestoreSessionStatus

from .activity_log_base import ActivityLogBase

@dataclass
class RestoreTaskActivityLog(ActivityLogBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.restoreTaskActivityLog"
    # The destinationType property
    destination_type: Optional[DestinationType] = None
    # Contains detailed information about the artifacts being restored, including counts and status of restored items.
    restore_artifact_details: Optional[RestoreArtifactDetails] = None
    # The date and time when the restore task was completed.
    restore_completion_date_time: Optional[datetime.datetime] = None
    # The unique identifier of the restore session associated with this activity log.
    restore_session_id: Optional[str] = None
    # The restoreSessionStatus property
    restore_session_status: Optional[RestoreSessionStatus] = None
    # The tags property
    tags: Optional[RestorePointTags] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RestoreTaskActivityLog:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RestoreTaskActivityLog
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RestoreTaskActivityLog()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .activity_log_base import ActivityLogBase
        from .destination_type import DestinationType
        from .restore_artifact_details import RestoreArtifactDetails
        from .restore_point_tags import RestorePointTags
        from .restore_session_status import RestoreSessionStatus

        from .activity_log_base import ActivityLogBase
        from .destination_type import DestinationType
        from .restore_artifact_details import RestoreArtifactDetails
        from .restore_point_tags import RestorePointTags
        from .restore_session_status import RestoreSessionStatus

        fields: dict[str, Callable[[Any], None]] = {
            "destinationType": lambda n : setattr(self, 'destination_type', n.get_enum_value(DestinationType)),
            "restoreArtifactDetails": lambda n : setattr(self, 'restore_artifact_details', n.get_object_value(RestoreArtifactDetails)),
            "restoreCompletionDateTime": lambda n : setattr(self, 'restore_completion_date_time', n.get_datetime_value()),
            "restoreSessionId": lambda n : setattr(self, 'restore_session_id', n.get_str_value()),
            "restoreSessionStatus": lambda n : setattr(self, 'restore_session_status', n.get_enum_value(RestoreSessionStatus)),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_enum_values(RestorePointTags)),
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
        writer.write_enum_value("destinationType", self.destination_type)
        writer.write_object_value("restoreArtifactDetails", self.restore_artifact_details)
        writer.write_datetime_value("restoreCompletionDateTime", self.restore_completion_date_time)
        writer.write_str_value("restoreSessionId", self.restore_session_id)
        writer.write_enum_value("restoreSessionStatus", self.restore_session_status)
        writer.write_enum_value("tags", self.tags)
    

