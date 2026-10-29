from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .sign_in_activity import SignInActivity

from .entity import Entity

@dataclass
class ServicePrincipalSignInActivity(Entity, Parsable):
    # The globally unique appId (also called client ID on the Microsoft Entra admin center) of the credentialed resource application.
    app_id: Optional[str] = None
    # The sign-in activity of the application in a app-only authentication flow (app-to-app tokens) where the application acts like a client.
    application_authentication_client_sign_in_activity: Optional[SignInActivity] = None
    # The sign-in activity of the application in a app-only authentication flow (app-to-app tokens) where the application acts like a resource.
    application_authentication_resource_sign_in_activity: Optional[SignInActivity] = None
    # The sign-in activity of the application in a delegated flow (user sign-in) where the application acts like a client.
    delegated_client_sign_in_activity: Optional[SignInActivity] = None
    # The sign-in activity of the application in a delegated flow (user sign-in) where the application acts like a resource.
    delegated_resource_sign_in_activity: Optional[SignInActivity] = None
    # The most recent sign-in activity of the application across delegated or app-only flows where the application is used either as a client or resource.
    last_sign_in_activity: Optional[SignInActivity] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ServicePrincipalSignInActivity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ServicePrincipalSignInActivity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ServicePrincipalSignInActivity()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .sign_in_activity import SignInActivity

        from .entity import Entity
        from .sign_in_activity import SignInActivity

        fields: dict[str, Callable[[Any], None]] = {
            "appId": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "applicationAuthenticationClientSignInActivity": lambda n : setattr(self, 'application_authentication_client_sign_in_activity', n.get_object_value(SignInActivity)),
            "applicationAuthenticationResourceSignInActivity": lambda n : setattr(self, 'application_authentication_resource_sign_in_activity', n.get_object_value(SignInActivity)),
            "delegatedClientSignInActivity": lambda n : setattr(self, 'delegated_client_sign_in_activity', n.get_object_value(SignInActivity)),
            "delegatedResourceSignInActivity": lambda n : setattr(self, 'delegated_resource_sign_in_activity', n.get_object_value(SignInActivity)),
            "lastSignInActivity": lambda n : setattr(self, 'last_sign_in_activity', n.get_object_value(SignInActivity)),
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
        writer.write_str_value("appId", self.app_id)
        writer.write_object_value("applicationAuthenticationClientSignInActivity", self.application_authentication_client_sign_in_activity)
        writer.write_object_value("applicationAuthenticationResourceSignInActivity", self.application_authentication_resource_sign_in_activity)
        writer.write_object_value("delegatedClientSignInActivity", self.delegated_client_sign_in_activity)
        writer.write_object_value("delegatedResourceSignInActivity", self.delegated_resource_sign_in_activity)
        writer.write_object_value("lastSignInActivity", self.last_sign_in_activity)
    

