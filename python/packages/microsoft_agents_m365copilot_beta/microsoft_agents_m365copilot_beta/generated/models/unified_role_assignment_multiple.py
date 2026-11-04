from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .app_scope import AppScope
    from .directory_object import DirectoryObject
    from .entity import Entity
    from .unified_role_definition import UnifiedRoleDefinition

from .entity import Entity

@dataclass
class UnifiedRoleAssignmentMultiple(Entity, Parsable):
    # Ids of the app specific scopes when the assignment scopes are app specific. The scopes of an assignment determine the set of resources for which the principal has access. Directory scopes are shared scopes stored in the directory that are understood by multiple applications. Use / for tenant-wide scope. App scopes are scopes that are defined and understood by this application only.
    app_scope_ids: Optional[list[str]] = None
    # Read-only collection with details of the app specific scopes when the assignment scopes are app specific. Containment entity. Read-only.
    app_scopes: Optional[list[AppScope]] = None
    # The condition property
    condition: Optional[str] = None
    # Description of the role assignment.
    description: Optional[str] = None
    # Ids of the directory objects that represent the scopes of the assignment. The scopes of an assignment determine the set of resources for which the principals have been granted access. Directory scopes are shared scopes stored in the directory that are understood by multiple applications. App scopes are scopes that are defined and understood by this application only.
    directory_scope_ids: Optional[list[str]] = None
    # Read-only collection that references the directory objects that are scope of the assignment. Provided so that callers can get the directory objects using $expand at the same time as getting the role assignment. Read-only. Supports $expand.
    directory_scopes: Optional[list[DirectoryObject]] = None
    # Name of the role assignment. Required.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Identifiers of the principals to which the assignment is granted. Supports $filter (any operator only).
    principal_ids: Optional[list[str]] = None
    # Read-only collection that references the assigned principals. Provided so that callers can get the principals using $expand at the same time as getting the role assignment. Read-only. Supports $expand.
    principals: Optional[list[DirectoryObject]] = None
    # Specifies the roleDefinition that the assignment is for. Provided so that callers can get the role definition using $expand at the same time as getting the role assignment. Supports $filter (eq operator on id, isBuiltIn, and displayName, and startsWith operator on displayName)  and $expand.
    role_definition: Optional[UnifiedRoleDefinition] = None
    # Identifier of the unifiedRoleDefinition the assignment is for.
    role_definition_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UnifiedRoleAssignmentMultiple:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleAssignmentMultiple
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UnifiedRoleAssignmentMultiple()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .app_scope import AppScope
        from .directory_object import DirectoryObject
        from .entity import Entity
        from .unified_role_definition import UnifiedRoleDefinition

        from .app_scope import AppScope
        from .directory_object import DirectoryObject
        from .entity import Entity
        from .unified_role_definition import UnifiedRoleDefinition

        fields: dict[str, Callable[[Any], None]] = {
            "appScopeIds": lambda n : setattr(self, 'app_scope_ids', n.get_collection_of_primitive_values(str)),
            "appScopes": lambda n : setattr(self, 'app_scopes', n.get_collection_of_object_values(AppScope)),
            "condition": lambda n : setattr(self, 'condition', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "directoryScopeIds": lambda n : setattr(self, 'directory_scope_ids', n.get_collection_of_primitive_values(str)),
            "directoryScopes": lambda n : setattr(self, 'directory_scopes', n.get_collection_of_object_values(DirectoryObject)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "principalIds": lambda n : setattr(self, 'principal_ids', n.get_collection_of_primitive_values(str)),
            "principals": lambda n : setattr(self, 'principals', n.get_collection_of_object_values(DirectoryObject)),
            "roleDefinition": lambda n : setattr(self, 'role_definition', n.get_object_value(UnifiedRoleDefinition)),
            "roleDefinitionId": lambda n : setattr(self, 'role_definition_id', n.get_str_value()),
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
        writer.write_collection_of_primitive_values("appScopeIds", self.app_scope_ids)
        writer.write_collection_of_object_values("appScopes", self.app_scopes)
        writer.write_str_value("condition", self.condition)
        writer.write_str_value("description", self.description)
        writer.write_collection_of_primitive_values("directoryScopeIds", self.directory_scope_ids)
        writer.write_collection_of_object_values("directoryScopes", self.directory_scopes)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_primitive_values("principalIds", self.principal_ids)
        writer.write_collection_of_object_values("principals", self.principals)
        writer.write_object_value("roleDefinition", self.role_definition)
        writer.write_str_value("roleDefinitionId", self.role_definition_id)
    

