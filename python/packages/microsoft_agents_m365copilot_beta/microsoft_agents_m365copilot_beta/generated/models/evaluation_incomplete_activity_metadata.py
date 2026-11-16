from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .error_actions import ErrorActions
    from .evaluation_error_detail import EvaluationErrorDetail
    from .process_content_metadata_base import ProcessContentMetadataBase

from .process_content_metadata_base import ProcessContentMetadataBase

@dataclass
class EvaluationIncompleteActivityMetadata(ProcessContentMetadataBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.evaluationIncompleteActivityMetadata"
    # The errorAction property
    error_action: Optional[ErrorActions] = None
    # The inspectionIncompleteReason property
    inspection_incomplete_reason: Optional[EvaluationErrorDetail] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EvaluationIncompleteActivityMetadata:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EvaluationIncompleteActivityMetadata
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EvaluationIncompleteActivityMetadata()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .error_actions import ErrorActions
        from .evaluation_error_detail import EvaluationErrorDetail
        from .process_content_metadata_base import ProcessContentMetadataBase

        from .error_actions import ErrorActions
        from .evaluation_error_detail import EvaluationErrorDetail
        from .process_content_metadata_base import ProcessContentMetadataBase

        fields: dict[str, Callable[[Any], None]] = {
            "errorAction": lambda n : setattr(self, 'error_action', n.get_collection_of_enum_values(ErrorActions)),
            "inspectionIncompleteReason": lambda n : setattr(self, 'inspection_incomplete_reason', n.get_object_value(EvaluationErrorDetail)),
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
        writer.write_enum_value("errorAction", self.error_action)
        writer.write_object_value("inspectionIncompleteReason", self.inspection_incomplete_reason)
    

