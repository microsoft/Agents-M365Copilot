from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .agent_info import AgentInfo
    from .agent_run_failure_info import AgentRunFailureInfo
    from .entity import Entity
    from .investigation_identity_set import InvestigationIdentitySet
    from .investigation_message import InvestigationMessage
    from .long_running_operation_status import LongRunningOperationStatus

from .entity import Entity

@dataclass
class AgentRun(Entity, Parsable):
    """
    An agent's contribution to a session. Read this resource to observe the agent's processing status.
    """
    # Embedded description of the agent that performed a run, without an independently addressable catalog.
    agent: Optional[AgentInfo] = None
    # The UTC date and time when the run completed successfully, in ISO 8601 format. Absent otherwise. Read-only.
    completed_date_time: Optional[datetime.datetime] = None
    # The UTC date and time when the resource was created, in ISO 8601 format. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    # The elapsed time from creation to successful completion, in milliseconds. Absent otherwise. Read-only.
    duration_in_milliseconds: Optional[int] = None
    # The run-level failure details, when available. Read-only.
    failure_info: Optional[AgentRunFailureInfo] = None
    # The initiating principals recorded by the service, when available. Read-only. This property doesn't select an execution identity.
    initiated_by: Optional[InvestigationIdentitySet] = None
    # The UTC date and time when the resource was last updated, in ISO 8601 format. Read-only.
    last_modified_date_time: Optional[datetime.datetime] = None
    # Read-only investigation messages contained by this run; id maps backend messageId. Supports collection and keyed reads. Message creation is not supported. Collection overflow requires an @odata.nextLink preserving tenant, caller, parent and query context; this schema requirement does not attest runtime implementation.
    messages: Optional[list[InvestigationMessage]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The UTC start timestamp, in ISO 8601 format. Currently reflects creation time, not a distinct execution-start measurement. Read-only.
    started_date_time: Optional[datetime.datetime] = None
    # The status property
    status: Optional[LongRunningOperationStatus] = None
    # Additional processing detail, including pendingInput or canceled, when the status alone doesn't describe the source lifecycle. Read-only. Doesn't support $filter.
    status_detail: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AgentRun:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AgentRun
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AgentRun()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .agent_info import AgentInfo
        from .agent_run_failure_info import AgentRunFailureInfo
        from .entity import Entity
        from .investigation_identity_set import InvestigationIdentitySet
        from .investigation_message import InvestigationMessage
        from .long_running_operation_status import LongRunningOperationStatus

        from .agent_info import AgentInfo
        from .agent_run_failure_info import AgentRunFailureInfo
        from .entity import Entity
        from .investigation_identity_set import InvestigationIdentitySet
        from .investigation_message import InvestigationMessage
        from .long_running_operation_status import LongRunningOperationStatus

        fields: dict[str, Callable[[Any], None]] = {
            "agent": lambda n : setattr(self, 'agent', n.get_object_value(AgentInfo)),
            "completedDateTime": lambda n : setattr(self, 'completed_date_time', n.get_datetime_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "durationInMilliseconds": lambda n : setattr(self, 'duration_in_milliseconds', n.get_int_value()),
            "failureInfo": lambda n : setattr(self, 'failure_info', n.get_object_value(AgentRunFailureInfo)),
            "initiatedBy": lambda n : setattr(self, 'initiated_by', n.get_object_value(InvestigationIdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "messages": lambda n : setattr(self, 'messages', n.get_collection_of_object_values(InvestigationMessage)),
            "startedDateTime": lambda n : setattr(self, 'started_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(LongRunningOperationStatus)),
            "statusDetail": lambda n : setattr(self, 'status_detail', n.get_str_value()),
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
        writer.write_object_value("agent", self.agent)
        writer.write_collection_of_object_values("messages", self.messages)
        writer.write_enum_value("status", self.status)
    

