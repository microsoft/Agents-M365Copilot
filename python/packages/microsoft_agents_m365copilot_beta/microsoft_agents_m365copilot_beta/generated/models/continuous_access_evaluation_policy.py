from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class ContinuousAccessEvaluationPolicy(Entity, Parsable):
    # Continuous access evaluation automatically blocks access to resources and applications in near real time when a user's access is removed or a client IP address changes. Read-only.
    description: Optional[str] = None
    # The value is always Continuous Access Evaluation. Read-only.
    display_name: Optional[str] = None
    # The collection of group identifiers in scope for evaluation. All groups are in scope when the collection is empty. Read-only.
    groups: Optional[list[str]] = None
    # true to indicate whether continuous access evaluation should be performed; otherwise false. Read-only.
    is_enabled: Optional[bool] = None
    # true to indicate that the continuous access evaluation policy settings should be or has been migrated to the conditional access policy.
    migrate: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The collection of user identifiers in scope for evaluation. All users are in scope when the collection is empty. Read-only.
    users: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ContinuousAccessEvaluationPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ContinuousAccessEvaluationPolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ContinuousAccessEvaluationPolicy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "groups": lambda n : setattr(self, 'groups', n.get_collection_of_primitive_values(str)),
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "migrate": lambda n : setattr(self, 'migrate', n.get_bool_value()),
            "users": lambda n : setattr(self, 'users', n.get_collection_of_primitive_values(str)),
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
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_primitive_values("groups", self.groups)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_bool_value("migrate", self.migrate)
        writer.write_collection_of_primitive_values("users", self.users)
    

