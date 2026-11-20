from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_script_assignment import DeviceManagementScriptAssignment
    from .device_management_script_device_state import DeviceManagementScriptDeviceState
    from .device_management_script_group_assignment import DeviceManagementScriptGroupAssignment
    from .device_management_script_run_summary import DeviceManagementScriptRunSummary
    from .device_management_script_user_state import DeviceManagementScriptUserState
    from .entity import Entity
    from .run_as_account_type import RunAsAccountType

from .entity import Entity

@dataclass
class DeviceShellScript(Entity, Parsable):
    """
    Intune will provide customer the ability to run their Shell scripts on the enrolled Mac OS devices. The script can be run once or periodically.
    """
    # The list of group assignments for the device management script.
    assignments: Optional[list[DeviceManagementScriptAssignment]] = None
    # Does not notify the user a script is being executed
    block_execution_notifications: Optional[bool] = None
    # The date and time the device management script was created. This property is read-only.
    created_date_time: Optional[datetime.datetime] = None
    # Optional description for the device management script.
    description: Optional[str] = None
    # List of run states for this script across all devices.
    device_run_states: Optional[list[DeviceManagementScriptDeviceState]] = None
    # Name of the device management script.
    display_name: Optional[str] = None
    # The interval for script to run. If not defined the script will run once
    execution_frequency: Optional[datetime.timedelta] = None
    # Script file name.
    file_name: Optional[str] = None
    # The list of group assignments for the device management script.
    group_assignments: Optional[list[DeviceManagementScriptGroupAssignment]] = None
    # The date and time the device management script was last modified. This property is read-only.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Number of times for the script to be retried if it fails
    retry_count: Optional[int] = None
    # List of Scope Tag IDs for this PowerShellScript instance.
    role_scope_tag_ids: Optional[list[str]] = None
    # Indicates the type of execution context the app runs in.
    run_as_account: Optional[RunAsAccountType] = None
    # Run summary for device management script.
    run_summary: Optional[DeviceManagementScriptRunSummary] = None
    # The script content.
    script_content: Optional[bytes] = None
    # List of run states for this script across all users.
    user_run_states: Optional[list[DeviceManagementScriptUserState]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceShellScript:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceShellScript
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceShellScript()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_script_assignment import DeviceManagementScriptAssignment
        from .device_management_script_device_state import DeviceManagementScriptDeviceState
        from .device_management_script_group_assignment import DeviceManagementScriptGroupAssignment
        from .device_management_script_run_summary import DeviceManagementScriptRunSummary
        from .device_management_script_user_state import DeviceManagementScriptUserState
        from .entity import Entity
        from .run_as_account_type import RunAsAccountType

        from .device_management_script_assignment import DeviceManagementScriptAssignment
        from .device_management_script_device_state import DeviceManagementScriptDeviceState
        from .device_management_script_group_assignment import DeviceManagementScriptGroupAssignment
        from .device_management_script_run_summary import DeviceManagementScriptRunSummary
        from .device_management_script_user_state import DeviceManagementScriptUserState
        from .entity import Entity
        from .run_as_account_type import RunAsAccountType

        fields: dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(DeviceManagementScriptAssignment)),
            "blockExecutionNotifications": lambda n : setattr(self, 'block_execution_notifications', n.get_bool_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "deviceRunStates": lambda n : setattr(self, 'device_run_states', n.get_collection_of_object_values(DeviceManagementScriptDeviceState)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "executionFrequency": lambda n : setattr(self, 'execution_frequency', n.get_timedelta_value()),
            "fileName": lambda n : setattr(self, 'file_name', n.get_str_value()),
            "groupAssignments": lambda n : setattr(self, 'group_assignments', n.get_collection_of_object_values(DeviceManagementScriptGroupAssignment)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "retryCount": lambda n : setattr(self, 'retry_count', n.get_int_value()),
            "roleScopeTagIds": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "runAsAccount": lambda n : setattr(self, 'run_as_account', n.get_enum_value(RunAsAccountType)),
            "runSummary": lambda n : setattr(self, 'run_summary', n.get_object_value(DeviceManagementScriptRunSummary)),
            "scriptContent": lambda n : setattr(self, 'script_content', n.get_bytes_value()),
            "userRunStates": lambda n : setattr(self, 'user_run_states', n.get_collection_of_object_values(DeviceManagementScriptUserState)),
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
        writer.write_bool_value("blockExecutionNotifications", self.block_execution_notifications)
        writer.write_str_value("description", self.description)
        writer.write_collection_of_object_values("deviceRunStates", self.device_run_states)
        writer.write_str_value("displayName", self.display_name)
        writer.write_timedelta_value("executionFrequency", self.execution_frequency)
        writer.write_str_value("fileName", self.file_name)
        writer.write_collection_of_object_values("groupAssignments", self.group_assignments)
        writer.write_int_value("retryCount", self.retry_count)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
        writer.write_enum_value("runAsAccount", self.run_as_account)
        writer.write_object_value("runSummary", self.run_summary)
        writer.write_bytes_value("scriptContent", self.script_content)
        writer.write_collection_of_object_values("userRunStates", self.user_run_states)
    

