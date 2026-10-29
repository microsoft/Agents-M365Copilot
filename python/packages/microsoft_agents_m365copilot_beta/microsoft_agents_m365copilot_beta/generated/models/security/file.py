from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .ediscovery_file import EdiscoveryFile
    from .file_processing_status import FileProcessingStatus
    from .source_type import SourceType
    from .string_value_dictionary import StringValueDictionary

from ..entity import Entity

@dataclass
class File(Entity, Parsable):
    # The content property
    content: Optional[bytes] = None
    # The dateTime property
    date_time: Optional[datetime.datetime] = None
    # The extension property
    extension: Optional[str] = None
    # The extractedTextContent property
    extracted_text_content: Optional[bytes] = None
    # The mediaType property
    media_type: Optional[str] = None
    # The name property
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The otherProperties property
    other_properties: Optional[StringValueDictionary] = None
    # The processingStatus property
    processing_status: Optional[FileProcessingStatus] = None
    # The senderOrAuthors property
    sender_or_authors: Optional[list[str]] = None
    # The size property
    size: Optional[int] = None
    # The sourceType property
    source_type: Optional[SourceType] = None
    # The subjectTitle property
    subject_title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> File:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: File
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryFile".casefold():
            from .ediscovery_file import EdiscoveryFile

            return EdiscoveryFile()
        return File()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .ediscovery_file import EdiscoveryFile
        from .file_processing_status import FileProcessingStatus
        from .source_type import SourceType
        from .string_value_dictionary import StringValueDictionary

        from ..entity import Entity
        from .ediscovery_file import EdiscoveryFile
        from .file_processing_status import FileProcessingStatus
        from .source_type import SourceType
        from .string_value_dictionary import StringValueDictionary

        fields: dict[str, Callable[[Any], None]] = {
            "content": lambda n : setattr(self, 'content', n.get_bytes_value()),
            "dateTime": lambda n : setattr(self, 'date_time', n.get_datetime_value()),
            "extension": lambda n : setattr(self, 'extension', n.get_str_value()),
            "extractedTextContent": lambda n : setattr(self, 'extracted_text_content', n.get_bytes_value()),
            "mediaType": lambda n : setattr(self, 'media_type', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "otherProperties": lambda n : setattr(self, 'other_properties', n.get_object_value(StringValueDictionary)),
            "processingStatus": lambda n : setattr(self, 'processing_status', n.get_enum_value(FileProcessingStatus)),
            "senderOrAuthors": lambda n : setattr(self, 'sender_or_authors', n.get_collection_of_primitive_values(str)),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
            "sourceType": lambda n : setattr(self, 'source_type', n.get_collection_of_enum_values(SourceType)),
            "subjectTitle": lambda n : setattr(self, 'subject_title', n.get_str_value()),
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
        writer.write_bytes_value("content", self.content)
        writer.write_datetime_value("dateTime", self.date_time)
        writer.write_str_value("extension", self.extension)
        writer.write_bytes_value("extractedTextContent", self.extracted_text_content)
        writer.write_str_value("mediaType", self.media_type)
        writer.write_str_value("name", self.name)
        writer.write_object_value("otherProperties", self.other_properties)
        writer.write_enum_value("processingStatus", self.processing_status)
        writer.write_collection_of_primitive_values("senderOrAuthors", self.sender_or_authors)
        writer.write_int_value("size", self.size)
        writer.write_enum_value("sourceType", self.source_type)
        writer.write_str_value("subjectTitle", self.subject_title)
    

