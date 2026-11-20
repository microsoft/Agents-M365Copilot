from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .privileged_role import PrivilegedRole

from .entity import Entity

@dataclass
class PrivilegedRoleAssignment(Entity, Parsable):
    # The expirationDateTime property
    expiration_date_time: Optional[datetime.datetime] = None
    # The isElevated property
    is_elevated: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The resultMessage property
    result_message: Optional[str] = None
    # The roleId property
    role_id: Optional[str] = None
    # The roleInfo property
    role_info: Optional[PrivilegedRole] = None
    # The userId property
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PrivilegedRoleAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PrivilegedRoleAssignment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PrivilegedRoleAssignment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .privileged_role import PrivilegedRole

        from .entity import Entity
        from .privileged_role import PrivilegedRole

        fields: dict[str, Callable[[Any], None]] = {
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "isElevated": lambda n : setattr(self, 'is_elevated', n.get_bool_value()),
            "resultMessage": lambda n : setattr(self, 'result_message', n.get_str_value()),
            "roleId": lambda n : setattr(self, 'role_id', n.get_str_value()),
            "roleInfo": lambda n : setattr(self, 'role_info', n.get_object_value(PrivilegedRole)),
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
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_bool_value("isElevated", self.is_elevated)
        writer.write_str_value("resultMessage", self.result_message)
        writer.write_str_value("roleId", self.role_id)
        writer.write_object_value("roleInfo", self.role_info)
        writer.write_str_value("userId", self.user_id)
    

