from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .evaluation_error_category import EvaluationErrorCategory
    from .evaluation_error_type import EvaluationErrorType

@dataclass
class EvaluationErrorDetail(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The errorCategory property
    error_category: Optional[EvaluationErrorCategory] = None
    # The errorMessage property
    error_message: Optional[str] = None
    # The errorType property
    error_type: Optional[EvaluationErrorType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EvaluationErrorDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EvaluationErrorDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EvaluationErrorDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .evaluation_error_category import EvaluationErrorCategory
        from .evaluation_error_type import EvaluationErrorType

        from .evaluation_error_category import EvaluationErrorCategory
        from .evaluation_error_type import EvaluationErrorType

        fields: dict[str, Callable[[Any], None]] = {
            "errorCategory": lambda n : setattr(self, 'error_category', n.get_enum_value(EvaluationErrorCategory)),
            "errorMessage": lambda n : setattr(self, 'error_message', n.get_str_value()),
            "errorType": lambda n : setattr(self, 'error_type', n.get_enum_value(EvaluationErrorType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_enum_value("errorCategory", self.error_category)
        writer.write_str_value("errorMessage", self.error_message)
        writer.write_enum_value("errorType", self.error_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

