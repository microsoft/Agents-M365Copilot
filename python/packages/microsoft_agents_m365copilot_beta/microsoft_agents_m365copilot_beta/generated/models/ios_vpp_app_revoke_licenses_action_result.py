from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .action_state import ActionState
    from .vpp_token_action_failure_reason import VppTokenActionFailureReason

@dataclass
class IosVppAppRevokeLicensesActionResult(AdditionalDataHolder, Parsable):
    """
    Defines results for actions on iOS Vpp Apps, contains inherited properties for ActionResult.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Possible types of reasons for an Apple Volume Purchase Program token action failure.
    action_failure_reason: Optional[VppTokenActionFailureReason] = None
    # Action name
    action_name: Optional[str] = None
    # The actionState property
    action_state: Optional[ActionState] = None
    # A count of the number of licenses for which revoke failed.
    failed_licenses_count: Optional[int] = None
    # Time the action state was last updated
    last_updated_date_time: Optional[datetime.datetime] = None
    # DeviceId associated with the action.
    managed_device_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Time the action was initiated
    start_date_time: Optional[datetime.datetime] = None
    # A count of the number of licenses for which revoke was attempted.
    total_licenses_count: Optional[int] = None
    # UserId associated with the action.
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IosVppAppRevokeLicensesActionResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IosVppAppRevokeLicensesActionResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IosVppAppRevokeLicensesActionResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .action_state import ActionState
        from .vpp_token_action_failure_reason import VppTokenActionFailureReason

        from .action_state import ActionState
        from .vpp_token_action_failure_reason import VppTokenActionFailureReason

        fields: dict[str, Callable[[Any], None]] = {
            "actionFailureReason": lambda n : setattr(self, 'action_failure_reason', n.get_enum_value(VppTokenActionFailureReason)),
            "actionName": lambda n : setattr(self, 'action_name', n.get_str_value()),
            "actionState": lambda n : setattr(self, 'action_state', n.get_enum_value(ActionState)),
            "failedLicensesCount": lambda n : setattr(self, 'failed_licenses_count', n.get_int_value()),
            "lastUpdatedDateTime": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "managedDeviceId": lambda n : setattr(self, 'managed_device_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "totalLicensesCount": lambda n : setattr(self, 'total_licenses_count', n.get_int_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
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
        writer.write_enum_value("actionFailureReason", self.action_failure_reason)
        writer.write_str_value("actionName", self.action_name)
        writer.write_enum_value("actionState", self.action_state)
        writer.write_int_value("failedLicensesCount", self.failed_licenses_count)
        writer.write_datetime_value("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_str_value("managedDeviceId", self.managed_device_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_int_value("totalLicensesCount", self.total_licenses_count)
        writer.write_str_value("userId", self.user_id)
        writer.write_additional_data_value(self.additional_data)
    

