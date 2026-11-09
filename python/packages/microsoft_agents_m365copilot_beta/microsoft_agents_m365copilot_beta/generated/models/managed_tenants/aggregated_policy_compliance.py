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
class AggregatedPolicyCompliance(Entity, Parsable):
    # Identifier for the device compliance policy. Optional. Read-only.
    compliance_policy_id: Optional[str] = None
    # Name of the device compliance policy. Optional. Read-only.
    compliance_policy_name: Optional[str] = None
    # Platform for the device compliance policy. The possible values are: android, androidForWork, iOS, macOS, windowsPhone81, windows81AndLater, windows10AndLater, androidWorkProfile, androidAOSP, all. Optional. Read-only.
    compliance_policy_platform: Optional[str] = None
    # The type of compliance policy. Optional. Read-only.
    compliance_policy_type: Optional[str] = None
    # Date and time the entity was last updated in the multi-tenant management platform. Optional. Read-only.
    last_refreshed_date_time: Optional[datetime.datetime] = None
    # The number of devices that are in a compliant status. Optional. Read-only.
    number_of_compliant_devices: Optional[int] = None
    # The number of devices that are in an error status. Optional. Read-only.
    number_of_error_devices: Optional[int] = None
    # The number of device that are in a non-compliant status. Optional. Read-only.
    number_of_non_compliant_devices: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The date and time the device policy was last modified. Optional. Read-only.
    policy_modified_date_time: Optional[datetime.datetime] = None
    # The display name for the managed tenant. Optional. Read-only.
    tenant_display_name: Optional[str] = None
    # The Microsoft Entra tenant identifier for the managed tenant. Optional. Read-only.
    tenant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AggregatedPolicyCompliance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AggregatedPolicyCompliance
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AggregatedPolicyCompliance()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity

        from ..entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "compliancePolicyId": lambda n : setattr(self, 'compliance_policy_id', n.get_str_value()),
            "compliancePolicyName": lambda n : setattr(self, 'compliance_policy_name', n.get_str_value()),
            "compliancePolicyPlatform": lambda n : setattr(self, 'compliance_policy_platform', n.get_str_value()),
            "compliancePolicyType": lambda n : setattr(self, 'compliance_policy_type', n.get_str_value()),
            "lastRefreshedDateTime": lambda n : setattr(self, 'last_refreshed_date_time', n.get_datetime_value()),
            "numberOfCompliantDevices": lambda n : setattr(self, 'number_of_compliant_devices', n.get_int_value()),
            "numberOfErrorDevices": lambda n : setattr(self, 'number_of_error_devices', n.get_int_value()),
            "numberOfNonCompliantDevices": lambda n : setattr(self, 'number_of_non_compliant_devices', n.get_int_value()),
            "policyModifiedDateTime": lambda n : setattr(self, 'policy_modified_date_time', n.get_datetime_value()),
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
        writer.write_str_value("compliancePolicyId", self.compliance_policy_id)
        writer.write_str_value("compliancePolicyName", self.compliance_policy_name)
        writer.write_str_value("compliancePolicyPlatform", self.compliance_policy_platform)
        writer.write_str_value("compliancePolicyType", self.compliance_policy_type)
        writer.write_datetime_value("lastRefreshedDateTime", self.last_refreshed_date_time)
        writer.write_int_value("numberOfCompliantDevices", self.number_of_compliant_devices)
        writer.write_int_value("numberOfErrorDevices", self.number_of_error_devices)
        writer.write_int_value("numberOfNonCompliantDevices", self.number_of_non_compliant_devices)
        writer.write_datetime_value("policyModifiedDateTime", self.policy_modified_date_time)
        writer.write_str_value("tenantDisplayName", self.tenant_display_name)
        writer.write_str_value("tenantId", self.tenant_id)
    

