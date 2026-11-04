from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class UnmanagedDevice(AdditionalDataHolder, Parsable):
    """
    Unmanaged device discovered in the network.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Device name.
    device_name: Optional[str] = None
    # Domain.
    domain: Optional[str] = None
    # IP address.
    ip_address: Optional[str] = None
    # Last logged on user.
    last_logged_on_user: Optional[str] = None
    # Last seen date and time.
    last_seen_date_time: Optional[datetime.datetime] = None
    # Location.
    location: Optional[str] = None
    # MAC address.
    mac_address: Optional[str] = None
    # Manufacturer.
    manufacturer: Optional[str] = None
    # Model.
    model: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Operating system.
    os: Optional[str] = None
    # Operating system version.
    os_version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UnmanagedDevice:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UnmanagedDevice
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UnmanagedDevice()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "domain": lambda n : setattr(self, 'domain', n.get_str_value()),
            "ipAddress": lambda n : setattr(self, 'ip_address', n.get_str_value()),
            "lastLoggedOnUser": lambda n : setattr(self, 'last_logged_on_user', n.get_str_value()),
            "lastSeenDateTime": lambda n : setattr(self, 'last_seen_date_time', n.get_datetime_value()),
            "location": lambda n : setattr(self, 'location', n.get_str_value()),
            "macAddress": lambda n : setattr(self, 'mac_address', n.get_str_value()),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "os": lambda n : setattr(self, 'os', n.get_str_value()),
            "osVersion": lambda n : setattr(self, 'os_version', n.get_str_value()),
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
        writer.write_str_value("deviceName", self.device_name)
        writer.write_str_value("domain", self.domain)
        writer.write_str_value("ipAddress", self.ip_address)
        writer.write_str_value("lastLoggedOnUser", self.last_logged_on_user)
        writer.write_datetime_value("lastSeenDateTime", self.last_seen_date_time)
        writer.write_str_value("location", self.location)
        writer.write_str_value("macAddress", self.mac_address)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_str_value("model", self.model)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("os", self.os)
        writer.write_str_value("osVersion", self.os_version)
        writer.write_additional_data_value(self.additional_data)
    

