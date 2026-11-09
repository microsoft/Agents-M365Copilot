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
class ManagementTemplateCollectionTenantSummary(Entity, Parsable):
    # The completeStepsCount property
    complete_steps_count: Optional[int] = None
    # The completeUsersCount property
    complete_users_count: Optional[int] = None
    # The createdByUserId property
    created_by_user_id: Optional[str] = None
    # The createdDateTime property
    created_date_time: Optional[datetime.datetime] = None
    # The dismissedStepsCount property
    dismissed_steps_count: Optional[int] = None
    # The excludedUsersCount property
    excluded_users_count: Optional[int] = None
    # The excludedUsersDistinctCount property
    excluded_users_distinct_count: Optional[int] = None
    # The incompleteStepsCount property
    incomplete_steps_count: Optional[int] = None
    # The incompleteUsersCount property
    incomplete_users_count: Optional[int] = None
    # The ineligibleStepsCount property
    ineligible_steps_count: Optional[int] = None
    # The isComplete property
    is_complete: Optional[bool] = None
    # The lastActionByUserId property
    last_action_by_user_id: Optional[str] = None
    # The lastActionDateTime property
    last_action_date_time: Optional[datetime.datetime] = None
    # The managementTemplateCollectionDisplayName property
    management_template_collection_display_name: Optional[str] = None
    # The managementTemplateCollectionId property
    management_template_collection_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The regressedStepsCount property
    regressed_steps_count: Optional[int] = None
    # The regressedUsersCount property
    regressed_users_count: Optional[int] = None
    # The tenantId property
    tenant_id: Optional[str] = None
    # The unlicensedUsersCount property
    unlicensed_users_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ManagementTemplateCollectionTenantSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManagementTemplateCollectionTenantSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ManagementTemplateCollectionTenantSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity

        from ..entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "completeStepsCount": lambda n : setattr(self, 'complete_steps_count', n.get_int_value()),
            "completeUsersCount": lambda n : setattr(self, 'complete_users_count', n.get_int_value()),
            "createdByUserId": lambda n : setattr(self, 'created_by_user_id', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "dismissedStepsCount": lambda n : setattr(self, 'dismissed_steps_count', n.get_int_value()),
            "excludedUsersCount": lambda n : setattr(self, 'excluded_users_count', n.get_int_value()),
            "excludedUsersDistinctCount": lambda n : setattr(self, 'excluded_users_distinct_count', n.get_int_value()),
            "incompleteStepsCount": lambda n : setattr(self, 'incomplete_steps_count', n.get_int_value()),
            "incompleteUsersCount": lambda n : setattr(self, 'incomplete_users_count', n.get_int_value()),
            "ineligibleStepsCount": lambda n : setattr(self, 'ineligible_steps_count', n.get_int_value()),
            "isComplete": lambda n : setattr(self, 'is_complete', n.get_bool_value()),
            "lastActionByUserId": lambda n : setattr(self, 'last_action_by_user_id', n.get_str_value()),
            "lastActionDateTime": lambda n : setattr(self, 'last_action_date_time', n.get_datetime_value()),
            "managementTemplateCollectionDisplayName": lambda n : setattr(self, 'management_template_collection_display_name', n.get_str_value()),
            "managementTemplateCollectionId": lambda n : setattr(self, 'management_template_collection_id', n.get_str_value()),
            "regressedStepsCount": lambda n : setattr(self, 'regressed_steps_count', n.get_int_value()),
            "regressedUsersCount": lambda n : setattr(self, 'regressed_users_count', n.get_int_value()),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "unlicensedUsersCount": lambda n : setattr(self, 'unlicensed_users_count', n.get_int_value()),
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
        writer.write_int_value("completeStepsCount", self.complete_steps_count)
        writer.write_int_value("completeUsersCount", self.complete_users_count)
        writer.write_str_value("createdByUserId", self.created_by_user_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_int_value("dismissedStepsCount", self.dismissed_steps_count)
        writer.write_int_value("excludedUsersCount", self.excluded_users_count)
        writer.write_int_value("excludedUsersDistinctCount", self.excluded_users_distinct_count)
        writer.write_int_value("incompleteStepsCount", self.incomplete_steps_count)
        writer.write_int_value("incompleteUsersCount", self.incomplete_users_count)
        writer.write_int_value("ineligibleStepsCount", self.ineligible_steps_count)
        writer.write_bool_value("isComplete", self.is_complete)
        writer.write_str_value("lastActionByUserId", self.last_action_by_user_id)
        writer.write_datetime_value("lastActionDateTime", self.last_action_date_time)
        writer.write_str_value("managementTemplateCollectionDisplayName", self.management_template_collection_display_name)
        writer.write_str_value("managementTemplateCollectionId", self.management_template_collection_id)
        writer.write_int_value("regressedStepsCount", self.regressed_steps_count)
        writer.write_int_value("regressedUsersCount", self.regressed_users_count)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_int_value("unlicensedUsersCount", self.unlicensed_users_count)
    

