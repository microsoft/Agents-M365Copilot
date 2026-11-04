from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .tenant_contact_information import TenantContactInformation

from ..entity import Entity

@dataclass
class TenantCustomizedInformation(Entity, Parsable):
    # Describes the relationship between the Managed Services Provider and the managed tenant; for example, Managed, Co-managed, Licensing. The maximum length is 250 characters. Optional.
    business_relationship: Optional[str] = None
    # Contains the compliance requirements for the customer tenant; for example, HIPPA, NIST, CMMC. The maximum length is 250 characters per compliance requirement. Optional.
    compliance_requirements: Optional[list[str]] = None
    # The collection of contacts for the managed tenant. Optional.
    contacts: Optional[list[TenantContactInformation]] = None
    # The display name for the managed tenant. Required. Read-only.
    display_name: Optional[str] = None
    # This is the Managed Services Plans for the customer tenant that the Managed Services Provider manages. The maximum length is 250 characters per managed service plan. Optional.
    managed_services_plans: Optional[list[str]] = None
    # A field for the Managed Services Provider technician to input custom text to share notes between technicians within the Managed Service Providers. The maximum length is 5000 characters. Optional.
    note: Optional[str] = None
    # The date on which the note field of this entity was last modified. Optional.
    note_last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The list of Entra user IDs for users in the Managed Services Provider that manage the relationship with the managed tenant. Optional.
    partner_relationship_manager_user_ids: Optional[list[str]] = None
    # The Microsoft Entra tenant identifier for the managed tenant. Optional. Read-only.
    tenant_id: Optional[str] = None
    # The website for the managed tenant. Required.
    website: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TenantCustomizedInformation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TenantCustomizedInformation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TenantCustomizedInformation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .tenant_contact_information import TenantContactInformation

        from ..entity import Entity
        from .tenant_contact_information import TenantContactInformation

        fields: dict[str, Callable[[Any], None]] = {
            "businessRelationship": lambda n : setattr(self, 'business_relationship', n.get_str_value()),
            "complianceRequirements": lambda n : setattr(self, 'compliance_requirements', n.get_collection_of_primitive_values(str)),
            "contacts": lambda n : setattr(self, 'contacts', n.get_collection_of_object_values(TenantContactInformation)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "managedServicesPlans": lambda n : setattr(self, 'managed_services_plans', n.get_collection_of_primitive_values(str)),
            "note": lambda n : setattr(self, 'note', n.get_str_value()),
            "noteLastModifiedDateTime": lambda n : setattr(self, 'note_last_modified_date_time', n.get_datetime_value()),
            "partnerRelationshipManagerUserIds": lambda n : setattr(self, 'partner_relationship_manager_user_ids', n.get_collection_of_primitive_values(str)),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "website": lambda n : setattr(self, 'website', n.get_str_value()),
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
        writer.write_str_value("businessRelationship", self.business_relationship)
        writer.write_collection_of_primitive_values("complianceRequirements", self.compliance_requirements)
        writer.write_collection_of_object_values("contacts", self.contacts)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_primitive_values("managedServicesPlans", self.managed_services_plans)
        writer.write_str_value("note", self.note)
        writer.write_datetime_value("noteLastModifiedDateTime", self.note_last_modified_date_time)
        writer.write_collection_of_primitive_values("partnerRelationshipManagerUserIds", self.partner_relationship_manager_user_ids)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_str_value("website", self.website)
    

