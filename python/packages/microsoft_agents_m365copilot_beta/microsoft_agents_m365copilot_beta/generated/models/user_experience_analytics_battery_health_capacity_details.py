from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class UserExperienceAnalyticsBatteryHealthCapacityDetails(Entity, Parsable):
    """
    The user experience analytics battery health capacity entity contains count of devices broken down into 3 categories - devices with capacity > 80%, devices with capacity 50-80% and devices with capacity < 50 %.This API provides the count of devices in these 3 categories..
    """
    # Number of active devices within the tenant. Valid values 0 to 2147483647
    active_devices: Optional[int] = None
    # Number of devices whose battery maximum capacity is greater than 50% but lesser than 80%. Valid values 0 to 2147483647
    battery_capacity_fair: Optional[int] = None
    # Number of devices whose battery maximum capacity is greater than 80%. Valid values 0 to 2147483647
    battery_capacity_good: Optional[int] = None
    # Number of devices whose battery maximum capacity is lesser than 50%. Valid values 0 to 2147483647
    battery_capacity_poor: Optional[int] = None
    # Recorded date time of this capacity details instance.
    last_refreshed_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserExperienceAnalyticsBatteryHealthCapacityDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsBatteryHealthCapacityDetails
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserExperienceAnalyticsBatteryHealthCapacityDetails()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "activeDevices": lambda n : setattr(self, 'active_devices', n.get_int_value()),
            "batteryCapacityFair": lambda n : setattr(self, 'battery_capacity_fair', n.get_int_value()),
            "batteryCapacityGood": lambda n : setattr(self, 'battery_capacity_good', n.get_int_value()),
            "batteryCapacityPoor": lambda n : setattr(self, 'battery_capacity_poor', n.get_int_value()),
            "lastRefreshedDateTime": lambda n : setattr(self, 'last_refreshed_date_time', n.get_datetime_value()),
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
        writer.write_int_value("activeDevices", self.active_devices)
        writer.write_int_value("batteryCapacityFair", self.battery_capacity_fair)
        writer.write_int_value("batteryCapacityGood", self.battery_capacity_good)
        writer.write_int_value("batteryCapacityPoor", self.battery_capacity_poor)
        writer.write_datetime_value("lastRefreshedDateTime", self.last_refreshed_date_time)
    

