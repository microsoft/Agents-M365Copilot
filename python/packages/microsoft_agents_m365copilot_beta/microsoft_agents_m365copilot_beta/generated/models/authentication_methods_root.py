from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .user_events_summary import UserEventsSummary
    from .user_mfa_sign_in_summary import UserMfaSignInSummary
    from .user_password_resets_and_changes_summary import UserPasswordResetsAndChangesSummary
    from .user_registration_details import UserRegistrationDetails

from .entity import Entity

@dataclass
class AuthenticationMethodsRoot(Entity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents a specific user MFA/SSPR registration or reset event, including whether the event was successful, which authentication method was targeted, and failure reason if any.
    user_events_summary: Optional[list[UserEventsSummary]] = None
    # Represents the total count of MFA vs non-MFA sign-in counts for a specified period.
    user_mfa_sign_in_summary: Optional[list[UserMfaSignInSummary]] = None
    # Represents the summary of password resets and changes for a specific day. This includes the number of password resets that were self-service and those triggered by an administrator.
    user_password_resets_and_changes_summary: Optional[list[UserPasswordResetsAndChangesSummary]] = None
    # Represents the state of a user's authentication methods, including which methods are registered and which features the user is registered and capable of (such as multifactor authentication, self-service password reset, and passwordless authentication).
    user_registration_details: Optional[list[UserRegistrationDetails]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuthenticationMethodsRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationMethodsRoot
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AuthenticationMethodsRoot()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .user_events_summary import UserEventsSummary
        from .user_mfa_sign_in_summary import UserMfaSignInSummary
        from .user_password_resets_and_changes_summary import UserPasswordResetsAndChangesSummary
        from .user_registration_details import UserRegistrationDetails

        from .entity import Entity
        from .user_events_summary import UserEventsSummary
        from .user_mfa_sign_in_summary import UserMfaSignInSummary
        from .user_password_resets_and_changes_summary import UserPasswordResetsAndChangesSummary
        from .user_registration_details import UserRegistrationDetails

        fields: dict[str, Callable[[Any], None]] = {
            "userEventsSummary": lambda n : setattr(self, 'user_events_summary', n.get_collection_of_object_values(UserEventsSummary)),
            "userMfaSignInSummary": lambda n : setattr(self, 'user_mfa_sign_in_summary', n.get_collection_of_object_values(UserMfaSignInSummary)),
            "userPasswordResetsAndChangesSummary": lambda n : setattr(self, 'user_password_resets_and_changes_summary', n.get_collection_of_object_values(UserPasswordResetsAndChangesSummary)),
            "userRegistrationDetails": lambda n : setattr(self, 'user_registration_details', n.get_collection_of_object_values(UserRegistrationDetails)),
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
        writer.write_collection_of_object_values("userEventsSummary", self.user_events_summary)
        writer.write_collection_of_object_values("userMfaSignInSummary", self.user_mfa_sign_in_summary)
        writer.write_collection_of_object_values("userPasswordResetsAndChangesSummary", self.user_password_resets_and_changes_summary)
        writer.write_collection_of_object_values("userRegistrationDetails", self.user_registration_details)
    

