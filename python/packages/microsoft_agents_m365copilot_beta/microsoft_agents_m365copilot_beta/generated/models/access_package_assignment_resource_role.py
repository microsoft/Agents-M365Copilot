from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package_assignment import AccessPackageAssignment
    from .access_package_resource_role import AccessPackageResourceRole
    from .access_package_resource_scope import AccessPackageResourceScope
    from .access_package_subject import AccessPackageSubject
    from .entity import Entity

from .entity import Entity

@dataclass
class AccessPackageAssignmentResourceRole(Entity, Parsable):
    # The access package assignments resulting in this role assignment. Read-only. Nullable.
    access_package_assignments: Optional[list[AccessPackageAssignment]] = None
    # The accessPackageResourceRole property
    access_package_resource_role: Optional[AccessPackageResourceRole] = None
    # The accessPackageResourceScope property
    access_package_resource_scope: Optional[AccessPackageResourceScope] = None
    # Read-only. Nullable. Supports $filter (eq) on objectId and $expand query parameters.
    access_package_subject: Optional[AccessPackageSubject] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A unique identifier relative to the origin system, corresponding to the originId property of the accessPackageResourceRole.
    origin_id: Optional[str] = None
    # The system where the role assignment is to be created or has been created for an access package assignment, such as SharePointOnline, AadGroup, or AadApplication, corresponding to the originSystem property of the accessPackageResourceRole.
    origin_system: Optional[str] = None
    # The value is PendingFulfillment before the access package assignment is delivered to the origin system, and Fulfilled after the access package assignment is delivered to the origin system.
    status: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessPackageAssignmentResourceRole:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageAssignmentResourceRole
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessPackageAssignmentResourceRole()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_package_assignment import AccessPackageAssignment
        from .access_package_resource_role import AccessPackageResourceRole
        from .access_package_resource_scope import AccessPackageResourceScope
        from .access_package_subject import AccessPackageSubject
        from .entity import Entity

        from .access_package_assignment import AccessPackageAssignment
        from .access_package_resource_role import AccessPackageResourceRole
        from .access_package_resource_scope import AccessPackageResourceScope
        from .access_package_subject import AccessPackageSubject
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "accessPackageAssignments": lambda n : setattr(self, 'access_package_assignments', n.get_collection_of_object_values(AccessPackageAssignment)),
            "accessPackageResourceRole": lambda n : setattr(self, 'access_package_resource_role', n.get_object_value(AccessPackageResourceRole)),
            "accessPackageResourceScope": lambda n : setattr(self, 'access_package_resource_scope', n.get_object_value(AccessPackageResourceScope)),
            "accessPackageSubject": lambda n : setattr(self, 'access_package_subject', n.get_object_value(AccessPackageSubject)),
            "originId": lambda n : setattr(self, 'origin_id', n.get_str_value()),
            "originSystem": lambda n : setattr(self, 'origin_system', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
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
        writer.write_collection_of_object_values("accessPackageAssignments", self.access_package_assignments)
        writer.write_object_value("accessPackageResourceRole", self.access_package_resource_role)
        writer.write_object_value("accessPackageResourceScope", self.access_package_resource_scope)
        writer.write_object_value("accessPackageSubject", self.access_package_subject)
        writer.write_str_value("originId", self.origin_id)
        writer.write_str_value("originSystem", self.origin_system)
        writer.write_str_value("status", self.status)
    

