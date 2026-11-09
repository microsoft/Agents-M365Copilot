from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...entity import Entity
    from .evaluation_result import EvaluationResult
    from .evaluation_state import EvaluationState

from ...entity import Entity

@dataclass
class Evaluation(Entity, Parsable):
    # Evaluation completion time.
    completed_date_time: Optional[datetime.datetime] = None
    # Evaluation created time.
    created_date_time: Optional[datetime.datetime] = None
    # Evaluation execution count.
    execution_count: Optional[int] = None
    # Evaluation cancellation status.
    is_cancelled: Optional[bool] = None
    # Evaluation modified time.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Evaluation results collection.
    result: Optional[EvaluationResult] = None
    # Evaluation Run start time.
    run_start_date_time: Optional[datetime.datetime] = None
    # The state property
    state: Optional[EvaluationState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Evaluation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Evaluation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Evaluation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ...entity import Entity
        from .evaluation_result import EvaluationResult
        from .evaluation_state import EvaluationState

        from ...entity import Entity
        from .evaluation_result import EvaluationResult
        from .evaluation_state import EvaluationState

        fields: dict[str, Callable[[Any], None]] = {
            "completedDateTime": lambda n : setattr(self, 'completed_date_time', n.get_datetime_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "executionCount": lambda n : setattr(self, 'execution_count', n.get_int_value()),
            "isCancelled": lambda n : setattr(self, 'is_cancelled', n.get_bool_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "result": lambda n : setattr(self, 'result', n.get_object_value(EvaluationResult)),
            "runStartDateTime": lambda n : setattr(self, 'run_start_date_time', n.get_datetime_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(EvaluationState)),
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
        writer.write_datetime_value("completedDateTime", self.completed_date_time)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_int_value("executionCount", self.execution_count)
        writer.write_bool_value("isCancelled", self.is_cancelled)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_object_value("result", self.result)
        writer.write_datetime_value("runStartDateTime", self.run_start_date_time)
        writer.write_enum_value("state", self.state)
    

