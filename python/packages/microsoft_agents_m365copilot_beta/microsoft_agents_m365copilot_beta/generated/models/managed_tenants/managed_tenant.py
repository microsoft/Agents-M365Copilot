from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .aggregated_policy_compliance import AggregatedPolicyCompliance
    from .app_performance import AppPerformance
    from .audit_event import AuditEvent
    from .cloud_pc_connection import CloudPcConnection
    from .cloud_pc_device import CloudPcDevice
    from .cloud_pc_overview import CloudPcOverview
    from .conditional_access_policy_coverage import ConditionalAccessPolicyCoverage
    from .credential_user_registrations_summary import CredentialUserRegistrationsSummary
    from .device_app_performance import DeviceAppPerformance
    from .device_compliance_policy_setting_state_summary import DeviceCompliancePolicySettingStateSummary
    from .device_health_status import DeviceHealthStatus
    from .managed_device_compliance import ManagedDeviceCompliance
    from .managed_device_compliance_trend import ManagedDeviceComplianceTrend
    from .managed_tenant_alert import ManagedTenantAlert
    from .managed_tenant_alert_log import ManagedTenantAlertLog
    from .managed_tenant_alert_rule import ManagedTenantAlertRule
    from .managed_tenant_alert_rule_definition import ManagedTenantAlertRuleDefinition
    from .managed_tenant_api_notification import ManagedTenantApiNotification
    from .managed_tenant_email_notification import ManagedTenantEmailNotification
    from .managed_tenant_ticketing_endpoint import ManagedTenantTicketingEndpoint
    from .management_action import ManagementAction
    from .management_action_tenant_deployment_status import ManagementActionTenantDeploymentStatus
    from .management_intent import ManagementIntent
    from .management_template import ManagementTemplate
    from .management_template_collection import ManagementTemplateCollection
    from .management_template_collection_tenant_summary import ManagementTemplateCollectionTenantSummary
    from .management_template_step import ManagementTemplateStep
    from .management_template_step_tenant_summary import ManagementTemplateStepTenantSummary
    from .management_template_step_version import ManagementTemplateStepVersion
    from .my_role import MyRole
    from .tenant import Tenant
    from .tenant_customized_information import TenantCustomizedInformation
    from .tenant_detailed_information import TenantDetailedInformation
    from .tenant_group import TenantGroup
    from .tenant_tag import TenantTag
    from .windows_device_malware_state import WindowsDeviceMalwareState
    from .windows_protection_state import WindowsProtectionState

from ..entity import Entity

