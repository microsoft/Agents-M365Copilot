from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package import AccessPackage
    from .access_package_assignment import AccessPackageAssignment
    from .access_package_assignment_policy import AccessPackageAssignmentPolicy
    from .access_package_assignment_request import AccessPackageAssignmentRequest
    from .access_package_assignment_resource_role import AccessPackageAssignmentResourceRole
    from .access_package_catalog import AccessPackageCatalog
    from .access_package_resource import AccessPackageResource
    from .access_package_resource_environment import AccessPackageResourceEnvironment
    from .access_package_resource_request import AccessPackageResourceRequest
    from .access_package_resource_role_scope import AccessPackageResourceRoleScope
    from .access_package_subject import AccessPackageSubject
    from .access_package_suggestion import AccessPackageSuggestion
    from .approval import Approval
    from .available_access_package import AvailableAccessPackage
    from .connected_organization import ConnectedOrganization
    from .control_configuration import ControlConfiguration
    from .entitlement_management_settings import EntitlementManagementSettings
    from .entity import Entity
    from .external_origin_resource_connector import ExternalOriginResourceConnector

from .entity import Entity

@dataclass
class EntitlementManagement(Entity, Parsable):
    # The accessPackageAssignmentApprovals property
    access_package_assignment_approvals: Optional[list[Approval]] = None
    # Represents the policy that governs which subjects can request or be assigned an access package via an access package assignment.
    access_package_assignment_policies: Optional[list[AccessPackageAssignmentPolicy]] = None
    # Represents access package assignment requests created by or on behalf of a user. DO NOT USE. TO BE RETIRED SOON. Use the assignmentRequests relationship instead.
    access_package_assignment_requests: Optional[list[AccessPackageAssignmentRequest]] = None
    # Represents the resource-specific role which a subject has been assigned through an access package assignment.
    access_package_assignment_resource_roles: Optional[list[AccessPackageAssignmentResourceRole]] = None
    # The assignment of an access package to a subject for a period of time.
    access_package_assignments: Optional[list[AccessPackageAssignment]] = None
    # A container of access packages.
    access_package_catalogs: Optional[list[AccessPackageCatalog]] = None
    # A reference to the geolocation environment in which a resource is located.
    access_package_resource_environments: Optional[list[AccessPackageResourceEnvironment]] = None
    # Represents a request to add or remove a resource to or from a catalog respectively.
    access_package_resource_requests: Optional[list[AccessPackageResourceRequest]] = None
    # A reference to both a scope within a resource, and a role in that resource for that scope.
    access_package_resource_role_scopes: Optional[list[AccessPackageResourceRoleScope]] = None
    # A reference to a resource associated with an access package catalog.
    access_package_resources: Optional[list[AccessPackageResource]] = None
    # The accessPackageSuggestions property
    access_package_suggestions: Optional[list[AccessPackageSuggestion]] = None
    # Represents access package objects.
    access_packages: Optional[list[AccessPackage]] = None
    # Represents access package assignment requests created by or on behalf of a user.
    assignment_requests: Optional[list[AccessPackageAssignmentRequest]] = None
    # The availableAccessPackages property
    available_access_packages: Optional[list[AvailableAccessPackage]] = None
    # Represents references to a directory or domain of another organization whose users can request access.
    connected_organizations: Optional[list[ConnectedOrganization]] = None
    # Represents the policies that control lifecycle and access to access packages across the organization.
    control_configurations: Optional[list[ControlConfiguration]] = None
    # Represents the connectors used to communicate with external resource systems.
    external_origin_resource_connectors: Optional[list[ExternalOriginResourceConnector]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents the settings that control the behavior of Microsoft Entra entitlement management.
    settings: Optional[EntitlementManagementSettings] = None
    # Represents the subjects within entitlement management.
    subjects: Optional[list[AccessPackageSubject]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EntitlementManagement:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EntitlementManagement
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EntitlementManagement()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_package import AccessPackage
        from .access_package_assignment import AccessPackageAssignment
        from .access_package_assignment_policy import AccessPackageAssignmentPolicy
        from .access_package_assignment_request import AccessPackageAssignmentRequest
        from .access_package_assignment_resource_role import AccessPackageAssignmentResourceRole
        from .access_package_catalog import AccessPackageCatalog
        from .access_package_resource import AccessPackageResource
        from .access_package_resource_environment import AccessPackageResourceEnvironment
        from .access_package_resource_request import AccessPackageResourceRequest
        from .access_package_resource_role_scope import AccessPackageResourceRoleScope
        from .access_package_subject import AccessPackageSubject
        from .access_package_suggestion import AccessPackageSuggestion
        from .approval import Approval
        from .available_access_package import AvailableAccessPackage
        from .connected_organization import ConnectedOrganization
        from .control_configuration import ControlConfiguration
        from .entitlement_management_settings import EntitlementManagementSettings
        from .entity import Entity
        from .external_origin_resource_connector import ExternalOriginResourceConnector

        from .access_package import AccessPackage
        from .access_package_assignment import AccessPackageAssignment
        from .access_package_assignment_policy import AccessPackageAssignmentPolicy
        from .access_package_assignment_request import AccessPackageAssignmentRequest
        from .access_package_assignment_resource_role import AccessPackageAssignmentResourceRole
        from .access_package_catalog import AccessPackageCatalog
        from .access_package_resource import AccessPackageResource
        from .access_package_resource_environment import AccessPackageResourceEnvironment
        from .access_package_resource_request import AccessPackageResourceRequest
        from .access_package_resource_role_scope import AccessPackageResourceRoleScope
        from .access_package_subject import AccessPackageSubject
        from .access_package_suggestion import AccessPackageSuggestion
        from .approval import Approval
        from .available_access_package import AvailableAccessPackage
        from .connected_organization import ConnectedOrganization
        from .control_configuration import ControlConfiguration
        from .entitlement_management_settings import EntitlementManagementSettings
        from .entity import Entity
        from .external_origin_resource_connector import ExternalOriginResourceConnector

        fields: dict[str, Callable[[Any], None]] = {
            "accessPackageAssignmentApprovals": lambda n : setattr(self, 'access_package_assignment_approvals', n.get_collection_of_object_values(Approval)),
            "accessPackageAssignmentPolicies": lambda n : setattr(self, 'access_package_assignment_policies', n.get_collection_of_object_values(AccessPackageAssignmentPolicy)),
            "accessPackageAssignmentRequests": lambda n : setattr(self, 'access_package_assignment_requests', n.get_collection_of_object_values(AccessPackageAssignmentRequest)),
            "accessPackageAssignmentResourceRoles": lambda n : setattr(self, 'access_package_assignment_resource_roles', n.get_collection_of_object_values(AccessPackageAssignmentResourceRole)),
            "accessPackageAssignments": lambda n : setattr(self, 'access_package_assignments', n.get_collection_of_object_values(AccessPackageAssignment)),
            "accessPackageCatalogs": lambda n : setattr(self, 'access_package_catalogs', n.get_collection_of_object_values(AccessPackageCatalog)),
            "accessPackageResourceEnvironments": lambda n : setattr(self, 'access_package_resource_environments', n.get_collection_of_object_values(AccessPackageResourceEnvironment)),
            "accessPackageResourceRequests": lambda n : setattr(self, 'access_package_resource_requests', n.get_collection_of_object_values(AccessPackageResourceRequest)),
            "accessPackageResourceRoleScopes": lambda n : setattr(self, 'access_package_resource_role_scopes', n.get_collection_of_object_values(AccessPackageResourceRoleScope)),
            "accessPackageResources": lambda n : setattr(self, 'access_package_resources', n.get_collection_of_object_values(AccessPackageResource)),
            "accessPackageSuggestions": lambda n : setattr(self, 'access_package_suggestions', n.get_collection_of_object_values(AccessPackageSuggestion)),
            "accessPackages": lambda n : setattr(self, 'access_packages', n.get_collection_of_object_values(AccessPackage)),
            "assignmentRequests": lambda n : setattr(self, 'assignment_requests', n.get_collection_of_object_values(AccessPackageAssignmentRequest)),
            "availableAccessPackages": lambda n : setattr(self, 'available_access_packages', n.get_collection_of_object_values(AvailableAccessPackage)),
            "connectedOrganizations": lambda n : setattr(self, 'connected_organizations', n.get_collection_of_object_values(ConnectedOrganization)),
            "controlConfigurations": lambda n : setattr(self, 'control_configurations', n.get_collection_of_object_values(ControlConfiguration)),
            "externalOriginResourceConnectors": lambda n : setattr(self, 'external_origin_resource_connectors', n.get_collection_of_object_values(ExternalOriginResourceConnector)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(EntitlementManagementSettings)),
            "subjects": lambda n : setattr(self, 'subjects', n.get_collection_of_object_values(AccessPackageSubject)),
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
        writer.write_collection_of_object_values("accessPackageAssignmentApprovals", self.access_package_assignment_approvals)
        writer.write_collection_of_object_values("accessPackageAssignmentPolicies", self.access_package_assignment_policies)
        writer.write_collection_of_object_values("accessPackageAssignmentRequests", self.access_package_assignment_requests)
        writer.write_collection_of_object_values("accessPackageAssignmentResourceRoles", self.access_package_assignment_resource_roles)
        writer.write_collection_of_object_values("accessPackageAssignments", self.access_package_assignments)
        writer.write_collection_of_object_values("accessPackageCatalogs", self.access_package_catalogs)
        writer.write_collection_of_object_values("accessPackageResourceEnvironments", self.access_package_resource_environments)
        writer.write_collection_of_object_values("accessPackageResourceRequests", self.access_package_resource_requests)
        writer.write_collection_of_object_values("accessPackageResourceRoleScopes", self.access_package_resource_role_scopes)
        writer.write_collection_of_object_values("accessPackageResources", self.access_package_resources)
        writer.write_collection_of_object_values("accessPackageSuggestions", self.access_package_suggestions)
        writer.write_collection_of_object_values("accessPackages", self.access_packages)
        writer.write_collection_of_object_values("assignmentRequests", self.assignment_requests)
        writer.write_collection_of_object_values("availableAccessPackages", self.available_access_packages)
        writer.write_collection_of_object_values("connectedOrganizations", self.connected_organizations)
        writer.write_collection_of_object_values("controlConfigurations", self.control_configurations)
        writer.write_collection_of_object_values("externalOriginResourceConnectors", self.external_origin_resource_connectors)
        writer.write_object_value("settings", self.settings)
        writer.write_collection_of_object_values("subjects", self.subjects)
    

