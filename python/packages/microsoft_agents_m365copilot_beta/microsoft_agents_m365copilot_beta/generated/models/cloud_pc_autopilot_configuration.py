from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class CloudPcAutopilotConfiguration(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Indicates the number of minutes allowed for the Autopilot application to apply the device preparation profile (DPP) configurations to the device. If the Autopilot application doesn't finish within the specified time (applicationTimeoutInMinutes), the application error is added to the statusDetail property of the cloudPC object. The supported value is an integer between 30 and 360. Required.
    application_timeout_in_minutes: Optional[int] = None
    # The unique identifier (ID) of the Autopilot device preparation profile (DPP) that links a Windows Autopilot device preparation policy to ensure that devices are ready for users after provisioning. Required.
    device_preparation_profile_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates whether the access to the device is allowed when the application of Autopilot device preparation profile (DPP) configurations fails or times out. If true, the status of the device is failed and the device is unable to access; otherwise, the status of the device is provisionedWithWarnings and the device is allowed to access. The default value is false. Required.
    on_failure_device_access_denied: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcAutopilotConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcAutopilotConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcAutopilotConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "applicationTimeoutInMinutes": lambda n : setattr(self, 'application_timeout_in_minutes', n.get_int_value()),
            "devicePreparationProfileId": lambda n : setattr(self, 'device_preparation_profile_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "onFailureDeviceAccessDenied": lambda n : setattr(self, 'on_failure_device_access_denied', n.get_bool_value()),
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
        writer.write_int_value("applicationTimeoutInMinutes", self.application_timeout_in_minutes)
        writer.write_str_value("devicePreparationProfileId", self.device_preparation_profile_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("onFailureDeviceAccessDenied", self.on_failure_device_access_denied)
        writer.write_additional_data_value(self.additional_data)
    

