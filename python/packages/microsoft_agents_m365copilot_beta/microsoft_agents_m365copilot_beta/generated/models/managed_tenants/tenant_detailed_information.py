from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity

from ..entity import Entity

@dataclass
class TenantDetailedInformation(Entity, Parsable):
    # The city where the managed tenant is located. Optional. Read-only.
    city: Optional[str] = None
    # The code for the country where the managed tenant is located. Optional. Read-only.
    country_code: Optional[str] = None
    # The name for the country where the managed tenant is located. Optional. Read-only.
    country_name: Optional[str] = None
    # The default domain name for the managed tenant. Optional. Read-only.
    default_domain_name: Optional[str] = None
    # The display name for the managed tenant.
    display_name: Optional[str] = None
    # The business industry associated with the managed tenant. Optional. Read-only.
    industry_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The region where the managed tenant is located. Optional. Read-only.
    region: Optional[str] = None
    # The business segment associated with the managed tenant. Optional. Read-only.
    segment_name: Optional[str] = None
    # The Microsoft Entra tenant identifier for the managed tenant.
    tenant_id: Optional[str] = None
    # The vertical associated with the managed tenant. Optional. Read-only.
    vertical_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TenantDetailedInformation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TenantDetailedInformation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TenantDetailedInformation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity

        from ..entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "city": lambda n : setattr(self, 'city', n.get_str_value()),
            "countryCode": lambda n : setattr(self, 'country_code', n.get_str_value()),
            "countryName": lambda n : setattr(self, 'country_name', n.get_str_value()),
            "defaultDomainName": lambda n : setattr(self, 'default_domain_name', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "industryName": lambda n : setattr(self, 'industry_name', n.get_str_value()),
            "region": lambda n : setattr(self, 'region', n.get_str_value()),
            "segmentName": lambda n : setattr(self, 'segment_name', n.get_str_value()),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "verticalName": lambda n : setattr(self, 'vertical_name', n.get_str_value()),
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
        writer.write_str_value("city", self.city)
        writer.write_str_value("countryCode", self.country_code)
        writer.write_str_value("countryName", self.country_name)
        writer.write_str_value("defaultDomainName", self.default_domain_name)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("industryName", self.industry_name)
        writer.write_str_value("region", self.region)
        writer.write_str_value("segmentName", self.segment_name)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_str_value("verticalName", self.vertical_name)
    

