from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .servicing_period import ServicingPeriod

from ..entity import Entity

@dataclass
class Edition(Entity, Parsable):
    # The device family targeted by the edition.
    device_family: Optional[str] = None
    # The date and time when the edition reached the end of service. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    end_of_service_date_time: Optional[datetime.datetime] = None
    # The date and time when the edition became available to the general customers for the first time. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    general_availability_date_time: Optional[datetime.datetime] = None
    # Indicates whether the edition is in service or out of service.
    is_in_service: Optional[bool] = None
    # The name of the edition. Read-only.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The public name of the edition. Read-only.
    released_name: Optional[str] = None
    # The servicingPeriods property
    servicing_periods: Optional[list[ServicingPeriod]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Edition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Edition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Edition()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .servicing_period import ServicingPeriod

        from ..entity import Entity
        from .servicing_period import ServicingPeriod

        fields: dict[str, Callable[[Any], None]] = {
            "deviceFamily": lambda n : setattr(self, 'device_family', n.get_str_value()),
            "endOfServiceDateTime": lambda n : setattr(self, 'end_of_service_date_time', n.get_datetime_value()),
            "generalAvailabilityDateTime": lambda n : setattr(self, 'general_availability_date_time', n.get_datetime_value()),
            "isInService": lambda n : setattr(self, 'is_in_service', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "releasedName": lambda n : setattr(self, 'released_name', n.get_str_value()),
            "servicingPeriods": lambda n : setattr(self, 'servicing_periods', n.get_collection_of_object_values(ServicingPeriod)),
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
        writer.write_str_value("deviceFamily", self.device_family)
        writer.write_datetime_value("endOfServiceDateTime", self.end_of_service_date_time)
        writer.write_datetime_value("generalAvailabilityDateTime", self.general_availability_date_time)
        writer.write_bool_value("isInService", self.is_in_service)
        writer.write_str_value("name", self.name)
        writer.write_str_value("releasedName", self.released_name)
        writer.write_collection_of_object_values("servicingPeriods", self.servicing_periods)
    

