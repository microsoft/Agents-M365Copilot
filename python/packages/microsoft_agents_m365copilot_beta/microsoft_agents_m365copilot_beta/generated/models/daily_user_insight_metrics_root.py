from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .active_users_metric import ActiveUsersMetric
    from .authentications_metric import AuthenticationsMetric
    from .daily_inactive_users_by_application_metric import DailyInactiveUsersByApplicationMetric
    from .daily_inactive_users_metric import DailyInactiveUsersMetric
    from .entity import Entity
    from .insight_summary import InsightSummary
    from .mfa_completion_metric import MfaCompletionMetric
    from .mfa_telecom_fraud_metric import MfaTelecomFraudMetric
    from .user_count_metric import UserCountMetric
    from .user_sign_up_metric import UserSignUpMetric

from .entity import Entity

@dataclass
class DailyUserInsightMetricsRoot(Entity, Parsable):
    # Insights for active users on apps registered in the tenant for a specified period.
    active_users: Optional[list[ActiveUsersMetric]] = None
    # Insights for authentications on apps registered in the tenant for a specified period.
    authentications: Optional[list[AuthenticationsMetric]] = None
    # The inactiveUsers property
    inactive_users: Optional[list[DailyInactiveUsersMetric]] = None
    # The inactiveUsersByApplication property
    inactive_users_by_application: Optional[list[DailyInactiveUsersByApplicationMetric]] = None
    # Insights for MFA usage on apps registered in the tenant for a specified period.
    mfa_completions: Optional[list[MfaCompletionMetric]] = None
    # The mfaTelecomFraud property
    mfa_telecom_fraud: Optional[list[MfaTelecomFraudMetric]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Total sign-ups on apps registered in the tenant for a specified period.
    sign_ups: Optional[list[UserSignUpMetric]] = None
    # Summary of all usage insights on apps registered in the tenant for a specified period.
    summary: Optional[list[InsightSummary]] = None
    # Insights for total users on apps registered in the tenant for a specified period.
    user_count: Optional[list[UserCountMetric]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DailyUserInsightMetricsRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DailyUserInsightMetricsRoot
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DailyUserInsightMetricsRoot()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .active_users_metric import ActiveUsersMetric
        from .authentications_metric import AuthenticationsMetric
        from .daily_inactive_users_by_application_metric import DailyInactiveUsersByApplicationMetric
        from .daily_inactive_users_metric import DailyInactiveUsersMetric
        from .entity import Entity
        from .insight_summary import InsightSummary
        from .mfa_completion_metric import MfaCompletionMetric
        from .mfa_telecom_fraud_metric import MfaTelecomFraudMetric
        from .user_count_metric import UserCountMetric
        from .user_sign_up_metric import UserSignUpMetric

        from .active_users_metric import ActiveUsersMetric
        from .authentications_metric import AuthenticationsMetric
        from .daily_inactive_users_by_application_metric import DailyInactiveUsersByApplicationMetric
        from .daily_inactive_users_metric import DailyInactiveUsersMetric
        from .entity import Entity
        from .insight_summary import InsightSummary
        from .mfa_completion_metric import MfaCompletionMetric
        from .mfa_telecom_fraud_metric import MfaTelecomFraudMetric
        from .user_count_metric import UserCountMetric
        from .user_sign_up_metric import UserSignUpMetric

        fields: dict[str, Callable[[Any], None]] = {
            "activeUsers": lambda n : setattr(self, 'active_users', n.get_collection_of_object_values(ActiveUsersMetric)),
            "authentications": lambda n : setattr(self, 'authentications', n.get_collection_of_object_values(AuthenticationsMetric)),
            "inactiveUsers": lambda n : setattr(self, 'inactive_users', n.get_collection_of_object_values(DailyInactiveUsersMetric)),
            "inactiveUsersByApplication": lambda n : setattr(self, 'inactive_users_by_application', n.get_collection_of_object_values(DailyInactiveUsersByApplicationMetric)),
            "mfaCompletions": lambda n : setattr(self, 'mfa_completions', n.get_collection_of_object_values(MfaCompletionMetric)),
            "mfaTelecomFraud": lambda n : setattr(self, 'mfa_telecom_fraud', n.get_collection_of_object_values(MfaTelecomFraudMetric)),
            "signUps": lambda n : setattr(self, 'sign_ups', n.get_collection_of_object_values(UserSignUpMetric)),
            "summary": lambda n : setattr(self, 'summary', n.get_collection_of_object_values(InsightSummary)),
            "userCount": lambda n : setattr(self, 'user_count', n.get_collection_of_object_values(UserCountMetric)),
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
        writer.write_collection_of_object_values("activeUsers", self.active_users)
        writer.write_collection_of_object_values("authentications", self.authentications)
        writer.write_collection_of_object_values("inactiveUsers", self.inactive_users)
        writer.write_collection_of_object_values("inactiveUsersByApplication", self.inactive_users_by_application)
        writer.write_collection_of_object_values("mfaCompletions", self.mfa_completions)
        writer.write_collection_of_object_values("mfaTelecomFraud", self.mfa_telecom_fraud)
        writer.write_collection_of_object_values("signUps", self.sign_ups)
        writer.write_collection_of_object_values("summary", self.summary)
        writer.write_collection_of_object_values("userCount", self.user_count)
    

