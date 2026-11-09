from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .attachment_origin import AttachmentOrigin
    from .attachment_scan_result import AttachmentScanResult
    from .case_management_entity import CaseManagementEntity

from .case_management_entity import CaseManagementEntity

@dataclass
class Attachment(CaseManagementEntity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.caseManagement.attachment"
    # The binary content stream for the attachment. Use the Upload content and Download content methods to access it.
    content: Optional[bytes] = None
    # The description of the attachment.
    description: Optional[str] = None
    # The display name of the attachment.
    display_name: Optional[str] = None
    # The file extension of the attachment. The service normalizes the value to include a leading period.
    file_extension: Optional[str] = None
    # The size of the attachment in bytes. The maximum file size is 100 MB.
    file_size: Optional[int] = None
    # The origin reference for the attachment.
    origin: Optional[AttachmentOrigin] = None
    # The scanResult property
    scan_result: Optional[AttachmentScanResult] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Attachment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Attachment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Attachment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .attachment_origin import AttachmentOrigin
        from .attachment_scan_result import AttachmentScanResult
        from .case_management_entity import CaseManagementEntity

        from .attachment_origin import AttachmentOrigin
        from .attachment_scan_result import AttachmentScanResult
        from .case_management_entity import CaseManagementEntity

        fields: dict[str, Callable[[Any], None]] = {
            "content": lambda n : setattr(self, 'content', n.get_bytes_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "fileExtension": lambda n : setattr(self, 'file_extension', n.get_str_value()),
            "fileSize": lambda n : setattr(self, 'file_size', n.get_int_value()),
            "origin": lambda n : setattr(self, 'origin', n.get_object_value(AttachmentOrigin)),
            "scanResult": lambda n : setattr(self, 'scan_result', n.get_enum_value(AttachmentScanResult)),
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
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("fileExtension", self.file_extension)
        writer.write_int_value("fileSize", self.file_size)
        writer.write_object_value("origin", self.origin)
        writer.write_enum_value("scanResult", self.scan_result)
    

