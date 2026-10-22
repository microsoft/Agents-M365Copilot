from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .group_policy_definition import GroupPolicyDefinition
    from .group_policy_definition_file import GroupPolicyDefinitionFile
    from .ingestion_source import IngestionSource

from .entity import Entity

@dataclass
class GroupPolicyCategory(Entity, Parsable):
    """
    The category entity stores the category of a group policy definition
    """
    # The children categories
    children: Optional[list[GroupPolicyCategory]] = None
    # The id of the definition file the category came from
    definition_file: Optional[GroupPolicyDefinitionFile] = None
    # The immediate GroupPolicyDefinition children of the category
    definitions: Optional[list[GroupPolicyDefinition]] = None
    # The string id of the category's display name
    display_name: Optional[str] = None
    # Category Ingestion source
    ingestion_source: Optional[IngestionSource] = None
    # Defines if the category is a root category
    is_root: Optional[bool] = None
    # The date and time the entity was last modified.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The parent category
    parent: Optional[GroupPolicyCategory] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GroupPolicyCategory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GroupPolicyCategory
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GroupPolicyCategory()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .group_policy_definition import GroupPolicyDefinition
        from .group_policy_definition_file import GroupPolicyDefinitionFile
        from .ingestion_source import IngestionSource

        from .entity import Entity
        from .group_policy_definition import GroupPolicyDefinition
        from .group_policy_definition_file import GroupPolicyDefinitionFile
        from .ingestion_source import IngestionSource

        fields: dict[str, Callable[[Any], None]] = {
            "children": lambda n : setattr(self, 'children', n.get_collection_of_object_values(GroupPolicyCategory)),
            "definitionFile": lambda n : setattr(self, 'definition_file', n.get_object_value(GroupPolicyDefinitionFile)),
            "definitions": lambda n : setattr(self, 'definitions', n.get_collection_of_object_values(GroupPolicyDefinition)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "ingestionSource": lambda n : setattr(self, 'ingestion_source', n.get_enum_value(IngestionSource)),
            "isRoot": lambda n : setattr(self, 'is_root', n.get_bool_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "parent": lambda n : setattr(self, 'parent', n.get_object_value(GroupPolicyCategory)),
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
        writer.write_collection_of_object_values("children", self.children)
        writer.write_object_value("definitionFile", self.definition_file)
        writer.write_collection_of_object_values("definitions", self.definitions)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("ingestionSource", self.ingestion_source)
        writer.write_bool_value("isRoot", self.is_root)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_object_value("parent", self.parent)
    

