from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .workbook_content import WorkbookContent

from ..entity import Entity

@dataclass
class Workbook(Entity, Parsable):
    """
    A tenant-scoped Microsoft Security workbook containing a display name and arbitrary JSON content.
    """
    # The workbook's JSON document. Required when creating or replacing a workbook. Supply a JSON object, not a JSON-encoded string. Replaced as a whole on update. Omitted from collection responses by default; use $select to include it.
    content: Optional[WorkbookContent] = None
    # The date and time when the workbook was created. Set by the service and preserved on update. Read-only.
    created_at_date_time: Optional[datetime.datetime] = None
    # The user principal name recorded when the workbook was created. Set by the service and preserved on update. Read-only.
    created_by_upn: Optional[str] = None
    # The opaque concurrency token derived from the workbook's storage ETag. Set by the service. Read-only. For conditional updates, use the value returned in the HTTP ETag response header.
    etag: Optional[str] = None
    # The user principal name recorded for the most recent update. Set by the service. Read-only.
    last_updated_by_upn: Optional[str] = None
    # The display name of the workbook. Required when creating or replacing a workbook. Maximum length is 256 characters.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The date and time of the most recent update. Set by the service. Read-only.
    updated_at_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Workbook:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Workbook
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Workbook()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .workbook_content import WorkbookContent

        from ..entity import Entity
        from .workbook_content import WorkbookContent

        fields: dict[str, Callable[[Any], None]] = {
            "content": lambda n : setattr(self, 'content', n.get_object_value(WorkbookContent)),
            "createdAtDateTime": lambda n : setattr(self, 'created_at_date_time', n.get_datetime_value()),
            "createdByUpn": lambda n : setattr(self, 'created_by_upn', n.get_str_value()),
            "etag": lambda n : setattr(self, 'etag', n.get_str_value()),
            "lastUpdatedByUpn": lambda n : setattr(self, 'last_updated_by_upn', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "updatedAtDateTime": lambda n : setattr(self, 'updated_at_date_time', n.get_datetime_value()),
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
        writer.write_object_value("content", self.content)
        writer.write_str_value("name", self.name)
    

