from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..long_running_operation import LongRunningOperation
    from ..public_error import PublicError
    from .file_validate_operation import FileValidateOperation

from ..long_running_operation import LongRunningOperation

@dataclass
class ValidateOperation(LongRunningOperation, Parsable):
    """
    The status of a long-running operation.
    """
    # Set of errors discovered through validation.
    errors: Optional[list[PublicError]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Set of warnings discovered through validation.
    warnings: Optional[list[PublicError]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ValidateOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ValidateOperation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.fileValidateOperation".casefold():
            from .file_validate_operation import FileValidateOperation

            return FileValidateOperation()
        return ValidateOperation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..long_running_operation import LongRunningOperation
        from ..public_error import PublicError
        from .file_validate_operation import FileValidateOperation

        from ..long_running_operation import LongRunningOperation
        from ..public_error import PublicError
        from .file_validate_operation import FileValidateOperation

        fields: dict[str, Callable[[Any], None]] = {
            "errors": lambda n : setattr(self, 'errors', n.get_collection_of_object_values(PublicError)),
            "warnings": lambda n : setattr(self, 'warnings', n.get_collection_of_object_values(PublicError)),
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
    

