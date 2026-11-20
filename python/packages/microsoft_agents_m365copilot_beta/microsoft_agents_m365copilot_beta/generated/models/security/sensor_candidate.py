from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .device_type import DeviceType

from ..entity import Entity

@dataclass
class SensorCandidate(Entity, Parsable):
    # The DNS name of the computer associated with the sensor.
    computer_dns_name: Optional[str] = None
    # The domain name of the sensor.
    domain_name: Optional[str] = None
    # The date and time when the sensor was last seen.
    last_seen_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The version of the Defender for Identity sensor client.  Supports $filter (eq).
    sense_client_version: Optional[str] = None
    # The list of device types for the sensor. The possible values are: domainController, adfs, adcs, entraConnect unknownFutureValue. This flagged enumeration allows multiple members to be returned simultaneously.
    sensor_types: Optional[list[DeviceType]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SensorCandidate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SensorCandidate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SensorCandidate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .device_type import DeviceType

        from ..entity import Entity
        from .device_type import DeviceType

        fields: dict[str, Callable[[Any], None]] = {
            "computerDnsName": lambda n : setattr(self, 'computer_dns_name', n.get_str_value()),
            "domainName": lambda n : setattr(self, 'domain_name', n.get_str_value()),
            "lastSeenDateTime": lambda n : setattr(self, 'last_seen_date_time', n.get_datetime_value()),
            "senseClientVersion": lambda n : setattr(self, 'sense_client_version', n.get_str_value()),
            "sensorTypes": lambda n : setattr(self, 'sensor_types', n.get_collection_of_enum_values(DeviceType)),
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
        writer.write_str_value("computerDnsName", self.computer_dns_name)
        writer.write_str_value("domainName", self.domain_name)
        writer.write_datetime_value("lastSeenDateTime", self.last_seen_date_time)
        writer.write_str_value("senseClientVersion", self.sense_client_version)
        writer.write_collection_of_enum_values("sensorTypes", self.sensor_types)
    

