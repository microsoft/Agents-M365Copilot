from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .domain_registrant import DomainRegistrant
    from .entity import Entity
    from .reputation_category import ReputationCategory
    from .security_vendor_information import SecurityVendorInformation

from .entity import Entity

@dataclass
class DomainSecurityProfile(Entity, Parsable):
    # The activityGroupNames property
    activity_group_names: Optional[list[str]] = None
    # The azureSubscriptionId property
    azure_subscription_id: Optional[str] = None
    # The azureTenantId property
    azure_tenant_id: Optional[str] = None
    # The countHits property
    count_hits: Optional[int] = None
    # The countInOrg property
    count_in_org: Optional[int] = None
    # The domainCategories property
    domain_categories: Optional[list[ReputationCategory]] = None
    # The domainRegisteredDateTime property
    domain_registered_date_time: Optional[datetime.datetime] = None
    # The firstSeenDateTime property
    first_seen_date_time: Optional[datetime.datetime] = None
    # The lastSeenDateTime property
    last_seen_date_time: Optional[datetime.datetime] = None
    # The name property
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The registrant property
    registrant: Optional[DomainRegistrant] = None
    # The riskScore property
    risk_score: Optional[str] = None
    # The tags property
    tags: Optional[list[str]] = None
    # The vendorInformation property
    vendor_information: Optional[SecurityVendorInformation] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DomainSecurityProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DomainSecurityProfile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DomainSecurityProfile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .domain_registrant import DomainRegistrant
        from .entity import Entity
        from .reputation_category import ReputationCategory
        from .security_vendor_information import SecurityVendorInformation

        from .domain_registrant import DomainRegistrant
        from .entity import Entity
        from .reputation_category import ReputationCategory
        from .security_vendor_information import SecurityVendorInformation

        fields: dict[str, Callable[[Any], None]] = {
            "activityGroupNames": lambda n : setattr(self, 'activity_group_names', n.get_collection_of_primitive_values(str)),
            "azureSubscriptionId": lambda n : setattr(self, 'azure_subscription_id', n.get_str_value()),
            "azureTenantId": lambda n : setattr(self, 'azure_tenant_id', n.get_str_value()),
            "countHits": lambda n : setattr(self, 'count_hits', n.get_int_value()),
            "countInOrg": lambda n : setattr(self, 'count_in_org', n.get_int_value()),
            "domainCategories": lambda n : setattr(self, 'domain_categories', n.get_collection_of_object_values(ReputationCategory)),
            "domainRegisteredDateTime": lambda n : setattr(self, 'domain_registered_date_time', n.get_datetime_value()),
            "firstSeenDateTime": lambda n : setattr(self, 'first_seen_date_time', n.get_datetime_value()),
            "lastSeenDateTime": lambda n : setattr(self, 'last_seen_date_time', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "registrant": lambda n : setattr(self, 'registrant', n.get_object_value(DomainRegistrant)),
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
        writer.write_str_value("azureSubscriptionId", self.azure_subscription_id)
        writer.write_str_value("azureTenantId", self.azure_tenant_id)
        writer.write_int_value("countHits", self.count_hits)
        writer.write_int_value("countInOrg", self.count_in_org)
        writer.write_collection_of_object_values("domainCategories", self.domain_categories)
        writer.write_datetime_value("domainRegisteredDateTime", self.domain_registered_date_time)
        writer.write_datetime_value("firstSeenDateTime", self.first_seen_date_time)
        writer.write_datetime_value("lastSeenDateTime", self.last_seen_date_time)
        writer.write_str_value("name", self.name)
        writer.write_object_value("registrant", self.registrant)
        writer.write_str_value("riskScore", self.risk_score)
        writer.write_collection_of_primitive_values("tags", self.tags)
        writer.write_object_value("vendorInformation", self.vendor_information)
    

