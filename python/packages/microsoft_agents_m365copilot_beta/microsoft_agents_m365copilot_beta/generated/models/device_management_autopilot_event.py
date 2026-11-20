from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .enrollment_state import EnrollmentState
    from .entity import Entity
    from .windows_autopilot_deployment_state import WindowsAutopilotDeploymentState
    from .windows_autopilot_enrollment_type import WindowsAutopilotEnrollmentType

from .entity import Entity

@dataclass
class DeviceManagementAutopilotEvent(Entity, Parsable):
    """
    Represents an Autopilot flow event.
    """
    # Time spent in user ESP.
    account_setup_duration: Optional[datetime.timedelta] = None
    # Deployment states for Autopilot devices
    account_setup_status: Optional[WindowsAutopilotDeploymentState] = None
    # Autopilot deployment duration including enrollment.
    deployment_duration: Optional[datetime.timedelta] = None
    # Deployment end time.
    deployment_end_date_time: Optional[datetime.datetime] = None
    # Deployment start time.
    deployment_start_date_time: Optional[datetime.datetime] = None
    # Deployment states for Autopilot devices
    deployment_state: Optional[WindowsAutopilotDeploymentState] = None
    # Total deployment duration from enrollment to Desktop screen.
    deployment_total_duration: Optional[datetime.timedelta] = None
    # Device id associated with the object
    device_id: Optional[str] = None
    # Device registration date.
    device_registered_date_time: Optional[datetime.datetime] = None
    # Device serial number.
    device_serial_number: Optional[str] = None
    # Time spent in device ESP.
    device_setup_duration: Optional[datetime.timedelta] = None
    # Deployment states for Autopilot devices
    device_setup_status: Optional[WindowsAutopilotDeploymentState] = None
    # Enrollment failure details.
    enrollment_failure_details: Optional[str] = None
    # Device enrollment start date.
    enrollment_start_date_time: Optional[datetime.datetime] = None
    # The enrollmentState property
    enrollment_state: Optional[EnrollmentState] = None
    # The enrollmentType property
    enrollment_type: Optional[WindowsAutopilotEnrollmentType] = None
    # Time when the event occurred .
    event_date_time: Optional[datetime.datetime] = None
    # Managed device name.
    managed_device_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Device operating system version.
    os_version: Optional[str] = None
    # UserId id associated with the object
    user_id: Optional[str] = None
    # User principal name used to enroll the device.
    user_principal_name: Optional[str] = None
    # Autopilot profile name.
    windows_autopilot_deployment_profile_display_name: Optional[str] = None
    # Enrollment Status Page profile name
    windows10_enrollment_completion_page_configuration_display_name: Optional[str] = None
    # Enrollment Status Page profile ID
    windows10_enrollment_completion_page_configuration_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementAutopilotEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementAutopilotEvent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementAutopilotEvent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .enrollment_state import EnrollmentState
        from .entity import Entity
        from .windows_autopilot_deployment_state import WindowsAutopilotDeploymentState
        from .windows_autopilot_enrollment_type import WindowsAutopilotEnrollmentType

        from .enrollment_state import EnrollmentState
        from .entity import Entity
        from .windows_autopilot_deployment_state import WindowsAutopilotDeploymentState
        from .windows_autopilot_enrollment_type import WindowsAutopilotEnrollmentType

        fields: dict[str, Callable[[Any], None]] = {
            "accountSetupDuration": lambda n : setattr(self, 'account_setup_duration', n.get_timedelta_value()),
            "accountSetupStatus": lambda n : setattr(self, 'account_setup_status', n.get_enum_value(WindowsAutopilotDeploymentState)),
            "deploymentDuration": lambda n : setattr(self, 'deployment_duration', n.get_timedelta_value()),
            "deploymentEndDateTime": lambda n : setattr(self, 'deployment_end_date_time', n.get_datetime_value()),
            "deploymentStartDateTime": lambda n : setattr(self, 'deployment_start_date_time', n.get_datetime_value()),
            "deploymentState": lambda n : setattr(self, 'deployment_state', n.get_enum_value(WindowsAutopilotDeploymentState)),
            "deploymentTotalDuration": lambda n : setattr(self, 'deployment_total_duration', n.get_timedelta_value()),
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "deviceRegisteredDateTime": lambda n : setattr(self, 'device_registered_date_time', n.get_datetime_value()),
            "deviceSerialNumber": lambda n : setattr(self, 'device_serial_number', n.get_str_value()),
            "deviceSetupDuration": lambda n : setattr(self, 'device_setup_duration', n.get_timedelta_value()),
            "deviceSetupStatus": lambda n : setattr(self, 'device_setup_status', n.get_enum_value(WindowsAutopilotDeploymentState)),
            "enrollmentFailureDetails": lambda n : setattr(self, 'enrollment_failure_details', n.get_str_value()),
            "enrollmentStartDateTime": lambda n : setattr(self, 'enrollment_start_date_time', n.get_datetime_value()),
            "enrollmentState": lambda n : setattr(self, 'enrollment_state', n.get_enum_value(EnrollmentState)),
            "enrollmentType": lambda n : setattr(self, 'enrollment_type', n.get_enum_value(WindowsAutopilotEnrollmentType)),
            "eventDateTime": lambda n : setattr(self, 'event_date_time', n.get_datetime_value()),
            "managedDeviceName": lambda n : setattr(self, 'managed_device_name', n.get_str_value()),
            "osVersion": lambda n : setattr(self, 'os_version', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
            "windowsAutopilotDeploymentProfileDisplayName": lambda n : setattr(self, 'windows_autopilot_deployment_profile_display_name', n.get_str_value()),
            "windows10EnrollmentCompletionPageConfigurationDisplayName": lambda n : setattr(self, 'windows10_enrollment_completion_page_configuration_display_name', n.get_str_value()),
            "windows10EnrollmentCompletionPageConfigurationId": lambda n : setattr(self, 'windows10_enrollment_completion_page_configuration_id', n.get_str_value()),
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
        writer.write_timedelta_value("accountSetupDuration", self.account_setup_duration)
        writer.write_enum_value("accountSetupStatus", self.account_setup_status)
        writer.write_timedelta_value("deploymentDuration", self.deployment_duration)
        writer.write_datetime_value("deploymentEndDateTime", self.deployment_end_date_time)
        writer.write_datetime_value("deploymentStartDateTime", self.deployment_start_date_time)
        writer.write_enum_value("deploymentState", self.deployment_state)
        writer.write_timedelta_value("deploymentTotalDuration", self.deployment_total_duration)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_datetime_value("deviceRegisteredDateTime", self.device_registered_date_time)
        writer.write_str_value("deviceSerialNumber", self.device_serial_number)
        writer.write_timedelta_value("deviceSetupDuration", self.device_setup_duration)
        writer.write_enum_value("deviceSetupStatus", self.device_setup_status)
        writer.write_str_value("enrollmentFailureDetails", self.enrollment_failure_details)
        writer.write_datetime_value("enrollmentStartDateTime", self.enrollment_start_date_time)
        writer.write_enum_value("enrollmentState", self.enrollment_state)
        writer.write_enum_value("enrollmentType", self.enrollment_type)
        writer.write_datetime_value("eventDateTime", self.event_date_time)
        writer.write_str_value("managedDeviceName", self.managed_device_name)
        writer.write_str_value("osVersion", self.os_version)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_str_value("windowsAutopilotDeploymentProfileDisplayName", self.windows_autopilot_deployment_profile_display_name)
        writer.write_str_value("windows10EnrollmentCompletionPageConfigurationDisplayName", self.windows10_enrollment_completion_page_configuration_display_name)
        writer.write_str_value("windows10EnrollmentCompletionPageConfigurationId", self.windows10_enrollment_completion_page_configuration_id)
    

