from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .public_error import PublicError
    from .share_point_migration_task_parameters import SharePointMigrationTaskParameters
    from .share_point_migration_task_status import SharePointMigrationTaskStatus

from .entity import Entity

@dataclass
class SharePointMigrationTask(Entity, Parsable):
    # The error property
    error: Optional[PublicError] = None
    # Date and time when the sharePointMigrationTask ended, if available. The task might complete successfully or fail, but it ends at that time. Read-only. Only on OneDrive and SharePoint. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    finished_date_time: Optional[datetime.datetime] = None
    # Date and time when the sharePointMigrationTask was last updated or processed, if available. Use this property to find tasks that stopped processing for a long time. Read-only. Optional. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    last_updated_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The parameters property
    parameters: Optional[SharePointMigrationTaskParameters] = None
    # Date and time when the sharePointMigrationTask started, if available. Read-only. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    started_date_time: Optional[datetime.datetime] = None
    # The status property
    status: Optional[SharePointMigrationTaskStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SharePointMigrationTask:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SharePointMigrationTask
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SharePointMigrationTask()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .public_error import PublicError
        from .share_point_migration_task_parameters import SharePointMigrationTaskParameters
        from .share_point_migration_task_status import SharePointMigrationTaskStatus

        from .entity import Entity
        from .public_error import PublicError
        from .share_point_migration_task_parameters import SharePointMigrationTaskParameters
        from .share_point_migration_task_status import SharePointMigrationTaskStatus

        fields: dict[str, Callable[[Any], None]] = {
            "error": lambda n : setattr(self, 'error', n.get_object_value(PublicError)),
            "finishedDateTime": lambda n : setattr(self, 'finished_date_time', n.get_datetime_value()),
            "lastUpdatedDateTime": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "parameters": lambda n : setattr(self, 'parameters', n.get_object_value(SharePointMigrationTaskParameters)),
            "startedDateTime": lambda n : setattr(self, 'started_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(SharePointMigrationTaskStatus)),
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
        writer.write_object_value("error", self.error)
        writer.write_datetime_value("finishedDateTime", self.finished_date_time)
        writer.write_datetime_value("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_object_value("parameters", self.parameters)
        writer.write_datetime_value("startedDateTime", self.started_date_time)
        writer.write_enum_value("status", self.status)
    

