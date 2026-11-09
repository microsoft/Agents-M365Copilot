from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .unified_role_permission import UnifiedRolePermission

from .entity import Entity

@dataclass
class DefaultUserRoleOverride(Entity, Parsable):
    # The isDefault property
    is_default: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The rolePermissions property
    role_permissions: Optional[list[UnifiedRolePermission]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DefaultUserRoleOverride:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DefaultUserRoleOverride
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DefaultUserRoleOverride()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .unified_role_permission import UnifiedRolePermission

        from .entity import Entity
        from .unified_role_permission import UnifiedRolePermission

        fields: dict[str, Callable[[Any], None]] = {
            "isDefault": lambda n : setattr(self, 'is_default', n.get_bool_value()),
            "rolePermissions": lambda n : setattr(self, 'role_permissions', n.get_collection_of_object_values(UnifiedRolePermission)),
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
        writer.write_bool_value("isDefault", self.is_default)
        writer.write_collection_of_object_values("rolePermissions", self.role_permissions)
    

