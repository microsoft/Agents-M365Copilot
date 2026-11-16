from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class PlannerRosterMember(Entity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    # Additional roles associated with the PlannerRosterMember, which determines permissions of the member in the plannerRoster. Currently there are no available roles to assign, and every member has full control over the contents of the plannerRoster.
    roles: Optional[list[str]] = None
    # Identifier of the tenant the user belongs to. Currently only the users from the same tenant can be added to a plannerRoster.
    tenant_id: Optional[str] = None
    # Identifier of the user.
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlannerRosterMember:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlannerRosterMember
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PlannerRosterMember()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "roles": lambda n : setattr(self, 'roles', n.get_collection_of_primitive_values(str)),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
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
        writer.write_collection_of_primitive_values("roles", self.roles)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_str_value("userId", self.user_id)
    

