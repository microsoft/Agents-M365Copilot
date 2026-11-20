from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .entity import Entity
    from .group_policy_category import GroupPolicyCategory
    from .group_policy_definition_class_type import GroupPolicyDefinitionClassType
    from .group_policy_definition_file import GroupPolicyDefinitionFile
    from .group_policy_presentation import GroupPolicyPresentation
    from .group_policy_type import GroupPolicyType

from .entity import Entity

@dataclass
class GroupPolicyDefinition(Entity, Parsable):
    """
    The entity describes all of the information about a single group policy.
    """
    # The group policy category associated with the definition.
    category: Optional[GroupPolicyCategory] = None
    # The localized full category path for the policy.
    category_path: Optional[str] = None
    # Group Policy Definition Class Type.
    class_type: Optional[GroupPolicyDefinitionClassType] = None
    # The group policy file associated with the definition.
    definition_file: Optional[GroupPolicyDefinitionFile] = None
    # The localized policy name.
    display_name: Optional[str] = None
    # The localized explanation or help text associated with the policy. The default value is empty.
    explain_text: Optional[str] = None
    # The category id of the parent category
    group_policy_category_id: Optional[UUID] = None
    # Signifies whether or not there are related definitions to this definition
    has_related_definitions: Optional[bool] = None
    # The date and time the entity was last modified.
    last_modified_date_time: Optional[datetime.datetime] = None
    # Minimum required CSP version for device configuration in this definition
    min_device_csp_version: Optional[str] = None
    # Minimum required CSP version for user configuration in this definition
    min_user_csp_version: Optional[str] = None
    # Definition of the next version of this definition
    next_version_definition: Optional[GroupPolicyDefinition] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Type of Group Policy File or Definition.
    policy_type: Optional[GroupPolicyType] = None
    # The group policy presentations associated with the definition.
    presentations: Optional[list[GroupPolicyPresentation]] = None
    # Definition of the previous version of this definition
    previous_version_definition: Optional[GroupPolicyDefinition] = None
    # Localized string used to specify what operating system or application version is affected by the policy.
    supported_on: Optional[str] = None
    # Setting definition version
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GroupPolicyDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GroupPolicyDefinition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GroupPolicyDefinition()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .group_policy_category import GroupPolicyCategory
        from .group_policy_definition_class_type import GroupPolicyDefinitionClassType
        from .group_policy_definition_file import GroupPolicyDefinitionFile
        from .group_policy_presentation import GroupPolicyPresentation
        from .group_policy_type import GroupPolicyType

        from .entity import Entity
        from .group_policy_category import GroupPolicyCategory
        from .group_policy_definition_class_type import GroupPolicyDefinitionClassType
        from .group_policy_definition_file import GroupPolicyDefinitionFile
        from .group_policy_presentation import GroupPolicyPresentation
        from .group_policy_type import GroupPolicyType

        fields: dict[str, Callable[[Any], None]] = {
            "category": lambda n : setattr(self, 'category', n.get_object_value(GroupPolicyCategory)),
            "categoryPath": lambda n : setattr(self, 'category_path', n.get_str_value()),
            "classType": lambda n : setattr(self, 'class_type', n.get_enum_value(GroupPolicyDefinitionClassType)),
            "definitionFile": lambda n : setattr(self, 'definition_file', n.get_object_value(GroupPolicyDefinitionFile)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "explainText": lambda n : setattr(self, 'explain_text', n.get_str_value()),
            "groupPolicyCategoryId": lambda n : setattr(self, 'group_policy_category_id', n.get_uuid_value()),
            "hasRelatedDefinitions": lambda n : setattr(self, 'has_related_definitions', n.get_bool_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "minDeviceCspVersion": lambda n : setattr(self, 'min_device_csp_version', n.get_str_value()),
            "minUserCspVersion": lambda n : setattr(self, 'min_user_csp_version', n.get_str_value()),
            "nextVersionDefinition": lambda n : setattr(self, 'next_version_definition', n.get_object_value(GroupPolicyDefinition)),
            "policyType": lambda n : setattr(self, 'policy_type', n.get_enum_value(GroupPolicyType)),
            "presentations": lambda n : setattr(self, 'presentations', n.get_collection_of_object_values(GroupPolicyPresentation)),
            "previousVersionDefinition": lambda n : setattr(self, 'previous_version_definition', n.get_object_value(GroupPolicyDefinition)),
            "supportedOn": lambda n : setattr(self, 'supported_on', n.get_str_value()),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
        writer.write_object_value("category", self.category)
        writer.write_str_value("categoryPath", self.category_path)
        writer.write_enum_value("classType", self.class_type)
        writer.write_object_value("definitionFile", self.definition_file)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("explainText", self.explain_text)
        writer.write_uuid_value("groupPolicyCategoryId", self.group_policy_category_id)
        writer.write_bool_value("hasRelatedDefinitions", self.has_related_definitions)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("minDeviceCspVersion", self.min_device_csp_version)
        writer.write_str_value("minUserCspVersion", self.min_user_csp_version)
        writer.write_object_value("nextVersionDefinition", self.next_version_definition)
        writer.write_enum_value("policyType", self.policy_type)
        writer.write_collection_of_object_values("presentations", self.presentations)
        writer.write_object_value("previousVersionDefinition", self.previous_version_definition)
        writer.write_str_value("supportedOn", self.supported_on)
        writer.write_str_value("version", self.version)
    

