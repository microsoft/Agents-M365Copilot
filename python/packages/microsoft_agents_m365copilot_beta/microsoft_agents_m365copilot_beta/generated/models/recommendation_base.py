from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .action_step import ActionStep
    from .entity import Entity
    from .impacted_resource import ImpactedResource
    from .nist_classification import NistClassification
    from .recommendation import Recommendation
    from .recommendation_category import RecommendationCategory
    from .recommendation_category_group import RecommendationCategoryGroup
    from .recommendation_feature_areas import RecommendationFeatureAreas
    from .recommendation_priority import RecommendationPriority
    from .recommendation_status import RecommendationStatus
    from .recommendation_tag import RecommendationTag
    from .recommendation_type import RecommendationType
    from .required_licenses import RequiredLicenses

from .entity import Entity

@dataclass
class RecommendationBase(Entity, Parsable):
    # List of actions to take to complete a recommendation.
    action_steps: Optional[list[ActionStep]] = None
    # An explanation of why completing the recommendation will benefit you. Corresponds to the Value section of a recommendation shown in the Microsoft Entra admin center.
    benefits: Optional[str] = None
    # The category property
    category: Optional[RecommendationCategory] = None
    # The categoryGroup property
    category_group: Optional[RecommendationCategoryGroup] = None
    # The date and time when the recommendations service verified that the recommendation was fully remediated and set its status to completedBySystem. Is null if the recommendation wasn't completed by the system. Supports $filter.
    completed_by_system_date_time: Optional[datetime.datetime] = None
    # The date and time when the recommendation was marked as completed by the user for the current review cycle, including when the value is rolled up from all impacted resources being marked as completed by the user. Is null if the recommendation wasn't completed by a user in the current cycle. Supports $filter.
    completed_by_user_date_time: Optional[datetime.datetime] = None
    # The date and time when the recommendation was detected as applicable to your directory.
    created_date_time: Optional[datetime.datetime] = None
    # The number of points the tenant has attained. Only applies to recommendations with category set to identitySecureScore.
    current_score: Optional[float] = None
    # The title of the recommendation.
    display_name: Optional[str] = None
    # The date and time when the recommendations service most recently verified that one or more impacted resources the user marked as completed are still impacted, moving them to needsMoreAction. Is cleared when the reviewed resources are remediated, so it's mutually exclusive with remediatedDateTime. Is null when no user-reviewed resource is currently failing verification. Supports $filter.
    failed_review_date_time: Optional[datetime.datetime] = None
    # The directory feature that the recommendation is related to.
    feature_areas: Optional[list[RecommendationFeatureAreas]] = None
    # The future date and time when a recommendation should be completed.
    impact_start_date_time: Optional[datetime.datetime] = None
    # Indicates the scope of impact of a recommendation. tenantLevel indicates that the recommendation impacts the whole tenant. Other possible values include users, apps.
    impact_type: Optional[str] = None
    # The list of directory objects associated with the recommendation.
    impacted_resources: Optional[list[ImpactedResource]] = None
    # Describes why a recommendation uniquely applies to your directory. Corresponds to the Description section of a recommendation shown in the Microsoft Entra admin center.
    insights: Optional[str] = None
    # The most recent date and time a recommendation was deemed applicable to your directory.
    last_checked_date_time: Optional[datetime.datetime] = None
    # Name of the user who last updated the status of the recommendation.
    last_modified_by: Optional[str] = None
    # The date and time the status of a recommendation was last updated.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The maximum number of points attainable. Only applies to recommendations with category set to identitySecureScore.
    max_score: Optional[float] = None
    # The number of impacted resources that the user marked as completed and that the recommendations service subsequently verified are still impacted (moved to needsMoreAction). This value is greater than zero exactly when failedReviewDateTime is set. Is null when the recommendation doesn't participate in the review lifecycle.
    needs_more_action_resource_count: Optional[int] = None
    # The NIST Cybersecurity Framework (CSF) 2.0 categories that the recommendation maps to. Read-only.
    nist_classifications: Optional[list[NistClassification]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The future date and time when the status of a postponed recommendation will be active again.
    postpone_until_date_time: Optional[datetime.datetime] = None
    # The priority property
    priority: Optional[RecommendationPriority] = None
    # Friendly shortname to identify the recommendation. The possible values are: adfsAppsMigration, enableDesktopSSO, enablePHS, enableProvisioning, switchFromPerUserMFA, tenantMFA, thirdPartyApps, turnOffPerUserMFA, useAuthenticatorApp, useMyApps, staleApps, staleAppCreds, applicationCredentialExpiry, servicePrincipalKeyExpiry, adminMFAV2, blockLegacyAuthentication, integratedApps, mfaRegistrationV2, pwagePolicyNew, passwordHashSync, oneAdmin, roleOverlap, selfServicePasswordReset, signinRiskPolicy, userRiskPolicy, verifyAppPublisher, privateLinkForAAD, appRoleAssignmentsGroups, appRoleAssignmentsUsers, managedIdentity, overprivilegedApps, unknownFutureValue, longLivedCredentials, aadConnectDeprecated, adalToMsalMigration, ownerlessApps, inactiveGuests, aadGraphDeprecationApplication, aadGraphDeprecationServicePrincipal, mfaServerDeprecation. Use the Prefer: include-unknown-enum-members request header to get the following members in this evolvable enum: longLivedCredentials , aadConnectDeprecated , adalToMsalMigration , ownerlessApps , inactiveGuests , aadGraphDeprecationApplication , aadGraphDeprecationServicePrincipal , mfaServerDeprecation.
    recommendation_type: Optional[RecommendationType] = None
    # The current release type of the recommendation. The possible values are: preview, generallyAvailable, unknownFutureValue.
    release_type: Optional[str] = None
    # The date and time when the recommendations service verified that the impacted resources the user marked as completed were remediated, meaning the user-reviewed resources reached completedBySystem. Is superseded by failedReviewDateTime if a reviewed resource subsequently fails verification. Is null if the system hasn't verified a user-driven remediation in the current cycle. Supports $filter.
    remediated_date_time: Optional[datetime.datetime] = None
    # Description of the impact on users of the remediation. Only applies to recommendations with category set to identitySecureScore.
    remediation_impact: Optional[str] = None
    # The required licenses to view the recommendation. The possible values are: notApplicable, microsoftEntraIdFree, microsoftEntraIdP1, microsoftEntraIdP2, microsoftEntraIdGovernance, microsoftEntraWorkloadId, unknownFutureValue, aatp, microsoftEntraSuite. Use the Prefer: include-unknown-enum-members request header to get the following values from this evolvable enum: aatp, microsoftEntraSuite.
    required_licenses: Optional[RequiredLicenses] = None
    # The status property
    status: Optional[RecommendationStatus] = None
    # The date and time when the recommendation's status last changed, for example from active to completedByUser, dismissed, postponed, or needsMoreAction. Unlike lastModifiedDateTime, this value isn't updated when only the recommendation's insight data changes while the status stays the same. Is null until the recommendation's status changes for the first time. Supports $filter.
    status_modified_date_time: Optional[datetime.datetime] = None
    # The user-defined free-form labels applied to the recommendation. The collection isn't directly writable; tags are created and removed through the addTag and removeTag actions.
    tags: Optional[list[RecommendationTag]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RecommendationBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RecommendationBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.recommendation".casefold():
            from .recommendation import Recommendation

            return Recommendation()
        return RecommendationBase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .action_step import ActionStep
        from .entity import Entity
        from .impacted_resource import ImpactedResource
        from .nist_classification import NistClassification
        from .recommendation import Recommendation
        from .recommendation_category import RecommendationCategory
        from .recommendation_category_group import RecommendationCategoryGroup
        from .recommendation_feature_areas import RecommendationFeatureAreas
        from .recommendation_priority import RecommendationPriority
        from .recommendation_status import RecommendationStatus
        from .recommendation_tag import RecommendationTag
        from .recommendation_type import RecommendationType
        from .required_licenses import RequiredLicenses

        from .action_step import ActionStep
        from .entity import Entity
        from .impacted_resource import ImpactedResource
        from .nist_classification import NistClassification
        from .recommendation import Recommendation
        from .recommendation_category import RecommendationCategory
        from .recommendation_category_group import RecommendationCategoryGroup
        from .recommendation_feature_areas import RecommendationFeatureAreas
        from .recommendation_priority import RecommendationPriority
        from .recommendation_status import RecommendationStatus
        from .recommendation_tag import RecommendationTag
        from .recommendation_type import RecommendationType
        from .required_licenses import RequiredLicenses

        fields: dict[str, Callable[[Any], None]] = {
            "actionSteps": lambda n : setattr(self, 'action_steps', n.get_collection_of_object_values(ActionStep)),
            "benefits": lambda n : setattr(self, 'benefits', n.get_str_value()),
            "category": lambda n : setattr(self, 'category', n.get_enum_value(RecommendationCategory)),
            "categoryGroup": lambda n : setattr(self, 'category_group', n.get_enum_value(RecommendationCategoryGroup)),
            "completedBySystemDateTime": lambda n : setattr(self, 'completed_by_system_date_time', n.get_datetime_value()),
            "completedByUserDateTime": lambda n : setattr(self, 'completed_by_user_date_time', n.get_datetime_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "currentScore": lambda n : setattr(self, 'current_score', n.get_float_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "failedReviewDateTime": lambda n : setattr(self, 'failed_review_date_time', n.get_datetime_value()),
            "featureAreas": lambda n : setattr(self, 'feature_areas', n.get_collection_of_enum_values(RecommendationFeatureAreas)),
            "impactStartDateTime": lambda n : setattr(self, 'impact_start_date_time', n.get_datetime_value()),
            "impactType": lambda n : setattr(self, 'impact_type', n.get_str_value()),
            "impactedResources": lambda n : setattr(self, 'impacted_resources', n.get_collection_of_object_values(ImpactedResource)),
            "insights": lambda n : setattr(self, 'insights', n.get_str_value()),
            "lastCheckedDateTime": lambda n : setattr(self, 'last_checked_date_time', n.get_datetime_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "maxScore": lambda n : setattr(self, 'max_score', n.get_float_value()),
            "needsMoreActionResourceCount": lambda n : setattr(self, 'needs_more_action_resource_count', n.get_int_value()),
            "nistClassifications": lambda n : setattr(self, 'nist_classifications', n.get_collection_of_object_values(NistClassification)),
            "postponeUntilDateTime": lambda n : setattr(self, 'postpone_until_date_time', n.get_datetime_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_enum_value(RecommendationPriority)),
            "recommendationType": lambda n : setattr(self, 'recommendation_type', n.get_enum_value(RecommendationType)),
            "releaseType": lambda n : setattr(self, 'release_type', n.get_str_value()),
            "remediatedDateTime": lambda n : setattr(self, 'remediated_date_time', n.get_datetime_value()),
            "remediationImpact": lambda n : setattr(self, 'remediation_impact', n.get_str_value()),
            "requiredLicenses": lambda n : setattr(self, 'required_licenses', n.get_enum_value(RequiredLicenses)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(RecommendationStatus)),
            "statusModifiedDateTime": lambda n : setattr(self, 'status_modified_date_time', n.get_datetime_value()),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_object_values(RecommendationTag)),
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
        writer.write_collection_of_object_values("actionSteps", self.action_steps)
        writer.write_str_value("benefits", self.benefits)
        writer.write_enum_value("category", self.category)
        writer.write_enum_value("categoryGroup", self.category_group)
        writer.write_datetime_value("completedBySystemDateTime", self.completed_by_system_date_time)
        writer.write_datetime_value("completedByUserDateTime", self.completed_by_user_date_time)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_float_value("currentScore", self.current_score)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("failedReviewDateTime", self.failed_review_date_time)
        writer.write_collection_of_enum_values("featureAreas", self.feature_areas)
        writer.write_datetime_value("impactStartDateTime", self.impact_start_date_time)
        writer.write_str_value("impactType", self.impact_type)
        writer.write_collection_of_object_values("impactedResources", self.impacted_resources)
        writer.write_str_value("insights", self.insights)
        writer.write_datetime_value("lastCheckedDateTime", self.last_checked_date_time)
        writer.write_str_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_float_value("maxScore", self.max_score)
        writer.write_int_value("needsMoreActionResourceCount", self.needs_more_action_resource_count)
        writer.write_collection_of_object_values("nistClassifications", self.nist_classifications)
        writer.write_datetime_value("postponeUntilDateTime", self.postpone_until_date_time)
        writer.write_enum_value("priority", self.priority)
        writer.write_enum_value("recommendationType", self.recommendation_type)
        writer.write_str_value("releaseType", self.release_type)
        writer.write_datetime_value("remediatedDateTime", self.remediated_date_time)
        writer.write_str_value("remediationImpact", self.remediation_impact)
        writer.write_enum_value("requiredLicenses", self.required_licenses)
        writer.write_enum_value("status", self.status)
        writer.write_datetime_value("statusModifiedDateTime", self.status_modified_date_time)
        writer.write_collection_of_object_values("tags", self.tags)
    

