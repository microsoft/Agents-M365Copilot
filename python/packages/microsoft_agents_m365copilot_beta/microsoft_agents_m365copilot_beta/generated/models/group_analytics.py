from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .group_type_enum import GroupTypeEnum

from .entity import Entity

@dataclass
class GroupAnalytics(Entity, Parsable):
    # The number of directory roles assigned to the group. Supports $filter (eq, ne, gt, ge, lt, le) and $orderby.
    assigned_role_count: Optional[int] = None
    # The date and time when the analytics for the group were last calculated. The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Supports $filter (eq, ne, gt, ge, lt, le) and $orderby.
    calculated_date_time: Optional[datetime.datetime] = None
    # The date and time when the group was created. The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Supports $filter (eq, ne, gt, ge, lt, le) and $orderby.
    created_date_time: Optional[datetime.datetime] = None
    # The number of direct members of the group that are themselves groups. Supports $filter (eq, ne, gt, ge, lt, le) and $orderby.
    direct_group_member_count: Optional[int] = None
    # The display name of the group. Supports $filter (eq, ne, startsWith, endsWith, contains) and $orderby.
    display_name: Optional[str] = None
    # The dynamic membership classification of the group, derived from its membership rule. Supports $filter (eq, ne, startsWith, endsWith, contains) and $orderby.
    dynamic_membership_type: Optional[str] = None
    # The date and time when the group expires. The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Supports $filter (eq, ne, gt, ge, lt, le) and $orderby.
    group_expiration_date_time: Optional[datetime.datetime] = None
    # The groupType property
    group_type: Optional[GroupTypeEnum] = None
    # The number of owners of the group that are guest users. Supports $filter (eq, ne, gt, ge, lt, le) and $orderby.
    guest_owner_count: Optional[int] = None
    # The number of transitive user members of the group that are guest users. Supports $filter (eq, ne, gt, ge, lt, le) and $orderby.
    guest_transitive_user_count: Optional[int] = None
    # Indicates whether the group is a non-soft-deleted cloud distribution list group. Supports $filter (eq, ne) and $orderby.
    is_cloud_distribution_list_group: Optional[bool] = None
    # Indicates whether the group is a non-soft-deleted cloud Microsoft 365 group. Supports $filter (eq, ne) and $orderby.
    is_cloud_m365_group: Optional[bool] = None
    # Indicates whether the group is a non-soft-deleted cloud mail-enabled security group. Supports $filter (eq, ne) and $orderby.
    is_cloud_mail_enabled_security_group: Optional[bool] = None
    # Indicates whether the group is a non-soft-deleted cloud security group. Supports $filter (eq, ne) and $orderby.
    is_cloud_security_group: Optional[bool] = None
    # Indicates whether the group is a dynamic group. Supports $filter (eq, ne) and $orderby.
    is_dynamic_group: Optional[bool] = None
    # Indicates whether the group is a non-soft-deleted on-premises distribution list group. Supports $filter (eq, ne) and $orderby.
    is_on_premise_distribution_list_group: Optional[bool] = None
    # Indicates whether the group is a non-soft-deleted on-premises mail-enabled security group. Supports $filter (eq, ne) and $orderby.
    is_on_premise_mail_enabled_security_group: Optional[bool] = None
    # Indicates whether the group is a non-soft-deleted on-premises security group. Supports $filter (eq, ne) and $orderby.
    is_on_premise_security_group: Optional[bool] = None
    # Indicates whether the group is a valid (non-soft-deleted) group. Supports $filter (eq, ne) and $orderby.
    is_valid_group: Optional[bool] = None
    # The date and time when the group was last restored from a soft-deleted state. The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Supports $filter (eq, ne, gt, ge, lt, le) and $orderby.
    last_restoration_date_time: Optional[datetime.datetime] = None
    # The number of owners of the group that are member (non-guest) users. Supports $filter (eq, ne, gt, ge, lt, le) and $orderby.
    member_owner_count: Optional[int] = None
    # The number of transitive user members of the group that are member (non-guest) users. Supports $filter (eq, ne, gt, ge, lt, le) and $orderby.
    member_transitive_user_count: Optional[int] = None
    # The number of contains expressions in the membership rule of the group. Supports $filter (eq, ne, gt, ge, lt, le) and $orderby.
    membership_rule_contains_count: Optional[int] = None
    # The number of expressions in the membership rule of the group. Supports $filter (eq, ne, gt, ge, lt, le) and $orderby.
    membership_rule_expression_count: Optional[int] = None
    # The number of match expressions in the membership rule of the group. Supports $filter (eq, ne, gt, ge, lt, le) and $orderby.
    membership_rule_match_count: Optional[int] = None
    # The number of memberOf expressions in the membership rule of the group. Supports $filter (eq, ne, gt, ge, lt, le) and $orderby.
    membership_rule_member_of_count: Optional[int] = None
    # The processing state of the membership rule of the group. Supports $filter (eq, ne, startsWith, endsWith, contains) and $orderby.
    membership_rule_processing_state: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The preferred data location of the group. Supports $filter (eq, ne, startsWith, endsWith, contains) and $orderby.
    preferred_data_location: Optional[str] = None
    # The number of sensitivity labels applied to the group. Supports $filter (eq, ne, gt, ge, lt, le) and $orderby.
    sensitivity_label_count: Optional[int] = None
    # The number of owners of the group that are service principals. Supports $filter (eq, ne, gt, ge, lt, le) and $orderby.
    service_principal_owner_count: Optional[int] = None
    # The date and time when the group was soft-deleted. If this property is empty, the group isn't soft-deleted. The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Supports $filter (eq, ne, gt, ge, lt, le) and $orderby.
    soft_deletion_date_time: Optional[datetime.datetime] = None
    # The unique identifier of the tenant that the group belongs to. Supports $filter (eq, ne) and $orderby.
    tenant_id: Optional[str] = None
    # The number of transitive members of the group that are service principals. Supports $filter (eq, ne, gt, ge, lt, le) and $orderby.
    transitive_service_principal_count: Optional[int] = None
    # The total number of transitive user members of the group. Supports $filter (eq, ne, gt, ge, lt, le) and $orderby.
    transitive_user_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GroupAnalytics:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GroupAnalytics
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GroupAnalytics()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .group_type_enum import GroupTypeEnum

        from .entity import Entity
        from .group_type_enum import GroupTypeEnum

        fields: dict[str, Callable[[Any], None]] = {
            "assignedRoleCount": lambda n : setattr(self, 'assigned_role_count', n.get_int_value()),
            "calculatedDateTime": lambda n : setattr(self, 'calculated_date_time', n.get_datetime_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "directGroupMemberCount": lambda n : setattr(self, 'direct_group_member_count', n.get_int_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "dynamicMembershipType": lambda n : setattr(self, 'dynamic_membership_type', n.get_str_value()),
            "groupExpirationDateTime": lambda n : setattr(self, 'group_expiration_date_time', n.get_datetime_value()),
            "groupType": lambda n : setattr(self, 'group_type', n.get_enum_value(GroupTypeEnum)),
            "guestOwnerCount": lambda n : setattr(self, 'guest_owner_count', n.get_int_value()),
            "guestTransitiveUserCount": lambda n : setattr(self, 'guest_transitive_user_count', n.get_int_value()),
            "isCloudDistributionListGroup": lambda n : setattr(self, 'is_cloud_distribution_list_group', n.get_bool_value()),
            "isCloudM365Group": lambda n : setattr(self, 'is_cloud_m365_group', n.get_bool_value()),
            "isCloudMailEnabledSecurityGroup": lambda n : setattr(self, 'is_cloud_mail_enabled_security_group', n.get_bool_value()),
            "isCloudSecurityGroup": lambda n : setattr(self, 'is_cloud_security_group', n.get_bool_value()),
            "isDynamicGroup": lambda n : setattr(self, 'is_dynamic_group', n.get_bool_value()),
            "isOnPremiseDistributionListGroup": lambda n : setattr(self, 'is_on_premise_distribution_list_group', n.get_bool_value()),
            "isOnPremiseMailEnabledSecurityGroup": lambda n : setattr(self, 'is_on_premise_mail_enabled_security_group', n.get_bool_value()),
            "isOnPremiseSecurityGroup": lambda n : setattr(self, 'is_on_premise_security_group', n.get_bool_value()),
            "isValidGroup": lambda n : setattr(self, 'is_valid_group', n.get_bool_value()),
            "lastRestorationDateTime": lambda n : setattr(self, 'last_restoration_date_time', n.get_datetime_value()),
            "memberOwnerCount": lambda n : setattr(self, 'member_owner_count', n.get_int_value()),
            "memberTransitiveUserCount": lambda n : setattr(self, 'member_transitive_user_count', n.get_int_value()),
            "membershipRuleContainsCount": lambda n : setattr(self, 'membership_rule_contains_count', n.get_int_value()),
            "membershipRuleExpressionCount": lambda n : setattr(self, 'membership_rule_expression_count', n.get_int_value()),
            "membershipRuleMatchCount": lambda n : setattr(self, 'membership_rule_match_count', n.get_int_value()),
            "membershipRuleMemberOfCount": lambda n : setattr(self, 'membership_rule_member_of_count', n.get_int_value()),
            "membershipRuleProcessingState": lambda n : setattr(self, 'membership_rule_processing_state', n.get_str_value()),
            "preferredDataLocation": lambda n : setattr(self, 'preferred_data_location', n.get_str_value()),
            "sensitivityLabelCount": lambda n : setattr(self, 'sensitivity_label_count', n.get_int_value()),
            "servicePrincipalOwnerCount": lambda n : setattr(self, 'service_principal_owner_count', n.get_int_value()),
            "softDeletionDateTime": lambda n : setattr(self, 'soft_deletion_date_time', n.get_datetime_value()),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "transitiveServicePrincipalCount": lambda n : setattr(self, 'transitive_service_principal_count', n.get_int_value()),
            "transitiveUserCount": lambda n : setattr(self, 'transitive_user_count', n.get_int_value()),
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
        writer.write_int_value("assignedRoleCount", self.assigned_role_count)
        writer.write_datetime_value("calculatedDateTime", self.calculated_date_time)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_int_value("directGroupMemberCount", self.direct_group_member_count)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("dynamicMembershipType", self.dynamic_membership_type)
        writer.write_datetime_value("groupExpirationDateTime", self.group_expiration_date_time)
        writer.write_enum_value("groupType", self.group_type)
        writer.write_int_value("guestOwnerCount", self.guest_owner_count)
        writer.write_int_value("guestTransitiveUserCount", self.guest_transitive_user_count)
        writer.write_bool_value("isCloudDistributionListGroup", self.is_cloud_distribution_list_group)
        writer.write_bool_value("isCloudM365Group", self.is_cloud_m365_group)
        writer.write_bool_value("isCloudMailEnabledSecurityGroup", self.is_cloud_mail_enabled_security_group)
        writer.write_bool_value("isCloudSecurityGroup", self.is_cloud_security_group)
        writer.write_bool_value("isDynamicGroup", self.is_dynamic_group)
        writer.write_bool_value("isOnPremiseDistributionListGroup", self.is_on_premise_distribution_list_group)
        writer.write_bool_value("isOnPremiseMailEnabledSecurityGroup", self.is_on_premise_mail_enabled_security_group)
        writer.write_bool_value("isOnPremiseSecurityGroup", self.is_on_premise_security_group)
        writer.write_bool_value("isValidGroup", self.is_valid_group)
        writer.write_datetime_value("lastRestorationDateTime", self.last_restoration_date_time)
        writer.write_int_value("memberOwnerCount", self.member_owner_count)
        writer.write_int_value("memberTransitiveUserCount", self.member_transitive_user_count)
        writer.write_int_value("membershipRuleContainsCount", self.membership_rule_contains_count)
        writer.write_int_value("membershipRuleExpressionCount", self.membership_rule_expression_count)
        writer.write_int_value("membershipRuleMatchCount", self.membership_rule_match_count)
        writer.write_int_value("membershipRuleMemberOfCount", self.membership_rule_member_of_count)
        writer.write_str_value("membershipRuleProcessingState", self.membership_rule_processing_state)
        writer.write_str_value("preferredDataLocation", self.preferred_data_location)
        writer.write_int_value("sensitivityLabelCount", self.sensitivity_label_count)
        writer.write_int_value("servicePrincipalOwnerCount", self.service_principal_owner_count)
        writer.write_datetime_value("softDeletionDateTime", self.soft_deletion_date_time)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_int_value("transitiveServicePrincipalCount", self.transitive_service_principal_count)
        writer.write_int_value("transitiveUserCount", self.transitive_user_count)
    

