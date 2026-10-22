from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .group_policy_definition import GroupPolicyDefinition
    from .group_policy_type import GroupPolicyType
    from .group_policy_uploaded_definition_file import GroupPolicyUploadedDefinitionFile

from .entity import Entity

@dataclass
class GroupPolicyDefinitionFile(Entity, Parsable):
    """
    The entity represents an ADMX (Administrative Template) XML file. The ADMX file contains a collection of group policy definitions and their locations by category path. The group policy definition file also contains the languages supported as determined by the language dependent ADML (Administrative Template) language files.
    """
    # The group policy definitions associated with the file.
    definitions: Optional[list[GroupPolicyDefinition]] = None
    # The localized description of the policy settings in the ADMX file. The default value is empty.
    description: Optional[str] = None
    # The localized friendly name of the ADMX file.
    display_name: Optional[str] = None
    # The file name of the ADMX file without the path. For example: edge.admx
    file_name: Optional[str] = None
    # The supported language codes for the ADMX file.
    language_codes: Optional[list[str]] = None
    # The date and time the entity was last modified.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Type of Group Policy File or Definition.
    policy_type: Optional[GroupPolicyType] = None
    # The revision version associated with the file.
    revision: Optional[str] = None
    # Specifies the URI used to identify the namespace within the ADMX file.
    target_namespace: Optional[str] = None
    # Specifies the logical name that refers to the namespace within the ADMX file.
    target_prefix: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GroupPolicyDefinitionFile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GroupPolicyDefinitionFile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupPolicyUploadedDefinitionFile".casefold():
            from .group_policy_uploaded_definition_file import GroupPolicyUploadedDefinitionFile

            return GroupPolicyUploadedDefinitionFile()
        return GroupPolicyDefinitionFile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .group_policy_definition import GroupPolicyDefinition
        from .group_policy_type import GroupPolicyType
        from .group_policy_uploaded_definition_file import GroupPolicyUploadedDefinitionFile

        from .entity import Entity
        from .group_policy_definition import GroupPolicyDefinition
        from .group_policy_type import GroupPolicyType
        from .group_policy_uploaded_definition_file import GroupPolicyUploadedDefinitionFile

        fields: dict[str, Callable[[Any], None]] = {
            "definitions": lambda n : setattr(self, 'definitions', n.get_collection_of_object_values(GroupPolicyDefinition)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "fileName": lambda n : setattr(self, 'file_name', n.get_str_value()),
            "languageCodes": lambda n : setattr(self, 'language_codes', n.get_collection_of_primitive_values(str)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "policyType": lambda n : setattr(self, 'policy_type', n.get_enum_value(GroupPolicyType)),
            "revision": lambda n : setattr(self, 'revision', n.get_str_value()),
            "targetNamespace": lambda n : setattr(self, 'target_namespace', n.get_str_value()),
            "targetPrefix": lambda n : setattr(self, 'target_prefix', n.get_str_value()),
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
        writer.write_collection_of_object_values("definitions", self.definitions)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("fileName", self.file_name)
        writer.write_collection_of_primitive_values("languageCodes", self.language_codes)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("policyType", self.policy_type)
        writer.write_str_value("revision", self.revision)
        writer.write_str_value("targetNamespace", self.target_namespace)
        writer.write_str_value("targetPrefix", self.target_prefix)
    

