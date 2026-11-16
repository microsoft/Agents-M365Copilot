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
class DeviceCompliancePolicySettingStateSummary(Entity, Parsable):
    # The number of devices in a conflict state. Optional. Read-only.
    conflict_device_count: Optional[int] = None
    # The number of devices in an error state. Optional. Read-only.
    error_device_count: Optional[int] = None
    # The number of devices in a failed state. Optional. Read-only.
    failed_device_count: Optional[int] = None
    # The identifer for the Microsoft Intune account. Required. Read-only.
    intune_account_id: Optional[str] = None
    # The identifier for the Intune setting. Optional. Read-only.
    intune_setting_id: Optional[str] = None
    # Date and time the entity was last updated in the multi-tenant management platform. Optional. Read-only.
    last_refreshed_date_time: Optional[datetime.datetime] = None
    # The number of devices in a not applicable state. Optional. Read-only.
    not_applicable_device_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The number of devices in a pending state. Optional. Read-only.
    pending_device_count: Optional[int] = None
    # The type for the device compliance policy. Optional. Read-only.
    policy_type: Optional[str] = None
    # The name for the setting within the device compliance policy. Optional. Read-only.
    setting_name: Optional[str] = None
    # The number of devices in a succeeded state. Optional. Read-only.
    succeeded_device_count: Optional[int] = None
    # The display name for the managed tenant. Required. Read-only.
    tenant_display_name: Optional[str] = None
    # The Microsoft Entra tenant identifier for the managed tenant. Required. Read-only.
    tenant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceCompliancePolicySettingStateSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceCompliancePolicySettingStateSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceCompliancePolicySettingStateSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity

        from ..entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "conflictDeviceCount": lambda n : setattr(self, 'conflict_device_count', n.get_int_value()),
            "errorDeviceCount": lambda n : setattr(self, 'error_device_count', n.get_int_value()),
            "failedDeviceCount": lambda n : setattr(self, 'failed_device_count', n.get_int_value()),
            "intuneAccountId": lambda n : setattr(self, 'intune_account_id', n.get_str_value()),
            "intuneSettingId": lambda n : setattr(self, 'intune_setting_id', n.get_str_value()),
            "lastRefreshedDateTime": lambda n : setattr(self, 'last_refreshed_date_time', n.get_datetime_value()),
            "notApplicableDeviceCount": lambda n : setattr(self, 'not_applicable_device_count', n.get_int_value()),
            "pendingDeviceCount": lambda n : setattr(self, 'pending_device_count', n.get_int_value()),
            "policyType": lambda n : setattr(self, 'policy_type', n.get_str_value()),
            "settingName": lambda n : setattr(self, 'setting_name', n.get_str_value()),
            "succeededDeviceCount": lambda n : setattr(self, 'succeeded_device_count', n.get_int_value()),
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
        writer.write_int_value("conflictDeviceCount", self.conflict_device_count)
        writer.write_int_value("errorDeviceCount", self.error_device_count)
        writer.write_int_value("failedDeviceCount", self.failed_device_count)
        writer.write_str_value("intuneAccountId", self.intune_account_id)
        writer.write_str_value("intuneSettingId", self.intune_setting_id)
        writer.write_datetime_value("lastRefreshedDateTime", self.last_refreshed_date_time)
        writer.write_int_value("notApplicableDeviceCount", self.not_applicable_device_count)
        writer.write_int_value("pendingDeviceCount", self.pending_device_count)
        writer.write_str_value("policyType", self.policy_type)
        writer.write_str_value("settingName", self.setting_name)
        writer.write_int_value("succeededDeviceCount", self.succeeded_device_count)
        writer.write_str_value("tenantDisplayName", self.tenant_display_name)
        writer.write_str_value("tenantId", self.tenant_id)
    

