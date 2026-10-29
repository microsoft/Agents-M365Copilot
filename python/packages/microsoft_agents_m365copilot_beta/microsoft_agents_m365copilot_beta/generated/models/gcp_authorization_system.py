from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authorization_system import AuthorizationSystem
    from .authorization_system_type_service import AuthorizationSystemTypeService
    from .gcp_associated_identities import GcpAssociatedIdentities
    from .gcp_authorization_system_resource import GcpAuthorizationSystemResource
    from .gcp_authorization_system_type_action import GcpAuthorizationSystemTypeAction
    from .gcp_role import GcpRole

from .authorization_system import AuthorizationSystem

@dataclass
class GcpAuthorizationSystem(AuthorizationSystem, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.gcpAuthorizationSystem"
    # List of actions for service in authorization system.
    actions: Optional[list[GcpAuthorizationSystemTypeAction]] = None
    # Identities in the authorization system.
    associated_identities: Optional[GcpAssociatedIdentities] = None
    # Resources associated with the authorization system type.
    resources: Optional[list[GcpAuthorizationSystemResource]] = None
    # Roles associated with the authorization system type.
    roles: Optional[list[GcpRole]] = None
    # Services associated with the authorization system type.
    services: Optional[list[AuthorizationSystemTypeService]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GcpAuthorizationSystem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GcpAuthorizationSystem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GcpAuthorizationSystem()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authorization_system import AuthorizationSystem
        from .authorization_system_type_service import AuthorizationSystemTypeService
        from .gcp_associated_identities import GcpAssociatedIdentities
        from .gcp_authorization_system_resource import GcpAuthorizationSystemResource
        from .gcp_authorization_system_type_action import GcpAuthorizationSystemTypeAction
        from .gcp_role import GcpRole

        from .authorization_system import AuthorizationSystem
        from .authorization_system_type_service import AuthorizationSystemTypeService
        from .gcp_associated_identities import GcpAssociatedIdentities
        from .gcp_authorization_system_resource import GcpAuthorizationSystemResource
        from .gcp_authorization_system_type_action import GcpAuthorizationSystemTypeAction
        from .gcp_role import GcpRole

        fields: dict[str, Callable[[Any], None]] = {
            "actions": lambda n : setattr(self, 'actions', n.get_collection_of_object_values(GcpAuthorizationSystemTypeAction)),
            "associatedIdentities": lambda n : setattr(self, 'associated_identities', n.get_object_value(GcpAssociatedIdentities)),
            "resources": lambda n : setattr(self, 'resources', n.get_collection_of_object_values(GcpAuthorizationSystemResource)),
            "roles": lambda n : setattr(self, 'roles', n.get_collection_of_object_values(GcpRole)),
            "services": lambda n : setattr(self, 'services', n.get_collection_of_object_values(AuthorizationSystemTypeService)),
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
        writer.write_object_value("associatedIdentities", self.associated_identities)
        writer.write_collection_of_object_values("resources", self.resources)
        writer.write_collection_of_object_values("roles", self.roles)
        writer.write_collection_of_object_values("services", self.services)
    

