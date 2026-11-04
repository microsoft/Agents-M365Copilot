from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .identity_set import IdentitySet
    from .teamwork_connection import TeamworkConnection
    from .teamwork_hardware_health import TeamworkHardwareHealth
    from .teamwork_login_status import TeamworkLoginStatus
    from .teamwork_peripherals_health import TeamworkPeripheralsHealth
    from .teamwork_software_update_health import TeamworkSoftwareUpdateHealth

from .entity import Entity

@dataclass
class TeamworkDeviceHealth(Entity, Parsable):
    # The connection property
    connection: Optional[TeamworkConnection] = None
    # Identity of the user who created the device health document.
    created_by: Optional[IdentitySet] = None
    # The UTC date and time when the device health document was created.
    created_date_time: Optional[datetime.datetime] = None
    # Health details about the device hardware.
    hardware_health: Optional[TeamworkHardwareHealth] = None
    # Identity of the user who last modified the device health details.
    last_modified_by: Optional[IdentitySet] = None
    # The UTC date and time when the device health detail was last modified.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The login status of Microsoft Teams, Skype for Business, and Exchange.
    login_status: Optional[TeamworkLoginStatus] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Health details about all peripherals (for example, speaker and microphone) attached to a device.
    peripherals_health: Optional[TeamworkPeripheralsHealth] = None
    # Software updates available for the device.
    software_update_health: Optional[TeamworkSoftwareUpdateHealth] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamworkDeviceHealth:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkDeviceHealth
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TeamworkDeviceHealth()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .identity_set import IdentitySet
        from .teamwork_connection import TeamworkConnection
        from .teamwork_hardware_health import TeamworkHardwareHealth
        from .teamwork_login_status import TeamworkLoginStatus
        from .teamwork_peripherals_health import TeamworkPeripheralsHealth
        from .teamwork_software_update_health import TeamworkSoftwareUpdateHealth

        from .entity import Entity
        from .identity_set import IdentitySet
        from .teamwork_connection import TeamworkConnection
        from .teamwork_hardware_health import TeamworkHardwareHealth
        from .teamwork_login_status import TeamworkLoginStatus
        from .teamwork_peripherals_health import TeamworkPeripheralsHealth
        from .teamwork_software_update_health import TeamworkSoftwareUpdateHealth

        fields: dict[str, Callable[[Any], None]] = {
            "connection": lambda n : setattr(self, 'connection', n.get_object_value(TeamworkConnection)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "hardwareHealth": lambda n : setattr(self, 'hardware_health', n.get_object_value(TeamworkHardwareHealth)),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "loginStatus": lambda n : setattr(self, 'login_status', n.get_object_value(TeamworkLoginStatus)),
            "peripheralsHealth": lambda n : setattr(self, 'peripherals_health', n.get_object_value(TeamworkPeripheralsHealth)),
            "softwareUpdateHealth": lambda n : setattr(self, 'software_update_health', n.get_object_value(TeamworkSoftwareUpdateHealth)),
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
        writer.write_object_value("connection", self.connection)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("hardwareHealth", self.hardware_health)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_object_value("loginStatus", self.login_status)
        writer.write_object_value("peripheralsHealth", self.peripherals_health)
        writer.write_object_value("softwareUpdateHealth", self.software_update_health)
    

