from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .management_category import ManagementCategory
    from .workload_action import WorkloadAction

from ..entity import Entity

@dataclass
class ManagementAction(Entity, Parsable):
    # The category property
    category: Optional[ManagementCategory] = None
    # The description for the management action. Optional. Read-only.
    description: Optional[str] = None
    # The display name for the management action. Optional. Read-only.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The reference for the management template used to generate the management action. Required. Read-only.
    reference_template_id: Optional[str] = None
    # The referenceTemplateVersion property
    reference_template_version: Optional[int] = None
    # The collection of workload actions associated with the management action. Required. Read-only.
    workload_actions: Optional[list[WorkloadAction]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ManagementAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManagementAction
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ManagementAction()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .management_category import ManagementCategory
        from .workload_action import WorkloadAction

        from ..entity import Entity
        from .management_category import ManagementCategory
        from .workload_action import WorkloadAction

        fields: dict[str, Callable[[Any], None]] = {
            "category": lambda n : setattr(self, 'category', n.get_enum_value(ManagementCategory)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "referenceTemplateId": lambda n : setattr(self, 'reference_template_id', n.get_str_value()),
            "referenceTemplateVersion": lambda n : setattr(self, 'reference_template_version', n.get_int_value()),
            "workloadActions": lambda n : setattr(self, 'workload_actions', n.get_collection_of_object_values(WorkloadAction)),
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
        writer.write_enum_value("category", self.category)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("referenceTemplateId", self.reference_template_id)
        writer.write_int_value("referenceTemplateVersion", self.reference_template_version)
        writer.write_collection_of_object_values("workloadActions", self.workload_actions)
    

