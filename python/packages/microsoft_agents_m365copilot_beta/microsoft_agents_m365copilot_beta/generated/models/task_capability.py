from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TaskCapability(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Indicates whether assigned priority is shown in the task's personal view.
    assigned_priority_for_task_personal_view: Optional[bool] = None
    # Indicates whether dependencies are enabled for the task.
    dependencies: Optional[bool] = None
    # Indicates whether history tracking is enabled for the task.
    history: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TaskCapability:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TaskCapability
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TaskCapability()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "assignedPriorityForTaskPersonalView": lambda n : setattr(self, 'assigned_priority_for_task_personal_view', n.get_bool_value()),
            "dependencies": lambda n : setattr(self, 'dependencies', n.get_bool_value()),
            "history": lambda n : setattr(self, 'history', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_bool_value("assignedPriorityForTaskPersonalView", self.assigned_priority_for_task_personal_view)
        writer.write_bool_value("dependencies", self.dependencies)
        writer.write_bool_value("history", self.history)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

