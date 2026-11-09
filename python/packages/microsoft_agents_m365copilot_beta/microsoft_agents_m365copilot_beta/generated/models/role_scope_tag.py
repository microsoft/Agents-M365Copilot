from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .role_scope_tag_auto_assignment import RoleScopeTagAutoAssignment

from .entity import Entity

@dataclass
class RoleScopeTag(Entity, Parsable):
    """
    Role Scope Tag
    """
    # The list of assignments for this Role Scope Tag.
    assignments: Optional[list[RoleScopeTagAutoAssignment]] = None
    # Description of the Role Scope Tag.
    description: Optional[str] = None
    # The display or friendly name of the Role Scope Tag.
    display_name: Optional[str] = None
    # Description of the Role Scope Tag. This property is read-only.
    is_built_in: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RoleScopeTag:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RoleScopeTag
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RoleScopeTag()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .role_scope_tag_auto_assignment import RoleScopeTagAutoAssignment

        from .entity import Entity
        from .role_scope_tag_auto_assignment import RoleScopeTagAutoAssignment

        fields: dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(RoleScopeTagAutoAssignment)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isBuiltIn": lambda n : setattr(self, 'is_built_in', n.get_bool_value()),
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
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
    

