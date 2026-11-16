from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class AuditActivityType(Entity, Parsable):
    # Indicates the activity name or the operation name (for example 'Create User', 'Add member to group'). For a list of activities logged, refer to Microsoft Entra audit log categories and activities. Supports $filter (eq).
    activity: Optional[str] = None
    # Indicates which resource category that's targeted by the activity. For example: UserManagement, GroupManagement, ApplicationManagement, RoleManagement. For a list of categories for activities logged, refer to Microsoft Entra audit log categories and activities. Supports $filter (eq).
    category: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates information on which service initiated the activity. For example: Self-service Password Management, Core Directory, B2C, Invited Users, Microsoft Identity Manager, Privileged Identity Management. Supports $filter (eq).
    service: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuditActivityType:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuditActivityType
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AuditActivityType()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "activity": lambda n : setattr(self, 'activity', n.get_str_value()),
            "category": lambda n : setattr(self, 'category', n.get_str_value()),
            "service": lambda n : setattr(self, 'service', n.get_str_value()),
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
        writer.write_str_value("activity", self.activity)
        writer.write_str_value("category", self.category)
        writer.write_str_value("service", self.service)
    

