from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from ..admin_consent import AdminConsent
    from ..advanced_threat_protection_onboarding_state_summary import AdvancedThreatProtectionOnboardingStateSummary
    from ..android_app_configuration_schema import AndroidAppConfigurationSchema
    from ..android_device_owner_enrollment_profile import AndroidDeviceOwnerEnrollmentProfile
    from ..android_for_work_app_configuration_schema import AndroidForWorkAppConfigurationSchema
    from ..android_for_work_enrollment_profile import AndroidForWorkEnrollmentProfile
    from ..android_for_work_settings import AndroidForWorkSettings
    from ..android_managed_store_account_enterprise_settings import AndroidManagedStoreAccountEnterpriseSettings
    from ..android_managed_store_app_configuration_schema import AndroidManagedStoreAppConfigurationSchema
    from ..apple_push_notification_certificate import ApplePushNotificationCertificate
    from ..apple_user_initiated_enrollment_profile import AppleUserInitiatedEnrollmentProfile
    from ..audit_event import AuditEvent
    from ..cart_to_class_association import CartToClassAssociation
    from ..certificate_connector_details import CertificateConnectorDetails
    from ..chrome_o_s_onboarding_settings import ChromeOSOnboardingSettings
    from ..cloud_certification_authority import CloudCertificationAuthority
    from ..cloud_certification_authority_leaf_certificate import CloudCertificationAuthorityLeafCertificate
    from ..cloud_p_c_connectivity_issue import CloudPCConnectivityIssue
    from ..comanagement_eligible_device import ComanagementEligibleDevice
    from ..compliance_management_partner import ComplianceManagementPartner
    from ..config_manager_collection import ConfigManagerCollection
    from ..connector_status_details import ConnectorStatusDetails
    from ..data_processor_service_for_windows_features_onboarding import DataProcessorServiceForWindowsFeaturesOnboarding
    from ..data_sharing_consent import DataSharingConsent
    from ..dep_onboarding_setting import DepOnboardingSetting
    from ..detected_app import DetectedApp
    from ..device_and_app_management_assignment_filter import DeviceAndAppManagementAssignmentFilter
    from ..device_and_app_management_role_assignment import DeviceAndAppManagementRoleAssignment
    from ..device_category import DeviceCategory
    from ..device_compliance_policy import DeviceCompliancePolicy
    from ..device_compliance_policy_device_state_summary import DeviceCompliancePolicyDeviceStateSummary
    from ..device_compliance_policy_setting_state_summary import DeviceCompliancePolicySettingStateSummary
    from ..device_compliance_script import DeviceComplianceScript
    from ..device_configuration import DeviceConfiguration
    from ..device_configuration_conflict_summary import DeviceConfigurationConflictSummary
    from ..device_configuration_device_state_summary import DeviceConfigurationDeviceStateSummary
    from ..device_configuration_user_state_summary import DeviceConfigurationUserStateSummary
    from ..device_custom_attribute_shell_script import DeviceCustomAttributeShellScript
    from ..device_enrollment_configuration import DeviceEnrollmentConfiguration
    from ..device_health_script import DeviceHealthScript
    from ..device_management_autopilot_event import DeviceManagementAutopilotEvent
    from ..device_management_compliance_policy import DeviceManagementCompliancePolicy
    from ..device_management_configuration_category import DeviceManagementConfigurationCategory
    from ..device_management_configuration_policy import DeviceManagementConfigurationPolicy
    from ..device_management_configuration_policy_template import DeviceManagementConfigurationPolicyTemplate
    from ..device_management_configuration_setting_definition import DeviceManagementConfigurationSettingDefinition
    from ..device_management_configuration_setting_template import DeviceManagementConfigurationSettingTemplate
    from ..device_management_derived_credential_settings import DeviceManagementDerivedCredentialSettings
    from ..device_management_domain_join_connector import DeviceManagementDomainJoinConnector
    from ..device_management_exchange_connector import DeviceManagementExchangeConnector
    from ..device_management_exchange_on_premises_policy import DeviceManagementExchangeOnPremisesPolicy
    from ..device_management_intent import DeviceManagementIntent
    from ..device_management_partner import DeviceManagementPartner
    from ..device_management_reports import DeviceManagementReports
    from ..device_management_resource_access_profile_base import DeviceManagementResourceAccessProfileBase
    from ..device_management_reusable_policy_setting import DeviceManagementReusablePolicySetting
    from ..device_management_script import DeviceManagementScript
    from ..device_management_settings import DeviceManagementSettings
    from ..device_management_setting_category import DeviceManagementSettingCategory
    from ..device_management_setting_definition import DeviceManagementSettingDefinition
    from ..device_management_subscriptions import DeviceManagementSubscriptions
    from ..device_management_subscription_state import DeviceManagementSubscriptionState
    from ..device_management_template import DeviceManagementTemplate
    from ..device_management_template_insights_definition import DeviceManagementTemplateInsightsDefinition
    from ..device_management_troubleshooting_event import DeviceManagementTroubleshootingEvent
    from ..device_protection_overview import DeviceProtectionOverview
    from ..device_shell_script import DeviceShellScript
    from ..embedded_s_i_m_activation_code_pool import EmbeddedSIMActivationCodePool
    from ..endpoint_privilege_management_provisioning_status import EndpointPrivilegeManagementProvisioningStatus
    from ..entity import Entity
    from ..group_policy_category import GroupPolicyCategory
    from ..group_policy_configuration import GroupPolicyConfiguration
    from ..group_policy_definition import GroupPolicyDefinition
    from ..group_policy_definition_file import GroupPolicyDefinitionFile
    from ..group_policy_migration_report import GroupPolicyMigrationReport
    from ..group_policy_object_file import GroupPolicyObjectFile
    from ..group_policy_uploaded_definition_file import GroupPolicyUploadedDefinitionFile
    from ..hardware_configuration import HardwareConfiguration
    from ..hardware_password_detail import HardwarePasswordDetail
    from ..hardware_password_info import HardwarePasswordInfo
    from ..imported_device_identity import ImportedDeviceIdentity
    from ..imported_windows_autopilot_device_identity import ImportedWindowsAutopilotDeviceIdentity
    from ..intune_brand import IntuneBrand
    from ..intune_branding_profile import IntuneBrandingProfile
    from ..ios_update_device_status import IosUpdateDeviceStatus
    from ..mac_o_s_software_update_account_summary import MacOSSoftwareUpdateAccountSummary
    from ..managed_all_device_certificate_state import ManagedAllDeviceCertificateState
    from ..managed_device import ManagedDevice
    from ..managed_device_cleanup_rule import ManagedDeviceCleanupRule
    from ..managed_device_cleanup_settings import ManagedDeviceCleanupSettings
    from ..managed_device_encryption_state import ManagedDeviceEncryptionState
    from ..managed_device_overview import ManagedDeviceOverview
    from ..managed_device_windows_operating_system_image import ManagedDeviceWindowsOperatingSystemImage
    from ..microsoft_tunnel_configuration import MicrosoftTunnelConfiguration
    from ..microsoft_tunnel_health_threshold import MicrosoftTunnelHealthThreshold
    from ..microsoft_tunnel_server_log_collection_response import MicrosoftTunnelServerLogCollectionResponse
    from ..microsoft_tunnel_site import MicrosoftTunnelSite
    from ..mobile_app_troubleshooting_event import MobileAppTroubleshootingEvent
    from ..mobile_threat_defense_connector import MobileThreatDefenseConnector
    from ..ndes_connector import NdesConnector
    from ..notification_message_template import NotificationMessageTemplate
    from ..on_premises_conditional_access_settings import OnPremisesConditionalAccessSettings
    from ..operation_approval_policy import OperationApprovalPolicy
    from ..operation_approval_request import OperationApprovalRequest
    from ..privilege_management_elevation import PrivilegeManagementElevation
    from ..privilege_management_elevation_request import PrivilegeManagementElevationRequest
    from ..remote_action_audit import RemoteActionAudit
    from ..remote_assistance_partner import RemoteAssistancePartner
    from ..remote_assistance_settings import RemoteAssistanceSettings
    from ..resource_operation import ResourceOperation
    from ..restricted_apps_violation import RestrictedAppsViolation
    from ..role_definition import RoleDefinition
    from ..role_scope_tag import RoleScopeTag
    from ..samsung_e_fota_firmware_version import SamsungEFotaFirmwareVersion
    from ..service_now_connection import ServiceNowConnection
    from ..software_update_status_summary import SoftwareUpdateStatusSummary
    from ..tenant_attach_r_b_a_c import TenantAttachRBAC
    from ..terms_and_conditions import TermsAndConditions
    from ..user_experience_analytics_anomaly import UserExperienceAnalyticsAnomaly
    from ..user_experience_analytics_anomaly_correlation_group_overview import UserExperienceAnalyticsAnomalyCorrelationGroupOverview
    from ..user_experience_analytics_anomaly_device import UserExperienceAnalyticsAnomalyDevice
    from ..user_experience_analytics_anomaly_severity_overview import UserExperienceAnalyticsAnomalySeverityOverview
    from ..user_experience_analytics_app_health_application_performance import UserExperienceAnalyticsAppHealthApplicationPerformance
    from ..user_experience_analytics_app_health_app_performance_by_app_version import UserExperienceAnalyticsAppHealthAppPerformanceByAppVersion
    from ..user_experience_analytics_app_health_app_performance_by_app_version_details import UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetails
    from ..user_experience_analytics_app_health_app_performance_by_app_version_device_id import UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId
    from ..user_experience_analytics_app_health_app_performance_by_o_s_version import UserExperienceAnalyticsAppHealthAppPerformanceByOSVersion
    from ..user_experience_analytics_app_health_device_model_performance import UserExperienceAnalyticsAppHealthDeviceModelPerformance
    from ..user_experience_analytics_app_health_device_performance import UserExperienceAnalyticsAppHealthDevicePerformance
    from ..user_experience_analytics_app_health_device_performance_details import UserExperienceAnalyticsAppHealthDevicePerformanceDetails
    from ..user_experience_analytics_app_health_o_s_version_performance import UserExperienceAnalyticsAppHealthOSVersionPerformance
    from ..user_experience_analytics_baseline import UserExperienceAnalyticsBaseline
    from ..user_experience_analytics_battery_health_app_impact import UserExperienceAnalyticsBatteryHealthAppImpact
    from ..user_experience_analytics_battery_health_capacity_details import UserExperienceAnalyticsBatteryHealthCapacityDetails
    from ..user_experience_analytics_battery_health_device_app_impact import UserExperienceAnalyticsBatteryHealthDeviceAppImpact
    from ..user_experience_analytics_battery_health_device_performance import UserExperienceAnalyticsBatteryHealthDevicePerformance
    from ..user_experience_analytics_battery_health_device_runtime_history import UserExperienceAnalyticsBatteryHealthDeviceRuntimeHistory
    from ..user_experience_analytics_battery_health_model_performance import UserExperienceAnalyticsBatteryHealthModelPerformance
    from ..user_experience_analytics_battery_health_os_performance import UserExperienceAnalyticsBatteryHealthOsPerformance
    from ..user_experience_analytics_battery_health_runtime_details import UserExperienceAnalyticsBatteryHealthRuntimeDetails
    from ..user_experience_analytics_category import UserExperienceAnalyticsCategory
    from ..user_experience_analytics_device_performance import UserExperienceAnalyticsDevicePerformance
    from ..user_experience_analytics_device_scope import UserExperienceAnalyticsDeviceScope
    from ..user_experience_analytics_device_scores import UserExperienceAnalyticsDeviceScores
    from ..user_experience_analytics_device_startup_history import UserExperienceAnalyticsDeviceStartupHistory
    from ..user_experience_analytics_device_startup_process import UserExperienceAnalyticsDeviceStartupProcess
    from ..user_experience_analytics_device_startup_process_performance import UserExperienceAnalyticsDeviceStartupProcessPerformance
    from ..user_experience_analytics_device_timeline_event import UserExperienceAnalyticsDeviceTimelineEvent
    from ..user_experience_analytics_device_without_cloud_identity import UserExperienceAnalyticsDeviceWithoutCloudIdentity
    from ..user_experience_analytics_impacting_process import UserExperienceAnalyticsImpactingProcess
    from ..user_experience_analytics_metric_history import UserExperienceAnalyticsMetricHistory
    from ..user_experience_analytics_model_scores import UserExperienceAnalyticsModelScores
    from ..user_experience_analytics_not_autopilot_ready_device import UserExperienceAnalyticsNotAutopilotReadyDevice
    from ..user_experience_analytics_overview import UserExperienceAnalyticsOverview
    from ..user_experience_analytics_remote_connection import UserExperienceAnalyticsRemoteConnection
    from ..user_experience_analytics_resource_performance import UserExperienceAnalyticsResourcePerformance
    from ..user_experience_analytics_score_history import UserExperienceAnalyticsScoreHistory
    from ..user_experience_analytics_settings import UserExperienceAnalyticsSettings
    from ..user_experience_analytics_work_from_anywhere_hardware_readiness_metric import UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric
    from ..user_experience_analytics_work_from_anywhere_metric import UserExperienceAnalyticsWorkFromAnywhereMetric
    from ..user_experience_analytics_work_from_anywhere_model_performance import UserExperienceAnalyticsWorkFromAnywhereModelPerformance
    from ..user_p_f_x_certificate import UserPFXCertificate
    from ..virtual_endpoint import VirtualEndpoint
    from ..windows_autopilot_deployment_profile import WindowsAutopilotDeploymentProfile
    from ..windows_autopilot_device_identity import WindowsAutopilotDeviceIdentity
    from ..windows_autopilot_settings import WindowsAutopilotSettings
    from ..windows_driver_update_profile import WindowsDriverUpdateProfile
    from ..windows_feature_update_profile import WindowsFeatureUpdateProfile
    from ..windows_information_protection_app_learning_summary import WindowsInformationProtectionAppLearningSummary
    from ..windows_information_protection_network_learning_summary import WindowsInformationProtectionNetworkLearningSummary
    from ..windows_malware_information import WindowsMalwareInformation
    from ..windows_malware_overview import WindowsMalwareOverview
    from ..windows_quality_update_policy import WindowsQualityUpdatePolicy
    from ..windows_quality_update_profile import WindowsQualityUpdateProfile
    from ..windows_update_catalog_item import WindowsUpdateCatalogItem
    from ..zebra_fota_artifact import ZebraFotaArtifact
    from ..zebra_fota_connector import ZebraFotaConnector
    from ..zebra_fota_deployment import ZebraFotaDeployment
    from .monitoring import Monitoring

from ..entity import Entity

