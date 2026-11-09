from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .remediation_state import RemediationState
    from .run_state import RunState

@dataclass
class DeviceHealthScriptPolicyState(AdditionalDataHolder, Parsable):
    """
    Contains properties for policy run state of the device health script.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # A list of the assignment filter ids used for health script applicability evaluation
    assignment_filter_ids: Optional[list[str]] = None
    # Indicates the type of execution status of the device management script.
    detection_state: Optional[RunState] = None
    # The Intune device Id
    device_id: Optional[str] = None
    # Display name of the device
    device_name: Optional[str] = None
    # The next timestamp of when the device health script is expected to execute
    expected_state_update_date_time: Optional[datetime.datetime] = None
    # Key of the device health script policy state is a concatenation of the MT sideCar policy Id and Intune device Id
    id: Optional[str] = None
    # The last timestamp of when the device health script executed
    last_state_update_date_time: Optional[datetime.datetime] = None
    # The last time that Intune Managment Extension synced with Intune
    last_sync_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Value of the OS Version in string
    os_version: Optional[str] = None
    # The MT sideCar policy Id
    policy_id: Optional[str] = None
    # Display name of the device health script
    policy_name: Optional[str] = None
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
    # Name of the user whom ran the device health script
    user_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceHealthScriptPolicyState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceHealthScriptPolicyState
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceHealthScriptPolicyState()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .remediation_state import RemediationState
        from .run_state import RunState

        from .remediation_state import RemediationState
        from .run_state import RunState

        fields: dict[str, Callable[[Any], None]] = {
            "assignmentFilterIds": lambda n : setattr(self, 'assignment_filter_ids', n.get_collection_of_primitive_values(str)),
            "detectionState": lambda n : setattr(self, 'detection_state', n.get_enum_value(RunState)),
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "expectedStateUpdateDateTime": lambda n : setattr(self, 'expected_state_update_date_time', n.get_datetime_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "lastStateUpdateDateTime": lambda n : setattr(self, 'last_state_update_date_time', n.get_datetime_value()),
            "lastSyncDateTime": lambda n : setattr(self, 'last_sync_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "osVersion": lambda n : setattr(self, 'os_version', n.get_str_value()),
            "policyId": lambda n : setattr(self, 'policy_id', n.get_str_value()),
            "policyName": lambda n : setattr(self, 'policy_name', n.get_str_value()),
            "postRemediationDetectionScriptError": lambda n : setattr(self, 'post_remediation_detection_script_error', n.get_str_value()),
            "postRemediationDetectionScriptOutput": lambda n : setattr(self, 'post_remediation_detection_script_output', n.get_str_value()),
            "preRemediationDetectionScriptError": lambda n : setattr(self, 'pre_remediation_detection_script_error', n.get_str_value()),
            "preRemediationDetectionScriptOutput": lambda n : setattr(self, 'pre_remediation_detection_script_output', n.get_str_value()),
            "remediationScriptError": lambda n : setattr(self, 'remediation_script_error', n.get_str_value()),
            "remediationState": lambda n : setattr(self, 'remediation_state', n.get_enum_value(RemediationState)),
            "userName": lambda n : setattr(self, 'user_name', n.get_str_value()),
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
        writer.write_collection_of_primitive_values("assignmentFilterIds", self.assignment_filter_ids)
        writer.write_enum_value("detectionState", self.detection_state)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_datetime_value("expectedStateUpdateDateTime", self.expected_state_update_date_time)
        writer.write_str_value("id", self.id)
        writer.write_datetime_value("lastStateUpdateDateTime", self.last_state_update_date_time)
        writer.write_datetime_value("lastSyncDateTime", self.last_sync_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("osVersion", self.os_version)
        writer.write_str_value("policyId", self.policy_id)
        writer.write_str_value("policyName", self.policy_name)
        writer.write_str_value("postRemediationDetectionScriptError", self.post_remediation_detection_script_error)
        writer.write_str_value("postRemediationDetectionScriptOutput", self.post_remediation_detection_script_output)
        writer.write_str_value("preRemediationDetectionScriptError", self.pre_remediation_detection_script_error)
        writer.write_str_value("preRemediationDetectionScriptOutput", self.pre_remediation_detection_script_output)
        writer.write_str_value("remediationScriptError", self.remediation_script_error)
        writer.write_enum_value("remediationState", self.remediation_state)
        writer.write_str_value("userName", self.user_name)
        writer.write_additional_data_value(self.additional_data)
    

