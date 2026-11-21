from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .policy_category import PolicyCategory
    from .resource_policy_assignment import ResourcePolicyAssignment
    from .resource_policy_definition_version import ResourcePolicyDefinitionVersion
    from .resource_policy_rule import ResourcePolicyRule

@dataclass
class ResourcePolicyDefinition(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The assignments property
    assignments: Optional[list[ResourcePolicyAssignment]] = None
    # The category property
    category: Optional[PolicyCategory] = None
    # The createdDateTime property
    created_date_time: Optional[datetime.datetime] = None
    # The deletedDateTime property
    deleted_date_time: Optional[datetime.datetime] = None
    # The description property
    description: Optional[str] = None
    # The displayName property
    display_name: Optional[str] = None
    # The lastModifiedDateTime property
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The previousVersions property
    previous_versions: Optional[list[ResourcePolicyDefinitionVersion]] = None
    # The rule property
    rule: Optional[ResourcePolicyRule] = None
    # The uniqueName property
    unique_name: Optional[str] = None
    # The version property
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ResourcePolicyDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ResourcePolicyDefinition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ResourcePolicyDefinition()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .policy_category import PolicyCategory
        from .resource_policy_assignment import ResourcePolicyAssignment
        from .resource_policy_definition_version import ResourcePolicyDefinitionVersion
        from .resource_policy_rule import ResourcePolicyRule

        from .policy_category import PolicyCategory
        from .resource_policy_assignment import ResourcePolicyAssignment
        from .resource_policy_definition_version import ResourcePolicyDefinitionVersion
        from .resource_policy_rule import ResourcePolicyRule

        fields: dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(ResourcePolicyAssignment)),
            "category": lambda n : setattr(self, 'category', n.get_enum_value(PolicyCategory)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "deletedDateTime": lambda n : setattr(self, 'deleted_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "previousVersions": lambda n : setattr(self, 'previous_versions', n.get_collection_of_object_values(ResourcePolicyDefinitionVersion)),
            "rule": lambda n : setattr(self, 'rule', n.get_object_value(ResourcePolicyRule)),
            "uniqueName": lambda n : setattr(self, 'unique_name', n.get_str_value()),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_enum_value("category", self.category)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("previousVersions", self.previous_versions)
        writer.write_object_value("rule", self.rule)
        writer.write_str_value("uniqueName", self.unique_name)
        writer.write_additional_data_value(self.additional_data)
    

