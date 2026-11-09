from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class CloudPcFrontLineServicePlan(Entity, Parsable):
    # The allotmentLicensesCount property
    allotment_licenses_count: Optional[int] = None
    # The display name of the frontline service plan. For example, 2vCPU/8GB/128GB Front-line or 4vCPU/16GB/256GB Front-line.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The total number of frontline service plans purchased by the customer.
    total_count: Optional[int] = None
    # The number of service plans that have been used for the account.
    used_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcFrontLineServicePlan:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcFrontLineServicePlan
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcFrontLineServicePlan()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "allotmentLicensesCount": lambda n : setattr(self, 'allotment_licenses_count', n.get_int_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "totalCount": lambda n : setattr(self, 'total_count', n.get_int_value()),
            "usedCount": lambda n : setattr(self, 'used_count', n.get_int_value()),
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
        writer.write_int_value("allotmentLicensesCount", self.allotment_licenses_count)
        writer.write_str_value("displayName", self.display_name)
        writer.write_int_value("totalCount", self.total_count)
        writer.write_int_value("usedCount", self.used_count)
    

