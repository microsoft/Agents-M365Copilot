from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .registration_auth_method import RegistrationAuthMethod

from .entity import Entity

@dataclass
class CredentialUserRegistrationDetails(Entity, Parsable):
    # Represents the authentication method that the user has registered. The possible values are: email, mobilePhone, officePhone,  securityQuestion (only used for self-service password reset), appNotification,  appCode, alternateMobilePhone (supported only in registration),  fido,  appPassword,  unknownFutureValue.
    auth_methods: Optional[list[RegistrationAuthMethod]] = None
    # Indicates whether the user is ready to perform self-service password reset or MFA.
    is_capable: Optional[bool] = None
    # Indicates whether the user enabled to perform self-service password reset.
    is_enabled: Optional[bool] = None
    # Indicates whether the user is registered for MFA.
    is_mfa_registered: Optional[bool] = None
    # Indicates whether the user has registered any authentication methods for self-service password reset.
    is_registered: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Provides the user name of the corresponding user.
    user_display_name: Optional[str] = None
    # Provides the user principal name of the corresponding user.
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CredentialUserRegistrationDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CredentialUserRegistrationDetails
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CredentialUserRegistrationDetails()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .registration_auth_method import RegistrationAuthMethod

        from .entity import Entity
        from .registration_auth_method import RegistrationAuthMethod

        fields: dict[str, Callable[[Any], None]] = {
            "authMethods": lambda n : setattr(self, 'auth_methods', n.get_collection_of_enum_values(RegistrationAuthMethod)),
            "isCapable": lambda n : setattr(self, 'is_capable', n.get_bool_value()),
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "isMfaRegistered": lambda n : setattr(self, 'is_mfa_registered', n.get_bool_value()),
            "isRegistered": lambda n : setattr(self, 'is_registered', n.get_bool_value()),
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
        writer.write_collection_of_enum_values("authMethods", self.auth_methods)
        writer.write_bool_value("isCapable", self.is_capable)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_bool_value("isMfaRegistered", self.is_mfa_registered)
        writer.write_bool_value("isRegistered", self.is_registered)
        writer.write_str_value("userDisplayName", self.user_display_name)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    

