from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .applied_authentication_event_listener import AppliedAuthenticationEventListener
    from .entity import Entity
    from .fraud_protection_details import FraudProtectionDetails
    from .sign_up_identity import SignUpIdentity
    from .sign_up_stage import SignUpStage
    from .sign_up_status import SignUpStatus

from .entity import Entity

@dataclass
class SelfServiceSignUp(Entity, Parsable):
    # App name displayed in the Microsoft Entra admin center.  Supports $filter (eq, startsWith).
    app_display_name: Optional[str] = None
    # Unique GUID that represents the app ID in the Microsoft Entra ID.  Supports $filter (eq).
    app_id: Optional[str] = None
    # Detailed information about the listeners, such as Azure Logic Apps and Azure Functions, which the corresponding events in the sign-up event triggered.
    applied_event_listeners: Optional[list[AppliedAuthenticationEventListener]] = None
    # The request ID sent from the client when the sign-up is initiated. Used to troubleshoot sign-up activity.  Supports $filter (eq).
    correlation_id: Optional[str] = None
    # Date and time (UTC) the sign-up was initiated. Example: midnight on Jan 1, 2014 is reported as 2014-01-01T00:00:00Z.  Supports $orderby, $filter (eq, le, and ge).
    created_date_time: Optional[datetime.datetime] = None
    # The fraudProtectionDetails property
    fraud_protection_details: Optional[FraudProtectionDetails] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Unique identifier for self-service sign-up user. Supports $filter (eq) on the signUpIdentifierType.
    sign_up_identity: Optional[SignUpIdentity] = None
    # Describes the type of account for which the user registered. Values include Email OTP, Email Password, Google.
    sign_up_identity_provider: Optional[str] = None
    # The signUpStage property
    sign_up_stage: Optional[SignUpStage] = None
    # Sign-up status. Includes the error code and description of the error (if a sign-up failure or interrupt occurs).  Supports $filter (eq) on errorCode property.
    status: Optional[SignUpStatus] = None
    # The identifier of the user object created during the sign-up.
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SelfServiceSignUp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SelfServiceSignUp
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SelfServiceSignUp()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .applied_authentication_event_listener import AppliedAuthenticationEventListener
        from .entity import Entity
        from .fraud_protection_details import FraudProtectionDetails
        from .sign_up_identity import SignUpIdentity
        from .sign_up_stage import SignUpStage
        from .sign_up_status import SignUpStatus

        from .applied_authentication_event_listener import AppliedAuthenticationEventListener
        from .entity import Entity
        from .fraud_protection_details import FraudProtectionDetails
        from .sign_up_identity import SignUpIdentity
        from .sign_up_stage import SignUpStage
        from .sign_up_status import SignUpStatus

        fields: dict[str, Callable[[Any], None]] = {
            "appDisplayName": lambda n : setattr(self, 'app_display_name', n.get_str_value()),
            "appId": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "appliedEventListeners": lambda n : setattr(self, 'applied_event_listeners', n.get_collection_of_object_values(AppliedAuthenticationEventListener)),
            "correlationId": lambda n : setattr(self, 'correlation_id', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "fraudProtectionDetails": lambda n : setattr(self, 'fraud_protection_details', n.get_object_value(FraudProtectionDetails)),
            "signUpIdentity": lambda n : setattr(self, 'sign_up_identity', n.get_object_value(SignUpIdentity)),
            "signUpIdentityProvider": lambda n : setattr(self, 'sign_up_identity_provider', n.get_str_value()),
            "signUpStage": lambda n : setattr(self, 'sign_up_stage', n.get_enum_value(SignUpStage)),
            "status": lambda n : setattr(self, 'status', n.get_object_value(SignUpStatus)),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
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
        writer.write_str_value("appDisplayName", self.app_display_name)
        writer.write_str_value("appId", self.app_id)
        writer.write_collection_of_object_values("appliedEventListeners", self.applied_event_listeners)
        writer.write_str_value("correlationId", self.correlation_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("fraudProtectionDetails", self.fraud_protection_details)
        writer.write_object_value("signUpIdentity", self.sign_up_identity)
        writer.write_str_value("signUpIdentityProvider", self.sign_up_identity_provider)
        writer.write_enum_value("signUpStage", self.sign_up_stage)
        writer.write_object_value("status", self.status)
        writer.write_str_value("userId", self.user_id)
    

