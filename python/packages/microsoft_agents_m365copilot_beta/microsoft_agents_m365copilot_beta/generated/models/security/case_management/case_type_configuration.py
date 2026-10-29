from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...entity import Entity
    from .custom_field_definition import CustomFieldDefinition
    from .status_definition import StatusDefinition

from ...entity import Entity

@dataclass
class CaseTypeConfiguration(Entity, Parsable):
    # The contained custom-field definitions that make up the blank-form schema for this case type. Read-only. Supports $count, $expand, $filter, $orderby, $select, $skip, and $top.
    custom_fields: Optional[list[CustomFieldDefinition]] = None
    # The id of the top-level status that a new case of this type starts in.
    default_status_id: Optional[str] = None
    # The human-readable label of the case type.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The contained top-level statuses that a case of this type can be set to. Read-only. Supports $count, $expand, $filter, $orderby, $select, $skip, and $top.
    statuses: Optional[list[StatusDefinition]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CaseTypeConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CaseTypeConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CaseTypeConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ...entity import Entity
        from .custom_field_definition import CustomFieldDefinition
        from .status_definition import StatusDefinition

        from ...entity import Entity
        from .custom_field_definition import CustomFieldDefinition
        from .status_definition import StatusDefinition

        fields: dict[str, Callable[[Any], None]] = {
            "customFields": lambda n : setattr(self, 'custom_fields', n.get_collection_of_object_values(CustomFieldDefinition)),
            "defaultStatusId": lambda n : setattr(self, 'default_status_id', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "statuses": lambda n : setattr(self, 'statuses', n.get_collection_of_object_values(StatusDefinition)),
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
        writer.write_collection_of_object_values("customFields", self.custom_fields)
        writer.write_str_value("defaultStatusId", self.default_status_id)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("statuses", self.statuses)
    