@dataclass
class ManagedTenant(Entity, Parsable):
    # Aggregate view of device compliance policies across managed tenants.
    aggregated_policy_compliances: Optional[list[AggregatedPolicyCompliance]] = None
    # The appPerformances property
    app_performances: Optional[list[AppPerformance]] = None
    # The collection of audit events across managed tenants.
    audit_events: Optional[list[AuditEvent]] = None
    # The collection of cloud PC connections across managed tenants.
    cloud_pc_connections: Optional[list[CloudPcConnection]] = None
    # The collection of cloud PC devices across managed tenants.
    cloud_pc_devices: Optional[list[CloudPcDevice]] = None
    # Overview of cloud PC information across managed tenants.
    cloud_pcs_overview: Optional[list[CloudPcOverview]] = None
    # Aggregate view of conditional access policy coverage across managed tenants.
    conditional_access_policy_coverages: Optional[list[ConditionalAccessPolicyCoverage]] = None
    # Summary information for user registration for multi-factor authentication and self service password reset across managed tenants.
    credential_user_registrations_summaries: Optional[list[CredentialUserRegistrationsSummary]] = None
    # The deviceAppPerformances property
    device_app_performances: Optional[list[DeviceAppPerformance]] = None
    # Summary information for device compliance policy setting states across managed tenants.
    device_compliance_policy_setting_state_summaries: Optional[list[DeviceCompliancePolicySettingStateSummary]] = None
    # The deviceHealthStatuses property
    device_health_statuses: Optional[list[DeviceHealthStatus]] = None
    # Trend insights for device compliance across managed tenants.
    managed_device_compliance_trends: Optional[list[ManagedDeviceComplianceTrend]] = None
    # The collection of compliance for managed devices across managed tenants.
    managed_device_compliances: Optional[list[ManagedDeviceCompliance]] = None
    # The managedTenantAlertLogs property
    managed_tenant_alert_logs: Optional[list[ManagedTenantAlertLog]] = None
    # The managedTenantAlertRuleDefinitions property
    managed_tenant_alert_rule_definitions: Optional[list[ManagedTenantAlertRuleDefinition]] = None
    # The managedTenantAlertRules property
    managed_tenant_alert_rules: Optional[list[ManagedTenantAlertRule]] = None
    # The managedTenantAlerts property
    managed_tenant_alerts: Optional[list[ManagedTenantAlert]] = None
    # The managedTenantApiNotifications property
    managed_tenant_api_notifications: Optional[list[ManagedTenantApiNotification]] = None
    # The managedTenantEmailNotifications property
    managed_tenant_email_notifications: Optional[list[ManagedTenantEmailNotification]] = None
    # The managedTenantTicketingEndpoints property
    managed_tenant_ticketing_endpoints: Optional[list[ManagedTenantTicketingEndpoint]] = None
    # The tenant level status of management actions across managed tenants.
    management_action_tenant_deployment_statuses: Optional[list[ManagementActionTenantDeploymentStatus]] = None
    # The collection of baseline management actions across managed tenants.
    management_actions: Optional[list[ManagementAction]] = None
    # The collection of baseline management intents across managed tenants.
    management_intents: Optional[list[ManagementIntent]] = None
    # The managementTemplateCollectionTenantSummaries property
    management_template_collection_tenant_summaries: Optional[list[ManagementTemplateCollectionTenantSummary]] = None
    # The managementTemplateCollections property
    management_template_collections: Optional[list[ManagementTemplateCollection]] = None
    # The managementTemplateStepTenantSummaries property
    management_template_step_tenant_summaries: Optional[list[ManagementTemplateStepTenantSummary]] = None
    # The managementTemplateStepVersions property
    management_template_step_versions: Optional[list[ManagementTemplateStepVersion]] = None
    # The managementTemplateSteps property
    management_template_steps: Optional[list[ManagementTemplateStep]] = None
    # The collection of baseline management templates across managed tenants.
    management_templates: Optional[list[ManagementTemplate]] = None
    # The collection of role assignments to a signed-in user for a managed tenant.
    my_roles: Optional[list[MyRole]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The collection of a logical grouping of managed tenants used by the multi-tenant management platform.
    tenant_groups: Optional[list[TenantGroup]] = None
    # The collection of tenant tags across managed tenants.
    tenant_tags: Optional[list[TenantTag]] = None
    # The collection of tenants associated with the managing entity.
    tenants: Optional[list[Tenant]] = None
    # The collection of tenant level customized information across managed tenants.
    tenants_customized_information: Optional[list[TenantCustomizedInformation]] = None
    # The collection tenant level detailed information across managed tenants.
    tenants_detailed_information: Optional[list[TenantDetailedInformation]] = None
    # The state of malware for Windows devices, registered with Microsoft Endpoint Manager, across managed tenants.
    windows_device_malware_states: Optional[list[WindowsDeviceMalwareState]] = None
    # The protection state for Windows devices, registered with Microsoft Endpoint Manager, across managed tenants.
    windows_protection_states: Optional[list[WindowsProtectionState]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ManagedTenant:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManagedTenant
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ManagedTenant()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .aggregated_policy_compliance import AggregatedPolicyCompliance
        from .app_performance import AppPerformance
        from .audit_event import AuditEvent
        from .cloud_pc_connection import CloudPcConnection
        from .cloud_pc_device import CloudPcDevice
        from .cloud_pc_overview import CloudPcOverview
        from .conditional_access_policy_coverage import ConditionalAccessPolicyCoverage
        from .credential_user_registrations_summary import CredentialUserRegistrationsSummary
        from .device_app_performance import DeviceAppPerformance
        from .device_compliance_policy_setting_state_summary import DeviceCompliancePolicySettingStateSummary
        from .device_health_status import DeviceHealthStatus
        from .managed_device_compliance import ManagedDeviceCompliance
        from .managed_device_compliance_trend import ManagedDeviceComplianceTrend
        from .managed_tenant_alert import ManagedTenantAlert
        from .managed_tenant_alert_log import ManagedTenantAlertLog
        from .managed_tenant_alert_rule import ManagedTenantAlertRule
        from .managed_tenant_alert_rule_definition import ManagedTenantAlertRuleDefinition
        from .managed_tenant_api_notification import ManagedTenantApiNotification
        from .managed_tenant_email_notification import ManagedTenantEmailNotification
        from .managed_tenant_ticketing_endpoint import ManagedTenantTicketingEndpoint
        from .management_action import ManagementAction
        from .management_action_tenant_deployment_status import ManagementActionTenantDeploymentStatus
        from .management_intent import ManagementIntent
        from .management_template import ManagementTemplate
        from .management_template_collection import ManagementTemplateCollection
        from .management_template_collection_tenant_summary import ManagementTemplateCollectionTenantSummary
        from .management_template_step import ManagementTemplateStep
        from .management_template_step_tenant_summary import ManagementTemplateStepTenantSummary
        from .management_template_step_version import ManagementTemplateStepVersion
        from .my_role import MyRole
        from .tenant import Tenant
        from .tenant_customized_information import TenantCustomizedInformation
        from .tenant_detailed_information import TenantDetailedInformation
        from .tenant_group import TenantGroup
        from .tenant_tag import TenantTag
        from .windows_device_malware_state import WindowsDeviceMalwareState
        from .windows_protection_state import WindowsProtectionState

        from ..entity import Entity
        from .aggregated_policy_compliance import AggregatedPolicyCompliance
        from .app_performance import AppPerformance
        from .audit_event import AuditEvent
        from .cloud_pc_connection import CloudPcConnection
        from .cloud_pc_device import CloudPcDevice
        from .cloud_pc_overview import CloudPcOverview
        from .conditional_access_policy_coverage import ConditionalAccessPolicyCoverage
        from .credential_user_registrations_summary import CredentialUserRegistrationsSummary
        from .device_app_performance import DeviceAppPerformance
        from .device_compliance_policy_setting_state_summary import DeviceCompliancePolicySettingStateSummary
        from .device_health_status import DeviceHealthStatus
        from .managed_device_compliance import ManagedDeviceCompliance
        from .managed_device_compliance_trend import ManagedDeviceComplianceTrend
        from .managed_tenant_alert import ManagedTenantAlert
        from .managed_tenant_alert_log import ManagedTenantAlertLog
        from .managed_tenant_alert_rule import ManagedTenantAlertRule
        from .managed_tenant_alert_rule_definition import ManagedTenantAlertRuleDefinition
        from .managed_tenant_api_notification import ManagedTenantApiNotification
        from .managed_tenant_email_notification import ManagedTenantEmailNotification
        from .managed_tenant_ticketing_endpoint import ManagedTenantTicketingEndpoint
        from .management_action import ManagementAction
        from .management_action_tenant_deployment_status import ManagementActionTenantDeploymentStatus
        from .management_intent import ManagementIntent
        from .management_template import ManagementTemplate
        from .management_template_collection import ManagementTemplateCollection
        from .management_template_collection_tenant_summary import ManagementTemplateCollectionTenantSummary
        from .management_template_step import ManagementTemplateStep
        from .management_template_step_tenant_summary import ManagementTemplateStepTenantSummary
        from .management_template_step_version import ManagementTemplateStepVersion
        from .my_role import MyRole
        from .tenant import Tenant
        from .tenant_customized_information import TenantCustomizedInformation
        from .tenant_detailed_information import TenantDetailedInformation
        from .tenant_group import TenantGroup
        from .tenant_tag import TenantTag
        from .windows_device_malware_state import WindowsDeviceMalwareState
        from .windows_protection_state import WindowsProtectionState

        fields: dict[str, Callable[[Any], None]] = {
            "aggregatedPolicyCompliances": lambda n : setattr(self, 'aggregated_policy_compliances', n.get_collection_of_object_values(AggregatedPolicyCompliance)),
            "appPerformances": lambda n : setattr(self, 'app_performances', n.get_collection_of_object_values(AppPerformance)),
            "auditEvents": lambda n : setattr(self, 'audit_events', n.get_collection_of_object_values(AuditEvent)),
            "cloudPcConnections": lambda n : setattr(self, 'cloud_pc_connections', n.get_collection_of_object_values(CloudPcConnection)),
            "cloudPcDevices": lambda n : setattr(self, 'cloud_pc_devices', n.get_collection_of_object_values(CloudPcDevice)),
            "cloudPcsOverview": lambda n : setattr(self, 'cloud_pcs_overview', n.get_collection_of_object_values(CloudPcOverview)),
            "conditionalAccessPolicyCoverages": lambda n : setattr(self, 'conditional_access_policy_coverages', n.get_collection_of_object_values(ConditionalAccessPolicyCoverage)),
            "credentialUserRegistrationsSummaries": lambda n : setattr(self, 'credential_user_registrations_summaries', n.get_collection_of_object_values(CredentialUserRegistrationsSummary)),
            "deviceAppPerformances": lambda n : setattr(self, 'device_app_performances', n.get_collection_of_object_values(DeviceAppPerformance)),
            "deviceCompliancePolicySettingStateSummaries": lambda n : setattr(self, 'device_compliance_policy_setting_state_summaries', n.get_collection_of_object_values(DeviceCompliancePolicySettingStateSummary)),
            "deviceHealthStatuses": lambda n : setattr(self, 'device_health_statuses', n.get_collection_of_object_values(DeviceHealthStatus)),
            "managedDeviceComplianceTrends": lambda n : setattr(self, 'managed_device_compliance_trends', n.get_collection_of_object_values(ManagedDeviceComplianceTrend)),
            "managedDeviceCompliances": lambda n : setattr(self, 'managed_device_compliances', n.get_collection_of_object_values(ManagedDeviceCompliance)),
            "managedTenantAlertLogs": lambda n : setattr(self, 'managed_tenant_alert_logs', n.get_collection_of_object_values(ManagedTenantAlertLog)),
            "managedTenantAlertRuleDefinitions": lambda n : setattr(self, 'managed_tenant_alert_rule_definitions', n.get_collection_of_object_values(ManagedTenantAlertRuleDefinition)),
            "managedTenantAlertRules": lambda n : setattr(self, 'managed_tenant_alert_rules', n.get_collection_of_object_values(ManagedTenantAlertRule)),
            "managedTenantAlerts": lambda n : setattr(self, 'managed_tenant_alerts', n.get_collection_of_object_values(ManagedTenantAlert)),
            "managedTenantApiNotifications": lambda n : setattr(self, 'managed_tenant_api_notifications', n.get_collection_of_object_values(ManagedTenantApiNotification)),
            "managedTenantEmailNotifications": lambda n : setattr(self, 'managed_tenant_email_notifications', n.get_collection_of_object_values(ManagedTenantEmailNotification)),
            "managedTenantTicketingEndpoints": lambda n : setattr(self, 'managed_tenant_ticketing_endpoints', n.get_collection_of_object_values(ManagedTenantTicketingEndpoint)),
            "managementActionTenantDeploymentStatuses": lambda n : setattr(self, 'management_action_tenant_deployment_statuses', n.get_collection_of_object_values(ManagementActionTenantDeploymentStatus)),
            "managementActions": lambda n : setattr(self, 'management_actions', n.get_collection_of_object_values(ManagementAction)),
            "managementIntents": lambda n : setattr(self, 'management_intents', n.get_collection_of_object_values(ManagementIntent)),
            "managementTemplateCollectionTenantSummaries": lambda n : setattr(self, 'management_template_collection_tenant_summaries', n.get_collection_of_object_values(ManagementTemplateCollectionTenantSummary)),
            "managementTemplateCollections": lambda n : setattr(self, 'management_template_collections', n.get_collection_of_object_values(ManagementTemplateCollection)),
            "managementTemplateStepTenantSummaries": lambda n : setattr(self, 'management_template_step_tenant_summaries', n.get_collection_of_object_values(ManagementTemplateStepTenantSummary)),
            "managementTemplateStepVersions": lambda n : setattr(self, 'management_template_step_versions', n.get_collection_of_object_values(ManagementTemplateStepVersion)),
            "managementTemplateSteps": lambda n : setattr(self, 'management_template_steps', n.get_collection_of_object_values(ManagementTemplateStep)),
            "managementTemplates": lambda n : setattr(self, 'management_templates', n.get_collection_of_object_values(ManagementTemplate)),
            "myRoles": lambda n : setattr(self, 'my_roles', n.get_collection_of_object_values(MyRole)),
            "tenantGroups": lambda n : setattr(self, 'tenant_groups', n.get_collection_of_object_values(TenantGroup)),
            "tenantTags": lambda n : setattr(self, 'tenant_tags', n.get_collection_of_object_values(TenantTag)),
            "tenants": lambda n : setattr(self, 'tenants', n.get_collection_of_object_values(Tenant)),
            "tenantsCustomizedInformation": lambda n : setattr(self, 'tenants_customized_information', n.get_collection_of_object_values(TenantCustomizedInformation)),
            "tenantsDetailedInformation": lambda n : setattr(self, 'tenants_detailed_information', n.get_collection_of_object_values(TenantDetailedInformation)),
            "windowsDeviceMalwareStates": lambda n : setattr(self, 'windows_device_malware_states', n.get_collection_of_object_values(WindowsDeviceMalwareState)),
            "windowsProtectionStates": lambda n : setattr(self, 'windows_protection_states', n.get_collection_of_object_values(WindowsProtectionState)),
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
        writer.write_collection_of_object_values("aggregatedPolicyCompliances", self.aggregated_policy_compliances)
        writer.write_collection_of_object_values("appPerformances", self.app_performances)
        writer.write_collection_of_object_values("auditEvents", self.audit_events)
        writer.write_collection_of_object_values("cloudPcConnections", self.cloud_pc_connections)
        writer.write_collection_of_object_values("cloudPcDevices", self.cloud_pc_devices)
        writer.write_collection_of_object_values("cloudPcsOverview", self.cloud_pcs_overview)
        writer.write_collection_of_object_values("conditionalAccessPolicyCoverages", self.conditional_access_policy_coverages)
        writer.write_collection_of_object_values("credentialUserRegistrationsSummaries", self.credential_user_registrations_summaries)
        writer.write_collection_of_object_values("deviceAppPerformances", self.device_app_performances)
        writer.write_collection_of_object_values("deviceCompliancePolicySettingStateSummaries", self.device_compliance_policy_setting_state_summaries)
        writer.write_collection_of_object_values("deviceHealthStatuses", self.device_health_statuses)
        writer.write_collection_of_object_values("managedDeviceComplianceTrends", self.managed_device_compliance_trends)
        writer.write_collection_of_object_values("managedDeviceCompliances", self.managed_device_compliances)
        writer.write_collection_of_object_values("managedTenantAlertLogs", self.managed_tenant_alert_logs)
        writer.write_collection_of_object_values("managedTenantAlertRuleDefinitions", self.managed_tenant_alert_rule_definitions)
        writer.write_collection_of_object_values("managedTenantAlertRules", self.managed_tenant_alert_rules)
        writer.write_collection_of_object_values("managedTenantAlerts", self.managed_tenant_alerts)
        writer.write_collection_of_object_values("managedTenantApiNotifications", self.managed_tenant_api_notifications)
        writer.write_collection_of_object_values("managedTenantEmailNotifications", self.managed_tenant_email_notifications)
        writer.write_collection_of_object_values("managedTenantTicketingEndpoints", self.managed_tenant_ticketing_endpoints)
        writer.write_collection_of_object_values("managementActionTenantDeploymentStatuses", self.management_action_tenant_deployment_statuses)
        writer.write_collection_of_object_values("managementActions", self.management_actions)
        writer.write_collection_of_object_values("managementIntents", self.management_intents)
        writer.write_collection_of_object_values("managementTemplateCollectionTenantSummaries", self.management_template_collection_tenant_summaries)
        writer.write_collection_of_object_values("managementTemplateCollections", self.management_template_collections)
        writer.write_collection_of_object_values("managementTemplateStepTenantSummaries", self.management_template_step_tenant_summaries)
        writer.write_collection_of_object_values("managementTemplateStepVersions", self.management_template_step_versions)
        writer.write_collection_of_object_values("managementTemplateSteps", self.management_template_steps)
        writer.write_collection_of_object_values("managementTemplates", self.management_templates)
        writer.write_collection_of_object_values("myRoles", self.my_roles)
        writer.write_collection_of_object_values("tenantGroups", self.tenant_groups)
        writer.write_collection_of_object_values("tenantTags", self.tenant_tags)
        writer.write_collection_of_object_values("tenants", self.tenants)
        writer.write_collection_of_object_values("tenantsCustomizedInformation", self.tenants_customized_information)
        writer.write_collection_of_object_values("tenantsDetailedInformation", self.tenants_detailed_information)
        writer.write_collection_of_object_values("windowsDeviceMalwareStates", self.windows_device_malware_states)
        writer.write_collection_of_object_values("windowsProtectionStates", self.windows_protection_states)
    

