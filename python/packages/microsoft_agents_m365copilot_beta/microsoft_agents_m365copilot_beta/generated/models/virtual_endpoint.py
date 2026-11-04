from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_audit_event import CloudPcAuditEvent
    from .cloud_pc_bulk_action import CloudPcBulkAction
    from .cloud_pc_cloud_app import CloudPcCloudApp
    from .cloud_pc_cross_cloud_government_organization_mapping import CloudPcCrossCloudGovernmentOrganizationMapping
    from .cloud_pc_device_image import CloudPcDeviceImage
    from .cloud_pc_external_partner import CloudPcExternalPartner
    from .cloud_pc_external_partner_setting import CloudPcExternalPartnerSetting
    from .cloud_pc_front_line_service_plan import CloudPcFrontLineServicePlan
    from .cloud_pc_gallery_image import CloudPcGalleryImage
    from .cloud_pc_managed_license import CloudPcManagedLicense
    from .cloud_pc_on_premises_connection import CloudPcOnPremisesConnection
    from .cloud_pc_organization_settings import CloudPcOrganizationSettings
    from .cloud_pc_pool import CloudPcPool
    from .cloud_pc_provisioning_policy import CloudPcProvisioningPolicy
    from .cloud_pc_report import CloudPcReport
    from .cloud_pc_reports import CloudPcReports
    from .cloud_pc_service_plan import CloudPcServicePlan
    from .cloud_pc_snapshot import CloudPcSnapshot
    from .cloud_pc_supported_region import CloudPcSupportedRegion
    from .cloud_pc_user_setting import CloudPcUserSetting
    from .cloud_p_c import CloudPC
    from .entity import Entity

from .entity import Entity

