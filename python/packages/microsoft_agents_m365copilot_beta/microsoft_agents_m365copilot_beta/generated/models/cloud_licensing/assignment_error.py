from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from ..directory_object import DirectoryObject
    from ..entity import Entity
    from .usage_right import UsageRight

from ..entity import Entity

@dataclass
class AssignmentError(Entity, Parsable):
    # The assignedTo property
    assigned_to: Optional[DirectoryObject] = None
    # The error code associated with the assignment synchronization failure.
    code: Optional[str] = None
    # The error message associated with the assignment synchronization failure.
    message: Optional[str] = None
    # The date and time at which the error most recently occurred. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    occurrence_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Unique identifier (GUID) for the service SKU that is equal to the skuId property on the related subscribedSku object. Read-only. Supports $filter.
    sku_id: Optional[UUID] = None
    # The affected usageRight, if one exists. Read-only.
    usage_right: Optional[UsageRight] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AssignmentError:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AssignmentError
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AssignmentError()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..directory_object import DirectoryObject
        from ..entity import Entity
        from .usage_right import UsageRight

        from ..directory_object import DirectoryObject
        from ..entity import Entity
        from .usage_right import UsageRight

        fields: dict[str, Callable[[Any], None]] = {
            "assignedTo": lambda n : setattr(self, 'assigned_to', n.get_object_value(DirectoryObject)),
            "code": lambda n : setattr(self, 'code', n.get_str_value()),
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "occurrenceDateTime": lambda n : setattr(self, 'occurrence_date_time', n.get_datetime_value()),
            "skuId": lambda n : setattr(self, 'sku_id', n.get_uuid_value()),
            "usageRight": lambda n : setattr(self, 'usage_right', n.get_object_value(UsageRight)),
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
        writer.write_object_value("assignedTo", self.assigned_to)
        writer.write_str_value("code", self.code)
        writer.write_str_value("message", self.message)
        writer.write_datetime_value("occurrenceDateTime", self.occurrence_date_time)
        writer.write_uuid_value("skuId", self.sku_id)
        writer.write_object_value("usageRight", self.usage_right)
    

