from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .email import Email
    from .managed_tenant_alert import ManagedTenantAlert

from ..entity import Entity

@dataclass
class ManagedTenantEmailNotification(Entity, Parsable):
    # The alert property
    alert: Optional[ManagedTenantAlert] = None
    # The createdByUserId property
    created_by_user_id: Optional[str] = None
    # The createdDateTime property
    created_date_time: Optional[datetime.datetime] = None
    # The emailAddresses property
    email_addresses: Optional[list[Email]] = None
    # The emailBody property
    email_body: Optional[str] = None
    # The lastActionByUserId property
    last_action_by_user_id: Optional[str] = None
    # The lastActionDateTime property
    last_action_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The subject property
    subject: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ManagedTenantEmailNotification:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManagedTenantEmailNotification
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ManagedTenantEmailNotification()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .email import Email
        from .managed_tenant_alert import ManagedTenantAlert

        from ..entity import Entity
        from .email import Email
        from .managed_tenant_alert import ManagedTenantAlert

        fields: dict[str, Callable[[Any], None]] = {
            "alert": lambda n : setattr(self, 'alert', n.get_object_value(ManagedTenantAlert)),
            "createdByUserId": lambda n : setattr(self, 'created_by_user_id', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "emailAddresses": lambda n : setattr(self, 'email_addresses', n.get_collection_of_object_values(Email)),
            "emailBody": lambda n : setattr(self, 'email_body', n.get_str_value()),
            "lastActionByUserId": lambda n : setattr(self, 'last_action_by_user_id', n.get_str_value()),
            "lastActionDateTime": lambda n : setattr(self, 'last_action_date_time', n.get_datetime_value()),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
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
        writer.write_collection_of_object_values("emailAddresses", self.email_addresses)
        writer.write_str_value("emailBody", self.email_body)
        writer.write_str_value("lastActionByUserId", self.last_action_by_user_id)
        writer.write_datetime_value("lastActionDateTime", self.last_action_date_time)
        writer.write_str_value("subject", self.subject)
    

