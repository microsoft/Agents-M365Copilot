from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from ..entity import Entity
    from .assignee_types import AssigneeTypes
    from .assignment import Assignment
    from .service import Service
    from .subscription import Subscription
    from .waiting_member import WaitingMember

from ..entity import Entity

@dataclass
class Allotment(Entity, Parsable):
    # The number of licenses contained within the allotment. Not nullable. Read-only.
    allotted_units: Optional[int] = None
    # The assignableTo property
    assignable_to: Optional[AssigneeTypes] = None
    # The list of license assignments that consume licenses from this allotment. Not nullable.
    assignments: Optional[list[Assignment]] = None
    # The number of licenses that are currently consumed by assignments from this allotment. Not nullable. Read-only.
    consumed_units: Optional[int] = None
    # The externalServiceIdentifier property
    external_service_identifier: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The list of services that might be enabled or disabled for assignments from this allotment. Not nullable. Read-only.
    services: Optional[list[Service]] = None
    # Unique identifier (GUID) for the service SKU that is equal to the skuId property on the related subscribedSku object. Read-only. Supports $filter.
    sku_id: Optional[UUID] = None
    # Unique SKU display name that is equal to the skuPartNumber on the related subscribedSku object; for example, AAD_Premium. Read-only.
    sku_part_number: Optional[str] = None
    # Basic information about the subscriptions that supports this allotment.
    subscriptions: Optional[list[Subscription]] = None
    # List of over-assigned users who are in the waiting room for an allotment due to license capacity limits.
    waiting_members: Optional[list[WaitingMember]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Allotment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Allotment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Allotment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .assignee_types import AssigneeTypes
        from .assignment import Assignment
        from .service import Service
        from .subscription import Subscription
        from .waiting_member import WaitingMember

        from ..entity import Entity
        from .assignee_types import AssigneeTypes
        from .assignment import Assignment
        from .service import Service
        from .subscription import Subscription
        from .waiting_member import WaitingMember

        fields: dict[str, Callable[[Any], None]] = {
            "allottedUnits": lambda n : setattr(self, 'allotted_units', n.get_int_value()),
            "assignableTo": lambda n : setattr(self, 'assignable_to', n.get_collection_of_enum_values(AssigneeTypes)),
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(Assignment)),
            "consumedUnits": lambda n : setattr(self, 'consumed_units', n.get_int_value()),
            "externalServiceIdentifier": lambda n : setattr(self, 'external_service_identifier', n.get_str_value()),
            "services": lambda n : setattr(self, 'services', n.get_collection_of_object_values(Service)),
            "skuId": lambda n : setattr(self, 'sku_id', n.get_uuid_value()),
            "skuPartNumber": lambda n : setattr(self, 'sku_part_number', n.get_str_value()),
            "subscriptions": lambda n : setattr(self, 'subscriptions', n.get_collection_of_object_values(Subscription)),
            "waitingMembers": lambda n : setattr(self, 'waiting_members', n.get_collection_of_object_values(WaitingMember)),
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
        writer.write_int_value("allottedUnits", self.allotted_units)
        writer.write_enum_value("assignableTo", self.assignable_to)
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_int_value("consumedUnits", self.consumed_units)
        writer.write_str_value("externalServiceIdentifier", self.external_service_identifier)
        writer.write_collection_of_object_values("services", self.services)
        writer.write_uuid_value("skuId", self.sku_id)
        writer.write_str_value("skuPartNumber", self.sku_part_number)
        writer.write_collection_of_object_values("subscriptions", self.subscriptions)
        writer.write_collection_of_object_values("waitingMembers", self.waiting_members)
    

