from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .place_execution_result import PlaceExecutionResult
    from .place_operation_progress import PlaceOperationProgress
    from .place_operation_status import PlaceOperationStatus

from .entity import Entity

@dataclass
class PlaceOperation(Entity, Parsable):
    # The detailed result of the operation, including errors and successful places.
    details: Optional[list[PlaceExecutionResult]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The progress of the operation.
    progress: Optional[PlaceOperationProgress] = None
    # The status property
    status: Optional[PlaceOperationStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlaceOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlaceOperation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PlaceOperation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .place_execution_result import PlaceExecutionResult
        from .place_operation_progress import PlaceOperationProgress
        from .place_operation_status import PlaceOperationStatus

        from .entity import Entity
        from .place_execution_result import PlaceExecutionResult
        from .place_operation_progress import PlaceOperationProgress
        from .place_operation_status import PlaceOperationStatus

        fields: dict[str, Callable[[Any], None]] = {
            "details": lambda n : setattr(self, 'details', n.get_collection_of_object_values(PlaceExecutionResult)),
            "progress": lambda n : setattr(self, 'progress', n.get_object_value(PlaceOperationProgress)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(PlaceOperationStatus)),
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
        writer.write_collection_of_object_values("details", self.details)
        writer.write_object_value("progress", self.progress)
        writer.write_enum_value("status", self.status)
    

