from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .approval import Approval
    from .entity import Entity
    from .permissions_request_change import PermissionsRequestChange
    from .scheduled_permissions_request import ScheduledPermissionsRequest

from .entity import Entity

@dataclass
class PermissionsManagement(Entity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents a change event of the scheduledPermissionsRequest entity.
    permissions_request_changes: Optional[list[PermissionsRequestChange]] = None
    # The scheduledPermissionsApprovals property
    scheduled_permissions_approvals: Optional[list[Approval]] = None
    # Represents a permissions request that Permissions Management uses to manage permissions for an identity on resources in the authorization system. This request can be granted, rejected or canceled by identities in Permissions Management.
    scheduled_permissions_requests: Optional[list[ScheduledPermissionsRequest]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PermissionsManagement:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PermissionsManagement
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PermissionsManagement()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .approval import Approval
        from .entity import Entity
        from .permissions_request_change import PermissionsRequestChange
        from .scheduled_permissions_request import ScheduledPermissionsRequest

        from .approval import Approval
        from .entity import Entity
        from .permissions_request_change import PermissionsRequestChange
        from .scheduled_permissions_request import ScheduledPermissionsRequest

        fields: dict[str, Callable[[Any], None]] = {
            "permissionsRequestChanges": lambda n : setattr(self, 'permissions_request_changes', n.get_collection_of_object_values(PermissionsRequestChange)),
            "scheduledPermissionsApprovals": lambda n : setattr(self, 'scheduled_permissions_approvals', n.get_collection_of_object_values(Approval)),
            "scheduledPermissionsRequests": lambda n : setattr(self, 'scheduled_permissions_requests', n.get_collection_of_object_values(ScheduledPermissionsRequest)),
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
        writer.write_collection_of_object_values("permissionsRequestChanges", self.permissions_request_changes)
        writer.write_collection_of_object_values("scheduledPermissionsApprovals", self.scheduled_permissions_approvals)
        writer.write_collection_of_object_values("scheduledPermissionsRequests", self.scheduled_permissions_requests)
    

