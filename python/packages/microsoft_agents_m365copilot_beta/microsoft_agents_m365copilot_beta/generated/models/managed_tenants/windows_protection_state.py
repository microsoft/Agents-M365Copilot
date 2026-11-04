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
class WindowsProtectionState(Entity, Parsable):
    # The anti-malware version for the managed device. Optional. Read-only.
    anti_malware_version: Optional[str] = None
    # A flag indicating whether attention is required for the managed device. Optional. Read-only.
    attention_required: Optional[bool] = None
    # A flag indicating whether the managed device has been deleted. Optional. Read-only.
    device_deleted: Optional[bool] = None
    # The date and time the device property has been refreshed. Optional. Read-only.
    device_property_refresh_date_time: Optional[datetime.datetime] = None
    # The anti-virus engine version for the managed device. Optional. Read-only.
    engine_version: Optional[str] = None
    # A flag indicating whether quick scan is overdue for the managed device. Optional. Read-only.
    full_scan_overdue: Optional[bool] = None
    # A flag indicating whether full scan is overdue for the managed device. Optional. Read-only.
    full_scan_required: Optional[bool] = None
    # The date and time a full scan was completed. Optional. Read-only.
    last_full_scan_date_time: Optional[datetime.datetime] = None
    # The version anti-malware version used to perform the last full scan. Optional. Read-only.
    last_full_scan_signature_version: Optional[str] = None
    # The date and time a quick scan was completed. Optional. Read-only.
    last_quick_scan_date_time: Optional[datetime.datetime] = None
    # The version anti-malware version used to perform the last full scan. Optional. Read-only.
    last_quick_scan_signature_version: Optional[str] = None
    # Date and time the entity was last updated in the multi-tenant management platform. Optional. Read-only.
    last_refreshed_date_time: Optional[datetime.datetime] = None
    # The date and time the protection state was last reported for the managed device. Optional. Read-only.
    last_reported_date_time: Optional[datetime.datetime] = None
    # A flag indicating whether malware protection is enabled for the managed device. Optional. Read-only.
    malware_protection_enabled: Optional[bool] = None
    # The health state for the managed device. Optional. Read-only.
    managed_device_health_state: Optional[str] = None
    # The unique identifier for the managed device. Optional. Read-only.
    managed_device_id: Optional[str] = None
    # The display name for the managed device. Optional. Read-only.
    managed_device_name: Optional[str] = None
    # A flag indicating whether the network inspection system is enabled. Optional. Read-only.
    network_inspection_system_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A flag indicating weather a quick scan is overdue. Optional. Read-only.
    quick_scan_overdue: Optional[bool] = None
    # A flag indicating whether real time protection is enabled. Optional. Read-only.
    real_time_protection_enabled: Optional[bool] = None
    # A flag indicating whether a reboot is required. Optional. Read-only.
    reboot_required: Optional[bool] = None
    # A flag indicating whether an signature update is overdue. Optional. Read-only.
    signature_update_overdue: Optional[bool] = None
    # The signature version for the managed device. Optional. Read-only.
    signature_version: Optional[str] = None
    # The display name for the managed tenant. Optional. Read-only.
    tenant_display_name: Optional[str] = None
    # The Microsoft Entra tenant identifier for the managed tenant. Optional. Read-only.
    tenant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsProtectionState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsProtectionState
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsProtectionState()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity

        from ..entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "antiMalwareVersion": lambda n : setattr(self, 'anti_malware_version', n.get_str_value()),
            "attentionRequired": lambda n : setattr(self, 'attention_required', n.get_bool_value()),
            "deviceDeleted": lambda n : setattr(self, 'device_deleted', n.get_bool_value()),
            "devicePropertyRefreshDateTime": lambda n : setattr(self, 'device_property_refresh_date_time', n.get_datetime_value()),
            "engineVersion": lambda n : setattr(self, 'engine_version', n.get_str_value()),
            "fullScanOverdue": lambda n : setattr(self, 'full_scan_overdue', n.get_bool_value()),
            "fullScanRequired": lambda n : setattr(self, 'full_scan_required', n.get_bool_value()),
            "lastFullScanDateTime": lambda n : setattr(self, 'last_full_scan_date_time', n.get_datetime_value()),
            "lastFullScanSignatureVersion": lambda n : setattr(self, 'last_full_scan_signature_version', n.get_str_value()),
            "lastQuickScanDateTime": lambda n : setattr(self, 'last_quick_scan_date_time', n.get_datetime_value()),
            "lastQuickScanSignatureVersion": lambda n : setattr(self, 'last_quick_scan_signature_version', n.get_str_value()),
            "lastRefreshedDateTime": lambda n : setattr(self, 'last_refreshed_date_time', n.get_datetime_value()),
            "lastReportedDateTime": lambda n : setattr(self, 'last_reported_date_time', n.get_datetime_value()),
            "malwareProtectionEnabled": lambda n : setattr(self, 'malware_protection_enabled', n.get_bool_value()),
            "managedDeviceHealthState": lambda n : setattr(self, 'managed_device_health_state', n.get_str_value()),
            "managedDeviceId": lambda n : setattr(self, 'managed_device_id', n.get_str_value()),
            "managedDeviceName": lambda n : setattr(self, 'managed_device_name', n.get_str_value()),
            "networkInspectionSystemEnabled": lambda n : setattr(self, 'network_inspection_system_enabled', n.get_bool_value()),
            "quickScanOverdue": lambda n : setattr(self, 'quick_scan_overdue', n.get_bool_value()),
            "realTimeProtectionEnabled": lambda n : setattr(self, 'real_time_protection_enabled', n.get_bool_value()),
            "rebootRequired": lambda n : setattr(self, 'reboot_required', n.get_bool_value()),
            "signatureUpdateOverdue": lambda n : setattr(self, 'signature_update_overdue', n.get_bool_value()),
            "signatureVersion": lambda n : setattr(self, 'signature_version', n.get_str_value()),
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
        writer.write_str_value("antiMalwareVersion", self.anti_malware_version)
        writer.write_bool_value("attentionRequired", self.attention_required)
        writer.write_bool_value("deviceDeleted", self.device_deleted)
        writer.write_datetime_value("devicePropertyRefreshDateTime", self.device_property_refresh_date_time)
        writer.write_str_value("engineVersion", self.engine_version)
        writer.write_bool_value("fullScanOverdue", self.full_scan_overdue)
        writer.write_bool_value("fullScanRequired", self.full_scan_required)
        writer.write_datetime_value("lastFullScanDateTime", self.last_full_scan_date_time)
        writer.write_str_value("lastFullScanSignatureVersion", self.last_full_scan_signature_version)
        writer.write_datetime_value("lastQuickScanDateTime", self.last_quick_scan_date_time)
        writer.write_str_value("lastQuickScanSignatureVersion", self.last_quick_scan_signature_version)
        writer.write_datetime_value("lastRefreshedDateTime", self.last_refreshed_date_time)
        writer.write_datetime_value("lastReportedDateTime", self.last_reported_date_time)
        writer.write_bool_value("malwareProtectionEnabled", self.malware_protection_enabled)
        writer.write_str_value("managedDeviceHealthState", self.managed_device_health_state)
        writer.write_str_value("managedDeviceId", self.managed_device_id)
        writer.write_str_value("managedDeviceName", self.managed_device_name)
        writer.write_bool_value("networkInspectionSystemEnabled", self.network_inspection_system_enabled)
        writer.write_bool_value("quickScanOverdue", self.quick_scan_overdue)
        writer.write_bool_value("realTimeProtectionEnabled", self.real_time_protection_enabled)
        writer.write_bool_value("rebootRequired", self.reboot_required)
        writer.write_bool_value("signatureUpdateOverdue", self.signature_update_overdue)
        writer.write_str_value("signatureVersion", self.signature_version)
        writer.write_str_value("tenantDisplayName", self.tenant_display_name)
        writer.write_str_value("tenantId", self.tenant_id)
    

