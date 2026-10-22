from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_troubleshooting_error_details import DeviceManagementTroubleshootingErrorDetails
    from .mobile_app_troubleshooting_app_policy_creation_history import MobileAppTroubleshootingAppPolicyCreationHistory
    from .mobile_app_troubleshooting_app_state_history import MobileAppTroubleshootingAppStateHistory
    from .mobile_app_troubleshooting_app_target_history import MobileAppTroubleshootingAppTargetHistory
    from .mobile_app_troubleshooting_app_update_history import MobileAppTroubleshootingAppUpdateHistory
    from .mobile_app_troubleshooting_device_checkin_history import MobileAppTroubleshootingDeviceCheckinHistory

@dataclass
class MobileAppTroubleshootingHistoryItem(AdditionalDataHolder, Parsable):
    """
    History Item contained in the Mobile App Troubleshooting Event.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Time when the history item occurred.
    occurrence_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Object containing detailed information about the error and its remediation.
    troubleshooting_error_details: Optional[DeviceManagementTroubleshootingErrorDetails] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MobileAppTroubleshootingHistoryItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MobileAppTroubleshootingHistoryItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobileAppTroubleshootingAppPolicyCreationHistory".casefold():
            from .mobile_app_troubleshooting_app_policy_creation_history import MobileAppTroubleshootingAppPolicyCreationHistory

            return MobileAppTroubleshootingAppPolicyCreationHistory()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobileAppTroubleshootingAppStateHistory".casefold():
            from .mobile_app_troubleshooting_app_state_history import MobileAppTroubleshootingAppStateHistory

            return MobileAppTroubleshootingAppStateHistory()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobileAppTroubleshootingAppTargetHistory".casefold():
            from .mobile_app_troubleshooting_app_target_history import MobileAppTroubleshootingAppTargetHistory

            return MobileAppTroubleshootingAppTargetHistory()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobileAppTroubleshootingAppUpdateHistory".casefold():
            from .mobile_app_troubleshooting_app_update_history import MobileAppTroubleshootingAppUpdateHistory

            return MobileAppTroubleshootingAppUpdateHistory()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobileAppTroubleshootingDeviceCheckinHistory".casefold():
            from .mobile_app_troubleshooting_device_checkin_history import MobileAppTroubleshootingDeviceCheckinHistory

            return MobileAppTroubleshootingDeviceCheckinHistory()
        return MobileAppTroubleshootingHistoryItem()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_troubleshooting_error_details import DeviceManagementTroubleshootingErrorDetails
        from .mobile_app_troubleshooting_app_policy_creation_history import MobileAppTroubleshootingAppPolicyCreationHistory
        from .mobile_app_troubleshooting_app_state_history import MobileAppTroubleshootingAppStateHistory
        from .mobile_app_troubleshooting_app_target_history import MobileAppTroubleshootingAppTargetHistory
        from .mobile_app_troubleshooting_app_update_history import MobileAppTroubleshootingAppUpdateHistory
        from .mobile_app_troubleshooting_device_checkin_history import MobileAppTroubleshootingDeviceCheckinHistory

        from .device_management_troubleshooting_error_details import DeviceManagementTroubleshootingErrorDetails
        from .mobile_app_troubleshooting_app_policy_creation_history import MobileAppTroubleshootingAppPolicyCreationHistory
        from .mobile_app_troubleshooting_app_state_history import MobileAppTroubleshootingAppStateHistory
        from .mobile_app_troubleshooting_app_target_history import MobileAppTroubleshootingAppTargetHistory
        from .mobile_app_troubleshooting_app_update_history import MobileAppTroubleshootingAppUpdateHistory
        from .mobile_app_troubleshooting_device_checkin_history import MobileAppTroubleshootingDeviceCheckinHistory

        fields: dict[str, Callable[[Any], None]] = {
            "occurrenceDateTime": lambda n : setattr(self, 'occurrence_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "troubleshootingErrorDetails": lambda n : setattr(self, 'troubleshooting_error_details', n.get_object_value(DeviceManagementTroubleshootingErrorDetails)),
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
        writer.write_datetime_value("occurrenceDateTime", self.occurrence_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("troubleshootingErrorDetails", self.troubleshooting_error_details)
        writer.write_additional_data_value(self.additional_data)
    

