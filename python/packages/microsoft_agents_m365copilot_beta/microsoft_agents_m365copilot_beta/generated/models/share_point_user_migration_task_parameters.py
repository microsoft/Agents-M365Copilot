from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .share_point_migration_task_parameters import SharePointMigrationTaskParameters
    from .user_identity import UserIdentity

from .share_point_migration_task_parameters import SharePointMigrationTaskParameters

@dataclass
class SharePointUserMigrationTaskParameters(SharePointMigrationTaskParameters, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.sharePointUserMigrationTaskParameters"
    # The source user in the source tenant, including the user object ID and the user principal name.
    source_user_identity: Optional[UserIdentity] = None
    # The target user in the target tenant, including the user object ID and the user principal name.
    target_user_identity: Optional[UserIdentity] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SharePointUserMigrationTaskParameters:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SharePointUserMigrationTaskParameters
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SharePointUserMigrationTaskParameters()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .share_point_migration_task_parameters import SharePointMigrationTaskParameters
        from .user_identity import UserIdentity

        from .share_point_migration_task_parameters import SharePointMigrationTaskParameters
        from .user_identity import UserIdentity

        fields: dict[str, Callable[[Any], None]] = {
            "sourceUserIdentity": lambda n : setattr(self, 'source_user_identity', n.get_object_value(UserIdentity)),
            "targetUserIdentity": lambda n : setattr(self, 'target_user_identity', n.get_object_value(UserIdentity)),
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
    

