from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .group_identity import GroupIdentity
    from .share_point_migration_task_parameters import SharePointMigrationTaskParameters

from .share_point_migration_task_parameters import SharePointMigrationTaskParameters

@dataclass
class SharePointGroupMigrationTaskParameters(SharePointMigrationTaskParameters, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.sharePointGroupMigrationTaskParameters"
    # The identity of the source group in the source tenant, including its mail nickname.
    source_group_identity: Optional[GroupIdentity] = None
    # The identity of the target group in the target tenant, including its mail nickname.
    target_group_identity: Optional[GroupIdentity] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SharePointGroupMigrationTaskParameters:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SharePointGroupMigrationTaskParameters
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SharePointGroupMigrationTaskParameters()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .group_identity import GroupIdentity
        from .share_point_migration_task_parameters import SharePointMigrationTaskParameters

        from .group_identity import GroupIdentity
        from .share_point_migration_task_parameters import SharePointMigrationTaskParameters

        fields: dict[str, Callable[[Any], None]] = {
            "sourceGroupIdentity": lambda n : setattr(self, 'source_group_identity', n.get_object_value(GroupIdentity)),
            "targetGroupIdentity": lambda n : setattr(self, 'target_group_identity', n.get_object_value(GroupIdentity)),
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
        writer.write_object_value("sourceGroupIdentity", self.source_group_identity)
        writer.write_object_value("targetGroupIdentity", self.target_group_identity)
    

