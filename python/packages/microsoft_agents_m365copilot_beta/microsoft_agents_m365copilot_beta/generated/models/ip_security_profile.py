from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .ip_category import IpCategory
    from .ip_reference_data import IpReferenceData
    from .security_vendor_information import SecurityVendorInformation

from .entity import Entity

@dataclass
class IpSecurityProfile(Entity, Parsable):
    # The activityGroupNames property
    activity_group_names: Optional[list[str]] = None
    # The address property
    address: Optional[str] = None
    # The azureSubscriptionId property
    azure_subscription_id: Optional[str] = None
    # The azureTenantId property
    azure_tenant_id: Optional[str] = None
    # The countHits property
    count_hits: Optional[int] = None
    # The countHosts property
    count_hosts: Optional[int] = None
    # The firstSeenDateTime property
    first_seen_date_time: Optional[datetime.datetime] = None
    # The ipCategories property
    ip_categories: Optional[list[IpCategory]] = None
    # The ipReferenceData property
    ip_reference_data: Optional[list[IpReferenceData]] = None
    # The lastSeenDateTime property
    last_seen_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The riskScore property
    risk_score: Optional[str] = None
    # The tags property
    tags: Optional[list[str]] = None
    # The vendorInformation property
    vendor_information: Optional[SecurityVendorInformation] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IpSecurityProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IpSecurityProfile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IpSecurityProfile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .ip_category import IpCategory
        from .ip_reference_data import IpReferenceData
        from .security_vendor_information import SecurityVendorInformation

        from .entity import Entity
        from .ip_category import IpCategory
        from .ip_reference_data import IpReferenceData
        from .security_vendor_information import SecurityVendorInformation

        fields: dict[str, Callable[[Any], None]] = {
            "activityGroupNames": lambda n : setattr(self, 'activity_group_names', n.get_collection_of_primitive_values(str)),
            "address": lambda n : setattr(self, 'address', n.get_str_value()),
            "azureSubscriptionId": lambda n : setattr(self, 'azure_subscription_id', n.get_str_value()),
            "azureTenantId": lambda n : setattr(self, 'azure_tenant_id', n.get_str_value()),
            "countHits": lambda n : setattr(self, 'count_hits', n.get_int_value()),
            "countHosts": lambda n : setattr(self, 'count_hosts', n.get_int_value()),
            "firstSeenDateTime": lambda n : setattr(self, 'first_seen_date_time', n.get_datetime_value()),
            "ipCategories": lambda n : setattr(self, 'ip_categories', n.get_collection_of_object_values(IpCategory)),
            "ipReferenceData": lambda n : setattr(self, 'ip_reference_data', n.get_collection_of_object_values(IpReferenceData)),
            "lastSeenDateTime": lambda n : setattr(self, 'last_seen_date_time', n.get_datetime_value()),
            "riskScore": lambda n : setattr(self, 'risk_score', n.get_str_value()),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_primitive_values(str)),
            "vendorInformation": lambda n : setattr(self, 'vendor_information', n.get_object_value(SecurityVendorInformation)),
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
        writer.write_collection_of_primitive_values("activityGroupNames", self.activity_group_names)
        writer.write_str_value("address", self.address)
        writer.write_str_value("azureSubscriptionId", self.azure_subscription_id)
        writer.write_str_value("azureTenantId", self.azure_tenant_id)
        writer.write_int_value("countHits", self.count_hits)
        writer.write_int_value("countHosts", self.count_hosts)
        writer.write_datetime_value("firstSeenDateTime", self.first_seen_date_time)
        writer.write_collection_of_object_values("ipCategories", self.ip_categories)
        writer.write_collection_of_object_values("ipReferenceData", self.ip_reference_data)
        writer.write_datetime_value("lastSeenDateTime", self.last_seen_date_time)
        writer.write_str_value("riskScore", self.risk_score)
        writer.write_collection_of_primitive_values("tags", self.tags)
        writer.write_object_value("vendorInformation", self.vendor_information)
    

