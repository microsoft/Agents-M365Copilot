from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .share_point_group_identity_mapping import SharePointGroupIdentityMapping
    from .share_point_migration_task import SharePointMigrationTask
    from .share_point_user_identity_mapping import SharePointUserIdentityMapping

from .entity import Entity

@dataclass
class SharePointMigrationsRoot(Entity, Parsable):
    # Collection of group identity mappings for cross-organization migration.
    cross_organization_group_mappings: Optional[list[SharePointGroupIdentityMapping]] = None
    # A collection of sharePointMigrationTask resources that represent cross-organization migration tasks.
    cross_organization_migration_tasks: Optional[list[SharePointMigrationTask]] = None
    # Collection of user identity mappings for cross-organization migration.
    cross_organization_user_mappings: Optional[list[SharePointUserIdentityMapping]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SharePointMigrationsRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SharePointMigrationsRoot
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SharePointMigrationsRoot()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .share_point_group_identity_mapping import SharePointGroupIdentityMapping
        from .share_point_migration_task import SharePointMigrationTask
        from .share_point_user_identity_mapping import SharePointUserIdentityMapping

        from .entity import Entity
        from .share_point_group_identity_mapping import SharePointGroupIdentityMapping
        from .share_point_migration_task import SharePointMigrationTask
        from .share_point_user_identity_mapping import SharePointUserIdentityMapping

        fields: dict[str, Callable[[Any], None]] = {
            "crossOrganizationGroupMappings": lambda n : setattr(self, 'cross_organization_group_mappings', n.get_collection_of_object_values(SharePointGroupIdentityMapping)),
            "crossOrganizationMigrationTasks": lambda n : setattr(self, 'cross_organization_migration_tasks', n.get_collection_of_object_values(SharePointMigrationTask)),
            "crossOrganizationUserMappings": lambda n : setattr(self, 'cross_organization_user_mappings', n.get_collection_of_object_values(SharePointUserIdentityMapping)),
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
        writer.write_collection_of_object_values("crossOrganizationGroupMappings", self.cross_organization_group_mappings)
        writer.write_collection_of_object_values("crossOrganizationMigrationTasks", self.cross_organization_migration_tasks)
        writer.write_collection_of_object_values("crossOrganizationUserMappings", self.cross_organization_user_mappings)
    