@dataclass
class VirtualEndpoint(Entity, Parsable):
    # Cloud PC audit event.
    audit_events: Optional[list[CloudPcAuditEvent]] = None
    # Bulk actions applied to a Cloud PC.
    bulk_actions: Optional[list[CloudPcBulkAction]] = None
    # A collection of cloud apps that are built on frontline shared options and provide Windows 365 end users with access to app-only sessions instead of a full desktop experience.
    cloud_apps: Optional[list[CloudPcCloudApp]] = None
    # Cloud managed virtual desktops.
    cloud_p_cs: Optional[list[CloudPC]] = None
    # The Cloud PC pools managed by the virtual endpoint.
    cloud_pc_pools: Optional[list[CloudPcPool]] = None
    # Cloud PC organization mapping between public and US Government Community Cloud (GCC) organizations.
    cross_cloud_government_organization_mapping: Optional[CloudPcCrossCloudGovernmentOrganizationMapping] = None
    # The image resource on Cloud PC.
    device_images: Optional[list[CloudPcDeviceImage]] = None
    # The external partner settings on a Cloud PC.
    external_partner_settings: Optional[list[CloudPcExternalPartnerSetting]] = None
    # The external partners on a Cloud PC.
    external_partners: Optional[list[CloudPcExternalPartner]] = None
    # Front-line service plans for a Cloud PC.
    front_line_service_plans: Optional[list[CloudPcFrontLineServicePlan]] = None
    # The gallery image resource on Cloud PC.
    gallery_images: Optional[list[CloudPcGalleryImage]] = None
    # The managed licenses for Cloud PCs in the organization.
    managed_licenses: Optional[list[CloudPcManagedLicense]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A defined collection of Azure resource information that can be used to establish on-premises network connectivity for Cloud PCs.
    on_premises_connections: Optional[list[CloudPcOnPremisesConnection]] = None
    # The Cloud PC organization settings for a tenant.
    organization_settings: Optional[CloudPcOrganizationSettings] = None
    # Cloud PC provisioning policy.
    provisioning_policies: Optional[list[CloudPcProvisioningPolicy]] = None
    # Cloud PC-related reports. Read-only.
    report: Optional[CloudPcReport] = None
    # Cloud PC-related reports. Read-only.
    reports: Optional[CloudPcReports] = None
    # Cloud PC service plans.
    service_plans: Optional[list[CloudPcServicePlan]] = None
    # Cloud PC snapshots.
    snapshots: Optional[list[CloudPcSnapshot]] = None
    # Cloud PC supported regions.
    supported_regions: Optional[list[CloudPcSupportedRegion]] = None
    # Cloud PC user settings.
    user_settings: Optional[list[CloudPcUserSetting]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VirtualEndpoint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VirtualEndpoint
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return VirtualEndpoint()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_audit_event import CloudPcAuditEvent
        from .cloud_pc_bulk_action import CloudPcBulkAction
        from .cloud_pc_cloud_app import CloudPcCloudApp
        from .cloud_pc_cross_cloud_government_organization_mapping import CloudPcCrossCloudGovernmentOrganizationMapping
        from .cloud_pc_device_image import CloudPcDeviceImage
        from .cloud_pc_external_partner import CloudPcExternalPartner
        from .cloud_pc_external_partner_setting import CloudPcExternalPartnerSetting
        from .cloud_pc_front_line_service_plan import CloudPcFrontLineServicePlan
        from .cloud_pc_gallery_image import CloudPcGalleryImage
        from .cloud_pc_managed_license import CloudPcManagedLicense
        from .cloud_pc_on_premises_connection import CloudPcOnPremisesConnection
        from .cloud_pc_organization_settings import CloudPcOrganizationSettings
        from .cloud_pc_pool import CloudPcPool
        from .cloud_pc_provisioning_policy import CloudPcProvisioningPolicy
        from .cloud_pc_report import CloudPcReport
        from .cloud_pc_reports import CloudPcReports
        from .cloud_pc_service_plan import CloudPcServicePlan
        from .cloud_pc_snapshot import CloudPcSnapshot
        from .cloud_pc_supported_region import CloudPcSupportedRegion
        from .cloud_pc_user_setting import CloudPcUserSetting
        from .cloud_p_c import CloudPC
        from .entity import Entity

        from .cloud_pc_audit_event import CloudPcAuditEvent
        from .cloud_pc_bulk_action import CloudPcBulkAction
        from .cloud_pc_cloud_app import CloudPcCloudApp
        from .cloud_pc_cross_cloud_government_organization_mapping import CloudPcCrossCloudGovernmentOrganizationMapping
        from .cloud_pc_device_image import CloudPcDeviceImage
        from .cloud_pc_external_partner import CloudPcExternalPartner
        from .cloud_pc_external_partner_setting import CloudPcExternalPartnerSetting
        from .cloud_pc_front_line_service_plan import CloudPcFrontLineServicePlan
        from .cloud_pc_gallery_image import CloudPcGalleryImage
        from .cloud_pc_managed_license import CloudPcManagedLicense
        from .cloud_pc_on_premises_connection import CloudPcOnPremisesConnection
        from .cloud_pc_organization_settings import CloudPcOrganizationSettings
        from .cloud_pc_pool import CloudPcPool
        from .cloud_pc_provisioning_policy import CloudPcProvisioningPolicy
        from .cloud_pc_report import CloudPcReport
        from .cloud_pc_reports import CloudPcReports
        from .cloud_pc_service_plan import CloudPcServicePlan
        from .cloud_pc_snapshot import CloudPcSnapshot
        from .cloud_pc_supported_region import CloudPcSupportedRegion
        from .cloud_pc_user_setting import CloudPcUserSetting
        from .cloud_p_c import CloudPC
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "auditEvents": lambda n : setattr(self, 'audit_events', n.get_collection_of_object_values(CloudPcAuditEvent)),
            "bulkActions": lambda n : setattr(self, 'bulk_actions', n.get_collection_of_object_values(CloudPcBulkAction)),
            "cloudApps": lambda n : setattr(self, 'cloud_apps', n.get_collection_of_object_values(CloudPcCloudApp)),
            "cloudPCs": lambda n : setattr(self, 'cloud_p_cs', n.get_collection_of_object_values(CloudPC)),
            "cloudPcPools": lambda n : setattr(self, 'cloud_pc_pools', n.get_collection_of_object_values(CloudPcPool)),
            "crossCloudGovernmentOrganizationMapping": lambda n : setattr(self, 'cross_cloud_government_organization_mapping', n.get_object_value(CloudPcCrossCloudGovernmentOrganizationMapping)),
            "deviceImages": lambda n : setattr(self, 'device_images', n.get_collection_of_object_values(CloudPcDeviceImage)),
            "externalPartnerSettings": lambda n : setattr(self, 'external_partner_settings', n.get_collection_of_object_values(CloudPcExternalPartnerSetting)),
            "externalPartners": lambda n : setattr(self, 'external_partners', n.get_collection_of_object_values(CloudPcExternalPartner)),
            "frontLineServicePlans": lambda n : setattr(self, 'front_line_service_plans', n.get_collection_of_object_values(CloudPcFrontLineServicePlan)),
            "galleryImages": lambda n : setattr(self, 'gallery_images', n.get_collection_of_object_values(CloudPcGalleryImage)),
            "managedLicenses": lambda n : setattr(self, 'managed_licenses', n.get_collection_of_object_values(CloudPcManagedLicense)),
            "onPremisesConnections": lambda n : setattr(self, 'on_premises_connections', n.get_collection_of_object_values(CloudPcOnPremisesConnection)),
            "organizationSettings": lambda n : setattr(self, 'organization_settings', n.get_object_value(CloudPcOrganizationSettings)),
            "provisioningPolicies": lambda n : setattr(self, 'provisioning_policies', n.get_collection_of_object_values(CloudPcProvisioningPolicy)),
            "report": lambda n : setattr(self, 'report', n.get_object_value(CloudPcReport)),
            "reports": lambda n : setattr(self, 'reports', n.get_object_value(CloudPcReports)),
            "servicePlans": lambda n : setattr(self, 'service_plans', n.get_collection_of_object_values(CloudPcServicePlan)),
            "snapshots": lambda n : setattr(self, 'snapshots', n.get_collection_of_object_values(CloudPcSnapshot)),
            "supportedRegions": lambda n : setattr(self, 'supported_regions', n.get_collection_of_object_values(CloudPcSupportedRegion)),
            "userSettings": lambda n : setattr(self, 'user_settings', n.get_collection_of_object_values(CloudPcUserSetting)),
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
        writer.write_collection_of_object_values("auditEvents", self.audit_events)
        writer.write_collection_of_object_values("bulkActions", self.bulk_actions)
        writer.write_collection_of_object_values("cloudApps", self.cloud_apps)
        writer.write_collection_of_object_values("cloudPCs", self.cloud_p_cs)
        writer.write_collection_of_object_values("cloudPcPools", self.cloud_pc_pools)
        writer.write_object_value("crossCloudGovernmentOrganizationMapping", self.cross_cloud_government_organization_mapping)
        writer.write_collection_of_object_values("deviceImages", self.device_images)
        writer.write_collection_of_object_values("externalPartnerSettings", self.external_partner_settings)
        writer.write_collection_of_object_values("externalPartners", self.external_partners)
        writer.write_collection_of_object_values("frontLineServicePlans", self.front_line_service_plans)
        writer.write_collection_of_object_values("galleryImages", self.gallery_images)
        writer.write_collection_of_object_values("managedLicenses", self.managed_licenses)
        writer.write_collection_of_object_values("onPremisesConnections", self.on_premises_connections)
        writer.write_object_value("organizationSettings", self.organization_settings)
        writer.write_collection_of_object_values("provisioningPolicies", self.provisioning_policies)
        writer.write_object_value("report", self.report)
        writer.write_object_value("reports", self.reports)
        writer.write_collection_of_object_values("servicePlans", self.service_plans)
        writer.write_collection_of_object_values("snapshots", self.snapshots)
        writer.write_collection_of_object_values("supportedRegions", self.supported_regions)
        writer.write_collection_of_object_values("userSettings", self.user_settings)
    

