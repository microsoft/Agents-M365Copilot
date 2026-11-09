from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .privileged_role_assignment import PrivilegedRoleAssignment
    from .privileged_role_settings import PrivilegedRoleSettings
    from .privileged_role_summary import PrivilegedRoleSummary

from .entity import Entity

@dataclass
class PrivilegedRole(Entity, Parsable):
    # The assignments property
    assignments: Optional[list[PrivilegedRoleAssignment]] = None
    # The name property
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The settings property
    settings: Optional[PrivilegedRoleSettings] = None
    # The summary property
    summary: Optional[PrivilegedRoleSummary] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PrivilegedRole:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PrivilegedRole
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PrivilegedRole()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .privileged_role_assignment import PrivilegedRoleAssignment
        from .privileged_role_settings import PrivilegedRoleSettings
        from .privileged_role_summary import PrivilegedRoleSummary

        from .entity import Entity
        from .privileged_role_assignment import PrivilegedRoleAssignment
        from .privileged_role_settings import PrivilegedRoleSettings
        from .privileged_role_summary import PrivilegedRoleSummary

        fields: dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(PrivilegedRoleAssignment)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(PrivilegedRoleSettings)),
            "summary": lambda n : setattr(self, 'summary', n.get_object_value(PrivilegedRoleSummary)),
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
        writer.write_str_value("name", self.name)
        writer.write_object_value("settings", self.settings)
        writer.write_object_value("summary", self.summary)
    

