from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .identity_set import IdentitySet
    from .teamwork_device_activity import TeamworkDeviceActivity
    from .teamwork_device_activity_state import TeamworkDeviceActivityState
    from .teamwork_device_configuration import TeamworkDeviceConfiguration
    from .teamwork_device_health import TeamworkDeviceHealth
    from .teamwork_device_health_status import TeamworkDeviceHealthStatus
    from .teamwork_device_operation import TeamworkDeviceOperation
    from .teamwork_device_type import TeamworkDeviceType
    from .teamwork_hardware_detail import TeamworkHardwareDetail
    from .teamwork_user_identity import TeamworkUserIdentity

from .entity import Entity

@dataclass
class TeamworkDevice(Entity, Parsable):
    # The activity properties that change based on the device usage.
    activity: Optional[TeamworkDeviceActivity] = None
    # The activity state of the device. The possible values are: unknown, busy, idle, unavailable, unknownFutureValue.
    activity_state: Optional[TeamworkDeviceActivityState] = None
    # The company asset tag assigned by the admin on the device.
    company_asset_tag: Optional[str] = None
    # The configuration properties of the device.
    configuration: Optional[TeamworkDeviceConfiguration] = None
    # Identity of the user who enrolled the device to the tenant.
    created_by: Optional[IdentitySet] = None
    # The UTC date and time when the device was enrolled to the tenant.
    created_date_time: Optional[datetime.datetime] = None
    # The signed-in user on the device.
    current_user: Optional[TeamworkUserIdentity] = None
    # The deviceType property
    device_type: Optional[TeamworkDeviceType] = None
    # The hardwareDetail property
    hardware_detail: Optional[TeamworkHardwareDetail] = None
    # The health properties of the device.
    health: Optional[TeamworkDeviceHealth] = None
    # The health status of the device. The possible values are: unknown, offline, critical, nonUrgent, healthy, unknownFutureValue.
    health_status: Optional[TeamworkDeviceHealthStatus] = None
    # Identity of the user who last modified the device details.
    last_modified_by: Optional[IdentitySet] = None
    # The UTC date and time when the device detail was last modified.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The notes added by the admin to the device.
    notes: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The async operations on the device.
    operations: Optional[list[TeamworkDeviceOperation]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamworkDevice:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkDevice
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TeamworkDevice()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .identity_set import IdentitySet
        from .teamwork_device_activity import TeamworkDeviceActivity
        from .teamwork_device_activity_state import TeamworkDeviceActivityState
        from .teamwork_device_configuration import TeamworkDeviceConfiguration
        from .teamwork_device_health import TeamworkDeviceHealth
        from .teamwork_device_health_status import TeamworkDeviceHealthStatus
        from .teamwork_device_operation import TeamworkDeviceOperation
        from .teamwork_device_type import TeamworkDeviceType
        from .teamwork_hardware_detail import TeamworkHardwareDetail
        from .teamwork_user_identity import TeamworkUserIdentity

        from .entity import Entity
        from .identity_set import IdentitySet
        from .teamwork_device_activity import TeamworkDeviceActivity
        from .teamwork_device_activity_state import TeamworkDeviceActivityState
        from .teamwork_device_configuration import TeamworkDeviceConfiguration
        from .teamwork_device_health import TeamworkDeviceHealth
        from .teamwork_device_health_status import TeamworkDeviceHealthStatus
        from .teamwork_device_operation import TeamworkDeviceOperation
        from .teamwork_device_type import TeamworkDeviceType
        from .teamwork_hardware_detail import TeamworkHardwareDetail
        from .teamwork_user_identity import TeamworkUserIdentity

        fields: dict[str, Callable[[Any], None]] = {
            "activity": lambda n : setattr(self, 'activity', n.get_object_value(TeamworkDeviceActivity)),
            "activityState": lambda n : setattr(self, 'activity_state', n.get_enum_value(TeamworkDeviceActivityState)),
            "companyAssetTag": lambda n : setattr(self, 'company_asset_tag', n.get_str_value()),
            "configuration": lambda n : setattr(self, 'configuration', n.get_object_value(TeamworkDeviceConfiguration)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "currentUser": lambda n : setattr(self, 'current_user', n.get_object_value(TeamworkUserIdentity)),
            "deviceType": lambda n : setattr(self, 'device_type', n.get_enum_value(TeamworkDeviceType)),
            "hardwareDetail": lambda n : setattr(self, 'hardware_detail', n.get_object_value(TeamworkHardwareDetail)),
            "health": lambda n : setattr(self, 'health', n.get_object_value(TeamworkDeviceHealth)),
            "healthStatus": lambda n : setattr(self, 'health_status', n.get_enum_value(TeamworkDeviceHealthStatus)),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_str_value()),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(TeamworkDeviceOperation)),
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
        writer.write_object_value("activity", self.activity)
        writer.write_enum_value("activityState", self.activity_state)
        writer.write_str_value("companyAssetTag", self.company_asset_tag)
        writer.write_object_value("configuration", self.configuration)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("currentUser", self.current_user)
        writer.write_enum_value("deviceType", self.device_type)
        writer.write_object_value("hardwareDetail", self.hardware_detail)
        writer.write_object_value("health", self.health)
        writer.write_enum_value("healthStatus", self.health_status)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("notes", self.notes)
        writer.write_collection_of_object_values("operations", self.operations)
    

