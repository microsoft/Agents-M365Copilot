from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .file_threat_submission import FileThreatSubmission

from .file_threat_submission import FileThreatSubmission

@dataclass
class FileContentThreatSubmission(FileThreatSubmission, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.fileContentThreatSubmission"
    # It specifies the file content in base 64 format.
    file_content: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FileContentThreatSubmission:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FileContentThreatSubmission
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FileContentThreatSubmission()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .file_threat_submission import FileThreatSubmission

        from .file_threat_submission import FileThreatSubmission

        fields: dict[str, Callable[[Any], None]] = {
            "fileContent": lambda n : setattr(self, 'file_content', n.get_str_value()),
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
        writer.write_str_value("fileContent", self.file_content)
    

