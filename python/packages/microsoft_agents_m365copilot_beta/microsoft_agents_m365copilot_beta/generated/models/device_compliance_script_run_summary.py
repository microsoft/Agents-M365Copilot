from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class DeviceComplianceScriptRunSummary(Entity, Parsable):
    """
    Contains properties for the run summary of a device management script.
    """
    # Number of devices on which the detection script execution encountered an error and did not complete. Valid values -2147483648 to 2147483647
    detection_script_error_device_count: Optional[int] = None
    # Number of devices which have not yet run the latest version of the device compliance script. Valid values -2147483648 to 2147483647
    detection_script_pending_device_count: Optional[int] = None
    # Number of devices for which the detection script found an issue. Valid values -2147483648 to 2147483647
    issue_detected_device_count: Optional[int] = None
    # Last run time for the script across all devices
    last_script_run_date_time: Optional[datetime.datetime] = None
    # Number of devices for which the detection script did not find an issue and the device is healthy. Valid values -2147483648 to 2147483647
    no_issue_detected_device_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceComplianceScriptRunSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceComplianceScriptRunSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceComplianceScriptRunSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "detectionScriptErrorDeviceCount": lambda n : setattr(self, 'detection_script_error_device_count', n.get_int_value()),
            "detectionScriptPendingDeviceCount": lambda n : setattr(self, 'detection_script_pending_device_count', n.get_int_value()),
            "issueDetectedDeviceCount": lambda n : setattr(self, 'issue_detected_device_count', n.get_int_value()),
            "lastScriptRunDateTime": lambda n : setattr(self, 'last_script_run_date_time', n.get_datetime_value()),
            "noIssueDetectedDeviceCount": lambda n : setattr(self, 'no_issue_detected_device_count', n.get_int_value()),
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
        writer.write_int_value("detectionScriptErrorDeviceCount", self.detection_script_error_device_count)
        writer.write_int_value("detectionScriptPendingDeviceCount", self.detection_script_pending_device_count)
        writer.write_int_value("issueDetectedDeviceCount", self.issue_detected_device_count)
        writer.write_datetime_value("lastScriptRunDateTime", self.last_script_run_date_time)
        writer.write_int_value("noIssueDetectedDeviceCount", self.no_issue_detected_device_count)
    