@dataclass
class DeviceManagement(Entity, Parsable):
    # The date & time when tenant data moved between scaleunits.
    account_move_completion_date_time: Optional[datetime.datetime] = None
    # Admin consent information.
    admin_consent: Optional[AdminConsent] = None
    # The summary state of ATP onboarding state for this account.
    advanced_threat_protection_onboarding_state_summary: Optional[AdvancedThreatProtectionOnboardingStateSummary] = None
    # Android App Configurations Schema entity.
    android_app_configuration_schema: Optional[AndroidAppConfigurationSchema] = None
    # Android device owner enrollment profile entities.
    android_device_owner_enrollment_profiles: Optional[list[AndroidDeviceOwnerEnrollmentProfile]] = None
    # Android for Work app configuration schema entities.
    android_for_work_app_configuration_schemas: Optional[list[AndroidForWorkAppConfigurationSchema]] = None
    # Android for Work enrollment profile entities.
    android_for_work_enrollment_profiles: Optional[list[AndroidForWorkEnrollmentProfile]] = None
    # The singleton Android for Work settings entity.
    android_for_work_settings: Optional[AndroidForWorkSettings] = None
    # The singleton Android managed store account enterprise settings entity.
    android_managed_store_account_enterprise_settings: Optional[AndroidManagedStoreAccountEnterpriseSettings] = None
    # Android Enterprise app configuration schema entities.
    android_managed_store_app_configuration_schemas: Optional[list[AndroidManagedStoreAppConfigurationSchema]] = None
    # Apple push notification certificate.
    apple_push_notification_certificate: Optional[ApplePushNotificationCertificate] = None
    # Apple user initiated enrollment profiles
    apple_user_initiated_enrollment_profiles: Optional[list[AppleUserInitiatedEnrollmentProfile]] = None
    # The list of assignment filters
    assignment_filters: Optional[list[DeviceAndAppManagementAssignmentFilter]] = None
    # The Audit Events
    audit_events: Optional[list[AuditEvent]] = None
    # The list of autopilot events for the tenant.
    autopilot_events: Optional[list[DeviceManagementAutopilotEvent]] = None
    # The Cart To Class Associations.
    cart_to_class_associations: Optional[list[CartToClassAssociation]] = None
    # The available categories
    categories: Optional[list[DeviceManagementSettingCategory]] = None
    # Collection of certificate connector details, each associated with a corresponding Intune Certificate Connector.
    certificate_connector_details: Optional[list[CertificateConnectorDetails]] = None
    # Collection of ChromeOSOnboardingSettings settings associated with account.
    chrome_o_s_onboarding_settings: Optional[list[ChromeOSOnboardingSettings]] = None
    # Collection of CloudCertificationAuthority records associated with account.
    cloud_certification_authority: Optional[list[CloudCertificationAuthority]] = None
    # Collection of CloudCertificationAuthorityLeafCertificate records associated with account.
    cloud_certification_authority_leaf_certificate: Optional[list[CloudCertificationAuthorityLeafCertificate]] = None
    # The list of CloudPC Connectivity Issue.
    cloud_p_c_connectivity_issues: Optional[list[CloudPCConnectivityIssue]] = None
    # The list of co-managed devices report
    comanaged_devices: Optional[list[ManagedDevice]] = None
    # The list of co-management eligible devices report
    comanagement_eligible_devices: Optional[list[ComanagementEligibleDevice]] = None
    # List of all compliance categories
    compliance_categories: Optional[list[DeviceManagementConfigurationCategory]] = None
    # The list of Compliance Management Partners configured by the tenant.
    compliance_management_partners: Optional[list[ComplianceManagementPartner]] = None
    # List of all compliance policies
    compliance_policies: Optional[list[DeviceManagementCompliancePolicy]] = None
    # List of all ComplianceSettings
    compliance_settings: Optional[list[DeviceManagementConfigurationSettingDefinition]] = None
    # The Exchange on premises conditional access settings. On premises conditional access will require devices to be both enrolled and compliant for mail access
    conditional_access_settings: Optional[OnPremisesConditionalAccessSettings] = None
    # A list of ConfigManagerCollection
    config_manager_collections: Optional[list[ConfigManagerCollection]] = None
    # List of all Configuration Categories
    configuration_categories: Optional[list[DeviceManagementConfigurationCategory]] = None
    # List of all Configuration policies
    configuration_policies: Optional[list[DeviceManagementConfigurationPolicy]] = None
    # List of all templates
    configuration_policy_templates: Optional[list[DeviceManagementConfigurationPolicyTemplate]] = None
    # List of all ConfigurationSettings
    configuration_settings: Optional[list[DeviceManagementConfigurationSettingDefinition]] = None
    # The list of connector status for the tenant.
    connector_status: Optional[list[ConnectorStatusDetails]] = None
    # A configuration entity for MEM features that utilize Data Processor Service for Windows (DPSW) data.
    data_processor_service_for_windows_features_onboarding: Optional[DataProcessorServiceForWindowsFeaturesOnboarding] = None
    # Data sharing consents.
    data_sharing_consents: Optional[list[DataSharingConsent]] = None
    # This collections of multiple DEP tokens per-tenant.
    dep_onboarding_settings: Optional[list[DepOnboardingSetting]] = None
    # Collection of Derived credential settings associated with account.
    derived_credentials: Optional[list[DeviceManagementDerivedCredentialSettings]] = None
    # The list of detected apps associated with a device.
    detected_apps: Optional[list[DetectedApp]] = None
    # The list of device categories with the tenant.
    device_categories: Optional[list[DeviceCategory]] = None
    # The device compliance policies.
    device_compliance_policies: Optional[list[DeviceCompliancePolicy]] = None
    # The device compliance state summary for this account.
    device_compliance_policy_device_state_summary: Optional[DeviceCompliancePolicyDeviceStateSummary] = None
    # The summary states of compliance policy settings for this account.
    device_compliance_policy_setting_state_summaries: Optional[list[DeviceCompliancePolicySettingStateSummary]] = None
    # The last requested time of device compliance reporting for this account. This property is read-only.
    device_compliance_report_summarization_date_time: Optional[datetime.datetime] = None
    # The list of device compliance scripts associated with the tenant.
    device_compliance_scripts: Optional[list[DeviceComplianceScript]] = None
    # Summary of policies in conflict state for this account.
    device_configuration_conflict_summary: Optional[list[DeviceConfigurationConflictSummary]] = None
    # The device configuration device state summary for this account.
    device_configuration_device_state_summaries: Optional[DeviceConfigurationDeviceStateSummary] = None
    # Restricted apps violations for this account.
    device_configuration_restricted_apps_violations: Optional[list[RestrictedAppsViolation]] = None
    # The device configuration user state summary for this account.
    device_configuration_user_state_summaries: Optional[DeviceConfigurationUserStateSummary] = None
    # The device configurations.
    device_configurations: Optional[list[DeviceConfiguration]] = None
    # Summary of all certificates for all devices.
    device_configurations_all_managed_device_certificate_states: Optional[list[ManagedAllDeviceCertificateState]] = None
    # The list of device custom attribute shell scripts associated with the tenant.
    device_custom_attribute_shell_scripts: Optional[list[DeviceCustomAttributeShellScript]] = None
    # The list of device enrollment configurations
    device_enrollment_configurations: Optional[list[DeviceEnrollmentConfiguration]] = None
    # The list of device health scripts associated with the tenant.
    device_health_scripts: Optional[list[DeviceHealthScript]] = None
    # The list of Device Management Partners configured by the tenant.
    device_management_partners: Optional[list[DeviceManagementPartner]] = None
    # The list of device management scripts associated with the tenant.
    device_management_scripts: Optional[list[DeviceManagementScript]] = None
    # Device protection overview.
    device_protection_overview: Optional[DeviceProtectionOverview] = None
    # The list of device shell scripts associated with the tenant.
    device_shell_scripts: Optional[list[DeviceShellScript]] = None
    # A list of connector objects.
    domain_join_connectors: Optional[list[DeviceManagementDomainJoinConnector]] = None
    # List of elevation requests
    elevation_requests: Optional[list[PrivilegeManagementElevationRequest]] = None
    # The embedded SIM activation code pools created by this account.
    embedded_s_i_m_activation_code_pools: Optional[list[EmbeddedSIMActivationCodePool]] = None
    # Endpoint privilege management (EPM) tenant provisioning status contains tenant level license and onboarding state information.
    endpoint_privilege_management_provisioning_status: Optional[EndpointPrivilegeManagementProvisioningStatus] = None
    # The list of Exchange Connectors configured by the tenant.
    exchange_connectors: Optional[list[DeviceManagementExchangeConnector]] = None
    # The list of Exchange On Premisis policies configured by the tenant.
    exchange_on_premises_policies: Optional[list[DeviceManagementExchangeOnPremisesPolicy]] = None
    # The policy which controls mobile device access to Exchange On Premises
    exchange_on_premises_policy: Optional[DeviceManagementExchangeOnPremisesPolicy] = None
    # The available group policy categories for this account.
    group_policy_categories: Optional[list[GroupPolicyCategory]] = None
    # The group policy configurations created by this account.
    group_policy_configurations: Optional[list[GroupPolicyConfiguration]] = None
    # The available group policy definition files for this account.
    group_policy_definition_files: Optional[list[GroupPolicyDefinitionFile]] = None
    # The available group policy definitions for this account.
    group_policy_definitions: Optional[list[GroupPolicyDefinition]] = None
    # A list of Group Policy migration reports.
    group_policy_migration_reports: Optional[list[GroupPolicyMigrationReport]] = None
    # A list of Group Policy Object files uploaded.
    group_policy_object_files: Optional[list[GroupPolicyObjectFile]] = None
    # The available group policy uploaded definition files for this account.
    group_policy_uploaded_definition_files: Optional[list[GroupPolicyUploadedDefinitionFile]] = None
    # BIOS configuration and other settings provides customers the ability to configure hardware/bios settings on the enrolled Windows 10/11 Entra ID joined devices by uploading a configuration file generated with their OEM tool (e.g. Dell Command tool). A BIOS configuration policy can be assigned to multiple devices, allowing admins to remotely control a device's hardware properties (e.g. enable Secure Boot) from the Intune Portal. Supported for Dell only at this time.
    hardware_configurations: Optional[list[HardwareConfiguration]] = None
    # Device BIOS password information for devices with managed BIOS and firmware configuration, which provides device serial number, list of previous passwords, and current password.
    hardware_password_details: Optional[list[HardwarePasswordDetail]] = None
    # Intune will provide customer the ability to configure BIOS configuration settings on the enrolled Windows 10 and Windows 11 Microsoft Entra joined devices. Starting from June, 2024, customers should start using hardwarePasswordDetail resource type - Microsoft Graph beta | Microsoft Learn. HardwarePasswordInfo will be marked as deprecated with Intune Release 2409
    hardware_password_info: Optional[list[HardwarePasswordInfo]] = None
    # The imported device identities.
    imported_device_identities: Optional[list[ImportedDeviceIdentity]] = None
    # Collection of imported Windows autopilot devices.
    imported_windows_autopilot_device_identities: Optional[list[ImportedWindowsAutopilotDeviceIdentity]] = None
    # The device management intents
    intents: Optional[list[DeviceManagementIntent]] = None
    # Intune Account Id for given tenant
    intune_account_id: Optional[UUID] = None
    # intuneBrand contains data which is used in customizing the appearance of the Company Portal applications as well as the end user web portal.
    intune_brand: Optional[IntuneBrand] = None
    # Intune branding profiles targeted to AAD groups
    intune_branding_profiles: Optional[list[IntuneBrandingProfile]] = None
    # The IOS software update installation statuses for this account.
    ios_update_statuses: Optional[list[IosUpdateDeviceStatus]] = None
    # The last modified time of reporting for this account. This property is read-only.
    last_report_aggregation_date_time: Optional[datetime.datetime] = None
    # The property to enable Non-MDM managed legacy PC management for this account. This property is read-only.
    legacy_pc_manangement_enabled: Optional[bool] = None
    # The MacOS software update account summaries for this account.
    mac_o_s_software_update_account_summaries: Optional[list[MacOSSoftwareUpdateAccountSummary]] = None
    # Device cleanup rule V2
    managed_device_cleanup_rules: Optional[list[ManagedDeviceCleanupRule]] = None
    # Device cleanup rule
    managed_device_cleanup_settings: Optional[ManagedDeviceCleanupSettings] = None
    # Encryption report for devices in this account
    managed_device_encryption_states: Optional[list[ManagedDeviceEncryptionState]] = None
    # Device overview
    managed_device_overview: Optional[ManagedDeviceOverview] = None
    # A list of ManagedDeviceWindowsOperatingSystemImages
    managed_device_windows_o_s_images: Optional[list[ManagedDeviceWindowsOperatingSystemImage]] = None
    # The list of managed devices.
    managed_devices: Optional[list[ManagedDevice]] = None
    # Maximum number of dep tokens allowed per-tenant.
    maximum_dep_tokens: Optional[int] = None
    # Collection of MicrosoftTunnelConfiguration settings associated with account.
    microsoft_tunnel_configurations: Optional[list[MicrosoftTunnelConfiguration]] = None
    # Collection of MicrosoftTunnelHealthThreshold settings associated with account.
    microsoft_tunnel_health_thresholds: Optional[list[MicrosoftTunnelHealthThreshold]] = None
    # Collection of MicrosoftTunnelServerLogCollectionResponse settings associated with account.
    microsoft_tunnel_server_log_collection_responses: Optional[list[MicrosoftTunnelServerLogCollectionResponse]] = None
    # Collection of MicrosoftTunnelSite settings associated with account.
    microsoft_tunnel_sites: Optional[list[MicrosoftTunnelSite]] = None
    # The collection property of MobileAppTroubleshootingEvent.
    mobile_app_troubleshooting_events: Optional[list[MobileAppTroubleshootingEvent]] = None
    # The list of Mobile threat Defense connectors configured by the tenant.
    mobile_threat_defense_connectors: Optional[list[MobileThreatDefenseConnector]] = None
    # The monitoring property
    monitoring: Optional[Monitoring] = None
    # The collection of Ndes connectors for this account.
    ndes_connectors: Optional[list[NdesConnector]] = None
    # The Notification Message Templates.
    notification_message_templates: Optional[list[NotificationMessageTemplate]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The Operation Approval Policies
    operation_approval_policies: Optional[list[OperationApprovalPolicy]] = None
    # The Operation Approval Requests
    operation_approval_requests: Optional[list[OperationApprovalRequest]] = None
    # The endpoint privilege management elevation event entity contains elevation details.
    privilege_management_elevations: Optional[list[PrivilegeManagementElevation]] = None
    # The list of device remote action audits with the tenant.
    remote_action_audits: Optional[list[RemoteActionAudit]] = None
    # The remote assist partners.
    remote_assistance_partners: Optional[list[RemoteAssistancePartner]] = None
    # The remote assistance settings singleton
    remote_assistance_settings: Optional[RemoteAssistanceSettings] = None
    # Reports singleton
    reports: Optional[DeviceManagementReports] = None
    # Collection of resource access settings associated with account.
    resource_access_profiles: Optional[list[DeviceManagementResourceAccessProfileBase]] = None
    # The Resource Operations.
    resource_operations: Optional[list[ResourceOperation]] = None
    # List of all reusable settings that can be referred in a policy
    reusable_policy_settings: Optional[list[DeviceManagementReusablePolicySetting]] = None
    # List of all reusable settings
    reusable_settings: Optional[list[DeviceManagementConfigurationSettingDefinition]] = None
    # The Role Assignments.
    role_assignments: Optional[list[DeviceAndAppManagementRoleAssignment]] = None
    # The Role Definitions.
    role_definitions: Optional[list[RoleDefinition]] = None
    # The Role Scope Tags.
    role_scope_tags: Optional[list[RoleScopeTag]] = None
    # The collection of Samsung EFOTA firmware versions.
    samsung_e_fota_firmware_versions: Optional[list[SamsungEFotaFirmwareVersion]] = None
    # A list of ServiceNowConnections
    service_now_connections: Optional[list[ServiceNowConnection]] = None
    # The device management intent setting definitions
    setting_definitions: Optional[list[DeviceManagementSettingDefinition]] = None
    # Account level settings.
    settings: Optional[DeviceManagementSettings] = None
    # The software update status summary.
    software_update_status_summary: Optional[SoftwareUpdateStatusSummary] = None
    # Tenant mobile device management subscription state.
    subscription_state: Optional[DeviceManagementSubscriptionState] = None
    # Tenant mobile device management subscriptions.
    subscriptions: Optional[DeviceManagementSubscriptions] = None
    # List of setting insights in a template
    template_insights: Optional[list[DeviceManagementTemplateInsightsDefinition]] = None
    # List of all TemplateSettings
    template_settings: Optional[list[DeviceManagementConfigurationSettingTemplate]] = None
    # The available templates
    templates: Optional[list[DeviceManagementTemplate]] = None
    # TenantAttach RBAC Enablement
    tenant_attach_r_b_a_c: Optional[TenantAttachRBAC] = None
    # The terms and conditions associated with device management of the company.
    terms_and_conditions: Optional[list[TermsAndConditions]] = None
    # The list of troubleshooting events for the tenant.
    troubleshooting_events: Optional[list[DeviceManagementTroubleshootingEvent]] = None
    # When enabled, users assigned as administrators via Role Assignment Memberships do not require an assigned Intune license. Prior to this, only Intune licensed users were granted permissions with an Intune role unless they were assigned a role via Azure Active Directory. You are limited to 350 unlicensed direct members for each AAD security group in a role assignment, but you can assign multiple AAD security groups to a role if you need to support more than 350 unlicensed administrators. Licensed administrators are unaffected, do not have to be direct members, nor does the 350 member limit apply. This property is read-only.
    unlicensed_adminstrators_enabled: Optional[bool] = None
    # The user experience analytics anomaly entity contains anomaly details.
    user_experience_analytics_anomaly: Optional[list[UserExperienceAnalyticsAnomaly]] = None
    # The user experience analytics anomaly correlation group overview entity contains the information for each correlation group of an anomaly.
    user_experience_analytics_anomaly_correlation_group_overview: Optional[list[UserExperienceAnalyticsAnomalyCorrelationGroupOverview]] = None
    # The user experience analytics anomaly entity contains device details.
    user_experience_analytics_anomaly_device: Optional[list[UserExperienceAnalyticsAnomalyDevice]] = None
    # The user experience analytics anomaly severity overview entity contains the count information for each severity of anomaly.
    user_experience_analytics_anomaly_severity_overview: Optional[UserExperienceAnalyticsAnomalySeverityOverview] = None
    # User experience analytics appHealth Application Performance
    user_experience_analytics_app_health_application_performance: Optional[list[UserExperienceAnalyticsAppHealthApplicationPerformance]] = None
    # User experience analytics appHealth Application Performance by App Version
    user_experience_analytics_app_health_application_performance_by_app_version: Optional[list[UserExperienceAnalyticsAppHealthAppPerformanceByAppVersion]] = None
    # User experience analytics appHealth Application Performance by App Version details
    user_experience_analytics_app_health_application_performance_by_app_version_details: Optional[list[UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetails]] = None
    # User experience analytics appHealth Application Performance by App Version Device Id
    user_experience_analytics_app_health_application_performance_by_app_version_device_id: Optional[list[UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId]] = None
    # User experience analytics appHealth Application Performance by OS Version
    user_experience_analytics_app_health_application_performance_by_o_s_version: Optional[list[UserExperienceAnalyticsAppHealthAppPerformanceByOSVersion]] = None
    # User experience analytics appHealth Model Performance
    user_experience_analytics_app_health_device_model_performance: Optional[list[UserExperienceAnalyticsAppHealthDeviceModelPerformance]] = None
    # User experience analytics appHealth Device Performance
    user_experience_analytics_app_health_device_performance: Optional[list[UserExperienceAnalyticsAppHealthDevicePerformance]] = None
    # User experience analytics device performance details
    user_experience_analytics_app_health_device_performance_details: Optional[list[UserExperienceAnalyticsAppHealthDevicePerformanceDetails]] = None
    # User experience analytics appHealth OS version Performance
    user_experience_analytics_app_health_o_s_version_performance: Optional[list[UserExperienceAnalyticsAppHealthOSVersionPerformance]] = None
    # User experience analytics appHealth overview
    user_experience_analytics_app_health_overview: Optional[UserExperienceAnalyticsCategory] = None
    # User experience analytics baselines
    user_experience_analytics_baselines: Optional[list[UserExperienceAnalyticsBaseline]] = None
    # User Experience Analytics Battery Health App Impact
    user_experience_analytics_battery_health_app_impact: Optional[list[UserExperienceAnalyticsBatteryHealthAppImpact]] = None
    # User Experience Analytics Battery Health Capacity Details
    user_experience_analytics_battery_health_capacity_details: Optional[UserExperienceAnalyticsBatteryHealthCapacityDetails] = None
    # User Experience Analytics Battery Health Device App Impact
    user_experience_analytics_battery_health_device_app_impact: Optional[list[UserExperienceAnalyticsBatteryHealthDeviceAppImpact]] = None
    # User Experience Analytics Battery Health Device Performance
    user_experience_analytics_battery_health_device_performance: Optional[list[UserExperienceAnalyticsBatteryHealthDevicePerformance]] = None
    # User Experience Analytics Battery Health Device Runtime History
    user_experience_analytics_battery_health_device_runtime_history: Optional[list[UserExperienceAnalyticsBatteryHealthDeviceRuntimeHistory]] = None
    # User Experience Analytics Battery Health Model Performance
    user_experience_analytics_battery_health_model_performance: Optional[list[UserExperienceAnalyticsBatteryHealthModelPerformance]] = None
    # User Experience Analytics Battery Health Os Performance
    user_experience_analytics_battery_health_os_performance: Optional[list[UserExperienceAnalyticsBatteryHealthOsPerformance]] = None
    # User Experience Analytics Battery Health Runtime Details
    user_experience_analytics_battery_health_runtime_details: Optional[UserExperienceAnalyticsBatteryHealthRuntimeDetails] = None
    # User experience analytics categories
    user_experience_analytics_categories: Optional[list[UserExperienceAnalyticsCategory]] = None
    # User experience analytics device metric history. The report will be retired on December 31, 2024. You can start using the Cloud PC connection quality report now via https://learn.microsoft.com/windows-365/enterprise/report-cloud-pc-connection-quality.
    user_experience_analytics_device_metric_history: Optional[list[UserExperienceAnalyticsMetricHistory]] = None
    # User experience analytics device performance
    user_experience_analytics_device_performance: Optional[list[UserExperienceAnalyticsDevicePerformance]] = None
    # The user experience analytics device scope entity endpoint to trigger on the service to either START or STOP computing metrics data based on a device scope configuration.
    user_experience_analytics_device_scope: Optional[UserExperienceAnalyticsDeviceScope] = None
    # The user experience analytics device scope entity contains device scope configuration use to apply filtering on the endpoint analytics reports.
    user_experience_analytics_device_scopes: Optional[list[UserExperienceAnalyticsDeviceScope]] = None
    # User experience analytics device scores
    user_experience_analytics_device_scores: Optional[list[UserExperienceAnalyticsDeviceScores]] = None
    # User experience analytics device Startup History
    user_experience_analytics_device_startup_history: Optional[list[UserExperienceAnalyticsDeviceStartupHistory]] = None
    # User experience analytics device Startup Process Performance
    user_experience_analytics_device_startup_process_performance: Optional[list[UserExperienceAnalyticsDeviceStartupProcessPerformance]] = None
    # User experience analytics device Startup Processes
    user_experience_analytics_device_startup_processes: Optional[list[UserExperienceAnalyticsDeviceStartupProcess]] = None
    # The user experience analytics device events entity contains NRT device timeline event details.
    user_experience_analytics_device_timeline_event: Optional[list[UserExperienceAnalyticsDeviceTimelineEvent]] = None
    # User experience analytics devices without cloud identity.
    user_experience_analytics_devices_without_cloud_identity: Optional[list[UserExperienceAnalyticsDeviceWithoutCloudIdentity]] = None
    # User experience analytics impacting process
    user_experience_analytics_impacting_process: Optional[list[UserExperienceAnalyticsImpactingProcess]] = None
    # User experience analytics metric history
    user_experience_analytics_metric_history: Optional[list[UserExperienceAnalyticsMetricHistory]] = None
    # User experience analytics model scores
    user_experience_analytics_model_scores: Optional[list[UserExperienceAnalyticsModelScores]] = None
    # User experience analytics devices not Windows Autopilot ready.
    user_experience_analytics_not_autopilot_ready_device: Optional[list[UserExperienceAnalyticsNotAutopilotReadyDevice]] = None
    # User experience analytics overview
    user_experience_analytics_overview: Optional[UserExperienceAnalyticsOverview] = None
    # User experience analytics remote connection. The report will be retired on December 31, 2024. You can start using the Cloud PC connection quality report now via https://learn.microsoft.com/windows-365/enterprise/report-cloud-pc-connection-quality.
    user_experience_analytics_remote_connection: Optional[list[UserExperienceAnalyticsRemoteConnection]] = None
    # User experience analytics resource performance
    user_experience_analytics_resource_performance: Optional[list[UserExperienceAnalyticsResourcePerformance]] = None
    # User experience analytics device Startup Score History
    user_experience_analytics_score_history: Optional[list[UserExperienceAnalyticsScoreHistory]] = None
    # User experience analytics device settings
    user_experience_analytics_settings: Optional[UserExperienceAnalyticsSettings] = None
    # User experience analytics work from anywhere hardware readiness metrics.
    user_experience_analytics_work_from_anywhere_hardware_readiness_metric: Optional[UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric] = None
    # User experience analytics work from anywhere metrics.
    user_experience_analytics_work_from_anywhere_metrics: Optional[list[UserExperienceAnalyticsWorkFromAnywhereMetric]] = None
    # The user experience analytics work from anywhere model performance
    user_experience_analytics_work_from_anywhere_model_performance: Optional[list[UserExperienceAnalyticsWorkFromAnywhereModelPerformance]] = None
    # Collection of PFX certificates associated with a user.
    user_pfx_certificates: Optional[list[UserPFXCertificate]] = None
    # The virtualEndpoint property
    virtual_endpoint: Optional[VirtualEndpoint] = None
    # Windows auto pilot deployment profiles
    windows_autopilot_deployment_profiles: Optional[list[WindowsAutopilotDeploymentProfile]] = None
    # The Windows autopilot device identities contained collection.
    windows_autopilot_device_identities: Optional[list[WindowsAutopilotDeviceIdentity]] = None
    # The Windows autopilot account settings.
    windows_autopilot_settings: Optional[WindowsAutopilotSettings] = None
    # A collection of windows driver update profiles
    windows_driver_update_profiles: Optional[list[WindowsDriverUpdateProfile]] = None
    # A collection of windows feature update profiles
    windows_feature_update_profiles: Optional[list[WindowsFeatureUpdateProfile]] = None
    # The windows information protection app learning summaries.
    windows_information_protection_app_learning_summaries: Optional[list[WindowsInformationProtectionAppLearningSummary]] = None
    # The windows information protection network learning summaries.
    windows_information_protection_network_learning_summaries: Optional[list[WindowsInformationProtectionNetworkLearningSummary]] = None
    # The list of affected malware in the tenant.
    windows_malware_information: Optional[list[WindowsMalwareInformation]] = None
    # Malware overview for windows devices.
    windows_malware_overview: Optional[WindowsMalwareOverview] = None
    # A collection of Windows quality update policies
    windows_quality_update_policies: Optional[list[WindowsQualityUpdatePolicy]] = None
    # A collection of windows quality update profiles
    windows_quality_update_profiles: Optional[list[WindowsQualityUpdateProfile]] = None
    # A collection of windows update catalog items (fetaure updates item , quality updates item)
    windows_update_catalog_items: Optional[list[WindowsUpdateCatalogItem]] = None
    # The Collection of ZebraFotaArtifacts.
    zebra_fota_artifacts: Optional[list[ZebraFotaArtifact]] = None
    # The singleton ZebraFotaConnector associated with account.
    zebra_fota_connector: Optional[ZebraFotaConnector] = None
    # Collection of ZebraFotaDeployments associated with account.
    zebra_fota_deployments: Optional[list[ZebraFotaDeployment]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagement:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagement
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagement()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..admin_consent import AdminConsent
        from ..advanced_threat_protection_onboarding_state_summary import AdvancedThreatProtectionOnboardingStateSummary
        from ..android_app_configuration_schema import AndroidAppConfigurationSchema
        from ..android_device_owner_enrollment_profile import AndroidDeviceOwnerEnrollmentProfile
        from ..android_for_work_app_configuration_schema import AndroidForWorkAppConfigurationSchema
        from ..android_for_work_enrollment_profile import AndroidForWorkEnrollmentProfile
        from ..android_for_work_settings import AndroidForWorkSettings
        from ..android_managed_store_account_enterprise_settings import AndroidManagedStoreAccountEnterpriseSettings
        from ..android_managed_store_app_configuration_schema import AndroidManagedStoreAppConfigurationSchema
        from ..apple_push_notification_certificate import ApplePushNotificationCertificate
        from ..apple_user_initiated_enrollment_profile import AppleUserInitiatedEnrollmentProfile
        from ..audit_event import AuditEvent
        from ..cart_to_class_association import CartToClassAssociation
        from ..certificate_connector_details import CertificateConnectorDetails
        from ..chrome_o_s_onboarding_settings import ChromeOSOnboardingSettings
        from ..cloud_certification_authority import CloudCertificationAuthority
        from ..cloud_certification_authority_leaf_certificate import CloudCertificationAuthorityLeafCertificate
        from ..cloud_p_c_connectivity_issue import CloudPCConnectivityIssue
        from ..comanagement_eligible_device import ComanagementEligibleDevice
        from ..compliance_management_partner import ComplianceManagementPartner
        from ..config_manager_collection import ConfigManagerCollection
        from ..connector_status_details import ConnectorStatusDetails
        from ..data_processor_service_for_windows_features_onboarding import DataProcessorServiceForWindowsFeaturesOnboarding
        from ..data_sharing_consent import DataSharingConsent
        from ..dep_onboarding_setting import DepOnboardingSetting
        from ..detected_app import DetectedApp
        from ..device_and_app_management_assignment_filter import DeviceAndAppManagementAssignmentFilter
        from ..device_and_app_management_role_assignment import DeviceAndAppManagementRoleAssignment
        from ..device_category import DeviceCategory
        from ..device_compliance_policy import DeviceCompliancePolicy
        from ..device_compliance_policy_device_state_summary import DeviceCompliancePolicyDeviceStateSummary
        from ..device_compliance_policy_setting_state_summary import DeviceCompliancePolicySettingStateSummary
        from ..device_compliance_script import DeviceComplianceScript
        from ..device_configuration import DeviceConfiguration
        from ..device_configuration_conflict_summary import DeviceConfigurationConflictSummary
        from ..device_configuration_device_state_summary import DeviceConfigurationDeviceStateSummary
        from ..device_configuration_user_state_summary import DeviceConfigurationUserStateSummary
        from ..device_custom_attribute_shell_script import DeviceCustomAttributeShellScript
        from ..device_enrollment_configuration import DeviceEnrollmentConfiguration
        from ..device_health_script import DeviceHealthScript
        from ..device_management_autopilot_event import DeviceManagementAutopilotEvent
        from ..device_management_compliance_policy import DeviceManagementCompliancePolicy
        from ..device_management_configuration_category import DeviceManagementConfigurationCategory
        from ..device_management_configuration_policy import DeviceManagementConfigurationPolicy
        from ..device_management_configuration_policy_template import DeviceManagementConfigurationPolicyTemplate
        from ..device_management_configuration_setting_definition import DeviceManagementConfigurationSettingDefinition
        from ..device_management_configuration_setting_template import DeviceManagementConfigurationSettingTemplate
        from ..device_management_derived_credential_settings import DeviceManagementDerivedCredentialSettings
        from ..device_management_domain_join_connector import DeviceManagementDomainJoinConnector
        from ..device_management_exchange_connector import DeviceManagementExchangeConnector
        from ..device_management_exchange_on_premises_policy import DeviceManagementExchangeOnPremisesPolicy
        from ..device_management_intent import DeviceManagementIntent
        from ..device_management_partner import DeviceManagementPartner
        from ..device_management_reports import DeviceManagementReports
        from ..device_management_resource_access_profile_base import DeviceManagementResourceAccessProfileBase
        from ..device_management_reusable_policy_setting import DeviceManagementReusablePolicySetting
        from ..device_management_script import DeviceManagementScript
        from ..device_management_settings import DeviceManagementSettings
        from ..device_management_setting_category import DeviceManagementSettingCategory
        from ..device_management_setting_definition import DeviceManagementSettingDefinition
        from ..device_management_subscriptions import DeviceManagementSubscriptions
        from ..device_management_subscription_state import DeviceManagementSubscriptionState
        from ..device_management_template import DeviceManagementTemplate
        from ..device_management_template_insights_definition import DeviceManagementTemplateInsightsDefinition
        from ..device_management_troubleshooting_event import DeviceManagementTroubleshootingEvent
        from ..device_protection_overview import DeviceProtectionOverview
        from ..device_shell_script import DeviceShellScript
        from ..embedded_s_i_m_activation_code_pool import EmbeddedSIMActivationCodePool
        from ..endpoint_privilege_management_provisioning_status import EndpointPrivilegeManagementProvisioningStatus
        from ..entity import Entity
        from ..group_policy_category import GroupPolicyCategory
        from ..group_policy_configuration import GroupPolicyConfiguration
        from ..group_policy_definition import GroupPolicyDefinition
        from ..group_policy_definition_file import GroupPolicyDefinitionFile
        from ..group_policy_migration_report import GroupPolicyMigrationReport
        from ..group_policy_object_file import GroupPolicyObjectFile
        from ..group_policy_uploaded_definition_file import GroupPolicyUploadedDefinitionFile
        from ..hardware_configuration import HardwareConfiguration
        from ..hardware_password_detail import HardwarePasswordDetail
        from ..hardware_password_info import HardwarePasswordInfo
        from ..imported_device_identity import ImportedDeviceIdentity
        from ..imported_windows_autopilot_device_identity import ImportedWindowsAutopilotDeviceIdentity
        from ..intune_brand import IntuneBrand
        from ..intune_branding_profile import IntuneBrandingProfile
        from ..ios_update_device_status import IosUpdateDeviceStatus
        from ..mac_o_s_software_update_account_summary import MacOSSoftwareUpdateAccountSummary
        from ..managed_all_device_certificate_state import ManagedAllDeviceCertificateState
        from ..managed_device import ManagedDevice
        from ..managed_device_cleanup_rule import ManagedDeviceCleanupRule
        from ..managed_device_cleanup_settings import ManagedDeviceCleanupSettings
        from ..managed_device_encryption_state import ManagedDeviceEncryptionState
        from ..managed_device_overview import ManagedDeviceOverview
        from ..managed_device_windows_operating_system_image import ManagedDeviceWindowsOperatingSystemImage
        from ..microsoft_tunnel_configuration import MicrosoftTunnelConfiguration
        from ..microsoft_tunnel_health_threshold import MicrosoftTunnelHealthThreshold
        from ..microsoft_tunnel_server_log_collection_response import MicrosoftTunnelServerLogCollectionResponse
        from ..microsoft_tunnel_site import MicrosoftTunnelSite
        from ..mobile_app_troubleshooting_event import MobileAppTroubleshootingEvent
        from ..mobile_threat_defense_connector import MobileThreatDefenseConnector
        from ..ndes_connector import NdesConnector
        from ..notification_message_template import NotificationMessageTemplate
        from ..on_premises_conditional_access_settings import OnPremisesConditionalAccessSettings
        from ..operation_approval_policy import OperationApprovalPolicy
        from ..operation_approval_request import OperationApprovalRequest
        from ..privilege_management_elevation import PrivilegeManagementElevation
        from ..privilege_management_elevation_request import PrivilegeManagementElevationRequest
        from ..remote_action_audit import RemoteActionAudit
        from ..remote_assistance_partner import RemoteAssistancePartner
        from ..remote_assistance_settings import RemoteAssistanceSettings
        from ..resource_operation import ResourceOperation
        from ..restricted_apps_violation import RestrictedAppsViolation
        from ..role_definition import RoleDefinition
        from ..role_scope_tag import RoleScopeTag
        from ..samsung_e_fota_firmware_version import SamsungEFotaFirmwareVersion
        from ..service_now_connection import ServiceNowConnection
        from ..software_update_status_summary import SoftwareUpdateStatusSummary
        from ..tenant_attach_r_b_a_c import TenantAttachRBAC
        from ..terms_and_conditions import TermsAndConditions
        from ..user_experience_analytics_anomaly import UserExperienceAnalyticsAnomaly
        from ..user_experience_analytics_anomaly_correlation_group_overview import UserExperienceAnalyticsAnomalyCorrelationGroupOverview
        from ..user_experience_analytics_anomaly_device import UserExperienceAnalyticsAnomalyDevice
        from ..user_experience_analytics_anomaly_severity_overview import UserExperienceAnalyticsAnomalySeverityOverview
        from ..user_experience_analytics_app_health_application_performance import UserExperienceAnalyticsAppHealthApplicationPerformance
        from ..user_experience_analytics_app_health_app_performance_by_app_version import UserExperienceAnalyticsAppHealthAppPerformanceByAppVersion
        from ..user_experience_analytics_app_health_app_performance_by_app_version_details import UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetails
        from ..user_experience_analytics_app_health_app_performance_by_app_version_device_id import UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId
        from ..user_experience_analytics_app_health_app_performance_by_o_s_version import UserExperienceAnalyticsAppHealthAppPerformanceByOSVersion
        from ..user_experience_analytics_app_health_device_model_performance import UserExperienceAnalyticsAppHealthDeviceModelPerformance
        from ..user_experience_analytics_app_health_device_performance import UserExperienceAnalyticsAppHealthDevicePerformance
        from ..user_experience_analytics_app_health_device_performance_details import UserExperienceAnalyticsAppHealthDevicePerformanceDetails
        from ..user_experience_analytics_app_health_o_s_version_performance import UserExperienceAnalyticsAppHealthOSVersionPerformance
        from ..user_experience_analytics_baseline import UserExperienceAnalyticsBaseline
        from ..user_experience_analytics_battery_health_app_impact import UserExperienceAnalyticsBatteryHealthAppImpact
        from ..user_experience_analytics_battery_health_capacity_details import UserExperienceAnalyticsBatteryHealthCapacityDetails
        from ..user_experience_analytics_battery_health_device_app_impact import UserExperienceAnalyticsBatteryHealthDeviceAppImpact
        from ..user_experience_analytics_battery_health_device_performance import UserExperienceAnalyticsBatteryHealthDevicePerformance
        from ..user_experience_analytics_battery_health_device_runtime_history import UserExperienceAnalyticsBatteryHealthDeviceRuntimeHistory
        from ..user_experience_analytics_battery_health_model_performance import UserExperienceAnalyticsBatteryHealthModelPerformance
        from ..user_experience_analytics_battery_health_os_performance import UserExperienceAnalyticsBatteryHealthOsPerformance
        from ..user_experience_analytics_battery_health_runtime_details import UserExperienceAnalyticsBatteryHealthRuntimeDetails
        from ..user_experience_analytics_category import UserExperienceAnalyticsCategory
        from ..user_experience_analytics_device_performance import UserExperienceAnalyticsDevicePerformance
        from ..user_experience_analytics_device_scope import UserExperienceAnalyticsDeviceScope
        from ..user_experience_analytics_device_scores import UserExperienceAnalyticsDeviceScores
        from ..user_experience_analytics_device_startup_history import UserExperienceAnalyticsDeviceStartupHistory
        from ..user_experience_analytics_device_startup_process import UserExperienceAnalyticsDeviceStartupProcess
        from ..user_experience_analytics_device_startup_process_performance import UserExperienceAnalyticsDeviceStartupProcessPerformance
        from ..user_experience_analytics_device_timeline_event import UserExperienceAnalyticsDeviceTimelineEvent
        from ..user_experience_analytics_device_without_cloud_identity import UserExperienceAnalyticsDeviceWithoutCloudIdentity
        from ..user_experience_analytics_impacting_process import UserExperienceAnalyticsImpactingProcess
        from ..user_experience_analytics_metric_history import UserExperienceAnalyticsMetricHistory
        from ..user_experience_analytics_model_scores import UserExperienceAnalyticsModelScores
        from ..user_experience_analytics_not_autopilot_ready_device import UserExperienceAnalyticsNotAutopilotReadyDevice
        from ..user_experience_analytics_overview import UserExperienceAnalyticsOverview
        from ..user_experience_analytics_remote_connection import UserExperienceAnalyticsRemoteConnection
        from ..user_experience_analytics_resource_performance import UserExperienceAnalyticsResourcePerformance
        from ..user_experience_analytics_score_history import UserExperienceAnalyticsScoreHistory
        from ..user_experience_analytics_settings import UserExperienceAnalyticsSettings
        from ..user_experience_analytics_work_from_anywhere_hardware_readiness_metric import UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric
        from ..user_experience_analytics_work_from_anywhere_metric import UserExperienceAnalyticsWorkFromAnywhereMetric
        from ..user_experience_analytics_work_from_anywhere_model_performance import UserExperienceAnalyticsWorkFromAnywhereModelPerformance
        from ..user_p_f_x_certificate import UserPFXCertificate
        from ..virtual_endpoint import VirtualEndpoint
        from ..windows_autopilot_deployment_profile import WindowsAutopilotDeploymentProfile
        from ..windows_autopilot_device_identity import WindowsAutopilotDeviceIdentity
        from ..windows_autopilot_settings import WindowsAutopilotSettings
        from ..windows_driver_update_profile import WindowsDriverUpdateProfile
        from ..windows_feature_update_profile import WindowsFeatureUpdateProfile
        from ..windows_information_protection_app_learning_summary import WindowsInformationProtectionAppLearningSummary
        from ..windows_information_protection_network_learning_summary import WindowsInformationProtectionNetworkLearningSummary
        from ..windows_malware_information import WindowsMalwareInformation
        from ..windows_malware_overview import WindowsMalwareOverview
        from ..windows_quality_update_policy import WindowsQualityUpdatePolicy
        from ..windows_quality_update_profile import WindowsQualityUpdateProfile
        from ..windows_update_catalog_item import WindowsUpdateCatalogItem
        from ..zebra_fota_artifact import ZebraFotaArtifact
        from ..zebra_fota_connector import ZebraFotaConnector
        from ..zebra_fota_deployment import ZebraFotaDeployment
        from .monitoring import Monitoring

        from ..admin_consent import AdminConsent
        from ..advanced_threat_protection_onboarding_state_summary import AdvancedThreatProtectionOnboardingStateSummary
        from ..android_app_configuration_schema import AndroidAppConfigurationSchema
        from ..android_device_owner_enrollment_profile import AndroidDeviceOwnerEnrollmentProfile
        from ..android_for_work_app_configuration_schema import AndroidForWorkAppConfigurationSchema
        from ..android_for_work_enrollment_profile import AndroidForWorkEnrollmentProfile
        from ..android_for_work_settings import AndroidForWorkSettings
        from ..android_managed_store_account_enterprise_settings import AndroidManagedStoreAccountEnterpriseSettings
        from ..android_managed_store_app_configuration_schema import AndroidManagedStoreAppConfigurationSchema
        from ..apple_push_notification_certificate import ApplePushNotificationCertificate
        from ..apple_user_initiated_enrollment_profile import AppleUserInitiatedEnrollmentProfile
        from ..audit_event import AuditEvent
        from ..cart_to_class_association import CartToClassAssociation
        from ..certificate_connector_details import CertificateConnectorDetails
        from ..chrome_o_s_onboarding_settings import ChromeOSOnboardingSettings
        from ..cloud_certification_authority import CloudCertificationAuthority
        from ..cloud_certification_authority_leaf_certificate import CloudCertificationAuthorityLeafCertificate
        from ..cloud_p_c_connectivity_issue import CloudPCConnectivityIssue
        from ..comanagement_eligible_device import ComanagementEligibleDevice
        from ..compliance_management_partner import ComplianceManagementPartner
        from ..config_manager_collection import ConfigManagerCollection
        from ..connector_status_details import ConnectorStatusDetails
        from ..data_processor_service_for_windows_features_onboarding import DataProcessorServiceForWindowsFeaturesOnboarding
        from ..data_sharing_consent import DataSharingConsent
        from ..dep_onboarding_setting import DepOnboardingSetting
        from ..detected_app import DetectedApp
        from ..device_and_app_management_assignment_filter import DeviceAndAppManagementAssignmentFilter
        from ..device_and_app_management_role_assignment import DeviceAndAppManagementRoleAssignment
        from ..device_category import DeviceCategory
        from ..device_compliance_policy import DeviceCompliancePolicy
        from ..device_compliance_policy_device_state_summary import DeviceCompliancePolicyDeviceStateSummary
        from ..device_compliance_policy_setting_state_summary import DeviceCompliancePolicySettingStateSummary
        from ..device_compliance_script import DeviceComplianceScript
        from ..device_configuration import DeviceConfiguration
        from ..device_configuration_conflict_summary import DeviceConfigurationConflictSummary
        from ..device_configuration_device_state_summary import DeviceConfigurationDeviceStateSummary
        from ..device_configuration_user_state_summary import DeviceConfigurationUserStateSummary
        from ..device_custom_attribute_shell_script import DeviceCustomAttributeShellScript
        from ..device_enrollment_configuration import DeviceEnrollmentConfiguration
        from ..device_health_script import DeviceHealthScript
        from ..device_management_autopilot_event import DeviceManagementAutopilotEvent
        from ..device_management_compliance_policy import DeviceManagementCompliancePolicy
        from ..device_management_configuration_category import DeviceManagementConfigurationCategory
        from ..device_management_configuration_policy import DeviceManagementConfigurationPolicy
        from ..device_management_configuration_policy_template import DeviceManagementConfigurationPolicyTemplate
        from ..device_management_configuration_setting_definition import DeviceManagementConfigurationSettingDefinition
        from ..device_management_configuration_setting_template import DeviceManagementConfigurationSettingTemplate
        from ..device_management_derived_credential_settings import DeviceManagementDerivedCredentialSettings
        from ..device_management_domain_join_connector import DeviceManagementDomainJoinConnector
        from ..device_management_exchange_connector import DeviceManagementExchangeConnector
        from ..device_management_exchange_on_premises_policy import DeviceManagementExchangeOnPremisesPolicy
        from ..device_management_intent import DeviceManagementIntent
        from ..device_management_partner import DeviceManagementPartner
        from ..device_management_reports import DeviceManagementReports
        from ..device_management_resource_access_profile_base import DeviceManagementResourceAccessProfileBase
        from ..device_management_reusable_policy_setting import DeviceManagementReusablePolicySetting
        from ..device_management_script import DeviceManagementScript
        from ..device_management_settings import DeviceManagementSettings
        from ..device_management_setting_category import DeviceManagementSettingCategory
        from ..device_management_setting_definition import DeviceManagementSettingDefinition
        from ..device_management_subscriptions import DeviceManagementSubscriptions
        from ..device_management_subscription_state import DeviceManagementSubscriptionState
        from ..device_management_template import DeviceManagementTemplate
        from ..device_management_template_insights_definition import DeviceManagementTemplateInsightsDefinition
        from ..device_management_troubleshooting_event import DeviceManagementTroubleshootingEvent
        from ..device_protection_overview import DeviceProtectionOverview
        from ..device_shell_script import DeviceShellScript
        from ..embedded_s_i_m_activation_code_pool import EmbeddedSIMActivationCodePool
        from ..endpoint_privilege_management_provisioning_status import EndpointPrivilegeManagementProvisioningStatus
        from ..entity import Entity
        from ..group_policy_category import GroupPolicyCategory
        from ..group_policy_configuration import GroupPolicyConfiguration
        from ..group_policy_definition import GroupPolicyDefinition
        from ..group_policy_definition_file import GroupPolicyDefinitionFile
        from ..group_policy_migration_report import GroupPolicyMigrationReport
        from ..group_policy_object_file import GroupPolicyObjectFile
        from ..group_policy_uploaded_definition_file import GroupPolicyUploadedDefinitionFile
        from ..hardware_configuration import HardwareConfiguration
        from ..hardware_password_detail import HardwarePasswordDetail
        from ..hardware_password_info import HardwarePasswordInfo
        from ..imported_device_identity import ImportedDeviceIdentity
        from ..imported_windows_autopilot_device_identity import ImportedWindowsAutopilotDeviceIdentity
        from ..intune_brand import IntuneBrand
        from ..intune_branding_profile import IntuneBrandingProfile
        from ..ios_update_device_status import IosUpdateDeviceStatus
        from ..mac_o_s_software_update_account_summary import MacOSSoftwareUpdateAccountSummary
        from ..managed_all_device_certificate_state import ManagedAllDeviceCertificateState
        from ..managed_device import ManagedDevice
        from ..managed_device_cleanup_rule import ManagedDeviceCleanupRule
        from ..managed_device_cleanup_settings import ManagedDeviceCleanupSettings
        from ..managed_device_encryption_state import ManagedDeviceEncryptionState
        from ..managed_device_overview import ManagedDeviceOverview
        from ..managed_device_windows_operating_system_image import ManagedDeviceWindowsOperatingSystemImage
        from ..microsoft_tunnel_configuration import MicrosoftTunnelConfiguration
        from ..microsoft_tunnel_health_threshold import MicrosoftTunnelHealthThreshold
        from ..microsoft_tunnel_server_log_collection_response import MicrosoftTunnelServerLogCollectionResponse
        from ..microsoft_tunnel_site import MicrosoftTunnelSite
        from ..mobile_app_troubleshooting_event import MobileAppTroubleshootingEvent
        from ..mobile_threat_defense_connector import MobileThreatDefenseConnector
        from ..ndes_connector import NdesConnector
        from ..notification_message_template import NotificationMessageTemplate
        from ..on_premises_conditional_access_settings import OnPremisesConditionalAccessSettings
        from ..operation_approval_policy import OperationApprovalPolicy
        from ..operation_approval_request import OperationApprovalRequest
        from ..privilege_management_elevation import PrivilegeManagementElevation
        from ..privilege_management_elevation_request import PrivilegeManagementElevationRequest
        from ..remote_action_audit import RemoteActionAudit
        from ..remote_assistance_partner import RemoteAssistancePartner
        from ..remote_assistance_settings import RemoteAssistanceSettings
        from ..resource_operation import ResourceOperation
        from ..restricted_apps_violation import RestrictedAppsViolation
        from ..role_definition import RoleDefinition
        from ..role_scope_tag import RoleScopeTag
        from ..samsung_e_fota_firmware_version import SamsungEFotaFirmwareVersion
        from ..service_now_connection import ServiceNowConnection
        from ..software_update_status_summary import SoftwareUpdateStatusSummary
        from ..tenant_attach_r_b_a_c import TenantAttachRBAC
        from ..terms_and_conditions import TermsAndConditions
        from ..user_experience_analytics_anomaly import UserExperienceAnalyticsAnomaly
        from ..user_experience_analytics_anomaly_correlation_group_overview import UserExperienceAnalyticsAnomalyCorrelationGroupOverview
        from ..user_experience_analytics_anomaly_device import UserExperienceAnalyticsAnomalyDevice
        from ..user_experience_analytics_anomaly_severity_overview import UserExperienceAnalyticsAnomalySeverityOverview
        from ..user_experience_analytics_app_health_application_performance import UserExperienceAnalyticsAppHealthApplicationPerformance
        from ..user_experience_analytics_app_health_app_performance_by_app_version import UserExperienceAnalyticsAppHealthAppPerformanceByAppVersion
        from ..user_experience_analytics_app_health_app_performance_by_app_version_details import UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetails
        from ..user_experience_analytics_app_health_app_performance_by_app_version_device_id import UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId
        from ..user_experience_analytics_app_health_app_performance_by_o_s_version import UserExperienceAnalyticsAppHealthAppPerformanceByOSVersion
        from ..user_experience_analytics_app_health_device_model_performance import UserExperienceAnalyticsAppHealthDeviceModelPerformance
        from ..user_experience_analytics_app_health_device_performance import UserExperienceAnalyticsAppHealthDevicePerformance
        from ..user_experience_analytics_app_health_device_performance_details import UserExperienceAnalyticsAppHealthDevicePerformanceDetails
        from ..user_experience_analytics_app_health_o_s_version_performance import UserExperienceAnalyticsAppHealthOSVersionPerformance
        from ..user_experience_analytics_baseline import UserExperienceAnalyticsBaseline
        from ..user_experience_analytics_battery_health_app_impact import UserExperienceAnalyticsBatteryHealthAppImpact
        from ..user_experience_analytics_battery_health_capacity_details import UserExperienceAnalyticsBatteryHealthCapacityDetails
        from ..user_experience_analytics_battery_health_device_app_impact import UserExperienceAnalyticsBatteryHealthDeviceAppImpact
        from ..user_experience_analytics_battery_health_device_performance import UserExperienceAnalyticsBatteryHealthDevicePerformance
        from ..user_experience_analytics_battery_health_device_runtime_history import UserExperienceAnalyticsBatteryHealthDeviceRuntimeHistory
        from ..user_experience_analytics_battery_health_model_performance import UserExperienceAnalyticsBatteryHealthModelPerformance
        from ..user_experience_analytics_battery_health_os_performance import UserExperienceAnalyticsBatteryHealthOsPerformance
        from ..user_experience_analytics_battery_health_runtime_details import UserExperienceAnalyticsBatteryHealthRuntimeDetails
        from ..user_experience_analytics_category import UserExperienceAnalyticsCategory
        from ..user_experience_analytics_device_performance import UserExperienceAnalyticsDevicePerformance
        from ..user_experience_analytics_device_scope import UserExperienceAnalyticsDeviceScope
        from ..user_experience_analytics_device_scores import UserExperienceAnalyticsDeviceScores
        from ..user_experience_analytics_device_startup_history import UserExperienceAnalyticsDeviceStartupHistory
        from ..user_experience_analytics_device_startup_process import UserExperienceAnalyticsDeviceStartupProcess
        from ..user_experience_analytics_device_startup_process_performance import UserExperienceAnalyticsDeviceStartupProcessPerformance
        from ..user_experience_analytics_device_timeline_event import UserExperienceAnalyticsDeviceTimelineEvent
        from ..user_experience_analytics_device_without_cloud_identity import UserExperienceAnalyticsDeviceWithoutCloudIdentity
        from ..user_experience_analytics_impacting_process import UserExperienceAnalyticsImpactingProcess
        from ..user_experience_analytics_metric_history import UserExperienceAnalyticsMetricHistory
        from ..user_experience_analytics_model_scores import UserExperienceAnalyticsModelScores
        from ..user_experience_analytics_not_autopilot_ready_device import UserExperienceAnalyticsNotAutopilotReadyDevice
        from ..user_experience_analytics_overview import UserExperienceAnalyticsOverview
        from ..user_experience_analytics_remote_connection import UserExperienceAnalyticsRemoteConnection
        from ..user_experience_analytics_resource_performance import UserExperienceAnalyticsResourcePerformance
        from ..user_experience_analytics_score_history import UserExperienceAnalyticsScoreHistory
        from ..user_experience_analytics_settings import UserExperienceAnalyticsSettings
        from ..user_experience_analytics_work_from_anywhere_hardware_readiness_metric import UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric
        from ..user_experience_analytics_work_from_anywhere_metric import UserExperienceAnalyticsWorkFromAnywhereMetric
        from ..user_experience_analytics_work_from_anywhere_model_performance import UserExperienceAnalyticsWorkFromAnywhereModelPerformance
        from ..user_p_f_x_certificate import UserPFXCertificate
        from ..virtual_endpoint import VirtualEndpoint
        from ..windows_autopilot_deployment_profile import WindowsAutopilotDeploymentProfile
        from ..windows_autopilot_device_identity import WindowsAutopilotDeviceIdentity
        from ..windows_autopilot_settings import WindowsAutopilotSettings
        from ..windows_driver_update_profile import WindowsDriverUpdateProfile
        from ..windows_feature_update_profile import WindowsFeatureUpdateProfile
        from ..windows_information_protection_app_learning_summary import WindowsInformationProtectionAppLearningSummary
        from ..windows_information_protection_network_learning_summary import WindowsInformationProtectionNetworkLearningSummary
        from ..windows_malware_information import WindowsMalwareInformation
        from ..windows_malware_overview import WindowsMalwareOverview
        from ..windows_quality_update_policy import WindowsQualityUpdatePolicy
        from ..windows_quality_update_profile import WindowsQualityUpdateProfile
        from ..windows_update_catalog_item import WindowsUpdateCatalogItem
        from ..zebra_fota_artifact import ZebraFotaArtifact
        from ..zebra_fota_connector import ZebraFotaConnector
        from ..zebra_fota_deployment import ZebraFotaDeployment
        from .monitoring import Monitoring

        fields: dict[str, Callable[[Any], None]] = {
            "accountMoveCompletionDateTime": lambda n : setattr(self, 'account_move_completion_date_time', n.get_datetime_value()),
            "adminConsent": lambda n : setattr(self, 'admin_consent', n.get_object_value(AdminConsent)),
            "advancedThreatProtectionOnboardingStateSummary": lambda n : setattr(self, 'advanced_threat_protection_onboarding_state_summary', n.get_object_value(AdvancedThreatProtectionOnboardingStateSummary)),
            "androidAppConfigurationSchema": lambda n : setattr(self, 'android_app_configuration_schema', n.get_object_value(AndroidAppConfigurationSchema)),
            "androidDeviceOwnerEnrollmentProfiles": lambda n : setattr(self, 'android_device_owner_enrollment_profiles', n.get_collection_of_object_values(AndroidDeviceOwnerEnrollmentProfile)),
            "androidForWorkAppConfigurationSchemas": lambda n : setattr(self, 'android_for_work_app_configuration_schemas', n.get_collection_of_object_values(AndroidForWorkAppConfigurationSchema)),
            "androidForWorkEnrollmentProfiles": lambda n : setattr(self, 'android_for_work_enrollment_profiles', n.get_collection_of_object_values(AndroidForWorkEnrollmentProfile)),
            "androidForWorkSettings": lambda n : setattr(self, 'android_for_work_settings', n.get_object_value(AndroidForWorkSettings)),
            "androidManagedStoreAccountEnterpriseSettings": lambda n : setattr(self, 'android_managed_store_account_enterprise_settings', n.get_object_value(AndroidManagedStoreAccountEnterpriseSettings)),
            "androidManagedStoreAppConfigurationSchemas": lambda n : setattr(self, 'android_managed_store_app_configuration_schemas', n.get_collection_of_object_values(AndroidManagedStoreAppConfigurationSchema)),
            "applePushNotificationCertificate": lambda n : setattr(self, 'apple_push_notification_certificate', n.get_object_value(ApplePushNotificationCertificate)),
            "appleUserInitiatedEnrollmentProfiles": lambda n : setattr(self, 'apple_user_initiated_enrollment_profiles', n.get_collection_of_object_values(AppleUserInitiatedEnrollmentProfile)),
            "assignmentFilters": lambda n : setattr(self, 'assignment_filters', n.get_collection_of_object_values(DeviceAndAppManagementAssignmentFilter)),
            "auditEvents": lambda n : setattr(self, 'audit_events', n.get_collection_of_object_values(AuditEvent)),
            "autopilotEvents": lambda n : setattr(self, 'autopilot_events', n.get_collection_of_object_values(DeviceManagementAutopilotEvent)),
            "cartToClassAssociations": lambda n : setattr(self, 'cart_to_class_associations', n.get_collection_of_object_values(CartToClassAssociation)),
            "categories": lambda n : setattr(self, 'categories', n.get_collection_of_object_values(DeviceManagementSettingCategory)),
            "certificateConnectorDetails": lambda n : setattr(self, 'certificate_connector_details', n.get_collection_of_object_values(CertificateConnectorDetails)),
            "chromeOSOnboardingSettings": lambda n : setattr(self, 'chrome_o_s_onboarding_settings', n.get_collection_of_object_values(ChromeOSOnboardingSettings)),
            "cloudCertificationAuthority": lambda n : setattr(self, 'cloud_certification_authority', n.get_collection_of_object_values(CloudCertificationAuthority)),
            "cloudCertificationAuthorityLeafCertificate": lambda n : setattr(self, 'cloud_certification_authority_leaf_certificate', n.get_collection_of_object_values(CloudCertificationAuthorityLeafCertificate)),
            "cloudPCConnectivityIssues": lambda n : setattr(self, 'cloud_p_c_connectivity_issues', n.get_collection_of_object_values(CloudPCConnectivityIssue)),
            "comanagedDevices": lambda n : setattr(self, 'comanaged_devices', n.get_collection_of_object_values(ManagedDevice)),
            "comanagementEligibleDevices": lambda n : setattr(self, 'comanagement_eligible_devices', n.get_collection_of_object_values(ComanagementEligibleDevice)),
            "complianceCategories": lambda n : setattr(self, 'compliance_categories', n.get_collection_of_object_values(DeviceManagementConfigurationCategory)),
            "complianceManagementPartners": lambda n : setattr(self, 'compliance_management_partners', n.get_collection_of_object_values(ComplianceManagementPartner)),
            "compliancePolicies": lambda n : setattr(self, 'compliance_policies', n.get_collection_of_object_values(DeviceManagementCompliancePolicy)),
            "complianceSettings": lambda n : setattr(self, 'compliance_settings', n.get_collection_of_object_values(DeviceManagementConfigurationSettingDefinition)),
            "conditionalAccessSettings": lambda n : setattr(self, 'conditional_access_settings', n.get_object_value(OnPremisesConditionalAccessSettings)),
            "configManagerCollections": lambda n : setattr(self, 'config_manager_collections', n.get_collection_of_object_values(ConfigManagerCollection)),
            "configurationCategories": lambda n : setattr(self, 'configuration_categories', n.get_collection_of_object_values(DeviceManagementConfigurationCategory)),
            "configurationPolicies": lambda n : setattr(self, 'configuration_policies', n.get_collection_of_object_values(DeviceManagementConfigurationPolicy)),
            "configurationPolicyTemplates": lambda n : setattr(self, 'configuration_policy_templates', n.get_collection_of_object_values(DeviceManagementConfigurationPolicyTemplate)),
            "configurationSettings": lambda n : setattr(self, 'configuration_settings', n.get_collection_of_object_values(DeviceManagementConfigurationSettingDefinition)),
            "connectorStatus": lambda n : setattr(self, 'connector_status', n.get_collection_of_object_values(ConnectorStatusDetails)),
            "dataProcessorServiceForWindowsFeaturesOnboarding": lambda n : setattr(self, 'data_processor_service_for_windows_features_onboarding', n.get_object_value(DataProcessorServiceForWindowsFeaturesOnboarding)),
            "dataSharingConsents": lambda n : setattr(self, 'data_sharing_consents', n.get_collection_of_object_values(DataSharingConsent)),
            "depOnboardingSettings": lambda n : setattr(self, 'dep_onboarding_settings', n.get_collection_of_object_values(DepOnboardingSetting)),
            "derivedCredentials": lambda n : setattr(self, 'derived_credentials', n.get_collection_of_object_values(DeviceManagementDerivedCredentialSettings)),
            "detectedApps": lambda n : setattr(self, 'detected_apps', n.get_collection_of_object_values(DetectedApp)),
            "deviceCategories": lambda n : setattr(self, 'device_categories', n.get_collection_of_object_values(DeviceCategory)),
            "deviceCompliancePolicies": lambda n : setattr(self, 'device_compliance_policies', n.get_collection_of_object_values(DeviceCompliancePolicy)),
            "deviceCompliancePolicyDeviceStateSummary": lambda n : setattr(self, 'device_compliance_policy_device_state_summary', n.get_object_value(DeviceCompliancePolicyDeviceStateSummary)),
            "deviceCompliancePolicySettingStateSummaries": lambda n : setattr(self, 'device_compliance_policy_setting_state_summaries', n.get_collection_of_object_values(DeviceCompliancePolicySettingStateSummary)),
            "deviceComplianceReportSummarizationDateTime": lambda n : setattr(self, 'device_compliance_report_summarization_date_time', n.get_datetime_value()),
            "deviceComplianceScripts": lambda n : setattr(self, 'device_compliance_scripts', n.get_collection_of_object_values(DeviceComplianceScript)),
            "deviceConfigurationConflictSummary": lambda n : setattr(self, 'device_configuration_conflict_summary', n.get_collection_of_object_values(DeviceConfigurationConflictSummary)),
            "deviceConfigurationDeviceStateSummaries": lambda n : setattr(self, 'device_configuration_device_state_summaries', n.get_object_value(DeviceConfigurationDeviceStateSummary)),
            "deviceConfigurationRestrictedAppsViolations": lambda n : setattr(self, 'device_configuration_restricted_apps_violations', n.get_collection_of_object_values(RestrictedAppsViolation)),
            "deviceConfigurationUserStateSummaries": lambda n : setattr(self, 'device_configuration_user_state_summaries', n.get_object_value(DeviceConfigurationUserStateSummary)),
            "deviceConfigurations": lambda n : setattr(self, 'device_configurations', n.get_collection_of_object_values(DeviceConfiguration)),
            "deviceConfigurationsAllManagedDeviceCertificateStates": lambda n : setattr(self, 'device_configurations_all_managed_device_certificate_states', n.get_collection_of_object_values(ManagedAllDeviceCertificateState)),
            "deviceCustomAttributeShellScripts": lambda n : setattr(self, 'device_custom_attribute_shell_scripts', n.get_collection_of_object_values(DeviceCustomAttributeShellScript)),
            "deviceEnrollmentConfigurations": lambda n : setattr(self, 'device_enrollment_configurations', n.get_collection_of_object_values(DeviceEnrollmentConfiguration)),
            "deviceHealthScripts": lambda n : setattr(self, 'device_health_scripts', n.get_collection_of_object_values(DeviceHealthScript)),
            "deviceManagementPartners": lambda n : setattr(self, 'device_management_partners', n.get_collection_of_object_values(DeviceManagementPartner)),
            "deviceManagementScripts": lambda n : setattr(self, 'device_management_scripts', n.get_collection_of_object_values(DeviceManagementScript)),
            "deviceProtectionOverview": lambda n : setattr(self, 'device_protection_overview', n.get_object_value(DeviceProtectionOverview)),
            "deviceShellScripts": lambda n : setattr(self, 'device_shell_scripts', n.get_collection_of_object_values(DeviceShellScript)),
            "domainJoinConnectors": lambda n : setattr(self, 'domain_join_connectors', n.get_collection_of_object_values(DeviceManagementDomainJoinConnector)),
            "elevationRequests": lambda n : setattr(self, 'elevation_requests', n.get_collection_of_object_values(PrivilegeManagementElevationRequest)),
            "embeddedSIMActivationCodePools": lambda n : setattr(self, 'embedded_s_i_m_activation_code_pools', n.get_collection_of_object_values(EmbeddedSIMActivationCodePool)),
            "endpointPrivilegeManagementProvisioningStatus": lambda n : setattr(self, 'endpoint_privilege_management_provisioning_status', n.get_object_value(EndpointPrivilegeManagementProvisioningStatus)),
            "exchangeConnectors": lambda n : setattr(self, 'exchange_connectors', n.get_collection_of_object_values(DeviceManagementExchangeConnector)),
            "exchangeOnPremisesPolicies": lambda n : setattr(self, 'exchange_on_premises_policies', n.get_collection_of_object_values(DeviceManagementExchangeOnPremisesPolicy)),
            "exchangeOnPremisesPolicy": lambda n : setattr(self, 'exchange_on_premises_policy', n.get_object_value(DeviceManagementExchangeOnPremisesPolicy)),
            "groupPolicyCategories": lambda n : setattr(self, 'group_policy_categories', n.get_collection_of_object_values(GroupPolicyCategory)),
            "groupPolicyConfigurations": lambda n : setattr(self, 'group_policy_configurations', n.get_collection_of_object_values(GroupPolicyConfiguration)),
            "groupPolicyDefinitionFiles": lambda n : setattr(self, 'group_policy_definition_files', n.get_collection_of_object_values(GroupPolicyDefinitionFile)),
            "groupPolicyDefinitions": lambda n : setattr(self, 'group_policy_definitions', n.get_collection_of_object_values(GroupPolicyDefinition)),
            "groupPolicyMigrationReports": lambda n : setattr(self, 'group_policy_migration_reports', n.get_collection_of_object_values(GroupPolicyMigrationReport)),
            "groupPolicyObjectFiles": lambda n : setattr(self, 'group_policy_object_files', n.get_collection_of_object_values(GroupPolicyObjectFile)),
            "groupPolicyUploadedDefinitionFiles": lambda n : setattr(self, 'group_policy_uploaded_definition_files', n.get_collection_of_object_values(GroupPolicyUploadedDefinitionFile)),
            "hardwareConfigurations": lambda n : setattr(self, 'hardware_configurations', n.get_collection_of_object_values(HardwareConfiguration)),
            "hardwarePasswordDetails": lambda n : setattr(self, 'hardware_password_details', n.get_collection_of_object_values(HardwarePasswordDetail)),
            "hardwarePasswordInfo": lambda n : setattr(self, 'hardware_password_info', n.get_collection_of_object_values(HardwarePasswordInfo)),
            "importedDeviceIdentities": lambda n : setattr(self, 'imported_device_identities', n.get_collection_of_object_values(ImportedDeviceIdentity)),
            "importedWindowsAutopilotDeviceIdentities": lambda n : setattr(self, 'imported_windows_autopilot_device_identities', n.get_collection_of_object_values(ImportedWindowsAutopilotDeviceIdentity)),
            "intents": lambda n : setattr(self, 'intents', n.get_collection_of_object_values(DeviceManagementIntent)),
            "intuneAccountId": lambda n : setattr(self, 'intune_account_id', n.get_uuid_value()),
            "intuneBrand": lambda n : setattr(self, 'intune_brand', n.get_object_value(IntuneBrand)),
            "intuneBrandingProfiles": lambda n : setattr(self, 'intune_branding_profiles', n.get_collection_of_object_values(IntuneBrandingProfile)),
            "iosUpdateStatuses": lambda n : setattr(self, 'ios_update_statuses', n.get_collection_of_object_values(IosUpdateDeviceStatus)),
            "lastReportAggregationDateTime": lambda n : setattr(self, 'last_report_aggregation_date_time', n.get_datetime_value()),
            "legacyPcManangementEnabled": lambda n : setattr(self, 'legacy_pc_manangement_enabled', n.get_bool_value()),
            "macOSSoftwareUpdateAccountSummaries": lambda n : setattr(self, 'mac_o_s_software_update_account_summaries', n.get_collection_of_object_values(MacOSSoftwareUpdateAccountSummary)),
            "managedDeviceCleanupRules": lambda n : setattr(self, 'managed_device_cleanup_rules', n.get_collection_of_object_values(ManagedDeviceCleanupRule)),
            "managedDeviceCleanupSettings": lambda n : setattr(self, 'managed_device_cleanup_settings', n.get_object_value(ManagedDeviceCleanupSettings)),
            "managedDeviceEncryptionStates": lambda n : setattr(self, 'managed_device_encryption_states', n.get_collection_of_object_values(ManagedDeviceEncryptionState)),
            "managedDeviceOverview": lambda n : setattr(self, 'managed_device_overview', n.get_object_value(ManagedDeviceOverview)),
            "managedDeviceWindowsOSImages": lambda n : setattr(self, 'managed_device_windows_o_s_images', n.get_collection_of_object_values(ManagedDeviceWindowsOperatingSystemImage)),
            "managedDevices": lambda n : setattr(self, 'managed_devices', n.get_collection_of_object_values(ManagedDevice)),
            "maximumDepTokens": lambda n : setattr(self, 'maximum_dep_tokens', n.get_int_value()),
            "microsoftTunnelConfigurations": lambda n : setattr(self, 'microsoft_tunnel_configurations', n.get_collection_of_object_values(MicrosoftTunnelConfiguration)),
            "microsoftTunnelHealthThresholds": lambda n : setattr(self, 'microsoft_tunnel_health_thresholds', n.get_collection_of_object_values(MicrosoftTunnelHealthThreshold)),
            "microsoftTunnelServerLogCollectionResponses": lambda n : setattr(self, 'microsoft_tunnel_server_log_collection_responses', n.get_collection_of_object_values(MicrosoftTunnelServerLogCollectionResponse)),
            "microsoftTunnelSites": lambda n : setattr(self, 'microsoft_tunnel_sites', n.get_collection_of_object_values(MicrosoftTunnelSite)),
            "mobileAppTroubleshootingEvents": lambda n : setattr(self, 'mobile_app_troubleshooting_events', n.get_collection_of_object_values(MobileAppTroubleshootingEvent)),
            "mobileThreatDefenseConnectors": lambda n : setattr(self, 'mobile_threat_defense_connectors', n.get_collection_of_object_values(MobileThreatDefenseConnector)),
            "monitoring": lambda n : setattr(self, 'monitoring', n.get_object_value(Monitoring)),
            "ndesConnectors": lambda n : setattr(self, 'ndes_connectors', n.get_collection_of_object_values(NdesConnector)),
            "notificationMessageTemplates": lambda n : setattr(self, 'notification_message_templates', n.get_collection_of_object_values(NotificationMessageTemplate)),
            "operationApprovalPolicies": lambda n : setattr(self, 'operation_approval_policies', n.get_collection_of_object_values(OperationApprovalPolicy)),
            "operationApprovalRequests": lambda n : setattr(self, 'operation_approval_requests', n.get_collection_of_object_values(OperationApprovalRequest)),
            "privilegeManagementElevations": lambda n : setattr(self, 'privilege_management_elevations', n.get_collection_of_object_values(PrivilegeManagementElevation)),
            "remoteActionAudits": lambda n : setattr(self, 'remote_action_audits', n.get_collection_of_object_values(RemoteActionAudit)),
            "remoteAssistancePartners": lambda n : setattr(self, 'remote_assistance_partners', n.get_collection_of_object_values(RemoteAssistancePartner)),
            "remoteAssistanceSettings": lambda n : setattr(self, 'remote_assistance_settings', n.get_object_value(RemoteAssistanceSettings)),
            "reports": lambda n : setattr(self, 'reports', n.get_object_value(DeviceManagementReports)),
            "resourceAccessProfiles": lambda n : setattr(self, 'resource_access_profiles', n.get_collection_of_object_values(DeviceManagementResourceAccessProfileBase)),
            "resourceOperations": lambda n : setattr(self, 'resource_operations', n.get_collection_of_object_values(ResourceOperation)),
            "reusablePolicySettings": lambda n : setattr(self, 'reusable_policy_settings', n.get_collection_of_object_values(DeviceManagementReusablePolicySetting)),
            "reusableSettings": lambda n : setattr(self, 'reusable_settings', n.get_collection_of_object_values(DeviceManagementConfigurationSettingDefinition)),
            "roleAssignments": lambda n : setattr(self, 'role_assignments', n.get_collection_of_object_values(DeviceAndAppManagementRoleAssignment)),
            "roleDefinitions": lambda n : setattr(self, 'role_definitions', n.get_collection_of_object_values(RoleDefinition)),
            "roleScopeTags": lambda n : setattr(self, 'role_scope_tags', n.get_collection_of_object_values(RoleScopeTag)),
            "samsungEFotaFirmwareVersions": lambda n : setattr(self, 'samsung_e_fota_firmware_versions', n.get_collection_of_object_values(SamsungEFotaFirmwareVersion)),
            "serviceNowConnections": lambda n : setattr(self, 'service_now_connections', n.get_collection_of_object_values(ServiceNowConnection)),
            "settingDefinitions": lambda n : setattr(self, 'setting_definitions', n.get_collection_of_object_values(DeviceManagementSettingDefinition)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(DeviceManagementSettings)),
            "softwareUpdateStatusSummary": lambda n : setattr(self, 'software_update_status_summary', n.get_object_value(SoftwareUpdateStatusSummary)),
            "subscriptionState": lambda n : setattr(self, 'subscription_state', n.get_enum_value(DeviceManagementSubscriptionState)),
            "subscriptions": lambda n : setattr(self, 'subscriptions', n.get_collection_of_enum_values(DeviceManagementSubscriptions)),
            "templateInsights": lambda n : setattr(self, 'template_insights', n.get_collection_of_object_values(DeviceManagementTemplateInsightsDefinition)),
            "templateSettings": lambda n : setattr(self, 'template_settings', n.get_collection_of_object_values(DeviceManagementConfigurationSettingTemplate)),
            "templates": lambda n : setattr(self, 'templates', n.get_collection_of_object_values(DeviceManagementTemplate)),
            "tenantAttachRBAC": lambda n : setattr(self, 'tenant_attach_r_b_a_c', n.get_object_value(TenantAttachRBAC)),
            "termsAndConditions": lambda n : setattr(self, 'terms_and_conditions', n.get_collection_of_object_values(TermsAndConditions)),
            "troubleshootingEvents": lambda n : setattr(self, 'troubleshooting_events', n.get_collection_of_object_values(DeviceManagementTroubleshootingEvent)),
            "unlicensedAdminstratorsEnabled": lambda n : setattr(self, 'unlicensed_adminstrators_enabled', n.get_bool_value()),
            "userExperienceAnalyticsAnomaly": lambda n : setattr(self, 'user_experience_analytics_anomaly', n.get_collection_of_object_values(UserExperienceAnalyticsAnomaly)),
            "userExperienceAnalyticsAnomalyCorrelationGroupOverview": lambda n : setattr(self, 'user_experience_analytics_anomaly_correlation_group_overview', n.get_collection_of_object_values(UserExperienceAnalyticsAnomalyCorrelationGroupOverview)),
            "userExperienceAnalyticsAnomalyDevice": lambda n : setattr(self, 'user_experience_analytics_anomaly_device', n.get_collection_of_object_values(UserExperienceAnalyticsAnomalyDevice)),
            "userExperienceAnalyticsAnomalySeverityOverview": lambda n : setattr(self, 'user_experience_analytics_anomaly_severity_overview', n.get_object_value(UserExperienceAnalyticsAnomalySeverityOverview)),
            "userExperienceAnalyticsAppHealthApplicationPerformance": lambda n : setattr(self, 'user_experience_analytics_app_health_application_performance', n.get_collection_of_object_values(UserExperienceAnalyticsAppHealthApplicationPerformance)),
            "userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersion": lambda n : setattr(self, 'user_experience_analytics_app_health_application_performance_by_app_version', n.get_collection_of_object_values(UserExperienceAnalyticsAppHealthAppPerformanceByAppVersion)),
            "userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDetails": lambda n : setattr(self, 'user_experience_analytics_app_health_application_performance_by_app_version_details', n.get_collection_of_object_values(UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetails)),
            "userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDeviceId": lambda n : setattr(self, 'user_experience_analytics_app_health_application_performance_by_app_version_device_id', n.get_collection_of_object_values(UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId)),
            "userExperienceAnalyticsAppHealthApplicationPerformanceByOSVersion": lambda n : setattr(self, 'user_experience_analytics_app_health_application_performance_by_o_s_version', n.get_collection_of_object_values(UserExperienceAnalyticsAppHealthAppPerformanceByOSVersion)),
            "userExperienceAnalyticsAppHealthDeviceModelPerformance": lambda n : setattr(self, 'user_experience_analytics_app_health_device_model_performance', n.get_collection_of_object_values(UserExperienceAnalyticsAppHealthDeviceModelPerformance)),
            "userExperienceAnalyticsAppHealthDevicePerformance": lambda n : setattr(self, 'user_experience_analytics_app_health_device_performance', n.get_collection_of_object_values(UserExperienceAnalyticsAppHealthDevicePerformance)),
            "userExperienceAnalyticsAppHealthDevicePerformanceDetails": lambda n : setattr(self, 'user_experience_analytics_app_health_device_performance_details', n.get_collection_of_object_values(UserExperienceAnalyticsAppHealthDevicePerformanceDetails)),
            "userExperienceAnalyticsAppHealthOSVersionPerformance": lambda n : setattr(self, 'user_experience_analytics_app_health_o_s_version_performance', n.get_collection_of_object_values(UserExperienceAnalyticsAppHealthOSVersionPerformance)),
            "userExperienceAnalyticsAppHealthOverview": lambda n : setattr(self, 'user_experience_analytics_app_health_overview', n.get_object_value(UserExperienceAnalyticsCategory)),
            "userExperienceAnalyticsBaselines": lambda n : setattr(self, 'user_experience_analytics_baselines', n.get_collection_of_object_values(UserExperienceAnalyticsBaseline)),
            "userExperienceAnalyticsBatteryHealthAppImpact": lambda n : setattr(self, 'user_experience_analytics_battery_health_app_impact', n.get_collection_of_object_values(UserExperienceAnalyticsBatteryHealthAppImpact)),
            "userExperienceAnalyticsBatteryHealthCapacityDetails": lambda n : setattr(self, 'user_experience_analytics_battery_health_capacity_details', n.get_object_value(UserExperienceAnalyticsBatteryHealthCapacityDetails)),
            "userExperienceAnalyticsBatteryHealthDeviceAppImpact": lambda n : setattr(self, 'user_experience_analytics_battery_health_device_app_impact', n.get_collection_of_object_values(UserExperienceAnalyticsBatteryHealthDeviceAppImpact)),
            "userExperienceAnalyticsBatteryHealthDevicePerformance": lambda n : setattr(self, 'user_experience_analytics_battery_health_device_performance', n.get_collection_of_object_values(UserExperienceAnalyticsBatteryHealthDevicePerformance)),
            "userExperienceAnalyticsBatteryHealthDeviceRuntimeHistory": lambda n : setattr(self, 'user_experience_analytics_battery_health_device_runtime_history', n.get_collection_of_object_values(UserExperienceAnalyticsBatteryHealthDeviceRuntimeHistory)),
            "userExperienceAnalyticsBatteryHealthModelPerformance": lambda n : setattr(self, 'user_experience_analytics_battery_health_model_performance', n.get_collection_of_object_values(UserExperienceAnalyticsBatteryHealthModelPerformance)),
            "userExperienceAnalyticsBatteryHealthOsPerformance": lambda n : setattr(self, 'user_experience_analytics_battery_health_os_performance', n.get_collection_of_object_values(UserExperienceAnalyticsBatteryHealthOsPerformance)),
            "userExperienceAnalyticsBatteryHealthRuntimeDetails": lambda n : setattr(self, 'user_experience_analytics_battery_health_runtime_details', n.get_object_value(UserExperienceAnalyticsBatteryHealthRuntimeDetails)),
            "userExperienceAnalyticsCategories": lambda n : setattr(self, 'user_experience_analytics_categories', n.get_collection_of_object_values(UserExperienceAnalyticsCategory)),
            "userExperienceAnalyticsDeviceMetricHistory": lambda n : setattr(self, 'user_experience_analytics_device_metric_history', n.get_collection_of_object_values(UserExperienceAnalyticsMetricHistory)),
            "userExperienceAnalyticsDevicePerformance": lambda n : setattr(self, 'user_experience_analytics_device_performance', n.get_collection_of_object_values(UserExperienceAnalyticsDevicePerformance)),
            "userExperienceAnalyticsDeviceScope": lambda n : setattr(self, 'user_experience_analytics_device_scope', n.get_object_value(UserExperienceAnalyticsDeviceScope)),
            "userExperienceAnalyticsDeviceScopes": lambda n : setattr(self, 'user_experience_analytics_device_scopes', n.get_collection_of_object_values(UserExperienceAnalyticsDeviceScope)),
            "userExperienceAnalyticsDeviceScores": lambda n : setattr(self, 'user_experience_analytics_device_scores', n.get_collection_of_object_values(UserExperienceAnalyticsDeviceScores)),
            "userExperienceAnalyticsDeviceStartupHistory": lambda n : setattr(self, 'user_experience_analytics_device_startup_history', n.get_collection_of_object_values(UserExperienceAnalyticsDeviceStartupHistory)),
            "userExperienceAnalyticsDeviceStartupProcessPerformance": lambda n : setattr(self, 'user_experience_analytics_device_startup_process_performance', n.get_collection_of_object_values(UserExperienceAnalyticsDeviceStartupProcessPerformance)),
            "userExperienceAnalyticsDeviceStartupProcesses": lambda n : setattr(self, 'user_experience_analytics_device_startup_processes', n.get_collection_of_object_values(UserExperienceAnalyticsDeviceStartupProcess)),
            "userExperienceAnalyticsDeviceTimelineEvent": lambda n : setattr(self, 'user_experience_analytics_device_timeline_event', n.get_collection_of_object_values(UserExperienceAnalyticsDeviceTimelineEvent)),
            "userExperienceAnalyticsDevicesWithoutCloudIdentity": lambda n : setattr(self, 'user_experience_analytics_devices_without_cloud_identity', n.get_collection_of_object_values(UserExperienceAnalyticsDeviceWithoutCloudIdentity)),
            "userExperienceAnalyticsImpactingProcess": lambda n : setattr(self, 'user_experience_analytics_impacting_process', n.get_collection_of_object_values(UserExperienceAnalyticsImpactingProcess)),
            "userExperienceAnalyticsMetricHistory": lambda n : setattr(self, 'user_experience_analytics_metric_history', n.get_collection_of_object_values(UserExperienceAnalyticsMetricHistory)),
            "userExperienceAnalyticsModelScores": lambda n : setattr(self, 'user_experience_analytics_model_scores', n.get_collection_of_object_values(UserExperienceAnalyticsModelScores)),
            "userExperienceAnalyticsNotAutopilotReadyDevice": lambda n : setattr(self, 'user_experience_analytics_not_autopilot_ready_device', n.get_collection_of_object_values(UserExperienceAnalyticsNotAutopilotReadyDevice)),
            "userExperienceAnalyticsOverview": lambda n : setattr(self, 'user_experience_analytics_overview', n.get_object_value(UserExperienceAnalyticsOverview)),
            "userExperienceAnalyticsRemoteConnection": lambda n : setattr(self, 'user_experience_analytics_remote_connection', n.get_collection_of_object_values(UserExperienceAnalyticsRemoteConnection)),
            "userExperienceAnalyticsResourcePerformance": lambda n : setattr(self, 'user_experience_analytics_resource_performance', n.get_collection_of_object_values(UserExperienceAnalyticsResourcePerformance)),
            "userExperienceAnalyticsScoreHistory": lambda n : setattr(self, 'user_experience_analytics_score_history', n.get_collection_of_object_values(UserExperienceAnalyticsScoreHistory)),
            "userExperienceAnalyticsSettings": lambda n : setattr(self, 'user_experience_analytics_settings', n.get_object_value(UserExperienceAnalyticsSettings)),
            "userExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric": lambda n : setattr(self, 'user_experience_analytics_work_from_anywhere_hardware_readiness_metric', n.get_object_value(UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric)),
            "userExperienceAnalyticsWorkFromAnywhereMetrics": lambda n : setattr(self, 'user_experience_analytics_work_from_anywhere_metrics', n.get_collection_of_object_values(UserExperienceAnalyticsWorkFromAnywhereMetric)),
            "userExperienceAnalyticsWorkFromAnywhereModelPerformance": lambda n : setattr(self, 'user_experience_analytics_work_from_anywhere_model_performance', n.get_collection_of_object_values(UserExperienceAnalyticsWorkFromAnywhereModelPerformance)),
            "userPfxCertificates": lambda n : setattr(self, 'user_pfx_certificates', n.get_collection_of_object_values(UserPFXCertificate)),
            "virtualEndpoint": lambda n : setattr(self, 'virtual_endpoint', n.get_object_value(VirtualEndpoint)),
            "windowsAutopilotDeploymentProfiles": lambda n : setattr(self, 'windows_autopilot_deployment_profiles', n.get_collection_of_object_values(WindowsAutopilotDeploymentProfile)),
            "windowsAutopilotDeviceIdentities": lambda n : setattr(self, 'windows_autopilot_device_identities', n.get_collection_of_object_values(WindowsAutopilotDeviceIdentity)),
            "windowsAutopilotSettings": lambda n : setattr(self, 'windows_autopilot_settings', n.get_object_value(WindowsAutopilotSettings)),
            "windowsDriverUpdateProfiles": lambda n : setattr(self, 'windows_driver_update_profiles', n.get_collection_of_object_values(WindowsDriverUpdateProfile)),
            "windowsFeatureUpdateProfiles": lambda n : setattr(self, 'windows_feature_update_profiles', n.get_collection_of_object_values(WindowsFeatureUpdateProfile)),
            "windowsInformationProtectionAppLearningSummaries": lambda n : setattr(self, 'windows_information_protection_app_learning_summaries', n.get_collection_of_object_values(WindowsInformationProtectionAppLearningSummary)),
            "windowsInformationProtectionNetworkLearningSummaries": lambda n : setattr(self, 'windows_information_protection_network_learning_summaries', n.get_collection_of_object_values(WindowsInformationProtectionNetworkLearningSummary)),
            "windowsMalwareInformation": lambda n : setattr(self, 'windows_malware_information', n.get_collection_of_object_values(WindowsMalwareInformation)),
            "windowsMalwareOverview": lambda n : setattr(self, 'windows_malware_overview', n.get_object_value(WindowsMalwareOverview)),
            "windowsQualityUpdatePolicies": lambda n : setattr(self, 'windows_quality_update_policies', n.get_collection_of_object_values(WindowsQualityUpdatePolicy)),
            "windowsQualityUpdateProfiles": lambda n : setattr(self, 'windows_quality_update_profiles', n.get_collection_of_object_values(WindowsQualityUpdateProfile)),
            "windowsUpdateCatalogItems": lambda n : setattr(self, 'windows_update_catalog_items', n.get_collection_of_object_values(WindowsUpdateCatalogItem)),
            "zebraFotaArtifacts": lambda n : setattr(self, 'zebra_fota_artifacts', n.get_collection_of_object_values(ZebraFotaArtifact)),
            "zebraFotaConnector": lambda n : setattr(self, 'zebra_fota_connector', n.get_object_value(ZebraFotaConnector)),
            "zebraFotaDeployments": lambda n : setattr(self, 'zebra_fota_deployments', n.get_collection_of_object_values(ZebraFotaDeployment)),
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
        writer.write_datetime_value("accountMoveCompletionDateTime", self.account_move_completion_date_time)
        writer.write_object_value("adminConsent", self.admin_consent)
        writer.write_object_value("advancedThreatProtectionOnboardingStateSummary", self.advanced_threat_protection_onboarding_state_summary)
        writer.write_object_value("androidAppConfigurationSchema", self.android_app_configuration_schema)
        writer.write_collection_of_object_values("androidDeviceOwnerEnrollmentProfiles", self.android_device_owner_enrollment_profiles)
        writer.write_collection_of_object_values("androidForWorkAppConfigurationSchemas", self.android_for_work_app_configuration_schemas)
        writer.write_collection_of_object_values("androidForWorkEnrollmentProfiles", self.android_for_work_enrollment_profiles)
        writer.write_object_value("androidForWorkSettings", self.android_for_work_settings)
        writer.write_object_value("androidManagedStoreAccountEnterpriseSettings", self.android_managed_store_account_enterprise_settings)
        writer.write_collection_of_object_values("androidManagedStoreAppConfigurationSchemas", self.android_managed_store_app_configuration_schemas)
        writer.write_object_value("applePushNotificationCertificate", self.apple_push_notification_certificate)
        writer.write_collection_of_object_values("appleUserInitiatedEnrollmentProfiles", self.apple_user_initiated_enrollment_profiles)
        writer.write_collection_of_object_values("assignmentFilters", self.assignment_filters)
        writer.write_collection_of_object_values("auditEvents", self.audit_events)
        writer.write_collection_of_object_values("autopilotEvents", self.autopilot_events)
        writer.write_collection_of_object_values("cartToClassAssociations", self.cart_to_class_associations)
        writer.write_collection_of_object_values("categories", self.categories)
        writer.write_collection_of_object_values("certificateConnectorDetails", self.certificate_connector_details)
        writer.write_collection_of_object_values("chromeOSOnboardingSettings", self.chrome_o_s_onboarding_settings)
        writer.write_collection_of_object_values("cloudCertificationAuthority", self.cloud_certification_authority)
        writer.write_collection_of_object_values("cloudCertificationAuthorityLeafCertificate", self.cloud_certification_authority_leaf_certificate)
        writer.write_collection_of_object_values("cloudPCConnectivityIssues", self.cloud_p_c_connectivity_issues)
        writer.write_collection_of_object_values("comanagedDevices", self.comanaged_devices)
        writer.write_collection_of_object_values("comanagementEligibleDevices", self.comanagement_eligible_devices)
        writer.write_collection_of_object_values("complianceCategories", self.compliance_categories)
        writer.write_collection_of_object_values("complianceManagementPartners", self.compliance_management_partners)
        writer.write_collection_of_object_values("compliancePolicies", self.compliance_policies)
        writer.write_collection_of_object_values("complianceSettings", self.compliance_settings)
        writer.write_object_value("conditionalAccessSettings", self.conditional_access_settings)
        writer.write_collection_of_object_values("configManagerCollections", self.config_manager_collections)
        writer.write_collection_of_object_values("configurationCategories", self.configuration_categories)
        writer.write_collection_of_object_values("configurationPolicies", self.configuration_policies)
        writer.write_collection_of_object_values("configurationPolicyTemplates", self.configuration_policy_templates)
        writer.write_collection_of_object_values("configurationSettings", self.configuration_settings)
        writer.write_collection_of_object_values("connectorStatus", self.connector_status)
        writer.write_object_value("dataProcessorServiceForWindowsFeaturesOnboarding", self.data_processor_service_for_windows_features_onboarding)
        writer.write_collection_of_object_values("dataSharingConsents", self.data_sharing_consents)
        writer.write_collection_of_object_values("depOnboardingSettings", self.dep_onboarding_settings)
        writer.write_collection_of_object_values("derivedCredentials", self.derived_credentials)
        writer.write_collection_of_object_values("detectedApps", self.detected_apps)
        writer.write_collection_of_object_values("deviceCategories", self.device_categories)
        writer.write_collection_of_object_values("deviceCompliancePolicies", self.device_compliance_policies)
        writer.write_object_value("deviceCompliancePolicyDeviceStateSummary", self.device_compliance_policy_device_state_summary)
        writer.write_collection_of_object_values("deviceCompliancePolicySettingStateSummaries", self.device_compliance_policy_setting_state_summaries)
        writer.write_collection_of_object_values("deviceComplianceScripts", self.device_compliance_scripts)
        writer.write_collection_of_object_values("deviceConfigurationConflictSummary", self.device_configuration_conflict_summary)
        writer.write_object_value("deviceConfigurationDeviceStateSummaries", self.device_configuration_device_state_summaries)
        writer.write_collection_of_object_values("deviceConfigurationRestrictedAppsViolations", self.device_configuration_restricted_apps_violations)
        writer.write_object_value("deviceConfigurationUserStateSummaries", self.device_configuration_user_state_summaries)
        writer.write_collection_of_object_values("deviceConfigurations", self.device_configurations)
        writer.write_collection_of_object_values("deviceConfigurationsAllManagedDeviceCertificateStates", self.device_configurations_all_managed_device_certificate_states)
        writer.write_collection_of_object_values("deviceCustomAttributeShellScripts", self.device_custom_attribute_shell_scripts)
        writer.write_collection_of_object_values("deviceEnrollmentConfigurations", self.device_enrollment_configurations)
        writer.write_collection_of_object_values("deviceHealthScripts", self.device_health_scripts)
        writer.write_collection_of_object_values("deviceManagementPartners", self.device_management_partners)
        writer.write_collection_of_object_values("deviceManagementScripts", self.device_management_scripts)
        writer.write_object_value("deviceProtectionOverview", self.device_protection_overview)
        writer.write_collection_of_object_values("deviceShellScripts", self.device_shell_scripts)
        writer.write_collection_of_object_values("domainJoinConnectors", self.domain_join_connectors)
        writer.write_collection_of_object_values("elevationRequests", self.elevation_requests)
        writer.write_collection_of_object_values("embeddedSIMActivationCodePools", self.embedded_s_i_m_activation_code_pools)
        writer.write_object_value("endpointPrivilegeManagementProvisioningStatus", self.endpoint_privilege_management_provisioning_status)
        writer.write_collection_of_object_values("exchangeConnectors", self.exchange_connectors)
        writer.write_collection_of_object_values("exchangeOnPremisesPolicies", self.exchange_on_premises_policies)
        writer.write_object_value("exchangeOnPremisesPolicy", self.exchange_on_premises_policy)
        writer.write_collection_of_object_values("groupPolicyCategories", self.group_policy_categories)
        writer.write_collection_of_object_values("groupPolicyConfigurations", self.group_policy_configurations)
        writer.write_collection_of_object_values("groupPolicyDefinitionFiles", self.group_policy_definition_files)
        writer.write_collection_of_object_values("groupPolicyDefinitions", self.group_policy_definitions)
        writer.write_collection_of_object_values("groupPolicyMigrationReports", self.group_policy_migration_reports)
        writer.write_collection_of_object_values("groupPolicyObjectFiles", self.group_policy_object_files)
        writer.write_collection_of_object_values("groupPolicyUploadedDefinitionFiles", self.group_policy_uploaded_definition_files)
        writer.write_collection_of_object_values("hardwareConfigurations", self.hardware_configurations)
        writer.write_collection_of_object_values("hardwarePasswordDetails", self.hardware_password_details)
        writer.write_collection_of_object_values("hardwarePasswordInfo", self.hardware_password_info)
        writer.write_collection_of_object_values("importedDeviceIdentities", self.imported_device_identities)
        writer.write_collection_of_object_values("importedWindowsAutopilotDeviceIdentities", self.imported_windows_autopilot_device_identities)
        writer.write_collection_of_object_values("intents", self.intents)
        writer.write_uuid_value("intuneAccountId", self.intune_account_id)
        writer.write_object_value("intuneBrand", self.intune_brand)
        writer.write_collection_of_object_values("intuneBrandingProfiles", self.intune_branding_profiles)
        writer.write_collection_of_object_values("iosUpdateStatuses", self.ios_update_statuses)
        writer.write_collection_of_object_values("macOSSoftwareUpdateAccountSummaries", self.mac_o_s_software_update_account_summaries)
        writer.write_collection_of_object_values("managedDeviceCleanupRules", self.managed_device_cleanup_rules)
        writer.write_object_value("managedDeviceCleanupSettings", self.managed_device_cleanup_settings)
        writer.write_collection_of_object_values("managedDeviceEncryptionStates", self.managed_device_encryption_states)
        writer.write_object_value("managedDeviceOverview", self.managed_device_overview)
        writer.write_collection_of_object_values("managedDeviceWindowsOSImages", self.managed_device_windows_o_s_images)
        writer.write_collection_of_object_values("managedDevices", self.managed_devices)
        writer.write_int_value("maximumDepTokens", self.maximum_dep_tokens)
        writer.write_collection_of_object_values("microsoftTunnelConfigurations", self.microsoft_tunnel_configurations)
        writer.write_collection_of_object_values("microsoftTunnelHealthThresholds", self.microsoft_tunnel_health_thresholds)
        writer.write_collection_of_object_values("microsoftTunnelServerLogCollectionResponses", self.microsoft_tunnel_server_log_collection_responses)
        writer.write_collection_of_object_values("microsoftTunnelSites", self.microsoft_tunnel_sites)
        writer.write_collection_of_object_values("mobileAppTroubleshootingEvents", self.mobile_app_troubleshooting_events)
        writer.write_collection_of_object_values("mobileThreatDefenseConnectors", self.mobile_threat_defense_connectors)
        writer.write_object_value("monitoring", self.monitoring)
        writer.write_collection_of_object_values("ndesConnectors", self.ndes_connectors)
        writer.write_collection_of_object_values("notificationMessageTemplates", self.notification_message_templates)
        writer.write_collection_of_object_values("operationApprovalPolicies", self.operation_approval_policies)
        writer.write_collection_of_object_values("operationApprovalRequests", self.operation_approval_requests)
        writer.write_collection_of_object_values("privilegeManagementElevations", self.privilege_management_elevations)
        writer.write_collection_of_object_values("remoteActionAudits", self.remote_action_audits)
        writer.write_collection_of_object_values("remoteAssistancePartners", self.remote_assistance_partners)
        writer.write_object_value("remoteAssistanceSettings", self.remote_assistance_settings)
        writer.write_object_value("reports", self.reports)
        writer.write_collection_of_object_values("resourceAccessProfiles", self.resource_access_profiles)
        writer.write_collection_of_object_values("resourceOperations", self.resource_operations)
        writer.write_collection_of_object_values("reusablePolicySettings", self.reusable_policy_settings)
        writer.write_collection_of_object_values("reusableSettings", self.reusable_settings)
        writer.write_collection_of_object_values("roleAssignments", self.role_assignments)
        writer.write_collection_of_object_values("roleDefinitions", self.role_definitions)
        writer.write_collection_of_object_values("roleScopeTags", self.role_scope_tags)
        writer.write_collection_of_object_values("samsungEFotaFirmwareVersions", self.samsung_e_fota_firmware_versions)
        writer.write_collection_of_object_values("serviceNowConnections", self.service_now_connections)
        writer.write_collection_of_object_values("settingDefinitions", self.setting_definitions)
        writer.write_object_value("settings", self.settings)
        writer.write_object_value("softwareUpdateStatusSummary", self.software_update_status_summary)
        writer.write_enum_value("subscriptionState", self.subscription_state)
        writer.write_enum_value("subscriptions", self.subscriptions)
        writer.write_collection_of_object_values("templateInsights", self.template_insights)
        writer.write_collection_of_object_values("templateSettings", self.template_settings)
        writer.write_collection_of_object_values("templates", self.templates)
        writer.write_object_value("tenantAttachRBAC", self.tenant_attach_r_b_a_c)
        writer.write_collection_of_object_values("termsAndConditions", self.terms_and_conditions)
        writer.write_collection_of_object_values("troubleshootingEvents", self.troubleshooting_events)
        writer.write_collection_of_object_values("userExperienceAnalyticsAnomaly", self.user_experience_analytics_anomaly)
        writer.write_collection_of_object_values("userExperienceAnalyticsAnomalyCorrelationGroupOverview", self.user_experience_analytics_anomaly_correlation_group_overview)
        writer.write_collection_of_object_values("userExperienceAnalyticsAnomalyDevice", self.user_experience_analytics_anomaly_device)
        writer.write_object_value("userExperienceAnalyticsAnomalySeverityOverview", self.user_experience_analytics_anomaly_severity_overview)
        writer.write_collection_of_object_values("userExperienceAnalyticsAppHealthApplicationPerformance", self.user_experience_analytics_app_health_application_performance)
        writer.write_collection_of_object_values("userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersion", self.user_experience_analytics_app_health_application_performance_by_app_version)
        writer.write_collection_of_object_values("userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDetails", self.user_experience_analytics_app_health_application_performance_by_app_version_details)
        writer.write_collection_of_object_values("userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDeviceId", self.user_experience_analytics_app_health_application_performance_by_app_version_device_id)
        writer.write_collection_of_object_values("userExperienceAnalyticsAppHealthApplicationPerformanceByOSVersion", self.user_experience_analytics_app_health_application_performance_by_o_s_version)
        writer.write_collection_of_object_values("userExperienceAnalyticsAppHealthDeviceModelPerformance", self.user_experience_analytics_app_health_device_model_performance)
        writer.write_collection_of_object_values("userExperienceAnalyticsAppHealthDevicePerformance", self.user_experience_analytics_app_health_device_performance)
        writer.write_collection_of_object_values("userExperienceAnalyticsAppHealthDevicePerformanceDetails", self.user_experience_analytics_app_health_device_performance_details)
        writer.write_collection_of_object_values("userExperienceAnalyticsAppHealthOSVersionPerformance", self.user_experience_analytics_app_health_o_s_version_performance)
        writer.write_object_value("userExperienceAnalyticsAppHealthOverview", self.user_experience_analytics_app_health_overview)
        writer.write_collection_of_object_values("userExperienceAnalyticsBaselines", self.user_experience_analytics_baselines)
        writer.write_collection_of_object_values("userExperienceAnalyticsBatteryHealthAppImpact", self.user_experience_analytics_battery_health_app_impact)
        writer.write_object_value("userExperienceAnalyticsBatteryHealthCapacityDetails", self.user_experience_analytics_battery_health_capacity_details)
        writer.write_collection_of_object_values("userExperienceAnalyticsBatteryHealthDeviceAppImpact", self.user_experience_analytics_battery_health_device_app_impact)
        writer.write_collection_of_object_values("userExperienceAnalyticsBatteryHealthDevicePerformance", self.user_experience_analytics_battery_health_device_performance)
        writer.write_collection_of_object_values("userExperienceAnalyticsBatteryHealthDeviceRuntimeHistory", self.user_experience_analytics_battery_health_device_runtime_history)
        writer.write_collection_of_object_values("userExperienceAnalyticsBatteryHealthModelPerformance", self.user_experience_analytics_battery_health_model_performance)
        writer.write_collection_of_object_values("userExperienceAnalyticsBatteryHealthOsPerformance", self.user_experience_analytics_battery_health_os_performance)
        writer.write_object_value("userExperienceAnalyticsBatteryHealthRuntimeDetails", self.user_experience_analytics_battery_health_runtime_details)
        writer.write_collection_of_object_values("userExperienceAnalyticsCategories", self.user_experience_analytics_categories)
        writer.write_collection_of_object_values("userExperienceAnalyticsDeviceMetricHistory", self.user_experience_analytics_device_metric_history)
        writer.write_collection_of_object_values("userExperienceAnalyticsDevicePerformance", self.user_experience_analytics_device_performance)
        writer.write_object_value("userExperienceAnalyticsDeviceScope", self.user_experience_analytics_device_scope)
        writer.write_collection_of_object_values("userExperienceAnalyticsDeviceScopes", self.user_experience_analytics_device_scopes)
        writer.write_collection_of_object_values("userExperienceAnalyticsDeviceScores", self.user_experience_analytics_device_scores)
        writer.write_collection_of_object_values("userExperienceAnalyticsDeviceStartupHistory", self.user_experience_analytics_device_startup_history)
        writer.write_collection_of_object_values("userExperienceAnalyticsDeviceStartupProcessPerformance", self.user_experience_analytics_device_startup_process_performance)
        writer.write_collection_of_object_values("userExperienceAnalyticsDeviceStartupProcesses", self.user_experience_analytics_device_startup_processes)
        writer.write_collection_of_object_values("userExperienceAnalyticsDeviceTimelineEvent", self.user_experience_analytics_device_timeline_event)
        writer.write_collection_of_object_values("userExperienceAnalyticsDevicesWithoutCloudIdentity", self.user_experience_analytics_devices_without_cloud_identity)
        writer.write_collection_of_object_values("userExperienceAnalyticsImpactingProcess", self.user_experience_analytics_impacting_process)
        writer.write_collection_of_object_values("userExperienceAnalyticsMetricHistory", self.user_experience_analytics_metric_history)
        writer.write_collection_of_object_values("userExperienceAnalyticsModelScores", self.user_experience_analytics_model_scores)
        writer.write_collection_of_object_values("userExperienceAnalyticsNotAutopilotReadyDevice", self.user_experience_analytics_not_autopilot_ready_device)
        writer.write_object_value("userExperienceAnalyticsOverview", self.user_experience_analytics_overview)
        writer.write_collection_of_object_values("userExperienceAnalyticsRemoteConnection", self.user_experience_analytics_remote_connection)
        writer.write_collection_of_object_values("userExperienceAnalyticsResourcePerformance", self.user_experience_analytics_resource_performance)
        writer.write_collection_of_object_values("userExperienceAnalyticsScoreHistory", self.user_experience_analytics_score_history)
        writer.write_object_value("userExperienceAnalyticsSettings", self.user_experience_analytics_settings)
        writer.write_object_value("userExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric", self.user_experience_analytics_work_from_anywhere_hardware_readiness_metric)
        writer.write_collection_of_object_values("userExperienceAnalyticsWorkFromAnywhereMetrics", self.user_experience_analytics_work_from_anywhere_metrics)
        writer.write_collection_of_object_values("userExperienceAnalyticsWorkFromAnywhereModelPerformance", self.user_experience_analytics_work_from_anywhere_model_performance)
        writer.write_collection_of_object_values("userPfxCertificates", self.user_pfx_certificates)
        writer.write_object_value("virtualEndpoint", self.virtual_endpoint)
        writer.write_collection_of_object_values("windowsAutopilotDeploymentProfiles", self.windows_autopilot_deployment_profiles)
        writer.write_collection_of_object_values("windowsAutopilotDeviceIdentities", self.windows_autopilot_device_identities)
        writer.write_object_value("windowsAutopilotSettings", self.windows_autopilot_settings)
        writer.write_collection_of_object_values("windowsDriverUpdateProfiles", self.windows_driver_update_profiles)
        writer.write_collection_of_object_values("windowsFeatureUpdateProfiles", self.windows_feature_update_profiles)
        writer.write_collection_of_object_values("windowsInformationProtectionAppLearningSummaries", self.windows_information_protection_app_learning_summaries)
        writer.write_collection_of_object_values("windowsInformationProtectionNetworkLearningSummaries", self.windows_information_protection_network_learning_summaries)
        writer.write_collection_of_object_values("windowsMalwareInformation", self.windows_malware_information)
        writer.write_object_value("windowsMalwareOverview", self.windows_malware_overview)
        writer.write_collection_of_object_values("windowsQualityUpdatePolicies", self.windows_quality_update_policies)
        writer.write_collection_of_object_values("windowsQualityUpdateProfiles", self.windows_quality_update_profiles)
        writer.write_collection_of_object_values("windowsUpdateCatalogItems", self.windows_update_catalog_items)
        writer.write_collection_of_object_values("zebraFotaArtifacts", self.zebra_fota_artifacts)
        writer.write_object_value("zebraFotaConnector", self.zebra_fota_connector)
        writer.write_collection_of_object_values("zebraFotaDeployments", self.zebra_fota_deployments)
    

