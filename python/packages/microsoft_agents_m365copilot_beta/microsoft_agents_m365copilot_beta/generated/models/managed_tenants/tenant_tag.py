from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .tenant_info import TenantInfo

from ..entity import Entity

@dataclass
class TenantTag(Entity, Parsable):
    # The identifier for the account that created the tenant tag. Required. Read-only.
    created_by_user_id: Optional[str] = None
    # The date and time when the tenant tag was created. Required. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    # The date and time when the tenant tag was deleted. Required. Read-only.
    deleted_date_time: Optional[datetime.datetime] = None
    # The description for the tenant tag. Optional. Read-only.
    description: Optional[str] = None
    # The display name for the tenant tag. Required. Read-only.
    display_name: Optional[str] = None
    # The identifier for the account that lasted on the tenant tag. Optional. Read-only.
    last_action_by_user_id: Optional[str] = None
    # The date and time the last action was performed against the tenant tag. Optional. Read-only.
    last_action_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The collection of managed tenants associated with the tenant tag. Optional.
    tenants: Optional[list[TenantInfo]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TenantTag:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TenantTag
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TenantTag()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .tenant_info import TenantInfo

        from ..entity import Entity
        from .tenant_info import TenantInfo

        fields: dict[str, Callable[[Any], None]] = {
            "createdByUserId": lambda n : setattr(self, 'created_by_user_id', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "deletedDateTime": lambda n : setattr(self, 'deleted_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastActionByUserId": lambda n : setattr(self, 'last_action_by_user_id', n.get_str_value()),
            "lastActionDateTime": lambda n : setattr(self, 'last_action_date_time', n.get_datetime_value()),
            "tenants": lambda n : setattr(self, 'tenants', n.get_collection_of_object_values(TenantInfo)),
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
        writer.write_str_value("createdByUserId", self.created_by_user_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_datetime_value("deletedDateTime", self.deleted_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("lastActionByUserId", self.last_action_by_user_id)
        writer.write_datetime_value("lastActionDateTime", self.last_action_date_time)
        writer.write_collection_of_object_values("tenants", self.tenants)
    

