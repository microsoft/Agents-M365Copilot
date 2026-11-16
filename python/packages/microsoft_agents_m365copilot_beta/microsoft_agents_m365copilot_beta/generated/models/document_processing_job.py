from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .document_processing_job_status import DocumentProcessingJobStatus
    from .document_processing_job_type import DocumentProcessingJobType
    from .entity import Entity

from .entity import Entity

@dataclass
class DocumentProcessingJob(Entity, Parsable):
    # Date and time of item creation. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    # The document processing job type. The possible values are: file, folder
    job_type: Optional[DocumentProcessingJobType] = None
    # The listItemUniqueId of the file, or folder to process. Use GET driveItem resource operation and read  sharepointIds property to get listItemUniqueId.
    list_item_unique_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The document processing Job status. The possible values are: inProgress, completed, failed, unknownFutureValue.
    status: Optional[DocumentProcessingJobStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DocumentProcessingJob:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DocumentProcessingJob
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DocumentProcessingJob()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .document_processing_job_status import DocumentProcessingJobStatus
        from .document_processing_job_type import DocumentProcessingJobType
        from .entity import Entity

        from .document_processing_job_status import DocumentProcessingJobStatus
        from .document_processing_job_type import DocumentProcessingJobType
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "jobType": lambda n : setattr(self, 'job_type', n.get_enum_value(DocumentProcessingJobType)),
            "listItemUniqueId": lambda n : setattr(self, 'list_item_unique_id', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(DocumentProcessingJobStatus)),
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_enum_value("jobType", self.job_type)
        writer.write_str_value("listItemUniqueId", self.list_item_unique_id)
        writer.write_enum_value("status", self.status)
    

