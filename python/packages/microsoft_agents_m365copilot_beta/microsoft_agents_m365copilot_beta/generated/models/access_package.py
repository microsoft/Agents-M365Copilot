from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package_assignment_policy import AccessPackageAssignmentPolicy
    from .access_package_catalog import AccessPackageCatalog
    from .access_package_resource_role_scope import AccessPackageResourceRoleScope
    from .entity import Entity
    from .group import Group

from .entity import Entity

@dataclass
class AccessPackage(Entity, Parsable):
    # Read-only. Nullable. Supports $expand.
    access_package_assignment_policies: Optional[list[AccessPackageAssignmentPolicy]] = None
    # The accessPackageCatalog property
    access_package_catalog: Optional[AccessPackageCatalog] = None
    # The accessPackageResourceRoleScopes property
    access_package_resource_role_scopes: Optional[list[AccessPackageResourceRoleScope]] = None
    # The access packages that are incompatible with this package. Read-only.
    access_packages_incompatible_with: Optional[list[AccessPackage]] = None
    # Identifier of the access package catalog referencing this access package. Read-only.
    catalog_id: Optional[str] = None
    # The userPrincipalName of the user or identity of the subject who created this resource. Read-only.
    created_by: Optional[str] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    # The description of the access package.
    description: Optional[str] = None
    # The display name of the access package. Supports $filter (eq, contains).
    display_name: Optional[str] = None
    # The  access packages whose assigned users are ineligible to be assigned this access package.
    incompatible_access_packages: Optional[list[AccessPackage]] = None
    # The groups whose members are ineligible to be assigned this access package.
    incompatible_groups: Optional[list[Group]] = None
    # Indicates whether the access package is hidden from the requestor.
    is_hidden: Optional[bool] = None
    # Indicates whether role scopes are visible.
    is_role_scopes_visible: Optional[bool] = None
    # The userPrincipalName of the user who last modified this resource. Read-only.
    modified_by: Optional[str] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The uniqueName property
    unique_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessPackage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessPackage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_package_assignment_policy import AccessPackageAssignmentPolicy
        from .access_package_catalog import AccessPackageCatalog
        from .access_package_resource_role_scope import AccessPackageResourceRoleScope
        from .entity import Entity
        from .group import Group

        from .access_package_assignment_policy import AccessPackageAssignmentPolicy
        from .access_package_catalog import AccessPackageCatalog
        from .access_package_resource_role_scope import AccessPackageResourceRoleScope
        from .entity import Entity
        from .group import Group

        fields: dict[str, Callable[[Any], None]] = {
            "accessPackageAssignmentPolicies": lambda n : setattr(self, 'access_package_assignment_policies', n.get_collection_of_object_values(AccessPackageAssignmentPolicy)),
            "accessPackageCatalog": lambda n : setattr(self, 'access_package_catalog', n.get_object_value(AccessPackageCatalog)),
            "accessPackageResourceRoleScopes": lambda n : setattr(self, 'access_package_resource_role_scopes', n.get_collection_of_object_values(AccessPackageResourceRoleScope)),
            "accessPackagesIncompatibleWith": lambda n : setattr(self, 'access_packages_incompatible_with', n.get_collection_of_object_values(AccessPackage)),
            "catalogId": lambda n : setattr(self, 'catalog_id', n.get_str_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "incompatibleAccessPackages": lambda n : setattr(self, 'incompatible_access_packages', n.get_collection_of_object_values(AccessPackage)),
            "incompatibleGroups": lambda n : setattr(self, 'incompatible_groups', n.get_collection_of_object_values(Group)),
            "isHidden": lambda n : setattr(self, 'is_hidden', n.get_bool_value()),
            "isRoleScopesVisible": lambda n : setattr(self, 'is_role_scopes_visible', n.get_bool_value()),
            "modifiedBy": lambda n : setattr(self, 'modified_by', n.get_str_value()),
            "modifiedDateTime": lambda n : setattr(self, 'modified_date_time', n.get_datetime_value()),
            "uniqueName": lambda n : setattr(self, 'unique_name', n.get_str_value()),
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
        writer.write_collection_of_object_values("accessPackageAssignmentPolicies", self.access_package_assignment_policies)
        writer.write_object_value("accessPackageCatalog", self.access_package_catalog)
        writer.write_collection_of_object_values("accessPackageResourceRoleScopes", self.access_package_resource_role_scopes)
        writer.write_collection_of_object_values("accessPackagesIncompatibleWith", self.access_packages_incompatible_with)
        writer.write_str_value("catalogId", self.catalog_id)
        writer.write_str_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("incompatibleAccessPackages", self.incompatible_access_packages)
        writer.write_collection_of_object_values("incompatibleGroups", self.incompatible_groups)
        writer.write_bool_value("isHidden", self.is_hidden)
        writer.write_bool_value("isRoleScopesVisible", self.is_role_scopes_visible)
        writer.write_str_value("modifiedBy", self.modified_by)
        writer.write_datetime_value("modifiedDateTime", self.modified_date_time)
        writer.write_str_value("uniqueName", self.unique_name)
    

