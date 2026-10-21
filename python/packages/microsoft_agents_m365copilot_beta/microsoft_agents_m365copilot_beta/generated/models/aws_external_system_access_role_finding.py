from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .aws_role import AwsRole
    from .finding import Finding
    from .permissions_creep_index import PermissionsCreepIndex

from .finding import Finding

@dataclass
class AwsExternalSystemAccessRoleFinding(Finding, Parsable):
    # The IDs of the accounts that this role is able to access.
    accessible_system_ids: Optional[list[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The permissionsCreepIndex property
    permissions_creep_index: Optional[PermissionsCreepIndex] = None
    # The role property
    role: Optional[AwsRole] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AwsExternalSystemAccessRoleFinding:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AwsExternalSystemAccessRoleFinding
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AwsExternalSystemAccessRoleFinding()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .aws_role import AwsRole
        from .finding import Finding
        from .permissions_creep_index import PermissionsCreepIndex

        from .aws_role import AwsRole
        from .finding import Finding
        from .permissions_creep_index import PermissionsCreepIndex

        fields: dict[str, Callable[[Any], None]] = {
            "accessibleSystemIds": lambda n : setattr(self, 'accessible_system_ids', n.get_collection_of_primitive_values(str)),
            "permissionsCreepIndex": lambda n : setattr(self, 'permissions_creep_index', n.get_object_value(PermissionsCreepIndex)),
            "role": lambda n : setattr(self, 'role', n.get_object_value(AwsRole)),
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
        writer.write_collection_of_primitive_values("accessibleSystemIds", self.accessible_system_ids)
        writer.write_object_value("permissionsCreepIndex", self.permissions_creep_index)
        writer.write_object_value("role", self.role)
    

