from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authorization_system_type_action import AuthorizationSystemTypeAction
    from .entity import Entity

from .entity import Entity

@dataclass
class AuthorizationSystemTypeService(Entity, Parsable):
    # List of actions for the service in an authorization system that is onboarded to Permissions Management.
    actions: Optional[list[AuthorizationSystemTypeAction]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuthorizationSystemTypeService:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuthorizationSystemTypeService
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AuthorizationSystemTypeService()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authorization_system_type_action import AuthorizationSystemTypeAction
        from .entity import Entity

        from .authorization_system_type_action import AuthorizationSystemTypeAction
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "actions": lambda n : setattr(self, 'actions', n.get_collection_of_object_values(AuthorizationSystemTypeAction)),
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
    

