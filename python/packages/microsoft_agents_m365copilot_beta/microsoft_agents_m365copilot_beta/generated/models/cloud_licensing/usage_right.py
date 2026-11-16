from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from ..entity import Entity
    from .allotment import Allotment
    from .assignment import Assignment
    from .service import Service

from ..entity import Entity

@dataclass
class UsageRight(Entity, Parsable):
    # The set of allotments associated with the assignments that combine to form this usageRight.
    allotments: Optional[list[Allotment]] = None
    # The set of assignments that combine to form this usageRight, including both direct assignments and assignments inherited through group membership.
    assignments: Optional[list[Assignment]] = None
    # The externalServiceIdentifier property
    external_service_identifier: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Information about the services associated with the usageRight. Not nullable. Read-only. Supports $filter on the planId property.
    services: Optional[list[Service]] = None
    # Unique identifier (GUID) for the service SKU that is equal to the skuId property on the related subscribedSku object. Read-only. Supports $filter.
    sku_id: Optional[UUID] = None
    # Unique SKU display name that is equal to the skuPartNumber on the related subscribedSku object; for example, AAD_Premium. Read-only.
    sku_part_number: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UsageRight:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UsageRight
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UsageRight()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .allotment import Allotment
        from .assignment import Assignment
        from .service import Service

        from ..entity import Entity
        from .allotment import Allotment
        from .assignment import Assignment
        from .service import Service

        fields: dict[str, Callable[[Any], None]] = {
            "allotments": lambda n : setattr(self, 'allotments', n.get_collection_of_object_values(Allotment)),
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(Assignment)),
            "externalServiceIdentifier": lambda n : setattr(self, 'external_service_identifier', n.get_str_value()),
            "services": lambda n : setattr(self, 'services', n.get_collection_of_object_values(Service)),
            "skuId": lambda n : setattr(self, 'sku_id', n.get_uuid_value()),
            "skuPartNumber": lambda n : setattr(self, 'sku_part_number', n.get_str_value()),
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
        writer.write_collection_of_object_values("allotments", self.allotments)
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_str_value("externalServiceIdentifier", self.external_service_identifier)
        writer.write_collection_of_object_values("services", self.services)
        writer.write_uuid_value("skuId", self.sku_id)
        writer.write_str_value("skuPartNumber", self.sku_part_number)
    

