from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authorization_system_resource import AuthorizationSystemResource
    from .authorization_system_type_action import AuthorizationSystemTypeAction
    from .entity import Entity

from .entity import Entity

@dataclass
class PrivilegeEscalation(Entity, Parsable):
    # The list of actions that the identity could perform.
    actions: Optional[list[AuthorizationSystemTypeAction]] = None
    # A detailed description of the privilege escalation.
    description: Optional[str] = None
    # The name of the policy that defines the escalation
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The list of resources that the identity could perform actions on.
    resources: Optional[list[AuthorizationSystemResource]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PrivilegeEscalation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PrivilegeEscalation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PrivilegeEscalation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authorization_system_resource import AuthorizationSystemResource
        from .authorization_system_type_action import AuthorizationSystemTypeAction
        from .entity import Entity

        from .authorization_system_resource import AuthorizationSystemResource
        from .authorization_system_type_action import AuthorizationSystemTypeAction
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "actions": lambda n : setattr(self, 'actions', n.get_collection_of_object_values(AuthorizationSystemTypeAction)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "resources": lambda n : setattr(self, 'resources', n.get_collection_of_object_values(AuthorizationSystemResource)),
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
        writer.write_collection_of_object_values("actions", self.actions)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("resources", self.resources)
    

