from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_autopilot_policy_compliance_status import DeviceManagementAutopilotPolicyComplianceStatus
    from .device_management_autopilot_policy_type import DeviceManagementAutopilotPolicyType
    from .entity import Entity

from .entity import Entity

@dataclass
class DeviceManagementAutopilotPolicyStatusDetail(Entity, Parsable):
    """
    Policy status detail item contained by an autopilot event.
    """
    # The complianceStatus property
    compliance_status: Optional[DeviceManagementAutopilotPolicyComplianceStatus] = None
    # The friendly name of the policy.
    display_name: Optional[str] = None
    # The errorode associated with the compliance or enforcement status of the policy. Error code for enforcement status takes precedence if it exists.
    error_code: Optional[int] = None
    # Timestamp of the reported policy status
    last_reported_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The policyType property
    policy_type: Optional[DeviceManagementAutopilotPolicyType] = None
    # Indicates if this policy was tracked as part of the autopilot bootstrap enrollment sync session
    tracked_on_enrollment_status: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementAutopilotPolicyStatusDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementAutopilotPolicyStatusDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementAutopilotPolicyStatusDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_autopilot_policy_compliance_status import DeviceManagementAutopilotPolicyComplianceStatus
        from .device_management_autopilot_policy_type import DeviceManagementAutopilotPolicyType
        from .entity import Entity

        from .device_management_autopilot_policy_compliance_status import DeviceManagementAutopilotPolicyComplianceStatus
        from .device_management_autopilot_policy_type import DeviceManagementAutopilotPolicyType
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "complianceStatus": lambda n : setattr(self, 'compliance_status', n.get_enum_value(DeviceManagementAutopilotPolicyComplianceStatus)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "errorCode": lambda n : setattr(self, 'error_code', n.get_int_value()),
            "lastReportedDateTime": lambda n : setattr(self, 'last_reported_date_time', n.get_datetime_value()),
            "policyType": lambda n : setattr(self, 'policy_type', n.get_enum_value(DeviceManagementAutopilotPolicyType)),
            "trackedOnEnrollmentStatus": lambda n : setattr(self, 'tracked_on_enrollment_status', n.get_bool_value()),
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
        writer.write_enum_value("complianceStatus", self.compliance_status)
        writer.write_str_value("displayName", self.display_name)
        writer.write_int_value("errorCode", self.error_code)
        writer.write_datetime_value("lastReportedDateTime", self.last_reported_date_time)
        writer.write_enum_value("policyType", self.policy_type)
        writer.write_bool_value("trackedOnEnrollmentStatus", self.tracked_on_enrollment_status)
    

