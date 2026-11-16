from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_assignment_item_intent import DeviceAssignmentItemIntent
    from .device_assignment_item_status import DeviceAssignmentItemStatus
    from .device_assignment_item_type import DeviceAssignmentItemType

@dataclass
class DeviceAssignmentItem(AdditionalDataHolder, Parsable):
    """
    Represents the application or configuration included in the ChangeAssignments action execution or result. For action execution, it represents the application or configuration intended to be uninstalled or removed on the managed device. For action result, it represents the live reporting data for this application or configuration regarding its removal or restoration process.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # A list of possible assignment item action intent values on the application or configuration when executing this action on the managed device. For example, if the application or configuration is intended to be removed on the managed device, then the intent value is remove, and if the application or configuration already under removal through previous actions and is now intended to be restored on the managed device, then the intent value is restore
    assignment_item_action_intent: Optional[DeviceAssignmentItemIntent] = None
    # A list of possible assignment item action status values for the application or configuration regarding their executed action on the managed device. For example, a configuration included in the deviceAssignmentItems list has just been executed the action. Its status starts with inProgress until it's successfully removed to reflect as removed status or failed to be removed to reflect as error status on the managed device. Similar status change happens for restoration process
    assignment_item_action_status: Optional[DeviceAssignmentItemStatus] = None
    # The error code for the application or configuration regarding the failed executed action on the managed device. Read-Only. Returned in the action result. 0 is default value and indicates no failure. Valid values -9.22337203685478E+18 to 9.22337203685478E+18. This property is read-only.
    error_code: Optional[int] = None
    # The intent action message for the application or configuration regarding the executed action on the managed device. When the action is on error, this property provides message on the reason of failure. When the action is in progress, this property provides message on what's being processed on the device. Read-Only. Returned in the action result. Can be null. Max length is 1500. This property is read-only.
    intent_action_message: Optional[str] = None
    # The item displayName name for the application or configuration. Read-Only. Returned in the action result. Default value is null. The property value cannot be modified and is automatically populated with the action result. Max length is 200. This property is read-only.
    item_display_name: Optional[str] = None
    # The unique identifier for the application or configuration. ItemId is required property which needs to be set in the action POST request parameter for the DeviceAssignmentItem intended to remove. Max length is 40
    item_id: Optional[str] = None
    # Indicates the specific type for the application or configuration. For example, unknown, application, appConfiguration, exploitProtection, bitLocker, deviceControl, microsoftEdgeBaseline, attackSurfaceReductionRulesConfigMgr, endpointDetectionandResponse, windowsUpdateforBusiness, microsoftDefenderFirewallRules, applicationControl, microsoftDefenderAntivirusexclusions, microsoftDefenderAntivirus, wiredNetwork, derivedPersonalIdentityVerificationCredential, windowsHealthMonitoring, extensions, mxProfileZebraOnly, deviceFirmwareConfigurationInterface, deliveryOptimization, identityProtection, kiosk, overrideGroupPolicy, domainJoinPreview, pkcsImportedCertificate, networkBoundary, endpointProtection, microsoftDefenderAtpWindows10Desktop, sharedMultiUserDevice, deviceFeatures, secureAssessmentEducation, wiFiImport, editionUpgradeAndModeSwitch, vpn, custom, softwareUpdates, deviceRestrictionsWindows10Team, email, trustedCertificate, scepCertificate, emailSamsungKnoxOnly, pkcsCertificate, deviceRestrictions, wiFi, settingsCatalog. Read-Only. Returned in the action result. Default value is null. The property value cannot be modified and is automatically populated with the action result. Max length is 200. This property is read-only.
    item_sub_type_display_name: Optional[str] = None
    # A list of possible device assignment item types to execute this action on the managed device. Device assignment item represents existing assigned Intune resource such as application or configuration. Currently supported device assignment item types are Application, DeviceConfiguration, DeviceManagementConfigurationPolicy and MobileAppConfiguration
    item_type: Optional[DeviceAssignmentItemType] = None
    # The date and time when the application or configuration was initiated an action execution. Read-Only. Returned in the action result. The property value cannot be modified and is automatically populated when the action is initiated. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2025 would look like this: '2025-01-01T00:00:00Z'. This property is read-only.
    last_action_date_time: Optional[datetime.datetime] = None
    # The date and time when the application or configuration was last modified because of either action execution or status change. Read-Only. Returned in the action result. The property value cannot be modified and is automatically populated when the action is initiated or the device has a status change. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2025 would look like this: '2025-01-01T00:00:00Z'. This property is read-only.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceAssignmentItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceAssignmentItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceAssignmentItem()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_assignment_item_intent import DeviceAssignmentItemIntent
        from .device_assignment_item_status import DeviceAssignmentItemStatus
        from .device_assignment_item_type import DeviceAssignmentItemType

        from .device_assignment_item_intent import DeviceAssignmentItemIntent
        from .device_assignment_item_status import DeviceAssignmentItemStatus
        from .device_assignment_item_type import DeviceAssignmentItemType

        fields: dict[str, Callable[[Any], None]] = {
            "assignmentItemActionIntent": lambda n : setattr(self, 'assignment_item_action_intent', n.get_enum_value(DeviceAssignmentItemIntent)),
            "assignmentItemActionStatus": lambda n : setattr(self, 'assignment_item_action_status', n.get_enum_value(DeviceAssignmentItemStatus)),
            "errorCode": lambda n : setattr(self, 'error_code', n.get_int_value()),
            "intentActionMessage": lambda n : setattr(self, 'intent_action_message', n.get_str_value()),
            "itemDisplayName": lambda n : setattr(self, 'item_display_name', n.get_str_value()),
            "itemId": lambda n : setattr(self, 'item_id', n.get_str_value()),
            "itemSubTypeDisplayName": lambda n : setattr(self, 'item_sub_type_display_name', n.get_str_value()),
            "itemType": lambda n : setattr(self, 'item_type', n.get_enum_value(DeviceAssignmentItemType)),
            "lastActionDateTime": lambda n : setattr(self, 'last_action_date_time', n.get_datetime_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_enum_value("assignmentItemActionIntent", self.assignment_item_action_intent)
        writer.write_enum_value("assignmentItemActionStatus", self.assignment_item_action_status)
        writer.write_str_value("itemId", self.item_id)
        writer.write_enum_value("itemType", self.item_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

