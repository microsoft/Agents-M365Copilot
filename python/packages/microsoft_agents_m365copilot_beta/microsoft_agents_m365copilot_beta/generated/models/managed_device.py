from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .assignment_filter_evaluation_status_details import AssignmentFilterEvaluationStatusDetails
    from .chassis_type import ChassisType
    from .chrome_o_s_device_property import ChromeOSDeviceProperty
    from .cloud_pc_remote_action_result import CloudPcRemoteActionResult
    from .compliance_state import ComplianceState
    from .configuration_manager_client_enabled_features import ConfigurationManagerClientEnabledFeatures
    from .configuration_manager_client_health_state import ConfigurationManagerClientHealthState
    from .configuration_manager_client_information import ConfigurationManagerClientInformation
    from .detected_app import DetectedApp
    from .device_action_result import DeviceActionResult
    from .device_category import DeviceCategory
    from .device_compliance_policy_state import DeviceCompliancePolicyState
    from .device_configuration_state import DeviceConfigurationState
    from .device_enrollment_type import DeviceEnrollmentType
    from .device_health_attestation_state import DeviceHealthAttestationState
    from .device_health_script_policy_state import DeviceHealthScriptPolicyState
    from .device_log_collection_response import DeviceLogCollectionResponse
    from .device_management_exchange_access_state import DeviceManagementExchangeAccessState
    from .device_management_exchange_access_state_reason import DeviceManagementExchangeAccessStateReason
    from .device_registration_state import DeviceRegistrationState
    from .device_type import DeviceType
    from .entity import Entity
    from .hardware_information import HardwareInformation
    from .join_type import JoinType
    from .logged_on_user import LoggedOnUser
    from .lost_mode_state import LostModeState
    from .managed_device_architecture import ManagedDeviceArchitecture
    from .managed_device_management_features import ManagedDeviceManagementFeatures
    from .managed_device_mobile_app_configuration_state import ManagedDeviceMobileAppConfigurationState
    from .managed_device_owner_type import ManagedDeviceOwnerType
    from .managed_device_partner_reported_health_state import ManagedDevicePartnerReportedHealthState
    from .management_agent_type import ManagementAgentType
    from .management_state import ManagementState
    from .owner_type import OwnerType
    from .security_baseline_state import SecurityBaselineState
    from .user import User
    from .windows_managed_device import WindowsManagedDevice
    from .windows_protection_state import WindowsProtectionState

from .entity import Entity

