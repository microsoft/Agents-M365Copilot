from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .identity import Identity
    from .share_point_identity_mapping import SharePointIdentityMapping
    from .share_point_identity_mapping_group_migration_data import SharePointIdentityMappingGroupMigrationData
    from .share_point_identity_mapping_group_type import SharePointIdentityMappingGroupType

from .share_point_identity_mapping import SharePointIdentityMapping

@dataclass
class SharePointGroupIdentityMapping(SharePointIdentityMapping, Parsable):
    # The groupType property
    group_type: Optional[SharePointIdentityMappingGroupType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The identity information of the source group in the originating organization. Contains the ID of the source group.
    source_group_identity: Optional[Identity] = None
    # The identity information of the target group in the destination organization. Contains the ID of the target group.
    target_group_identity: Optional[Identity] = None
    # Additional migration-specific data for the target group.
    target_group_migration_data: Optional[SharePointIdentityMappingGroupMigrationData] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SharePointGroupIdentityMapping:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SharePointGroupIdentityMapping
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SharePointGroupIdentityMapping()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .identity import Identity
        from .share_point_identity_mapping import SharePointIdentityMapping
        from .share_point_identity_mapping_group_migration_data import SharePointIdentityMappingGroupMigrationData
        from .share_point_identity_mapping_group_type import SharePointIdentityMappingGroupType

        from .identity import Identity
        from .share_point_identity_mapping import SharePointIdentityMapping
        from .share_point_identity_mapping_group_migration_data import SharePointIdentityMappingGroupMigrationData
        from .share_point_identity_mapping_group_type import SharePointIdentityMappingGroupType

        fields: dict[str, Callable[[Any], None]] = {
            "groupType": lambda n : setattr(self, 'group_type', n.get_enum_value(SharePointIdentityMappingGroupType)),
            "sourceGroupIdentity": lambda n : setattr(self, 'source_group_identity', n.get_object_value(Identity)),
            "targetGroupIdentity": lambda n : setattr(self, 'target_group_identity', n.get_object_value(Identity)),
            "targetGroupMigrationData": lambda n : setattr(self, 'target_group_migration_data', n.get_object_value(SharePointIdentityMappingGroupMigrationData)),
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
        writer.write_enum_value("groupType", self.group_type)
        writer.write_object_value("sourceGroupIdentity", self.source_group_identity)
        writer.write_object_value("targetGroupIdentity", self.target_group_identity)
        writer.write_object_value("targetGroupMigrationData", self.target_group_migration_data)
    

