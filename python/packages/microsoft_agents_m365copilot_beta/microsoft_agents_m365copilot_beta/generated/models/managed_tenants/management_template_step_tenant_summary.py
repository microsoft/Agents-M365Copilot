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
class ManagementTemplateStepTenantSummary(Entity, Parsable):
    # The assignedTenantsCount property
    assigned_tenants_count: Optional[int] = None
    # The compliantTenantsCount property
    compliant_tenants_count: Optional[int] = None
    # The createdByUserId property
    created_by_user_id: Optional[str] = None
    # The createdDateTime property
    created_date_time: Optional[datetime.datetime] = None
    # The dismissedTenantsCount property
    dismissed_tenants_count: Optional[int] = None
    # The ineligibleTenantsCount property
    ineligible_tenants_count: Optional[int] = None
    # The lastActionByUserId property
    last_action_by_user_id: Optional[str] = None
    # The lastActionDateTime property
    last_action_date_time: Optional[datetime.datetime] = None
    # The managementTemplateCollectionDisplayName property
    management_template_collection_display_name: Optional[str] = None
    # The managementTemplateCollectionId property
    management_template_collection_id: Optional[str] = None
    # The managementTemplateDisplayName property
    management_template_display_name: Optional[str] = None
    # The managementTemplateId property
    management_template_id: Optional[str] = None
    # The managementTemplateStepDisplayName property
    management_template_step_display_name: Optional[str] = None
    # The managementTemplateStepId property
    management_template_step_id: Optional[str] = None
    # The notCompliantTenantsCount property
    not_compliant_tenants_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ManagementTemplateStepTenantSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManagementTemplateStepTenantSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ManagementTemplateStepTenantSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity

        from ..entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "assignedTenantsCount": lambda n : setattr(self, 'assigned_tenants_count', n.get_int_value()),
            "compliantTenantsCount": lambda n : setattr(self, 'compliant_tenants_count', n.get_int_value()),
            "createdByUserId": lambda n : setattr(self, 'created_by_user_id', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "dismissedTenantsCount": lambda n : setattr(self, 'dismissed_tenants_count', n.get_int_value()),
            "ineligibleTenantsCount": lambda n : setattr(self, 'ineligible_tenants_count', n.get_int_value()),
            "lastActionByUserId": lambda n : setattr(self, 'last_action_by_user_id', n.get_str_value()),
            "lastActionDateTime": lambda n : setattr(self, 'last_action_date_time', n.get_datetime_value()),
            "managementTemplateCollectionDisplayName": lambda n : setattr(self, 'management_template_collection_display_name', n.get_str_value()),
            "managementTemplateCollectionId": lambda n : setattr(self, 'management_template_collection_id', n.get_str_value()),
            "managementTemplateDisplayName": lambda n : setattr(self, 'management_template_display_name', n.get_str_value()),
            "managementTemplateId": lambda n : setattr(self, 'management_template_id', n.get_str_value()),
            "managementTemplateStepDisplayName": lambda n : setattr(self, 'management_template_step_display_name', n.get_str_value()),
            "managementTemplateStepId": lambda n : setattr(self, 'management_template_step_id', n.get_str_value()),
            "notCompliantTenantsCount": lambda n : setattr(self, 'not_compliant_tenants_count', n.get_int_value()),
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
        writer.write_int_value("assignedTenantsCount", self.assigned_tenants_count)
        writer.write_int_value("compliantTenantsCount", self.compliant_tenants_count)
        writer.write_str_value("createdByUserId", self.created_by_user_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_int_value("dismissedTenantsCount", self.dismissed_tenants_count)
        writer.write_int_value("ineligibleTenantsCount", self.ineligible_tenants_count)
        writer.write_str_value("lastActionByUserId", self.last_action_by_user_id)
        writer.write_datetime_value("lastActionDateTime", self.last_action_date_time)
        writer.write_str_value("managementTemplateCollectionDisplayName", self.management_template_collection_display_name)
        writer.write_str_value("managementTemplateCollectionId", self.management_template_collection_id)
        writer.write_str_value("managementTemplateDisplayName", self.management_template_display_name)
        writer.write_str_value("managementTemplateId", self.management_template_id)
        writer.write_str_value("managementTemplateStepDisplayName", self.management_template_step_display_name)
        writer.write_str_value("managementTemplateStepId", self.management_template_step_id)
        writer.write_int_value("notCompliantTenantsCount", self.not_compliant_tenants_count)
    

