from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .assignee_types import AssigneeTypes

@dataclass
class Service(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The assignableTo property
    assignable_to: Optional[AssigneeTypes] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The unique identifier of the service plan that is equal to the servicePlanId property on the related servicePlanInfo objects.
    plan_id: Optional[UUID] = None
    # The name of the service plan that is equal to the servicePlanName property on the related servicePlanInfo objects.
    plan_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Service:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Service
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Service()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .assignee_types import AssigneeTypes

        from .assignee_types import AssigneeTypes

        fields: dict[str, Callable[[Any], None]] = {
            "assignableTo": lambda n : setattr(self, 'assignable_to', n.get_collection_of_enum_values(AssigneeTypes)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "planId": lambda n : setattr(self, 'plan_id', n.get_uuid_value()),
            "planName": lambda n : setattr(self, 'plan_name', n.get_str_value()),
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
        writer.write_enum_value("assignableTo", self.assignable_to)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_uuid_value("planId", self.plan_id)
        writer.write_str_value("planName", self.plan_name)
        writer.write_additional_data_value(self.additional_data)
    

