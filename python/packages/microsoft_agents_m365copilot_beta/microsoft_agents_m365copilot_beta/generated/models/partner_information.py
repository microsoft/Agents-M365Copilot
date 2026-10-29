from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .partner_tenant_type import PartnerTenantType

@dataclass
class PartnerInformation(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The commerceUrl property
    commerce_url: Optional[str] = None
    # The companyName property
    company_name: Optional[str] = None
    # The companyType property
    company_type: Optional[PartnerTenantType] = None
    # The helpUrl property
    help_url: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The partnerTenantId property
    partner_tenant_id: Optional[str] = None
    # The supportEmails property
    support_emails: Optional[list[str]] = None
    # The supportTelephones property
    support_telephones: Optional[list[str]] = None
    # The supportUrl property
    support_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PartnerInformation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PartnerInformation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PartnerInformation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .partner_tenant_type import PartnerTenantType

        from .partner_tenant_type import PartnerTenantType

        fields: dict[str, Callable[[Any], None]] = {
            "commerceUrl": lambda n : setattr(self, 'commerce_url', n.get_str_value()),
            "companyName": lambda n : setattr(self, 'company_name', n.get_str_value()),
            "companyType": lambda n : setattr(self, 'company_type', n.get_enum_value(PartnerTenantType)),
            "helpUrl": lambda n : setattr(self, 'help_url', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "partnerTenantId": lambda n : setattr(self, 'partner_tenant_id', n.get_str_value()),
            "supportEmails": lambda n : setattr(self, 'support_emails', n.get_collection_of_primitive_values(str)),
            "supportTelephones": lambda n : setattr(self, 'support_telephones', n.get_collection_of_primitive_values(str)),
            "supportUrl": lambda n : setattr(self, 'support_url', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("commerceUrl", self.commerce_url)
        writer.write_str_value("companyName", self.company_name)
        writer.write_enum_value("companyType", self.company_type)
        writer.write_str_value("helpUrl", self.help_url)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("partnerTenantId", self.partner_tenant_id)
        writer.write_collection_of_primitive_values("supportEmails", self.support_emails)
        writer.write_collection_of_primitive_values("supportTelephones", self.support_telephones)
        writer.write_str_value("supportUrl", self.support_url)
        writer.write_additional_data_value(self.additional_data)
    

