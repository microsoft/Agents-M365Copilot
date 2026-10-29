from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .share_point_identity_mapping import SharePointIdentityMapping
    from .share_point_identity_mapping_user_migration_data import SharePointIdentityMappingUserMigrationData
    from .share_point_identity_mapping_user_type import SharePointIdentityMappingUserType
    from .user_identity import UserIdentity

from .share_point_identity_mapping import SharePointIdentityMapping

@dataclass
class SharePointUserIdentityMapping(SharePointIdentityMapping, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    # The identity information of the source user in the originating organization. Contains the source user's principal name.
    source_user_identity: Optional[UserIdentity] = None
    # The identity information of the target user in the destination organization. Contains the target user's principal name.
    target_user_identity: Optional[UserIdentity] = None
    # Additional migration-specific data for the target user. Contains the email address for the user in the destination organization.
    target_user_migration_data: Optional[SharePointIdentityMappingUserMigrationData] = None
    # The userType property
    user_type: Optional[SharePointIdentityMappingUserType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SharePointUserIdentityMapping:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SharePointUserIdentityMapping
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SharePointUserIdentityMapping()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .share_point_identity_mapping import SharePointIdentityMapping
        from .share_point_identity_mapping_user_migration_data import SharePointIdentityMappingUserMigrationData
        from .share_point_identity_mapping_user_type import SharePointIdentityMappingUserType
        from .user_identity import UserIdentity

        from .share_point_identity_mapping import SharePointIdentityMapping
        from .share_point_identity_mapping_user_migration_data import SharePointIdentityMappingUserMigrationData
        from .share_point_identity_mapping_user_type import SharePointIdentityMappingUserType
        from .user_identity import UserIdentity

        fields: dict[str, Callable[[Any], None]] = {
            "sourceUserIdentity": lambda n : setattr(self, 'source_user_identity', n.get_object_value(UserIdentity)),
            "targetUserIdentity": lambda n : setattr(self, 'target_user_identity', n.get_object_value(UserIdentity)),
            "targetUserMigrationData": lambda n : setattr(self, 'target_user_migration_data', n.get_object_value(SharePointIdentityMappingUserMigrationData)),
            "userType": lambda n : setattr(self, 'user_type', n.get_enum_value(SharePointIdentityMappingUserType)),
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
        writer.write_object_value("sourceUserIdentity", self.source_user_identity)
        writer.write_object_value("targetUserIdentity", self.target_user_identity)
        writer.write_object_value("targetUserMigrationData", self.target_user_migration_data)
        writer.write_enum_value("userType", self.user_type)
    

