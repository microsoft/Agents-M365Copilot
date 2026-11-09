from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package import AccessPackage
    from .access_package_assignment_policy import AccessPackageAssignmentPolicy
    from .access_package_assignment_request import AccessPackageAssignmentRequest
    from .access_package_assignment_resource_role import AccessPackageAssignmentResourceRole
    from .access_package_subject import AccessPackageSubject
    from .custom_extension_callout_instance import CustomExtensionCalloutInstance
    from .entity import Entity
    from .request_schedule import RequestSchedule

from .entity import Entity

@dataclass
class AccessPackageAssignment(Entity, Parsable):
    # Read-only. Nullable. Supports $filter (eq) on the id property and $expand query parameters.
    access_package: Optional[AccessPackage] = None
    # Read-only. Nullable. Supports $filter (eq) on the id property
    access_package_assignment_policy: Optional[AccessPackageAssignmentPolicy] = None
    # The accessPackageAssignmentRequests property
    access_package_assignment_requests: Optional[list[AccessPackageAssignmentRequest]] = None
    # The resource roles delivered to the target user for this assignment. Read-only. Nullable.
    access_package_assignment_resource_roles: Optional[list[AccessPackageAssignmentResourceRole]] = None
    # The identifier of the access package. Read-only.
    access_package_id: Optional[str] = None
    # The identifier of the access package assignment policy. Read-only.
    assignment_policy_id: Optional[str] = None
    # The state of the access package assignment. Possible values are Delivering, Delivered, or Expired. Read-only. Supports $filter (eq).
    assignment_state: Optional[str] = None
    # More information about the assignment lifecycle. Possible values include Delivering, Delivered, AutoAssignmentInGracePeriod, NearExpiry1DayNotificationTriggered, or ExpiredNotificationTriggered. Read-only.
    assignment_status: Optional[str] = None
    # The identifier of the catalog containing the access package. Read-only.
    catalog_id: Optional[str] = None
    # Information about all the custom extension calls that were made during the access package assignment workflow.
    custom_extension_callout_instances: Optional[list[CustomExtensionCalloutInstance]] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    expired_date_time: Optional[datetime.datetime] = None
    # Indicates whether the access package assignment is extended. Read-only.
    is_extended: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # When the access assignment is to be in place. Read-only.
    schedule: Optional[RequestSchedule] = None
    # The subject of the access package assignment. Read-only. Nullable. Supports $expand. Supports $filter (eq) on objectId.
    target: Optional[AccessPackageSubject] = None
    # This property should not be used as a dependency, as it may change without notice. Instead, expand the target relationship and use the objectId property. Read-only.
    target_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessPackageAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageAssignment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessPackageAssignment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_package import AccessPackage
        from .access_package_assignment_policy import AccessPackageAssignmentPolicy
        from .access_package_assignment_request import AccessPackageAssignmentRequest
        from .access_package_assignment_resource_role import AccessPackageAssignmentResourceRole
        from .access_package_subject import AccessPackageSubject
        from .custom_extension_callout_instance import CustomExtensionCalloutInstance
        from .entity import Entity
        from .request_schedule import RequestSchedule

        from .access_package import AccessPackage
        from .access_package_assignment_policy import AccessPackageAssignmentPolicy
        from .access_package_assignment_request import AccessPackageAssignmentRequest
        from .access_package_assignment_resource_role import AccessPackageAssignmentResourceRole
        from .access_package_subject import AccessPackageSubject
        from .custom_extension_callout_instance import CustomExtensionCalloutInstance
        from .entity import Entity
        from .request_schedule import RequestSchedule

        fields: dict[str, Callable[[Any], None]] = {
            "accessPackage": lambda n : setattr(self, 'access_package', n.get_object_value(AccessPackage)),
            "accessPackageAssignmentPolicy": lambda n : setattr(self, 'access_package_assignment_policy', n.get_object_value(AccessPackageAssignmentPolicy)),
            "accessPackageAssignmentRequests": lambda n : setattr(self, 'access_package_assignment_requests', n.get_collection_of_object_values(AccessPackageAssignmentRequest)),
            "accessPackageAssignmentResourceRoles": lambda n : setattr(self, 'access_package_assignment_resource_roles', n.get_collection_of_object_values(AccessPackageAssignmentResourceRole)),
            "accessPackageId": lambda n : setattr(self, 'access_package_id', n.get_str_value()),
            "assignmentPolicyId": lambda n : setattr(self, 'assignment_policy_id', n.get_str_value()),
            "assignmentState": lambda n : setattr(self, 'assignment_state', n.get_str_value()),
            "assignmentStatus": lambda n : setattr(self, 'assignment_status', n.get_str_value()),
            "catalogId": lambda n : setattr(self, 'catalog_id', n.get_str_value()),
            "customExtensionCalloutInstances": lambda n : setattr(self, 'custom_extension_callout_instances', n.get_collection_of_object_values(CustomExtensionCalloutInstance)),
            "expiredDateTime": lambda n : setattr(self, 'expired_date_time', n.get_datetime_value()),
            "isExtended": lambda n : setattr(self, 'is_extended', n.get_bool_value()),
            "schedule": lambda n : setattr(self, 'schedule', n.get_object_value(RequestSchedule)),
            "target": lambda n : setattr(self, 'target', n.get_object_value(AccessPackageSubject)),
            "targetId": lambda n : setattr(self, 'target_id', n.get_str_value()),
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
        writer.write_object_value("accessPackage", self.access_package)
        writer.write_object_value("accessPackageAssignmentPolicy", self.access_package_assignment_policy)
        writer.write_collection_of_object_values("accessPackageAssignmentRequests", self.access_package_assignment_requests)
        writer.write_collection_of_object_values("accessPackageAssignmentResourceRoles", self.access_package_assignment_resource_roles)
        writer.write_str_value("accessPackageId", self.access_package_id)
        writer.write_str_value("assignmentPolicyId", self.assignment_policy_id)
        writer.write_str_value("assignmentState", self.assignment_state)
        writer.write_str_value("assignmentStatus", self.assignment_status)
        writer.write_str_value("catalogId", self.catalog_id)
        writer.write_collection_of_object_values("customExtensionCalloutInstances", self.custom_extension_callout_instances)
        writer.write_datetime_value("expiredDateTime", self.expired_date_time)
        writer.write_bool_value("isExtended", self.is_extended)
        writer.write_object_value("schedule", self.schedule)
        writer.write_object_value("target", self.target)
        writer.write_str_value("targetId", self.target_id)
    

