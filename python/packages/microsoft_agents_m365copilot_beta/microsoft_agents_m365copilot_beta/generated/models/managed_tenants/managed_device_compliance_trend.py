from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity

from ..entity import Entity

@dataclass
class ManagedDeviceComplianceTrend(Entity, Parsable):
    # The number of devices with a compliant status. Required. Read-only.
    compliant_device_count: Optional[int] = None
    # The number of devices manged by Configuration Manager. Required. Read-only.
    config_manager_device_count: Optional[int] = None
    # The date and time compliance snapshot was performed. Required. Read-only.
    count_date_time: Optional[str] = None
    # The number of devices with an error status. Required. Read-only.
    error_device_count: Optional[int] = None
    # The number of devices that are in a grace period status. Required. Read-only.
    in_grace_period_device_count: Optional[int] = None
    # The number of devices that are in a non-compliant status. Required. Read-only.
    noncompliant_device_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The display name for the managed tenant. Optional. Read-only.
    tenant_display_name: Optional[str] = None
    # The Microsoft Entra tenant identifier for the managed tenant. Optional. Read-only.
    tenant_id: Optional[str] = None
    # The number of devices in an unknown status. Required. Read-only.
    unknown_device_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ManagedDeviceComplianceTrend:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManagedDeviceComplianceTrend
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ManagedDeviceComplianceTrend()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity

        from ..entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "compliantDeviceCount": lambda n : setattr(self, 'compliant_device_count', n.get_int_value()),
            "configManagerDeviceCount": lambda n : setattr(self, 'config_manager_device_count', n.get_int_value()),
            "countDateTime": lambda n : setattr(self, 'count_date_time', n.get_str_value()),
            "errorDeviceCount": lambda n : setattr(self, 'error_device_count', n.get_int_value()),
            "inGracePeriodDeviceCount": lambda n : setattr(self, 'in_grace_period_device_count', n.get_int_value()),
            "noncompliantDeviceCount": lambda n : setattr(self, 'noncompliant_device_count', n.get_int_value()),
            "tenantDisplayName": lambda n : setattr(self, 'tenant_display_name', n.get_str_value()),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "unknownDeviceCount": lambda n : setattr(self, 'unknown_device_count', n.get_int_value()),
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
        writer.write_int_value("compliantDeviceCount", self.compliant_device_count)
        writer.write_int_value("configManagerDeviceCount", self.config_manager_device_count)
        writer.write_str_value("countDateTime", self.count_date_time)
        writer.write_int_value("errorDeviceCount", self.error_device_count)
        writer.write_int_value("inGracePeriodDeviceCount", self.in_grace_period_device_count)
        writer.write_int_value("noncompliantDeviceCount", self.noncompliant_device_count)
        writer.write_str_value("tenantDisplayName", self.tenant_display_name)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_int_value("unknownDeviceCount", self.unknown_device_count)
    

