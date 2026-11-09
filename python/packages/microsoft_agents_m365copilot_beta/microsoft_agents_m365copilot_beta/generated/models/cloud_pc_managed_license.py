from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_managed_license_status import CloudPcManagedLicenseStatus
    from .cloud_pc_managed_license_type import CloudPcManagedLicenseType
    from .entity import Entity

from .entity import Entity

@dataclass
class CloudPcManagedLicense(Entity, Parsable):
    # The date and time when the license becomes active. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Supports $filter (eq, ne, gt, ge, lt, le). Read-only.
    active_date_time: Optional[datetime.datetime] = None
    # The number of licenses that are allocated to assignments. The total number of allotted licenses can't be greater than the total license count. The allowed range is from 0 to the value of licensesCount. Supports $filter (eq, ne, gt, ge, lt, le). Read-only. Nullable.
    allotment_licenses_count: Optional[int] = None
    # The number of licenses currently assigned to users. The allowed range is from 0 to the value of licensesCount. Supports $filter (eq, ne, gt, ge, lt, le). Read-only.
    assigned_count: Optional[int] = None
    # The display name of the license. For example, Cloud PC Enterprise 4vCPU/16GB/256GB. Supports $filter (eq, ne, in, startsWith). Read-only.
    display_name: Optional[str] = None
    # The date and time when the license expires. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Supports $filter (eq, ne, gt, ge, lt, le). Read-only.
    expiration_date_time: Optional[datetime.datetime] = None
    # The start date of the current license term. This date is the date of the initial purchase or the most recent renewal. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Supports $filter (eq, ne, gt, ge, lt, le). Read-only.
    latest_license_start_date_time: Optional[datetime.datetime] = None
    # The licenseType property
    license_type: Optional[CloudPcManagedLicenseType] = None
    # The total number of licenses purchased. The allowed range is fropm 0 to 2,147,483,647. Supports $filter (eq, ne, gt, ge, lt, le). Read-only.
    licenses_count: Optional[int] = None
    # The date and time of the next billing cycle. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Supports $filter (eq, ne, gt, ge, lt, le). Read-only.
    next_billing_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The unique identifier for the service plan that defines the specific stock keeping unit (SKU) of the license. For example, this ID maps to a specific offering like Cloud PC Enterprise 4vCPU/16GB/256GB. For example, 3a94476b-504b-41a4-9f6a-18c5199a55e9. Supports $filter (eq). Read-only.
    service_plan_id: Optional[str] = None
    # The status property
    status: Optional[CloudPcManagedLicenseStatus] = None
    # The ID of the Azure commercial subscription to which the license belongs. This unique identifier specifies the subscription where the organization purchased and manages the license. For example, 0d5b1a2b-4d6e-4b8e-88e2-3e7a5b9d0f1a. Supports $filter (eq). Read-only.
    subscription_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcManagedLicense:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcManagedLicense
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcManagedLicense()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_managed_license_status import CloudPcManagedLicenseStatus
        from .cloud_pc_managed_license_type import CloudPcManagedLicenseType
        from .entity import Entity

        from .cloud_pc_managed_license_status import CloudPcManagedLicenseStatus
        from .cloud_pc_managed_license_type import CloudPcManagedLicenseType
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "activeDateTime": lambda n : setattr(self, 'active_date_time', n.get_datetime_value()),
            "allotmentLicensesCount": lambda n : setattr(self, 'allotment_licenses_count', n.get_int_value()),
            "assignedCount": lambda n : setattr(self, 'assigned_count', n.get_int_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "latestLicenseStartDateTime": lambda n : setattr(self, 'latest_license_start_date_time', n.get_datetime_value()),
            "licenseType": lambda n : setattr(self, 'license_type', n.get_enum_value(CloudPcManagedLicenseType)),
            "licensesCount": lambda n : setattr(self, 'licenses_count', n.get_int_value()),
            "nextBillingDateTime": lambda n : setattr(self, 'next_billing_date_time', n.get_datetime_value()),
            "servicePlanId": lambda n : setattr(self, 'service_plan_id', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(CloudPcManagedLicenseStatus)),
            "subscriptionId": lambda n : setattr(self, 'subscription_id', n.get_str_value()),
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
        writer.write_datetime_value("activeDateTime", self.active_date_time)
        writer.write_int_value("allotmentLicensesCount", self.allotment_licenses_count)
        writer.write_int_value("assignedCount", self.assigned_count)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_datetime_value("latestLicenseStartDateTime", self.latest_license_start_date_time)
        writer.write_enum_value("licenseType", self.license_type)
        writer.write_int_value("licensesCount", self.licenses_count)
        writer.write_datetime_value("nextBillingDateTime", self.next_billing_date_time)
        writer.write_str_value("servicePlanId", self.service_plan_id)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("subscriptionId", self.subscription_id)
    

