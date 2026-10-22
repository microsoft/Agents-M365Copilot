from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .all_users_spending_policy import AllUsersSpendingPolicy
    from .cost_management_alert_setting import CostManagementAlertSetting
    from .cost_management_billing_methods import CostManagementBillingMethods
    from .cost_management_quantity import CostManagementQuantity
    from .entity import Entity
    from .identity_set import IdentitySet
    from .selected_groups_spending_policy import SelectedGroupsSpendingPolicy
    from .spending_policy_service_setting import SpendingPolicyServiceSetting
    from .spending_policy_status import SpendingPolicyStatus

from .entity import Entity

@dataclass
class SpendingPolicy(Entity, Parsable):
    """
    A policy that governs Copilot Credits consumption for an audience. Every policy is one ofits derived types, identified by @odata.type on create.
    """
    # How Copilot consumption is billed when more than one method may apply. This is a flags enum,so combined values such as prepaidCredits,payAsYouGo are valid.
    billing_methods: Optional[CostManagementBillingMethods] = None
    # The createdBy property
    created_by: Optional[IdentitySet] = None
    # When the policy was created. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    # The policy display name. Must be 10-64 characters, letters, digits, and spaces only.
    display_name: Optional[str] = None
    # Notify-only email threshold configuration for the policy. Alerts are delivered by emailonly. Addressed beneath the policy rather than returned inline in the policy response.
    email_threshold_settings: Optional[CostManagementAlertSetting] = None
    # The lastModifiedBy property
    last_modified_by: Optional[IdentitySet] = None
    # When the policy was last modified. Read-only.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A unit-bearing quantity that is either limited to a value or unlimited. Every quantity isone of its derived types, identified by @odata.type on create.
    per_user_limit: Optional[CostManagementQuantity] = None
    # A unit-bearing quantity that is either limited to a value or unlimited. Every quantity isone of its derived types, identified by @odata.type on create.
    period_limit: Optional[CostManagementQuantity] = None
    # Per-service settings contained by the policy. Add a service with POST; remove one bysetting its state to disabled, which retains the entry in that state.
    service_settings: Optional[list[SpendingPolicyServiceSetting]] = None
    # Lifecycle status of a spending policy.
    status: Optional[SpendingPolicyStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SpendingPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SpendingPolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.allUsersSpendingPolicy".casefold():
            from .all_users_spending_policy import AllUsersSpendingPolicy

            return AllUsersSpendingPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.selectedGroupsSpendingPolicy".casefold():
            from .selected_groups_spending_policy import SelectedGroupsSpendingPolicy

            return SelectedGroupsSpendingPolicy()
        return SpendingPolicy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .all_users_spending_policy import AllUsersSpendingPolicy
        from .cost_management_alert_setting import CostManagementAlertSetting
        from .cost_management_billing_methods import CostManagementBillingMethods
        from .cost_management_quantity import CostManagementQuantity
        from .entity import Entity
        from .identity_set import IdentitySet
        from .selected_groups_spending_policy import SelectedGroupsSpendingPolicy
        from .spending_policy_service_setting import SpendingPolicyServiceSetting
        from .spending_policy_status import SpendingPolicyStatus

        from .all_users_spending_policy import AllUsersSpendingPolicy
        from .cost_management_alert_setting import CostManagementAlertSetting
        from .cost_management_billing_methods import CostManagementBillingMethods
        from .cost_management_quantity import CostManagementQuantity
        from .entity import Entity
        from .identity_set import IdentitySet
        from .selected_groups_spending_policy import SelectedGroupsSpendingPolicy
        from .spending_policy_service_setting import SpendingPolicyServiceSetting
        from .spending_policy_status import SpendingPolicyStatus

        fields: dict[str, Callable[[Any], None]] = {
            "billingMethods": lambda n : setattr(self, 'billing_methods', n.get_collection_of_enum_values(CostManagementBillingMethods)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "emailThresholdSettings": lambda n : setattr(self, 'email_threshold_settings', n.get_object_value(CostManagementAlertSetting)),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "perUserLimit": lambda n : setattr(self, 'per_user_limit', n.get_object_value(CostManagementQuantity)),
            "periodLimit": lambda n : setattr(self, 'period_limit', n.get_object_value(CostManagementQuantity)),
            "serviceSettings": lambda n : setattr(self, 'service_settings', n.get_collection_of_object_values(SpendingPolicyServiceSetting)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(SpendingPolicyStatus)),
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
        writer.write_enum_value("billingMethods", self.billing_methods)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("emailThresholdSettings", self.email_threshold_settings)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_object_value("perUserLimit", self.per_user_limit)
        writer.write_object_value("periodLimit", self.period_limit)
        writer.write_collection_of_object_values("serviceSettings", self.service_settings)
        writer.write_enum_value("status", self.status)
    

