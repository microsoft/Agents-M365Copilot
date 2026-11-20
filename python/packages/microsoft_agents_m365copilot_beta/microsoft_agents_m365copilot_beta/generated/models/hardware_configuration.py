from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .hardware_configuration_assignment import HardwareConfigurationAssignment
    from .hardware_configuration_device_state import HardwareConfigurationDeviceState
    from .hardware_configuration_format import HardwareConfigurationFormat
    from .hardware_configuration_run_summary import HardwareConfigurationRunSummary
    from .hardware_configuration_user_state import HardwareConfigurationUserState

from .entity import Entity

@dataclass
class HardwareConfiguration(Entity, Parsable):
    """
    BIOS configuration and other settings provides customers the ability to configure hardware/bios settings on the enrolled Windows 10/11 Entra ID joined devices by uploading a configuration file generated with their OEM tool (e.g. Dell Command tool). A BIOS configuration policy can be assigned to multiple devices, allowing admins to remotely control a device's hardware properties (e.g. enable Secure Boot) from the Intune Portal. Supported for Dell only at this time.
    """
    # A list of the Entra user group ids that hardware configuration will be applied to. Only security groups and Office 365 Groups are supported. Optional.
    assignments: Optional[list[HardwareConfigurationAssignment]] = None
    # The file content contains custom hardware settings that will be applied to the assigned devices' BIOS. Max allowed file size is 5KB. Represented as bytes. Required.
    configuration_file_content: Optional[bytes] = None
    # The date and time  of when the BIOS configuration profile was created. The value cannot be modified and is automatically populated when the device is enrolled. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-Only. This property is read-only.
    created_date_time: Optional[datetime.datetime] = None
    # The description of the hardware configuration. Use this to provide context, purpose, applications, etc of the BIOS configuration profile for your organization's admins. Max length is 1000 characters. Optional.
    description: Optional[str] = None
    # List of run states for the hardware configuration across all devices. Read-Only.
    device_run_states: Optional[list[HardwareConfigurationDeviceState]] = None
    # The name of the hardware BIOS configuration profile. It serves as user-friendly name to identify hardware BIOS configuration profiles. Max length is 150 characters. Required. Read-Only.
    display_name: Optional[str] = None
    # The file name for the BIOS configuration profile's ConfigurationFileContent. Max length is 150 characters. Required.
    file_name: Optional[str] = None
    # Indicates the supported oems of hardware configuration
    hardware_configuration_format: Optional[HardwareConfigurationFormat] = None
    # The date and time  of when the BIOS configuration profile was last modified. The value cannot be modified and is automatically populated when the device is enrolled. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-Only. Read-Only. This property is read-only.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # When TRUE, indicates whether the policy-assigned devices' passwords are disabled. When FALSE, indicates they are enabled. Default is FALSE. Required.
    per_device_password_disabled: Optional[bool] = None
    # A list of unique Scope Tag IDs associated with the hardware configuration. Optional.
    role_scope_tag_ids: Optional[list[str]] = None
    # A summary of the results from an attempt to configure hardware settings. Read-Only.
    run_summary: Optional[HardwareConfigurationRunSummary] = None
    # List of run states for the hardware configuration across all users. Read-Only.
    user_run_states: Optional[list[HardwareConfigurationUserState]] = None
    # The version of the hardware configuration (E.g. 1, 2, 3 ...). This is incremented after a change to the BIOS configuration profile's settings file name (FileName property), settings file content (ConfigurationFileContent property), or the PerDevicePasswordDisabled property. Read-Only.
    version: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> HardwareConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: HardwareConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return HardwareConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .hardware_configuration_assignment import HardwareConfigurationAssignment
        from .hardware_configuration_device_state import HardwareConfigurationDeviceState
        from .hardware_configuration_format import HardwareConfigurationFormat
        from .hardware_configuration_run_summary import HardwareConfigurationRunSummary
        from .hardware_configuration_user_state import HardwareConfigurationUserState

        from .entity import Entity
        from .hardware_configuration_assignment import HardwareConfigurationAssignment
        from .hardware_configuration_device_state import HardwareConfigurationDeviceState
        from .hardware_configuration_format import HardwareConfigurationFormat
        from .hardware_configuration_run_summary import HardwareConfigurationRunSummary
        from .hardware_configuration_user_state import HardwareConfigurationUserState

        fields: dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(HardwareConfigurationAssignment)),
            "configurationFileContent": lambda n : setattr(self, 'configuration_file_content', n.get_bytes_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "deviceRunStates": lambda n : setattr(self, 'device_run_states', n.get_collection_of_object_values(HardwareConfigurationDeviceState)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "fileName": lambda n : setattr(self, 'file_name', n.get_str_value()),
            "hardwareConfigurationFormat": lambda n : setattr(self, 'hardware_configuration_format', n.get_enum_value(HardwareConfigurationFormat)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "perDevicePasswordDisabled": lambda n : setattr(self, 'per_device_password_disabled', n.get_bool_value()),
            "roleScopeTagIds": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "runSummary": lambda n : setattr(self, 'run_summary', n.get_object_value(HardwareConfigurationRunSummary)),
            "userRunStates": lambda n : setattr(self, 'user_run_states', n.get_collection_of_object_values(HardwareConfigurationUserState)),
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
        writer.write_bytes_value("configurationFileContent", self.configuration_file_content)
        writer.write_str_value("description", self.description)
        writer.write_collection_of_object_values("deviceRunStates", self.device_run_states)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("fileName", self.file_name)
        writer.write_enum_value("hardwareConfigurationFormat", self.hardware_configuration_format)
        writer.write_bool_value("perDevicePasswordDisabled", self.per_device_password_disabled)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
        writer.write_object_value("runSummary", self.run_summary)
        writer.write_collection_of_object_values("userRunStates", self.user_run_states)
        writer.write_int_value("version", self.version)
    

