from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .filter import Filter
    from .provisioning_flow import ProvisioningFlow

from ..entity import Entity

@dataclass
class OutboundProvisioningFlowSet(Entity, Parsable):
    # The date and time when the flowSet was created. The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime.datetime] = None
    # The display name of the flowSet provided by the caller.
    display_name: Optional[str] = None
    # The collection of provisioning filters applicable to all the flows under the given flowSet.
    filter: Optional[Filter] = None
    # The date and time when the flowSet was most recently changed. The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A flow that provisions relevant records of a given entity type in the Microsoft 365 tenant.
    provisioning_flows: Optional[list[ProvisioningFlow]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OutboundProvisioningFlowSet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OutboundProvisioningFlowSet
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OutboundProvisioningFlowSet()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .filter import Filter
        from .provisioning_flow import ProvisioningFlow

        from ..entity import Entity
        from .filter import Filter
        from .provisioning_flow import ProvisioningFlow

        fields: dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "filter": lambda n : setattr(self, 'filter', n.get_object_value(Filter)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "provisioningFlows": lambda n : setattr(self, 'provisioning_flows', n.get_collection_of_object_values(ProvisioningFlow)),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("filter", self.filter)
        writer.write_collection_of_object_values("provisioningFlows", self.provisioning_flows)
    

