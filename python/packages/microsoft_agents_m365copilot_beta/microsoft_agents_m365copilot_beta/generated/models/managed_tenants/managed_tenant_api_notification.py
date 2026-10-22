from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .managed_tenant_alert import ManagedTenantAlert

from ..entity import Entity

@dataclass
class ManagedTenantApiNotification(Entity, Parsable):
    # The alert property
    alert: Optional[ManagedTenantAlert] = None
    # The createdByUserId property
    created_by_user_id: Optional[str] = None
    # The createdDateTime property
    created_date_time: Optional[datetime.datetime] = None
    # The isAcknowledged property
    is_acknowledged: Optional[bool] = None
    # The lastActionByUserId property
    last_action_by_user_id: Optional[str] = None
    # The lastActionDateTime property
    last_action_date_time: Optional[datetime.datetime] = None
    # The message property
    message: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The title property
    title: Optional[str] = None
    # The userId property
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ManagedTenantApiNotification:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManagedTenantApiNotification
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ManagedTenantApiNotification()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .managed_tenant_alert import ManagedTenantAlert

        from ..entity import Entity
        from .managed_tenant_alert import ManagedTenantAlert

        fields: dict[str, Callable[[Any], None]] = {
            "alert": lambda n : setattr(self, 'alert', n.get_object_value(ManagedTenantAlert)),
            "createdByUserId": lambda n : setattr(self, 'created_by_user_id', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "isAcknowledged": lambda n : setattr(self, 'is_acknowledged', n.get_bool_value()),
            "lastActionByUserId": lambda n : setattr(self, 'last_action_by_user_id', n.get_str_value()),
            "lastActionDateTime": lambda n : setattr(self, 'last_action_date_time', n.get_datetime_value()),
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
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
        writer.write_object_value("alert", self.alert)
        writer.write_str_value("createdByUserId", self.created_by_user_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_bool_value("isAcknowledged", self.is_acknowledged)
        writer.write_str_value("lastActionByUserId", self.last_action_by_user_id)
        writer.write_datetime_value("lastActionDateTime", self.last_action_date_time)
        writer.write_str_value("message", self.message)
        writer.write_str_value("title", self.title)
        writer.write_str_value("userId", self.user_id)
    

