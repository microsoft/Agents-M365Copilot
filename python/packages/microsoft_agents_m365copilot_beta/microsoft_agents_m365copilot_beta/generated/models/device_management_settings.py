from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .derived_credential_provider_type import DerivedCredentialProviderType

@dataclass
class DeviceManagementSettings(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The property to determine if Android device administrator enrollment is enabled for this account.
    android_device_administrator_enrollment_enabled: Optional[bool] = None
    # Provider type for Derived Credentials.
    derived_credential_provider: Optional[DerivedCredentialProviderType] = None
    # The Derived Credential Provider self-service URI.
    derived_credential_url: Optional[str] = None
    # The number of days a device is allowed to go without checking in to remain compliant.
    device_compliance_checkin_threshold_days: Optional[int] = None
    # When the device does not check in for specified number of days, the company data might be removed and the device will not be under management. Valid values 30 to 270
    device_inactivity_before_retirement_in_day: Optional[int] = None
    # Determines whether the autopilot diagnostic feature is enabled or not.
    enable_autopilot_diagnostics: Optional[bool] = None
    # Determines whether the device group membership report feature is enabled or not.
    enable_device_group_membership_report: Optional[bool] = None
    # Determines whether the enhanced troubleshooting UX is enabled or not.
    enable_enhanced_troubleshooting_experience: Optional[bool] = None
    # Determines whether the log collection feature should be available for use.
    enable_log_collection: Optional[bool] = None
    # Is feature enabled or not for enhanced jailbreak detection.
    enhanced_jail_break: Optional[bool] = None
    # The property to determine whether to ignore unsupported compliance settings on certian models of devices.
    ignore_devices_for_unsupported_settings_enabled: Optional[bool] = None
    # Is feature enabled or not for scheduled action for rule.
    is_scheduled_action_enabled: Optional[bool] = None
    # The property to determine if M365 App log collection is enabled for account. When TRUE it indicates that M365 app log collection is enabled for account.  When FALSE it indicates that M365 app log collection is disabled for account. Default value is FALSE
    m365_app_diagnostics_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Device should be noncompliant when there is no compliance policy targeted when this is true
    secure_by_default: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .derived_credential_provider_type import DerivedCredentialProviderType

        from .derived_credential_provider_type import DerivedCredentialProviderType

        fields: dict[str, Callable[[Any], None]] = {
            "androidDeviceAdministratorEnrollmentEnabled": lambda n : setattr(self, 'android_device_administrator_enrollment_enabled', n.get_bool_value()),
            "derivedCredentialProvider": lambda n : setattr(self, 'derived_credential_provider', n.get_enum_value(DerivedCredentialProviderType)),
            "derivedCredentialUrl": lambda n : setattr(self, 'derived_credential_url', n.get_str_value()),
            "deviceComplianceCheckinThresholdDays": lambda n : setattr(self, 'device_compliance_checkin_threshold_days', n.get_int_value()),
            "deviceInactivityBeforeRetirementInDay": lambda n : setattr(self, 'device_inactivity_before_retirement_in_day', n.get_int_value()),
            "enableAutopilotDiagnostics": lambda n : setattr(self, 'enable_autopilot_diagnostics', n.get_bool_value()),
            "enableDeviceGroupMembershipReport": lambda n : setattr(self, 'enable_device_group_membership_report', n.get_bool_value()),
            "enableEnhancedTroubleshootingExperience": lambda n : setattr(self, 'enable_enhanced_troubleshooting_experience', n.get_bool_value()),
            "enableLogCollection": lambda n : setattr(self, 'enable_log_collection', n.get_bool_value()),
            "enhancedJailBreak": lambda n : setattr(self, 'enhanced_jail_break', n.get_bool_value()),
            "ignoreDevicesForUnsupportedSettingsEnabled": lambda n : setattr(self, 'ignore_devices_for_unsupported_settings_enabled', n.get_bool_value()),
            "isScheduledActionEnabled": lambda n : setattr(self, 'is_scheduled_action_enabled', n.get_bool_value()),
            "m365AppDiagnosticsEnabled": lambda n : setattr(self, 'm365_app_diagnostics_enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "secureByDefault": lambda n : setattr(self, 'secure_by_default', n.get_bool_value()),
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
        writer.write_bool_value("androidDeviceAdministratorEnrollmentEnabled", self.android_device_administrator_enrollment_enabled)
        writer.write_enum_value("derivedCredentialProvider", self.derived_credential_provider)
        writer.write_str_value("derivedCredentialUrl", self.derived_credential_url)
        writer.write_int_value("deviceComplianceCheckinThresholdDays", self.device_compliance_checkin_threshold_days)
        writer.write_int_value("deviceInactivityBeforeRetirementInDay", self.device_inactivity_before_retirement_in_day)
        writer.write_bool_value("enableAutopilotDiagnostics", self.enable_autopilot_diagnostics)
        writer.write_bool_value("enableDeviceGroupMembershipReport", self.enable_device_group_membership_report)
        writer.write_bool_value("enableEnhancedTroubleshootingExperience", self.enable_enhanced_troubleshooting_experience)
        writer.write_bool_value("enableLogCollection", self.enable_log_collection)
        writer.write_bool_value("enhancedJailBreak", self.enhanced_jail_break)
        writer.write_bool_value("ignoreDevicesForUnsupportedSettingsEnabled", self.ignore_devices_for_unsupported_settings_enabled)
        writer.write_bool_value("isScheduledActionEnabled", self.is_scheduled_action_enabled)
        writer.write_bool_value("m365AppDiagnosticsEnabled", self.m365_app_diagnostics_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("secureByDefault", self.secure_by_default)
        writer.write_additional_data_value(self.additional_data)
    

