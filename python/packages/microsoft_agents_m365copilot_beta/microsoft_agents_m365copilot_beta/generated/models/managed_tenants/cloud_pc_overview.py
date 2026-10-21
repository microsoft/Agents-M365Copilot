from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity

from ..entity import Entity

@dataclass
class CloudPcOverview(Entity, Parsable):
    # The total number of cloud PC devices that have the Frontline SKU. Optional. Read-only.
    frontline_licenses_count: Optional[int] = None
    # Date and time the entity was last updated in the multi-tenant management platform. Optional. Read-only.
    last_refreshed_date_time: Optional[datetime.datetime] = None
    # The number of cloud PC connections that have a status of failed. Optional. Read-only.
    number_of_cloud_pc_connection_status_failed: Optional[int] = None
    # The number of cloud PC connections that have a status of passed. Optional. Read-only.
    number_of_cloud_pc_connection_status_passed: Optional[int] = None
    # The number of cloud PC connections that have a status of pending. Optional. Read-only.
    number_of_cloud_pc_connection_status_pending: Optional[int] = None
    # The number of cloud PC connections that have a status of running. Optional. Read-only.
    number_of_cloud_pc_connection_status_running: Optional[int] = None
    # The number of cloud PC connections that have a status of unknownFutureValue. Optional. Read-only.
    number_of_cloud_pc_connection_status_unkown_future_value: Optional[int] = None
    # The number of cloud PCs that have a status of deprovisioning. Optional. Read-only.
    number_of_cloud_pc_status_deprovisioning: Optional[int] = None
    # The number of cloud PCs that have a status of failed. Optional. Read-only.
    number_of_cloud_pc_status_failed: Optional[int] = None
    # The number of cloud PCs that have a status of inGracePeriod. Optional. Read-only.
    number_of_cloud_pc_status_in_grace_period: Optional[int] = None
    # The number of cloud PCs that have a status of notProvisioned. Optional. Read-only.
    number_of_cloud_pc_status_not_provisioned: Optional[int] = None
    # The number of cloud PCs that have a status of provisioned. Optional. Read-only.
    number_of_cloud_pc_status_provisioned: Optional[int] = None
    # The number of cloud PCs that have a status of provisioning. Optional. Read-only.
    number_of_cloud_pc_status_provisioning: Optional[int] = None
    # The number of cloud PCs that have a status of unknown. Optional. Read-only.
    number_of_cloud_pc_status_unknown: Optional[int] = None
    # The number of cloud PCs that have a status of upgrading. Optional. Read-only.
    number_of_cloud_pc_status_upgrading: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The display name for the managed tenant. Optional. Read-only.
    tenant_display_name: Optional[str] = None
    # The tenantId property
    tenant_id: Optional[str] = None
    # The total number of cloud PC devices that have the Business SKU. Optional. Read-only.
    total_business_licenses: Optional[int] = None
    # The total number of cloud PC connection statuses for the given managed tenant. Optional. Read-only.
    total_cloud_pc_connection_status: Optional[int] = None
    # The total number of cloud PC statues for the given managed tenant. Optional. Read-only.
    total_cloud_pc_status: Optional[int] = None
    # The total number of cloud PC devices that have the Enterprise SKU. Optional. Read-only.
    total_enterprise_licenses: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcOverview:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcOverview
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcOverview()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity

        from ..entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "frontlineLicensesCount": lambda n : setattr(self, 'frontline_licenses_count', n.get_int_value()),
            "lastRefreshedDateTime": lambda n : setattr(self, 'last_refreshed_date_time', n.get_datetime_value()),
            "numberOfCloudPcConnectionStatusFailed": lambda n : setattr(self, 'number_of_cloud_pc_connection_status_failed', n.get_int_value()),
            "numberOfCloudPcConnectionStatusPassed": lambda n : setattr(self, 'number_of_cloud_pc_connection_status_passed', n.get_int_value()),
            "numberOfCloudPcConnectionStatusPending": lambda n : setattr(self, 'number_of_cloud_pc_connection_status_pending', n.get_int_value()),
            "numberOfCloudPcConnectionStatusRunning": lambda n : setattr(self, 'number_of_cloud_pc_connection_status_running', n.get_int_value()),
            "numberOfCloudPcConnectionStatusUnkownFutureValue": lambda n : setattr(self, 'number_of_cloud_pc_connection_status_unkown_future_value', n.get_int_value()),
            "numberOfCloudPcStatusDeprovisioning": lambda n : setattr(self, 'number_of_cloud_pc_status_deprovisioning', n.get_int_value()),
            "numberOfCloudPcStatusFailed": lambda n : setattr(self, 'number_of_cloud_pc_status_failed', n.get_int_value()),
            "numberOfCloudPcStatusInGracePeriod": lambda n : setattr(self, 'number_of_cloud_pc_status_in_grace_period', n.get_int_value()),
            "numberOfCloudPcStatusNotProvisioned": lambda n : setattr(self, 'number_of_cloud_pc_status_not_provisioned', n.get_int_value()),
            "numberOfCloudPcStatusProvisioned": lambda n : setattr(self, 'number_of_cloud_pc_status_provisioned', n.get_int_value()),
            "numberOfCloudPcStatusProvisioning": lambda n : setattr(self, 'number_of_cloud_pc_status_provisioning', n.get_int_value()),
            "numberOfCloudPcStatusUnknown": lambda n : setattr(self, 'number_of_cloud_pc_status_unknown', n.get_int_value()),
            "numberOfCloudPcStatusUpgrading": lambda n : setattr(self, 'number_of_cloud_pc_status_upgrading', n.get_int_value()),
            "tenantDisplayName": lambda n : setattr(self, 'tenant_display_name', n.get_str_value()),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "totalBusinessLicenses": lambda n : setattr(self, 'total_business_licenses', n.get_int_value()),
            "totalCloudPcConnectionStatus": lambda n : setattr(self, 'total_cloud_pc_connection_status', n.get_int_value()),
            "totalCloudPcStatus": lambda n : setattr(self, 'total_cloud_pc_status', n.get_int_value()),
            "totalEnterpriseLicenses": lambda n : setattr(self, 'total_enterprise_licenses', n.get_int_value()),
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
        writer.write_int_value("frontlineLicensesCount", self.frontline_licenses_count)
        writer.write_datetime_value("lastRefreshedDateTime", self.last_refreshed_date_time)
        writer.write_int_value("numberOfCloudPcConnectionStatusFailed", self.number_of_cloud_pc_connection_status_failed)
        writer.write_int_value("numberOfCloudPcConnectionStatusPassed", self.number_of_cloud_pc_connection_status_passed)
        writer.write_int_value("numberOfCloudPcConnectionStatusPending", self.number_of_cloud_pc_connection_status_pending)
        writer.write_int_value("numberOfCloudPcConnectionStatusRunning", self.number_of_cloud_pc_connection_status_running)
        writer.write_int_value("numberOfCloudPcConnectionStatusUnkownFutureValue", self.number_of_cloud_pc_connection_status_unkown_future_value)
        writer.write_int_value("numberOfCloudPcStatusDeprovisioning", self.number_of_cloud_pc_status_deprovisioning)
        writer.write_int_value("numberOfCloudPcStatusFailed", self.number_of_cloud_pc_status_failed)
        writer.write_int_value("numberOfCloudPcStatusInGracePeriod", self.number_of_cloud_pc_status_in_grace_period)
        writer.write_int_value("numberOfCloudPcStatusNotProvisioned", self.number_of_cloud_pc_status_not_provisioned)
        writer.write_int_value("numberOfCloudPcStatusProvisioned", self.number_of_cloud_pc_status_provisioned)
        writer.write_int_value("numberOfCloudPcStatusProvisioning", self.number_of_cloud_pc_status_provisioning)
        writer.write_int_value("numberOfCloudPcStatusUnknown", self.number_of_cloud_pc_status_unknown)
        writer.write_int_value("numberOfCloudPcStatusUpgrading", self.number_of_cloud_pc_status_upgrading)
        writer.write_str_value("tenantDisplayName", self.tenant_display_name)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_int_value("totalBusinessLicenses", self.total_business_licenses)
        writer.write_int_value("totalCloudPcConnectionStatus", self.total_cloud_pc_connection_status)
        writer.write_int_value("totalCloudPcStatus", self.total_cloud_pc_status)
        writer.write_int_value("totalEnterpriseLicenses", self.total_enterprise_licenses)
    

