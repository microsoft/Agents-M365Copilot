from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class PlanCapability(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Indicates whether calendar features are enabled for the plan.
    calendar: Optional[bool] = None
    # Indicates whether custom fields are enabled for the plan.
    custom_fields: Optional[bool] = None
    # Indicates whether custom extension fields are enabled for the plan.
    extensions: Optional[bool] = None
    # Indicates whether goals are enabled for the plan.
    goals: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates whether undo is enabled for the plan.
    undo: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlanCapability:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlanCapability
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PlanCapability()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "calendar": lambda n : setattr(self, 'calendar', n.get_bool_value()),
            "customFields": lambda n : setattr(self, 'custom_fields', n.get_bool_value()),
            "extensions": lambda n : setattr(self, 'extensions', n.get_bool_value()),
            "goals": lambda n : setattr(self, 'goals', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "undo": lambda n : setattr(self, 'undo', n.get_bool_value()),
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
        writer.write_bool_value("calendar", self.calendar)
        writer.write_bool_value("customFields", self.custom_fields)
        writer.write_bool_value("extensions", self.extensions)
        writer.write_bool_value("goals", self.goals)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("undo", self.undo)
        writer.write_additional_data_value(self.additional_data)
    

