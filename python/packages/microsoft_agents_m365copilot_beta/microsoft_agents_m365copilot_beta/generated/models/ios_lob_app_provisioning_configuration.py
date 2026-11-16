from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .ios_lob_app_provisioning_configuration_assignment import IosLobAppProvisioningConfigurationAssignment
    from .managed_device_mobile_app_configuration_device_status import ManagedDeviceMobileAppConfigurationDeviceStatus
    from .managed_device_mobile_app_configuration_user_status import ManagedDeviceMobileAppConfigurationUserStatus
    from .mobile_app_provisioning_config_group_assignment import MobileAppProvisioningConfigGroupAssignment

from .entity import Entity

@dataclass
class IosLobAppProvisioningConfiguration(Entity, Parsable):
    """
    This topic provides descriptions of the declared methods, properties and relationships exposed by the iOS LOB App Provisioning Configuration resource.
    """
    # The associated group assignments for IosLobAppProvisioningConfiguration, this determines which devices/users the IOS LOB app provisioning conifguration will be targeted to.
    assignments: Optional[list[IosLobAppProvisioningConfigurationAssignment]] = None
    # DateTime the object was created.
    created_date_time: Optional[datetime.datetime] = None
    # Admin provided description of the Device Configuration.
    description: Optional[str] = None
    # The list of device installation states for this mobile app configuration.
    device_statuses: Optional[list[ManagedDeviceMobileAppConfigurationDeviceStatus]] = None
    # Admin provided name of the device configuration.
    display_name: Optional[str] = None
    # Optional profile expiration date and time. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default.
    expiration_date_time: Optional[datetime.datetime] = None
    # The associated group assignments.
    group_assignments: Optional[list[MobileAppProvisioningConfigGroupAssignment]] = None
    # DateTime the object was last modified.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Payload. (UTF8 encoded byte array)
    payload: Optional[bytes] = None
    # Payload file name (.mobileprovision
    payload_file_name: Optional[str] = None
    # List of Scope Tags for this iOS LOB app provisioning configuration entity.
    role_scope_tag_ids: Optional[list[str]] = None
    # The list of user installation states for this mobile app configuration.
    user_statuses: Optional[list[ManagedDeviceMobileAppConfigurationUserStatus]] = None
    # Version of the device configuration.
    version: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IosLobAppProvisioningConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IosLobAppProvisioningConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IosLobAppProvisioningConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .ios_lob_app_provisioning_configuration_assignment import IosLobAppProvisioningConfigurationAssignment
        from .managed_device_mobile_app_configuration_device_status import ManagedDeviceMobileAppConfigurationDeviceStatus
        from .managed_device_mobile_app_configuration_user_status import ManagedDeviceMobileAppConfigurationUserStatus
        from .mobile_app_provisioning_config_group_assignment import MobileAppProvisioningConfigGroupAssignment

        from .entity import Entity
        from .ios_lob_app_provisioning_configuration_assignment import IosLobAppProvisioningConfigurationAssignment
        from .managed_device_mobile_app_configuration_device_status import ManagedDeviceMobileAppConfigurationDeviceStatus
        from .managed_device_mobile_app_configuration_user_status import ManagedDeviceMobileAppConfigurationUserStatus
        from .mobile_app_provisioning_config_group_assignment import MobileAppProvisioningConfigGroupAssignment

        fields: dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(IosLobAppProvisioningConfigurationAssignment)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "deviceStatuses": lambda n : setattr(self, 'device_statuses', n.get_collection_of_object_values(ManagedDeviceMobileAppConfigurationDeviceStatus)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "groupAssignments": lambda n : setattr(self, 'group_assignments', n.get_collection_of_object_values(MobileAppProvisioningConfigGroupAssignment)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "payload": lambda n : setattr(self, 'payload', n.get_bytes_value()),
            "payloadFileName": lambda n : setattr(self, 'payload_file_name', n.get_str_value()),
            "roleScopeTagIds": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "userStatuses": lambda n : setattr(self, 'user_statuses', n.get_collection_of_object_values(ManagedDeviceMobileAppConfigurationUserStatus)),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
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
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_collection_of_object_values("deviceStatuses", self.device_statuses)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_collection_of_object_values("groupAssignments", self.group_assignments)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_bytes_value("payload", self.payload)
        writer.write_str_value("payloadFileName", self.payload_file_name)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
        writer.write_collection_of_object_values("userStatuses", self.user_statuses)
        writer.write_int_value("version", self.version)
    

