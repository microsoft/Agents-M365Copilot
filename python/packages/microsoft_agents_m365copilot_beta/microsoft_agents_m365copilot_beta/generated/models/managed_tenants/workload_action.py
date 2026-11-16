from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .setting import Setting
    from .workload_action_category import WorkloadActionCategory

@dataclass
class WorkloadAction(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The unique identifier for the workload action. Required. Read-only.
    action_id: Optional[str] = None
    # The category for the workload action. The possible values are: automated, manual, unknownFutureValue. Optional. Read-only.
    category: Optional[WorkloadActionCategory] = None
    # The description for the workload action. Optional. Read-only.
    description: Optional[str] = None
    # The display name for the workload action. Optional. Read-only.
    display_name: Optional[str] = None
    # The licenses property
    licenses: Optional[list[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The service associated with workload action. Optional. Read-only.
    service: Optional[str] = None
    # The collection of settings associated with the workload action. Optional. Read-only.
    settings: Optional[list[Setting]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WorkloadAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkloadAction
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WorkloadAction()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .setting import Setting
        from .workload_action_category import WorkloadActionCategory

        from .setting import Setting
        from .workload_action_category import WorkloadActionCategory

        fields: dict[str, Callable[[Any], None]] = {
            "actionId": lambda n : setattr(self, 'action_id', n.get_str_value()),
            "category": lambda n : setattr(self, 'category', n.get_enum_value(WorkloadActionCategory)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "licenses": lambda n : setattr(self, 'licenses', n.get_collection_of_primitive_values(str)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "service": lambda n : setattr(self, 'service', n.get_str_value()),
            "settings": lambda n : setattr(self, 'settings', n.get_collection_of_object_values(Setting)),
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
        writer.write_str_value("actionId", self.action_id)
        writer.write_enum_value("category", self.category)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_primitive_values("licenses", self.licenses)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("service", self.service)
        writer.write_collection_of_object_values("settings", self.settings)
        writer.write_additional_data_value(self.additional_data)
    