@dataclass
class ManagedDevice(Entity, Parsable):
    """
    Devices that are managed or pre-enrolled through Intune. Limited support for $filter: Only properties whose descriptions mention support for $filter may be used, and combinations of those filtered properties must use 'and', not 'or'.
    """
    # Whether the device is Azure Active Directory registered. This property is read-only.
    aad_registered: Optional[bool] = None
    # The code that allows the Activation Lock on managed device to be bypassed. Default, is Null (Non-Default property) for this property when returned as part of managedDevice entity in LIST call. To retrieve actual values GET call needs to be made, with device id and included in select parameter. Supports: $select. $Search is not supported. Read-only. This property is read-only.
    activation_lock_bypass_code: Optional[str] = None
    # Android security patch level. This property is read-only.
    android_security_patch_level: Optional[str] = None
    # Managed device mobile app configuration states for this device.
    assignment_filter_evaluation_status_details: Optional[list[AssignmentFilterEvaluationStatusDetails]] = None
    # Reports if the managed device is enrolled via auto-pilot. This property is read-only.
    autopilot_enrolled: Optional[bool] = None
    # The unique identifier for the Azure Active Directory device. Read only. This property is read-only.
    azure_a_d_device_id: Optional[str] = None
    # Whether the device is Azure Active Directory registered. This property is read-only.
    azure_a_d_registered: Optional[bool] = None
    # The unique identifier for the Azure Active Directory device. Read only. This property is read-only.
    azure_active_directory_device_id: Optional[str] = None
    # Reports if the managed device has an escrowed Bootstrap Token. This is only for macOS devices. To get, include BootstrapTokenEscrowed in the select clause and query with a device id. If FALSE, no bootstrap token is escrowed. If TRUE, the device has escrowed a bootstrap token with Intune. This property is read-only.
    bootstrap_token_escrowed: Optional[bool] = None
    # Chassis type.
    chassis_type: Optional[ChassisType] = None
    # List of properties of the ChromeOS Device. Default is an empty list. To retrieve actual values GET call needs to be made, with device id and included in select parameter.
    chrome_o_s_device_info: Optional[list[ChromeOSDeviceProperty]] = None
    # The cloudPcRemoteActionResults property
    cloud_pc_remote_action_results: Optional[list[CloudPcRemoteActionResult]] = None
    # The DateTime when device compliance grace period expires. This property is read-only.
    compliance_grace_period_expiration_date_time: Optional[datetime.datetime] = None
    # Compliance state.
    compliance_state: Optional[ComplianceState] = None
    # ConfigrMgr client enabled features. This property is read-only.
    configuration_manager_client_enabled_features: Optional[ConfigurationManagerClientEnabledFeatures] = None
    # Configuration manager client health state, valid only for devices managed by MDM/ConfigMgr Agent
    configuration_manager_client_health_state: Optional[ConfigurationManagerClientHealthState] = None
    # Configuration manager client information, valid only for devices managed, duel-managed or tri-managed by ConfigMgr Agent
    configuration_manager_client_information: Optional[ConfigurationManagerClientInformation] = None
    # All applications currently installed on the device
    detected_apps: Optional[list[DetectedApp]] = None
    # List of ComplexType deviceActionResult objects. This property is read-only.
    device_action_results: Optional[list[DeviceActionResult]] = None
    # Device category
    device_category: Optional[DeviceCategory] = None
    # Device category display name. Default is an empty string. Supports $filter operator 'eq' and 'or'. This property is read-only.
    device_category_display_name: Optional[str] = None
    # Device compliance policy states for this device.
    device_compliance_policy_states: Optional[list[DeviceCompliancePolicyState]] = None
    # Device configuration states for this device.
    device_configuration_states: Optional[list[DeviceConfigurationState]] = None
    # Possible ways of adding a mobile device to management.
    device_enrollment_type: Optional[DeviceEnrollmentType] = None
    # Indicates whether the device is DFCI managed. When TRUE the device is DFCI managed. When FALSE, the device is not DFCI managed. The default value is FALSE.
    device_firmware_configuration_interface_managed: Optional[bool] = None
    # The device health attestation state. This property is read-only.
    device_health_attestation_state: Optional[DeviceHealthAttestationState] = None
    # Results of device health scripts that ran for this device. Default is empty list. This property is read-only.
    device_health_script_states: Optional[list[DeviceHealthScriptPolicyState]] = None
    # Name of the device. Supports $filter operator 'eq' and 'contains'. This property is read-only.
    device_name: Optional[str] = None
    # Device registration status.
    device_registration_state: Optional[DeviceRegistrationState] = None
    # Device type.
    device_type: Optional[DeviceType] = None
    # Whether the device is Exchange ActiveSync activated. This property is read-only.
    eas_activated: Optional[bool] = None
    # Exchange ActivationSync activation time of the device. This property is read-only.
    eas_activation_date_time: Optional[datetime.datetime] = None
    # Exchange ActiveSync Id of the device. This property is read-only.
    eas_device_id: Optional[str] = None
    # Email(s) for the user associated with the device. This property is read-only.
    email_address: Optional[str] = None
    # The Entra (Azure AD) User Principal Name (UPN) of the user responsible for the enrollment of the device. This property is read-only.
    enrolled_by_user_principal_name: Optional[str] = None
    # Enrollment time of the device. Supports $filter operator 'lt' and 'gt'. This property is read-only.
    enrolled_date_time: Optional[datetime.datetime] = None
    # Name of the enrollment profile assigned to the device. Default value is empty string, indicating no enrollment profile was assgined. This property is read-only.
    enrollment_profile_name: Optional[str] = None
    # Indicates Ethernet MAC Address of the device. Default, is Null (Non-Default property) for this property when returned as part of managedDevice entity. Individual get call with select query options is needed to retrieve actual values. Example: deviceManagement/managedDevices({managedDeviceId})?$select=ethernetMacAddress Supports: $select. $Search is not supported. Read-only. This property is read-only.
    ethernet_mac_address: Optional[str] = None
    # Device Exchange Access State.
    exchange_access_state: Optional[DeviceManagementExchangeAccessState] = None
    # Device Exchange Access State Reason.
    exchange_access_state_reason: Optional[DeviceManagementExchangeAccessStateReason] = None
    # Last time the device contacted Exchange. This property is read-only.
    exchange_last_successful_sync_date_time: Optional[datetime.datetime] = None
    # Free Storage in Bytes. Default value is 0. Read-only. This property is read-only.
    free_storage_space_in_bytes: Optional[int] = None
    # The hardward details for the device. Includes information such as storage space, manufacturer, serial number, etc. By default most property of this type are set to null/0/false and enum defaults for associated types. To retrieve actual values GET call needs to be made, with device id and included in select parameter. Supports: $select. $Search is not supported. Read-only. This property is read-only.
    hardware_information: Optional[HardwareInformation] = None
    # Integrated Circuit Card Identifier, it is A SIM card's unique identification number. Default is an empty string. To retrieve actual values GET call needs to be made, with device id and included in select parameter. Supports: $select. $Search is not supported. Read-only. This property is read-only.
    iccid: Optional[str] = None
    # IMEI. This property is read-only.
    imei: Optional[str] = None
    # Device encryption status. This property is read-only.
    is_encrypted: Optional[bool] = None
    # Device supervised status. This property is read-only.
    is_supervised: Optional[bool] = None
    # Whether the device is jail broken or rooted. Default is an empty string. Supports $filter operator 'eq' and 'or'. This property is read-only.
    jail_broken: Optional[str] = None
    # Device enrollment join type.
    join_type: Optional[JoinType] = None
    # The date and time that the device last completed a successful sync with Intune. Supports $filter operator 'lt' and 'gt'. This property is read-only.
    last_sync_date_time: Optional[datetime.datetime] = None
    # List of log collection requests
    log_collection_requests: Optional[list[DeviceLogCollectionResponse]] = None
    # State of lost mode, indicating if lost mode is enabled or disabled
    lost_mode_state: Optional[LostModeState] = None
    # Managed device mobile app configuration states for this device.
    managed_device_mobile_app_configuration_states: Optional[list[ManagedDeviceMobileAppConfigurationState]] = None
    # Automatically generated name to identify a device. Can be overwritten to a user friendly name.
    managed_device_name: Optional[str] = None
    # Owner type of device.
    managed_device_owner_type: Optional[ManagedDeviceOwnerType] = None
    # Management agent type.
    management_agent: Optional[ManagementAgentType] = None
    # Reports device management certificate expiration date. This property is read-only.
    management_certificate_expiration_date: Optional[datetime.datetime] = None
    # Device management features.
    management_features: Optional[ManagedDeviceManagementFeatures] = None
    # Management state of device in Microsoft Intune.
    management_state: Optional[ManagementState] = None
    # Manufacturer of the device. This property is read-only.
    manufacturer: Optional[str] = None
    # MEID. This property is read-only.
    meid: Optional[str] = None
    # Model of the device. This property is read-only.
    model: Optional[str] = None
    # Notes on the device created by IT Admin. Default is null. To retrieve actual values GET call needs to be made, with device id and included in select parameter. Supports: $select. $Search is not supported.
    notes: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Operating system of the device. Windows, iOS, etc. This property is read-only.
    operating_system: Optional[str] = None
    # Operating system version of the device. This property is read-only.
    os_version: Optional[str] = None
    # Owner type of device.
    owner_type: Optional[OwnerType] = None
    # Available health states for the Device Health API
    partner_reported_threat_state: Optional[ManagedDevicePartnerReportedHealthState] = None
    # Phone number of the device. This property is read-only.
    phone_number: Optional[str] = None
    # Total Memory in Bytes. Default is 0. To retrieve actual values GET call needs to be made, with device id and included in select parameter. Supports: $select. Read-only. This property is read-only.
    physical_memory_in_bytes: Optional[int] = None
    # Reports the DateTime the preferMdmOverGroupPolicy setting was set.  When set, the Intune MDM settings will override Group Policy settings if there is a conflict. Read Only. This property is read-only.
    prefer_mdm_over_group_policy_applied_date_time: Optional[datetime.datetime] = None
    # Processor architecture
    processor_architecture: Optional[ManagedDeviceArchitecture] = None
    # An error string that identifies issues when creating Remote Assistance session objects. This property is read-only.
    remote_assistance_session_error_details: Optional[str] = None
    # Url that allows a Remote Assistance session to be established with the device. Default is an empty string. To retrieve actual values GET call needs to be made, with device id and included in select parameter. This property is read-only.
    remote_assistance_session_url: Optional[str] = None
    # Reports if the managed iOS device is user approval enrollment. This property is read-only.
    require_user_enrollment_approval: Optional[bool] = None
    # Indicates the time after when a device will be auto retired because of scheduled action. This property is read-only.
    retire_after_date_time: Optional[datetime.datetime] = None
    # List of Scope Tag IDs for this Device instance.
    role_scope_tag_ids: Optional[list[str]] = None
    # Security baseline states for this device.
    security_baseline_states: Optional[list[SecurityBaselineState]] = None
    # This indicates the security patch level of the operating system. These special updates contain important security fixes. For iOS/MacOS they are in (a) format. For android its in 2017-08-07 format. This property is read-only.
    security_patch_level: Optional[str] = None
    # SerialNumber. This property is read-only.
    serial_number: Optional[str] = None
    # Device sku family
    sku_family: Optional[str] = None
    # Device sku number, see also: https://learn.microsoft.com/windows/win32/api/sysinfoapi/nf-sysinfoapi-getproductinfo. Valid values 0 to 2147483647. This property is read-only.
    sku_number: Optional[int] = None
    # Specification version. This property is read-only.
    specification_version: Optional[str] = None
    # Subscriber Carrier. This property is read-only.
    subscriber_carrier: Optional[str] = None
    # Total Storage in Bytes. This property is read-only.
    total_storage_space_in_bytes: Optional[int] = None
    # Unique Device Identifier for iOS and macOS devices. Default is an empty string. To retrieve actual values GET call needs to be made, with device id and included in select parameter. Supports: $select. $Search is not supported. Read-only. This property is read-only.
    udid: Optional[str] = None
    # User display name. This property is read-only.
    user_display_name: Optional[str] = None
    # Unique Identifier for the user associated with the device. This property is read-only.
    user_id: Optional[str] = None
    # Device user principal name. This property is read-only.
    user_principal_name: Optional[str] = None
    # The primary users associated with the managed device.
    users: Optional[list[User]] = None
    # Indicates the last logged on users of a device. This property is read-only.
    users_logged_on: Optional[list[LoggedOnUser]] = None
    # Wi-Fi MAC. This property is read-only.
    wi_fi_mac_address: Optional[str] = None
    # Count of active malware for this windows device. Default is 0. To retrieve actual values GET call needs to be made, with device id and included in select parameter. This property is read-only.
    windows_active_malware_count: Optional[int] = None
    # The device protection status. This property is read-only.
    windows_protection_state: Optional[WindowsProtectionState] = None
    # Count of remediated malware for this windows device. Default is 0. To retrieve actual values GET call needs to be made, with device id and included in select parameter. This property is read-only.
    windows_remediated_malware_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ManagedDevice:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManagedDevice
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsManagedDevice".casefold():
            from .windows_managed_device import WindowsManagedDevice

            return WindowsManagedDevice()
        return ManagedDevice()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .assignment_filter_evaluation_status_details import AssignmentFilterEvaluationStatusDetails
        from .chassis_type import ChassisType
        from .chrome_o_s_device_property import ChromeOSDeviceProperty
        from .cloud_pc_remote_action_result import CloudPcRemoteActionResult
        from .compliance_state import ComplianceState
        from .configuration_manager_client_enabled_features import ConfigurationManagerClientEnabledFeatures
        from .configuration_manager_client_health_state import ConfigurationManagerClientHealthState
        from .configuration_manager_client_information import ConfigurationManagerClientInformation
        from .detected_app import DetectedApp
        from .device_action_result import DeviceActionResult
        from .device_category import DeviceCategory
        from .device_compliance_policy_state import DeviceCompliancePolicyState
        from .device_configuration_state import DeviceConfigurationState
        from .device_enrollment_type import DeviceEnrollmentType
        from .device_health_attestation_state import DeviceHealthAttestationState
        from .device_health_script_policy_state import DeviceHealthScriptPolicyState
        from .device_log_collection_response import DeviceLogCollectionResponse
        from .device_management_exchange_access_state import DeviceManagementExchangeAccessState
        from .device_management_exchange_access_state_reason import DeviceManagementExchangeAccessStateReason
        from .device_registration_state import DeviceRegistrationState
        from .device_type import DeviceType
        from .entity import Entity
        from .hardware_information import HardwareInformation
        from .join_type import JoinType
        from .logged_on_user import LoggedOnUser
        from .lost_mode_state import LostModeState
        from .managed_device_architecture import ManagedDeviceArchitecture
        from .managed_device_management_features import ManagedDeviceManagementFeatures
        from .managed_device_mobile_app_configuration_state import ManagedDeviceMobileAppConfigurationState
        from .managed_device_owner_type import ManagedDeviceOwnerType
        from .managed_device_partner_reported_health_state import ManagedDevicePartnerReportedHealthState
        from .management_agent_type import ManagementAgentType
        from .management_state import ManagementState
        from .owner_type import OwnerType
        from .security_baseline_state import SecurityBaselineState
        from .user import User
        from .windows_managed_device import WindowsManagedDevice
        from .windows_protection_state import WindowsProtectionState

        from .assignment_filter_evaluation_status_details import AssignmentFilterEvaluationStatusDetails
        from .chassis_type import ChassisType
        from .chrome_o_s_device_property import ChromeOSDeviceProperty
        from .cloud_pc_remote_action_result import CloudPcRemoteActionResult
        from .compliance_state import ComplianceState
        from .configuration_manager_client_enabled_features import ConfigurationManagerClientEnabledFeatures
        from .configuration_manager_client_health_state import ConfigurationManagerClientHealthState
        from .configuration_manager_client_information import ConfigurationManagerClientInformation
        from .detected_app import DetectedApp
        from .device_action_result import DeviceActionResult
        from .device_category import DeviceCategory
        from .device_compliance_policy_state import DeviceCompliancePolicyState
        from .device_configuration_state import DeviceConfigurationState
        from .device_enrollment_type import DeviceEnrollmentType
        from .device_health_attestation_state import DeviceHealthAttestationState
        from .device_health_script_policy_state import DeviceHealthScriptPolicyState
        from .device_log_collection_response import DeviceLogCollectionResponse
        from .device_management_exchange_access_state import DeviceManagementExchangeAccessState
        from .device_management_exchange_access_state_reason import DeviceManagementExchangeAccessStateReason
        from .device_registration_state import DeviceRegistrationState
        from .device_type import DeviceType
        from .entity import Entity
        from .hardware_information import HardwareInformation
        from .join_type import JoinType
        from .logged_on_user import LoggedOnUser
        from .lost_mode_state import LostModeState
        from .managed_device_architecture import ManagedDeviceArchitecture
        from .managed_device_management_features import ManagedDeviceManagementFeatures
        from .managed_device_mobile_app_configuration_state import ManagedDeviceMobileAppConfigurationState
        from .managed_device_owner_type import ManagedDeviceOwnerType
        from .managed_device_partner_reported_health_state import ManagedDevicePartnerReportedHealthState
        from .management_agent_type import ManagementAgentType
        from .management_state import ManagementState
        from .owner_type import OwnerType
        from .security_baseline_state import SecurityBaselineState
        from .user import User
        from .windows_managed_device import WindowsManagedDevice
        from .windows_protection_state import WindowsProtectionState

        fields: dict[str, Callable[[Any], None]] = {
            "aadRegistered": lambda n : setattr(self, 'aad_registered', n.get_bool_value()),
            "activationLockBypassCode": lambda n : setattr(self, 'activation_lock_bypass_code', n.get_str_value()),
            "androidSecurityPatchLevel": lambda n : setattr(self, 'android_security_patch_level', n.get_str_value()),
            "assignmentFilterEvaluationStatusDetails": lambda n : setattr(self, 'assignment_filter_evaluation_status_details', n.get_collection_of_object_values(AssignmentFilterEvaluationStatusDetails)),
            "autopilotEnrolled": lambda n : setattr(self, 'autopilot_enrolled', n.get_bool_value()),
            "azureADDeviceId": lambda n : setattr(self, 'azure_a_d_device_id', n.get_str_value()),
            "azureADRegistered": lambda n : setattr(self, 'azure_a_d_registered', n.get_bool_value()),
            "azureActiveDirectoryDeviceId": lambda n : setattr(self, 'azure_active_directory_device_id', n.get_str_value()),
            "bootstrapTokenEscrowed": lambda n : setattr(self, 'bootstrap_token_escrowed', n.get_bool_value()),
            "chassisType": lambda n : setattr(self, 'chassis_type', n.get_enum_value(ChassisType)),
            "chromeOSDeviceInfo": lambda n : setattr(self, 'chrome_o_s_device_info', n.get_collection_of_object_values(ChromeOSDeviceProperty)),
            "cloudPcRemoteActionResults": lambda n : setattr(self, 'cloud_pc_remote_action_results', n.get_collection_of_object_values(CloudPcRemoteActionResult)),
            "complianceGracePeriodExpirationDateTime": lambda n : setattr(self, 'compliance_grace_period_expiration_date_time', n.get_datetime_value()),
            "complianceState": lambda n : setattr(self, 'compliance_state', n.get_enum_value(ComplianceState)),
            "configurationManagerClientEnabledFeatures": lambda n : setattr(self, 'configuration_manager_client_enabled_features', n.get_object_value(ConfigurationManagerClientEnabledFeatures)),
            "configurationManagerClientHealthState": lambda n : setattr(self, 'configuration_manager_client_health_state', n.get_object_value(ConfigurationManagerClientHealthState)),
            "configurationManagerClientInformation": lambda n : setattr(self, 'configuration_manager_client_information', n.get_object_value(ConfigurationManagerClientInformation)),
            "detectedApps": lambda n : setattr(self, 'detected_apps', n.get_collection_of_object_values(DetectedApp)),
            "deviceActionResults": lambda n : setattr(self, 'device_action_results', n.get_collection_of_object_values(DeviceActionResult)),
            "deviceCategory": lambda n : setattr(self, 'device_category', n.get_object_value(DeviceCategory)),
            "deviceCategoryDisplayName": lambda n : setattr(self, 'device_category_display_name', n.get_str_value()),
            "deviceCompliancePolicyStates": lambda n : setattr(self, 'device_compliance_policy_states', n.get_collection_of_object_values(DeviceCompliancePolicyState)),
            "deviceConfigurationStates": lambda n : setattr(self, 'device_configuration_states', n.get_collection_of_object_values(DeviceConfigurationState)),
            "deviceEnrollmentType": lambda n : setattr(self, 'device_enrollment_type', n.get_enum_value(DeviceEnrollmentType)),
            "deviceFirmwareConfigurationInterfaceManaged": lambda n : setattr(self, 'device_firmware_configuration_interface_managed', n.get_bool_value()),
            "deviceHealthAttestationState": lambda n : setattr(self, 'device_health_attestation_state', n.get_object_value(DeviceHealthAttestationState)),
            "deviceHealthScriptStates": lambda n : setattr(self, 'device_health_script_states', n.get_collection_of_object_values(DeviceHealthScriptPolicyState)),
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "deviceRegistrationState": lambda n : setattr(self, 'device_registration_state', n.get_enum_value(DeviceRegistrationState)),
            "deviceType": lambda n : setattr(self, 'device_type', n.get_enum_value(DeviceType)),
            "easActivated": lambda n : setattr(self, 'eas_activated', n.get_bool_value()),
            "easActivationDateTime": lambda n : setattr(self, 'eas_activation_date_time', n.get_datetime_value()),
            "easDeviceId": lambda n : setattr(self, 'eas_device_id', n.get_str_value()),
            "emailAddress": lambda n : setattr(self, 'email_address', n.get_str_value()),
            "enrolledByUserPrincipalName": lambda n : setattr(self, 'enrolled_by_user_principal_name', n.get_str_value()),
            "enrolledDateTime": lambda n : setattr(self, 'enrolled_date_time', n.get_datetime_value()),
            "enrollmentProfileName": lambda n : setattr(self, 'enrollment_profile_name', n.get_str_value()),
            "ethernetMacAddress": lambda n : setattr(self, 'ethernet_mac_address', n.get_str_value()),
            "exchangeAccessState": lambda n : setattr(self, 'exchange_access_state', n.get_enum_value(DeviceManagementExchangeAccessState)),
            "exchangeAccessStateReason": lambda n : setattr(self, 'exchange_access_state_reason', n.get_enum_value(DeviceManagementExchangeAccessStateReason)),
            "exchangeLastSuccessfulSyncDateTime": lambda n : setattr(self, 'exchange_last_successful_sync_date_time', n.get_datetime_value()),
            "freeStorageSpaceInBytes": lambda n : setattr(self, 'free_storage_space_in_bytes', n.get_int_value()),
            "hardwareInformation": lambda n : setattr(self, 'hardware_information', n.get_object_value(HardwareInformation)),
            "iccid": lambda n : setattr(self, 'iccid', n.get_str_value()),
            "imei": lambda n : setattr(self, 'imei', n.get_str_value()),
            "isEncrypted": lambda n : setattr(self, 'is_encrypted', n.get_bool_value()),
            "isSupervised": lambda n : setattr(self, 'is_supervised', n.get_bool_value()),
            "jailBroken": lambda n : setattr(self, 'jail_broken', n.get_str_value()),
            "joinType": lambda n : setattr(self, 'join_type', n.get_enum_value(JoinType)),
            "lastSyncDateTime": lambda n : setattr(self, 'last_sync_date_time', n.get_datetime_value()),
            "logCollectionRequests": lambda n : setattr(self, 'log_collection_requests', n.get_collection_of_object_values(DeviceLogCollectionResponse)),
            "lostModeState": lambda n : setattr(self, 'lost_mode_state', n.get_enum_value(LostModeState)),
            "managedDeviceMobileAppConfigurationStates": lambda n : setattr(self, 'managed_device_mobile_app_configuration_states', n.get_collection_of_object_values(ManagedDeviceMobileAppConfigurationState)),
            "managedDeviceName": lambda n : setattr(self, 'managed_device_name', n.get_str_value()),
            "managedDeviceOwnerType": lambda n : setattr(self, 'managed_device_owner_type', n.get_enum_value(ManagedDeviceOwnerType)),
            "managementAgent": lambda n : setattr(self, 'management_agent', n.get_enum_value(ManagementAgentType)),
            "managementCertificateExpirationDate": lambda n : setattr(self, 'management_certificate_expiration_date', n.get_datetime_value()),
            "managementFeatures": lambda n : setattr(self, 'management_features', n.get_enum_value(ManagedDeviceManagementFeatures)),
            "managementState": lambda n : setattr(self, 'management_state', n.get_enum_value(ManagementState)),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "meid": lambda n : setattr(self, 'meid', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_str_value()),
            "operatingSystem": lambda n : setattr(self, 'operating_system', n.get_str_value()),
            "osVersion": lambda n : setattr(self, 'os_version', n.get_str_value()),
            "ownerType": lambda n : setattr(self, 'owner_type', n.get_enum_value(OwnerType)),
            "partnerReportedThreatState": lambda n : setattr(self, 'partner_reported_threat_state', n.get_enum_value(ManagedDevicePartnerReportedHealthState)),
            "phoneNumber": lambda n : setattr(self, 'phone_number', n.get_str_value()),
            "physicalMemoryInBytes": lambda n : setattr(self, 'physical_memory_in_bytes', n.get_int_value()),
            "preferMdmOverGroupPolicyAppliedDateTime": lambda n : setattr(self, 'prefer_mdm_over_group_policy_applied_date_time', n.get_datetime_value()),
            "processorArchitecture": lambda n : setattr(self, 'processor_architecture', n.get_enum_value(ManagedDeviceArchitecture)),
            "remoteAssistanceSessionErrorDetails": lambda n : setattr(self, 'remote_assistance_session_error_details', n.get_str_value()),
            "remoteAssistanceSessionUrl": lambda n : setattr(self, 'remote_assistance_session_url', n.get_str_value()),
            "requireUserEnrollmentApproval": lambda n : setattr(self, 'require_user_enrollment_approval', n.get_bool_value()),
            "retireAfterDateTime": lambda n : setattr(self, 'retire_after_date_time', n.get_datetime_value()),
            "roleScopeTagIds": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "securityBaselineStates": lambda n : setattr(self, 'security_baseline_states', n.get_collection_of_object_values(SecurityBaselineState)),
            "securityPatchLevel": lambda n : setattr(self, 'security_patch_level', n.get_str_value()),
            "serialNumber": lambda n : setattr(self, 'serial_number', n.get_str_value()),
            "skuFamily": lambda n : setattr(self, 'sku_family', n.get_str_value()),
            "skuNumber": lambda n : setattr(self, 'sku_number', n.get_int_value()),
            "specificationVersion": lambda n : setattr(self, 'specification_version', n.get_str_value()),
            "subscriberCarrier": lambda n : setattr(self, 'subscriber_carrier', n.get_str_value()),
            "totalStorageSpaceInBytes": lambda n : setattr(self, 'total_storage_space_in_bytes', n.get_int_value()),
            "udid": lambda n : setattr(self, 'udid', n.get_str_value()),
            "userDisplayName": lambda n : setattr(self, 'user_display_name', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
            "users": lambda n : setattr(self, 'users', n.get_collection_of_object_values(User)),
            "usersLoggedOn": lambda n : setattr(self, 'users_logged_on', n.get_collection_of_object_values(LoggedOnUser)),
            "wiFiMacAddress": lambda n : setattr(self, 'wi_fi_mac_address', n.get_str_value()),
            "windowsActiveMalwareCount": lambda n : setattr(self, 'windows_active_malware_count', n.get_int_value()),
            "windowsProtectionState": lambda n : setattr(self, 'windows_protection_state', n.get_object_value(WindowsProtectionState)),
            "windowsRemediatedMalwareCount": lambda n : setattr(self, 'windows_remediated_malware_count', n.get_int_value()),
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
        writer.write_collection_of_object_values("assignmentFilterEvaluationStatusDetails", self.assignment_filter_evaluation_status_details)
        writer.write_enum_value("chassisType", self.chassis_type)
        writer.write_collection_of_object_values("chromeOSDeviceInfo", self.chrome_o_s_device_info)
        writer.write_collection_of_object_values("cloudPcRemoteActionResults", self.cloud_pc_remote_action_results)
        writer.write_enum_value("complianceState", self.compliance_state)
        writer.write_object_value("configurationManagerClientHealthState", self.configuration_manager_client_health_state)
        writer.write_object_value("configurationManagerClientInformation", self.configuration_manager_client_information)
        writer.write_collection_of_object_values("detectedApps", self.detected_apps)
        writer.write_object_value("deviceCategory", self.device_category)
        writer.write_collection_of_object_values("deviceCompliancePolicyStates", self.device_compliance_policy_states)
        writer.write_collection_of_object_values("deviceConfigurationStates", self.device_configuration_states)
        writer.write_enum_value("deviceEnrollmentType", self.device_enrollment_type)
        writer.write_bool_value("deviceFirmwareConfigurationInterfaceManaged", self.device_firmware_configuration_interface_managed)
        writer.write_collection_of_object_values("deviceHealthScriptStates", self.device_health_script_states)
        writer.write_enum_value("deviceRegistrationState", self.device_registration_state)
        writer.write_enum_value("deviceType", self.device_type)
        writer.write_enum_value("exchangeAccessState", self.exchange_access_state)
        writer.write_enum_value("exchangeAccessStateReason", self.exchange_access_state_reason)
        writer.write_enum_value("joinType", self.join_type)
        writer.write_collection_of_object_values("logCollectionRequests", self.log_collection_requests)
        writer.write_enum_value("lostModeState", self.lost_mode_state)
        writer.write_collection_of_object_values("managedDeviceMobileAppConfigurationStates", self.managed_device_mobile_app_configuration_states)
        writer.write_str_value("managedDeviceName", self.managed_device_name)
        writer.write_enum_value("managedDeviceOwnerType", self.managed_device_owner_type)
        writer.write_enum_value("managementAgent", self.management_agent)
        writer.write_enum_value("managementFeatures", self.management_features)
        writer.write_enum_value("managementState", self.management_state)
        writer.write_str_value("notes", self.notes)
        writer.write_enum_value("ownerType", self.owner_type)
        writer.write_enum_value("partnerReportedThreatState", self.partner_reported_threat_state)
        writer.write_enum_value("processorArchitecture", self.processor_architecture)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
        writer.write_collection_of_object_values("securityBaselineStates", self.security_baseline_states)
        writer.write_str_value("skuFamily", self.sku_family)
        writer.write_collection_of_object_values("users", self.users)
        writer.write_object_value("windowsProtectionState", self.windows_protection_state)
    

