from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package import AccessPackage
    from .access_package_resource import AccessPackageResource
    from .access_package_resource_role import AccessPackageResourceRole
    from .access_package_resource_scope import AccessPackageResourceScope
    from .custom_access_package_workflow_extension import CustomAccessPackageWorkflowExtension
    from .custom_callout_extension import CustomCalloutExtension
    from .entity import Entity
    from .privilege_level import PrivilegeLevel

from .entity import Entity

@dataclass
class AccessPackageCatalog(Entity, Parsable):
    # The attributes of a logic app, which can be called at various stages of an access package request and assignment cycle.
    access_package_custom_workflow_extensions: Optional[list[CustomCalloutExtension]] = None
    # The roles in each resource in a catalog. Read-only.
    access_package_resource_roles: Optional[list[AccessPackageResourceRole]] = None
    # The accessPackageResourceScopes property
    access_package_resource_scopes: Optional[list[AccessPackageResourceScope]] = None
    # The accessPackageResources property
    access_package_resources: Optional[list[AccessPackageResource]] = None
    # The access packages in this catalog. Read-only. Nullable. Supports $expand.
    access_packages: Optional[list[AccessPackage]] = None
    # Has the value Published if the access packages are available for management.
    catalog_status: Optional[str] = None
    # One of UserManaged or ServiceDefault.
    catalog_type: Optional[str] = None
    # UPN of the user who created this resource. Read-only.
    created_by: Optional[str] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    # The customAccessPackageWorkflowExtensions property
    custom_access_package_workflow_extensions: Optional[list[CustomAccessPackageWorkflowExtension]] = None
    # The description of the access package catalog.
    description: Optional[str] = None
    # The display name of the access package catalog. Supports $filter (eq, contains).
    display_name: Optional[str] = None
    # Whether the access packages in this catalog can be requested by users outside of the tenant.
    is_externally_visible: Optional[bool] = None
    # The UPN of the user who last modified this resource. Read-only.
    modified_by: Optional[str] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The privilegeLevel property
    privilege_level: Optional[PrivilegeLevel] = None
    # The uniqueName property
    unique_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessPackageCatalog:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageCatalog
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessPackageCatalog()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_package import AccessPackage
        from .access_package_resource import AccessPackageResource
        from .access_package_resource_role import AccessPackageResourceRole
        from .access_package_resource_scope import AccessPackageResourceScope
        from .custom_access_package_workflow_extension import CustomAccessPackageWorkflowExtension
        from .custom_callout_extension import CustomCalloutExtension
        from .entity import Entity
        from .privilege_level import PrivilegeLevel

        from .access_package import AccessPackage
        from .access_package_resource import AccessPackageResource
        from .access_package_resource_role import AccessPackageResourceRole
        from .access_package_resource_scope import AccessPackageResourceScope
        from .custom_access_package_workflow_extension import CustomAccessPackageWorkflowExtension
        from .custom_callout_extension import CustomCalloutExtension
        from .entity import Entity
        from .privilege_level import PrivilegeLevel

        fields: dict[str, Callable[[Any], None]] = {
            "accessPackageCustomWorkflowExtensions": lambda n : setattr(self, 'access_package_custom_workflow_extensions', n.get_collection_of_object_values(CustomCalloutExtension)),
            "accessPackageResourceRoles": lambda n : setattr(self, 'access_package_resource_roles', n.get_collection_of_object_values(AccessPackageResourceRole)),
            "accessPackageResourceScopes": lambda n : setattr(self, 'access_package_resource_scopes', n.get_collection_of_object_values(AccessPackageResourceScope)),
            "accessPackageResources": lambda n : setattr(self, 'access_package_resources', n.get_collection_of_object_values(AccessPackageResource)),
            "accessPackages": lambda n : setattr(self, 'access_packages', n.get_collection_of_object_values(AccessPackage)),
            "catalogStatus": lambda n : setattr(self, 'catalog_status', n.get_str_value()),
            "catalogType": lambda n : setattr(self, 'catalog_type', n.get_str_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "customAccessPackageWorkflowExtensions": lambda n : setattr(self, 'custom_access_package_workflow_extensions', n.get_collection_of_object_values(CustomAccessPackageWorkflowExtension)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isExternallyVisible": lambda n : setattr(self, 'is_externally_visible', n.get_bool_value()),
            "modifiedBy": lambda n : setattr(self, 'modified_by', n.get_str_value()),
            "modifiedDateTime": lambda n : setattr(self, 'modified_date_time', n.get_datetime_value()),
            "privilegeLevel": lambda n : setattr(self, 'privilege_level', n.get_enum_value(PrivilegeLevel)),
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
        writer.write_collection_of_object_values("accessPackageCustomWorkflowExtensions", self.access_package_custom_workflow_extensions)
        writer.write_collection_of_object_values("accessPackageResourceRoles", self.access_package_resource_roles)
        writer.write_collection_of_object_values("accessPackageResourceScopes", self.access_package_resource_scopes)
        writer.write_collection_of_object_values("accessPackageResources", self.access_package_resources)
        writer.write_collection_of_object_values("accessPackages", self.access_packages)
        writer.write_str_value("catalogStatus", self.catalog_status)
        writer.write_str_value("catalogType", self.catalog_type)
        writer.write_str_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_collection_of_object_values("customAccessPackageWorkflowExtensions", self.custom_access_package_workflow_extensions)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isExternallyVisible", self.is_externally_visible)
        writer.write_str_value("modifiedBy", self.modified_by)
        writer.write_datetime_value("modifiedDateTime", self.modified_date_time)
        writer.write_enum_value("privilegeLevel", self.privilege_level)
        writer.write_str_value("uniqueName", self.unique_name)
    

