from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .incident import Incident
    from .incident_task_action_status import IncidentTaskActionStatus
    from .incident_task_action_type import IncidentTaskActionType
    from .incident_task_response_action import IncidentTaskResponseAction
    from .incident_task_source import IncidentTaskSource
    from .incident_task_status import IncidentTaskStatus

from ..entity import Entity

@dataclass
class IncidentTask(Entity, Parsable):
    # The actionStatus property
    action_status: Optional[IncidentTaskActionStatus] = None
    # The actionType property
    action_type: Optional[IncidentTaskActionType] = None
    # Name of the entity that created the task. Read-only.
    created_by_display_name: Optional[str] = None
    # Creation time of the task. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    # Description of the remediation action.
    description: Optional[str] = None
    # Title of the task.
    display_name: Optional[str] = None
    # Required. The incident that contains this task. Must contain a valid incident ID.
    incident: Optional[Incident] = None
    # Name of the entity that last updated the task. Read-only.
    last_modified_by_display_name: Optional[str] = None
    # Last update time of the task. Read-only.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The reponse action.
    response_action: Optional[IncidentTaskResponseAction] = None
    # The source property
    source: Optional[IncidentTaskSource] = None
    # The status property
    status: Optional[IncidentTaskStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IncidentTask:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IncidentTask
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IncidentTask()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .incident import Incident
        from .incident_task_action_status import IncidentTaskActionStatus
        from .incident_task_action_type import IncidentTaskActionType
        from .incident_task_response_action import IncidentTaskResponseAction
        from .incident_task_source import IncidentTaskSource
        from .incident_task_status import IncidentTaskStatus

        from ..entity import Entity
        from .incident import Incident
        from .incident_task_action_status import IncidentTaskActionStatus
        from .incident_task_action_type import IncidentTaskActionType
        from .incident_task_response_action import IncidentTaskResponseAction
        from .incident_task_source import IncidentTaskSource
        from .incident_task_status import IncidentTaskStatus

        fields: dict[str, Callable[[Any], None]] = {
            "actionStatus": lambda n : setattr(self, 'action_status', n.get_enum_value(IncidentTaskActionStatus)),
            "actionType": lambda n : setattr(self, 'action_type', n.get_enum_value(IncidentTaskActionType)),
            "createdByDisplayName": lambda n : setattr(self, 'created_by_display_name', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "incident": lambda n : setattr(self, 'incident', n.get_object_value(Incident)),
            "lastModifiedByDisplayName": lambda n : setattr(self, 'last_modified_by_display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "responseAction": lambda n : setattr(self, 'response_action', n.get_object_value(IncidentTaskResponseAction)),
            "source": lambda n : setattr(self, 'source', n.get_enum_value(IncidentTaskSource)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(IncidentTaskStatus)),
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
        writer.write_enum_value("actionStatus", self.action_status)
        writer.write_enum_value("actionType", self.action_type)
        writer.write_str_value("createdByDisplayName", self.created_by_display_name)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("incident", self.incident)
        writer.write_str_value("lastModifiedByDisplayName", self.last_modified_by_display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_object_value("responseAction", self.response_action)
        writer.write_enum_value("source", self.source)
        writer.write_enum_value("status", self.status)
    

