from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .managed_device import ManagedDevice
    from .remediation_state import RemediationState
    from .run_state import RunState

from .entity import Entity

@dataclass
class DeviceHealthScriptDeviceState(Entity, Parsable):
    """
    Contains properties for device run state of the device health script.
    """
    # A list of the assignment filter ids used for health script applicability evaluation
    assignment_filter_ids: Optional[list[str]] = None
    # Indicates the type of execution status of the device management script.
    detection_state: Optional[RunState] = None
    # The next timestamp of when the device health script is expected to execute
    expected_state_update_date_time: Optional[datetime.datetime] = None
    # The last timestamp of when the device health script executed
    last_state_update_date_time: Optional[datetime.datetime] = None
    # The last time that Intune Managment Extension synced with Intune
    last_sync_date_time: Optional[datetime.datetime] = None
    # The managed device on which the device health script executed
    managed_device: Optional[ManagedDevice] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Error from the detection script after remediation
    post_remediation_detection_script_error: Optional[str] = None
    # Detection script output after remediation
    post_remediation_detection_script_output: Optional[str] = None
    # Error from the detection script before remediation
    pre_remediation_detection_script_error: Optional[str] = None
    # Output of the detection script before remediation
    pre_remediation_detection_script_output: Optional[str] = None
    # Error output of the remediation script
    remediation_script_error: Optional[str] = None
    # Indicates the type of execution status of the device management script.
    remediation_state: Optional[RemediationState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceHealthScriptDeviceState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceHealthScriptDeviceState
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceHealthScriptDeviceState()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .managed_device import ManagedDevice
        from .remediation_state import RemediationState
        from .run_state import RunState

        from .entity import Entity
        from .managed_device import ManagedDevice
        from .remediation_state import RemediationState
        from .run_state import RunState

        fields: dict[str, Callable[[Any], None]] = {
            "assignmentFilterIds": lambda n : setattr(self, 'assignment_filter_ids', n.get_collection_of_primitive_values(str)),
            "detectionState": lambda n : setattr(self, 'detection_state', n.get_enum_value(RunState)),
            "expectedStateUpdateDateTime": lambda n : setattr(self, 'expected_state_update_date_time', n.get_datetime_value()),
            "lastStateUpdateDateTime": lambda n : setattr(self, 'last_state_update_date_time', n.get_datetime_value()),
            "lastSyncDateTime": lambda n : setattr(self, 'last_sync_date_time', n.get_datetime_value()),
            "managedDevice": lambda n : setattr(self, 'managed_device', n.get_object_value(ManagedDevice)),
            "postRemediationDetectionScriptError": lambda n : setattr(self, 'post_remediation_detection_script_error', n.get_str_value()),
            "postRemediationDetectionScriptOutput": lambda n : setattr(self, 'post_remediation_detection_script_output', n.get_str_value()),
            "preRemediationDetectionScriptError": lambda n : setattr(self, 'pre_remediation_detection_script_error', n.get_str_value()),
            "preRemediationDetectionScriptOutput": lambda n : setattr(self, 'pre_remediation_detection_script_output', n.get_str_value()),
            "remediationScriptError": lambda n : setattr(self, 'remediation_script_error', n.get_str_value()),
            "remediationState": lambda n : setattr(self, 'remediation_state', n.get_enum_value(RemediationState)),
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
        writer.write_collection_of_primitive_values("assignmentFilterIds", self.assignment_filter_ids)
        writer.write_enum_value("detectionState", self.detection_state)
        writer.write_datetime_value("expectedStateUpdateDateTime", self.expected_state_update_date_time)
        writer.write_datetime_value("lastStateUpdateDateTime", self.last_state_update_date_time)
        writer.write_datetime_value("lastSyncDateTime", self.last_sync_date_time)
        writer.write_object_value("managedDevice", self.managed_device)
        writer.write_str_value("postRemediationDetectionScriptError", self.post_remediation_detection_script_error)
        writer.write_str_value("postRemediationDetectionScriptOutput", self.post_remediation_detection_script_output)
        writer.write_str_value("preRemediationDetectionScriptError", self.pre_remediation_detection_script_error)
        writer.write_str_value("preRemediationDetectionScriptOutput", self.pre_remediation_detection_script_output)
        writer.write_str_value("remediationScriptError", self.remediation_script_error)
        writer.write_enum_value("remediationState", self.remediation_state)
    

