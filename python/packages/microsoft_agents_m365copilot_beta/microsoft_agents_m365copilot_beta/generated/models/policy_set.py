from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .error_code import ErrorCode
    from .policy_set_assignment import PolicySetAssignment
    from .policy_set_item import PolicySetItem
    from .policy_set_status import PolicySetStatus

from .entity import Entity

@dataclass
class PolicySet(Entity, Parsable):
    """
    A class containing the properties used for PolicySet.
    """
    # Assignments of the PolicySet.
    assignments: Optional[list[PolicySetAssignment]] = None
    # Creation time of the PolicySet.
    created_date_time: Optional[datetime.datetime] = None
    # Description of the PolicySet.
    description: Optional[str] = None
    # DisplayName of the PolicySet.
    display_name: Optional[str] = None
    # The errorCode property
    error_code: Optional[ErrorCode] = None
    # Tags of the guided deployment
    guided_deployment_tags: Optional[list[str]] = None
    # Items of the PolicySet with maximum count 100.
    items: Optional[list[PolicySetItem]] = None
    # Last modified time of the PolicySet.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # RoleScopeTags of the PolicySet
    role_scope_tags: Optional[list[str]] = None
    # The enum to specify the status of PolicySet.
    status: Optional[PolicySetStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PolicySet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PolicySet
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PolicySet()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .error_code import ErrorCode
        from .policy_set_assignment import PolicySetAssignment
        from .policy_set_item import PolicySetItem
        from .policy_set_status import PolicySetStatus

        from .entity import Entity
        from .error_code import ErrorCode
        from .policy_set_assignment import PolicySetAssignment
        from .policy_set_item import PolicySetItem
        from .policy_set_status import PolicySetStatus

        fields: dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(PolicySetAssignment)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "errorCode": lambda n : setattr(self, 'error_code', n.get_enum_value(ErrorCode)),
            "guidedDeploymentTags": lambda n : setattr(self, 'guided_deployment_tags', n.get_collection_of_primitive_values(str)),
            "items": lambda n : setattr(self, 'items', n.get_collection_of_object_values(PolicySetItem)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "roleScopeTags": lambda n : setattr(self, 'role_scope_tags', n.get_collection_of_primitive_values(str)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(PolicySetStatus)),
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
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("errorCode", self.error_code)
        writer.write_collection_of_primitive_values("guidedDeploymentTags", self.guided_deployment_tags)
        writer.write_collection_of_object_values("items", self.items)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_primitive_values("roleScopeTags", self.role_scope_tags)
        writer.write_enum_value("status", self.status)
    

