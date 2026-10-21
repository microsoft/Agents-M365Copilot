from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .feature_type import FeatureType
    from .usage_auth_method import UsageAuthMethod

from .entity import Entity

@dataclass
class UserCredentialUsageDetails(Entity, Parsable):
    # The authMethod property
    auth_method: Optional[UsageAuthMethod] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    event_date_time: Optional[datetime.datetime] = None
    # Provides the failure reason for the corresponding reset or registration workflow.
    failure_reason: Optional[str] = None
    # The feature property
    feature: Optional[FeatureType] = None
    # Indicates success or failure of the workflow.
    is_success: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # User name of the user performing the reset or registration workflow.
    user_display_name: Optional[str] = None
    # User principal name of the user performing the reset or registration workflow.
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserCredentialUsageDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserCredentialUsageDetails
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserCredentialUsageDetails()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .feature_type import FeatureType
        from .usage_auth_method import UsageAuthMethod

        from .entity import Entity
        from .feature_type import FeatureType
        from .usage_auth_method import UsageAuthMethod

        fields: dict[str, Callable[[Any], None]] = {
            "authMethod": lambda n : setattr(self, 'auth_method', n.get_enum_value(UsageAuthMethod)),
            "eventDateTime": lambda n : setattr(self, 'event_date_time', n.get_datetime_value()),
            "failureReason": lambda n : setattr(self, 'failure_reason', n.get_str_value()),
            "feature": lambda n : setattr(self, 'feature', n.get_enum_value(FeatureType)),
            "isSuccess": lambda n : setattr(self, 'is_success', n.get_bool_value()),
            "userDisplayName": lambda n : setattr(self, 'user_display_name', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
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
        writer.write_enum_value("authMethod", self.auth_method)
        writer.write_datetime_value("eventDateTime", self.event_date_time)
        writer.write_str_value("failureReason", self.failure_reason)
        writer.write_enum_value("feature", self.feature)
        writer.write_bool_value("isSuccess", self.is_success)
        writer.write_str_value("userDisplayName", self.user_display_name)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    

