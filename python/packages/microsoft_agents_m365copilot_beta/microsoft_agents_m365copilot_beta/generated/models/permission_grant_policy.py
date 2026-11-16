from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .permission_grant_condition_set import PermissionGrantConditionSet
    from .policy_base import PolicyBase
    from .resource_scope_type import ResourceScopeType

from .policy_base import PolicyBase

@dataclass
class PermissionGrantPolicy(PolicyBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.permissionGrantPolicy"
    # Condition sets that are excluded in this permission grant policy. Automatically expanded on GET.
    excludes: Optional[list[PermissionGrantConditionSet]] = None
    # Set to true to create all pre-approval policies in the tenant. Set to false to disable all pre-approval policies in the tenant. The default is false.
    include_all_pre_approved_applications: Optional[bool] = None
    # Condition sets that are included in this permission grant policy. Automatically expanded on GET.
    includes: Optional[list[PermissionGrantConditionSet]] = None
    # The resource type the pre-approval policy applies to. Possible values: team for groups and teams, chat for chats, tenant for all supported resources in the tenant. Required.
    resource_scope_type: Optional[ResourceScopeType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PermissionGrantPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PermissionGrantPolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PermissionGrantPolicy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .permission_grant_condition_set import PermissionGrantConditionSet
        from .policy_base import PolicyBase
        from .resource_scope_type import ResourceScopeType

        from .permission_grant_condition_set import PermissionGrantConditionSet
        from .policy_base import PolicyBase
        from .resource_scope_type import ResourceScopeType

        fields: dict[str, Callable[[Any], None]] = {
            "excludes": lambda n : setattr(self, 'excludes', n.get_collection_of_object_values(PermissionGrantConditionSet)),
            "includeAllPreApprovedApplications": lambda n : setattr(self, 'include_all_pre_approved_applications', n.get_bool_value()),
            "includes": lambda n : setattr(self, 'includes', n.get_collection_of_object_values(PermissionGrantConditionSet)),
            "resourceScopeType": lambda n : setattr(self, 'resource_scope_type', n.get_enum_value(ResourceScopeType)),
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
        writer.write_collection_of_object_values("excludes", self.excludes)
        writer.write_bool_value("includeAllPreApprovedApplications", self.include_all_pre_approved_applications)
        writer.write_collection_of_object_values("includes", self.includes)
        writer.write_enum_value("resourceScopeType", self.resource_scope_type)
    

