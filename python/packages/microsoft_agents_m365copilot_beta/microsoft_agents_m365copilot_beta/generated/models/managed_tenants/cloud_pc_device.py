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
class CloudPcDevice(Entity, Parsable):
    # The status of the cloud PC. The possible values are: notProvisioned, provisioning, provisioned, upgrading, inGracePeriod, deprovisioning, failed. Required. Read-only.
    cloud_pc_status: Optional[str] = None
    # The specification of the cloud PC device. Required. Read-only.
    device_specification: Optional[str] = None
    # The display name  of the cloud PC device. Required. Read-only.
    display_name: Optional[str] = None
    # Date and time the entity was last updated in the multi-tenant management platform. Required. Read-only.
    last_refreshed_date_time: Optional[datetime.datetime] = None
    # The managed device identifier of the cloud PC device. Optional. Read-only.
    managed_device_id: Optional[str] = None
    # The managed device display name of the cloud PC device. Optional. Read-only.
    managed_device_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The provisioning policy identifier for the cloud PC device. Required. Read-only.
    provisioning_policy_id: Optional[str] = None
    # The service plan name of the cloud PC device. Required. Read-only.
    service_plan_name: Optional[str] = None
    # The service plan type of the cloud PC device. Required. Read-only.
    service_plan_type: Optional[str] = None
    # The display name for the managed tenant. Required. Read-only.
    tenant_display_name: Optional[str] = None
    # The Microsoft Entra tenant identifier for the managed tenant. Required. Read-only.
    tenant_id: Optional[str] = None
    # The user principal name (UPN) of the user assigned to the cloud PC device. Required. Read-only.
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcDevice:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcDevice
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcDevice()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity

        from ..entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "cloudPcStatus": lambda n : setattr(self, 'cloud_pc_status', n.get_str_value()),
            "deviceSpecification": lambda n : setattr(self, 'device_specification', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastRefreshedDateTime": lambda n : setattr(self, 'last_refreshed_date_time', n.get_datetime_value()),
            "managedDeviceId": lambda n : setattr(self, 'managed_device_id', n.get_str_value()),
            "managedDeviceName": lambda n : setattr(self, 'managed_device_name', n.get_str_value()),
            "provisioningPolicyId": lambda n : setattr(self, 'provisioning_policy_id', n.get_str_value()),
            "servicePlanName": lambda n : setattr(self, 'service_plan_name', n.get_str_value()),
            "servicePlanType": lambda n : setattr(self, 'service_plan_type', n.get_str_value()),
            "tenantDisplayName": lambda n : setattr(self, 'tenant_display_name', n.get_str_value()),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
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
        writer.write_str_value("cloudPcStatus", self.cloud_pc_status)
        writer.write_str_value("deviceSpecification", self.device_specification)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastRefreshedDateTime", self.last_refreshed_date_time)
        writer.write_str_value("managedDeviceId", self.managed_device_id)
        writer.write_str_value("managedDeviceName", self.managed_device_name)
        writer.write_str_value("provisioningPolicyId", self.provisioning_policy_id)
        writer.write_str_value("servicePlanName", self.service_plan_name)
        writer.write_str_value("servicePlanType", self.service_plan_type)
        writer.write_str_value("tenantDisplayName", self.tenant_display_name)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    

