from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .file_archive_status import FileArchiveStatus
    from .hashes import Hashes

@dataclass
class File(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The archiveStatus property
    archive_status: Optional[FileArchiveStatus] = None
    # Hashes of the file's binary content, if available. Read-only.
    hashes: Optional[Hashes] = None
    # The MIME type for the file. This is determined by logic on the server and might not be the value provided when the file was uploaded. Read-only.
    mime_type: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The processingMetadata property
    processing_metadata: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> File:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: File
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return File()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .file_archive_status import FileArchiveStatus
        from .hashes import Hashes

        from .file_archive_status import FileArchiveStatus
        from .hashes import Hashes

        fields: dict[str, Callable[[Any], None]] = {
            "archiveStatus": lambda n : setattr(self, 'archive_status', n.get_enum_value(FileArchiveStatus)),
            "hashes": lambda n : setattr(self, 'hashes', n.get_object_value(Hashes)),
            "mimeType": lambda n : setattr(self, 'mime_type', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "processingMetadata": lambda n : setattr(self, 'processing_metadata', n.get_bool_value()),
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
        writer.write_enum_value("archiveStatus", self.archive_status)
        writer.write_object_value("hashes", self.hashes)
        writer.write_str_value("mimeType", self.mime_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("processingMetadata", self.processing_metadata)
        writer.write_additional_data_value(self.additional_data)
    

