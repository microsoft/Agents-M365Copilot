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
class ManagedDeviceCompliance(Entity, Parsable):
    # Compliance state of the device. This property is read-only. The possible values are: unknown, compliant, noncompliant, conflict, error, inGracePeriod, configManager. Optional. Read-only.
    compliance_status: Optional[str] = None
    # Platform of the device. This property is read-only. The possible values are: desktop, windowsRT, winMO6, nokia, windowsPhone, mac, winCE, winEmbedded, iPhone, iPad, iPod, android, iSocConsumer, unix, macMDM, holoLens, surfaceHub, androidForWork, androidEnterprise, windows10x, androidnGMS, chromeOS, linux, blackberry, palm, unknown, cloudPC.  Optional. Read-only.
    device_type: Optional[str] = None
    # The date and time when the grace period will expire. Optional. Read-only.
    in_grace_period_until_date_time: Optional[datetime.datetime] = None
    # Date and time the entity was last updated in the multi-tenant management platform. Optional. Read-only.
    last_refreshed_date_time: Optional[datetime.datetime] = None
    # The date and time that the device last completed a successful sync with Microsoft Endpoint Manager. Optional. Read-only.
    last_sync_date_time: Optional[datetime.datetime] = None
    # The identifier for the managed device in Microsoft Endpoint Manager. Optional. Read-only.
    managed_device_id: Optional[str] = None
    # The display name for the managed device. Optional. Read-only.
    managed_device_name: Optional[str] = None
    # The manufacture for the device. Optional. Read-only.
    manufacturer: Optional[str] = None
    # The model for the device. Optional. Read-only.
    model: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The description of the operating system for the managed device. Optional. Read-only.
    os_description: Optional[str] = None
    # The version of the operating system for the managed device. Optional. Read-only.
    os_version: Optional[str] = None
    # The type of owner for the managed device. Optional. Read-only.
    owner_type: Optional[str] = None
    # The display name for the managed tenant. Optional. Read-only.
    tenant_display_name: Optional[str] = None
    # The Microsoft Entra tenant identifier for the managed tenant. Optional. Read-only.
    tenant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ManagedDeviceCompliance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManagedDeviceCompliance
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ManagedDeviceCompliance()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity

        from ..entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "complianceStatus": lambda n : setattr(self, 'compliance_status', n.get_str_value()),
            "deviceType": lambda n : setattr(self, 'device_type', n.get_str_value()),
            "inGracePeriodUntilDateTime": lambda n : setattr(self, 'in_grace_period_until_date_time', n.get_datetime_value()),
            "lastRefreshedDateTime": lambda n : setattr(self, 'last_refreshed_date_time', n.get_datetime_value()),
            "lastSyncDateTime": lambda n : setattr(self, 'last_sync_date_time', n.get_datetime_value()),
            "managedDeviceId": lambda n : setattr(self, 'managed_device_id', n.get_str_value()),
            "managedDeviceName": lambda n : setattr(self, 'managed_device_name', n.get_str_value()),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "osDescription": lambda n : setattr(self, 'os_description', n.get_str_value()),
            "osVersion": lambda n : setattr(self, 'os_version', n.get_str_value()),
            "ownerType": lambda n : setattr(self, 'owner_type', n.get_str_value()),
            "tenantDisplayName": lambda n : setattr(self, 'tenant_display_name', n.get_str_value()),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
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
        writer.write_str_value("complianceStatus", self.compliance_status)
        writer.write_str_value("deviceType", self.device_type)
        writer.write_datetime_value("inGracePeriodUntilDateTime", self.in_grace_period_until_date_time)
        writer.write_datetime_value("lastRefreshedDateTime", self.last_refreshed_date_time)
        writer.write_datetime_value("lastSyncDateTime", self.last_sync_date_time)
        writer.write_str_value("managedDeviceId", self.managed_device_id)
        writer.write_str_value("managedDeviceName", self.managed_device_name)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_str_value("model", self.model)
        writer.write_str_value("osDescription", self.os_description)
        writer.write_str_value("osVersion", self.os_version)
        writer.write_str_value("ownerType", self.owner_type)
        writer.write_str_value("tenantDisplayName", self.tenant_display_name)
        writer.write_str_value("tenantId", self.tenant_id)
    

