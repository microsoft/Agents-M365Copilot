from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .approval_status import ApprovalStatus
    from .catalog_entry import CatalogEntry

from ..entity import Entity

@dataclass
class PolicyApproval(Entity, Parsable):
    # The content that you can approve for deployment. Read-only.
    catalog_entry: Optional[CatalogEntry] = None
    # The catalog entry ID to approve.
    catalog_entry_id: Optional[str] = None
    # The date and time the policy approval is created. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    # The date and time the policy approval was last modified. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status property
    status: Optional[ApprovalStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PolicyApproval:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PolicyApproval
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PolicyApproval()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .approval_status import ApprovalStatus
        from .catalog_entry import CatalogEntry

        from ..entity import Entity
        from .approval_status import ApprovalStatus
        from .catalog_entry import CatalogEntry

        fields: dict[str, Callable[[Any], None]] = {
            "catalogEntry": lambda n : setattr(self, 'catalog_entry', n.get_object_value(CatalogEntry)),
            "catalogEntryId": lambda n : setattr(self, 'catalog_entry_id', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(ApprovalStatus)),
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
        writer.write_object_value("catalogEntry", self.catalog_entry)
        writer.write_str_value("catalogEntryId", self.catalog_entry_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("status", self.status)
    

