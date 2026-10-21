from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class UserPasswordResetsAndChangesSummary(Entity, Parsable):
    # The aggregated day for which the summary applies to. This property will always represent the entire day. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    aggregated_date_time: Optional[datetime.datetime] = None
    # The number of self-service password changes that occurred during this window.
    change_password_self_service_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The number of admin-triggered password resets that occurred during this window.
    password_resets_by_admin_count: Optional[int] = None
    # The number of self-service password resets that occurred during this window.
    password_resets_self_service_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserPasswordResetsAndChangesSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserPasswordResetsAndChangesSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserPasswordResetsAndChangesSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "aggregatedDateTime": lambda n : setattr(self, 'aggregated_date_time', n.get_datetime_value()),
            "changePasswordSelfServiceCount": lambda n : setattr(self, 'change_password_self_service_count', n.get_int_value()),
            "passwordResetsByAdminCount": lambda n : setattr(self, 'password_resets_by_admin_count', n.get_int_value()),
            "passwordResetsSelfServiceCount": lambda n : setattr(self, 'password_resets_self_service_count', n.get_int_value()),
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
        writer.write_datetime_value("aggregatedDateTime", self.aggregated_date_time)
        writer.write_int_value("changePasswordSelfServiceCount", self.change_password_self_service_count)
        writer.write_int_value("passwordResetsByAdminCount", self.password_resets_by_admin_count)
        writer.write_int_value("passwordResetsSelfServiceCount", self.password_resets_self_service_count)
    

