from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .implicit_grant_settings import ImplicitGrantSettings
    from .redirect_uri_settings import RedirectUriSettings

@dataclass
class WebApplication(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Home page or landing page of the application.
    home_page_url: Optional[str] = None
    # Specifies whether this web application can request tokens using the OAuth 2.0 implicit flow.
    implicit_grant_settings: Optional[ImplicitGrantSettings] = None
    # Specifies the URL that will be used by Microsoft's authorization service to logout a user using front-channel, back-channel or SAML logout protocols.
    logout_url: Optional[str] = None
    # The oauth2AllowImplicitFlow property
    oauth2_allow_implicit_flow: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Specifies the index of the URLs where user tokens are sent for sign-in. This is only valid for applications using SAML.
    redirect_uri_settings: Optional[list[RedirectUriSettings]] = None
    # Specifies the URLs where user tokens are sent for sign-in, or the redirect URIs where OAuth 2.0 authorization codes and access tokens are sent.
    redirect_uris: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WebApplication:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WebApplication
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WebApplication()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .implicit_grant_settings import ImplicitGrantSettings
        from .redirect_uri_settings import RedirectUriSettings

        from .implicit_grant_settings import ImplicitGrantSettings
        from .redirect_uri_settings import RedirectUriSettings

        fields: dict[str, Callable[[Any], None]] = {
            "homePageUrl": lambda n : setattr(self, 'home_page_url', n.get_str_value()),
            "implicitGrantSettings": lambda n : setattr(self, 'implicit_grant_settings', n.get_object_value(ImplicitGrantSettings)),
            "logoutUrl": lambda n : setattr(self, 'logout_url', n.get_str_value()),
            "oauth2AllowImplicitFlow": lambda n : setattr(self, 'oauth2_allow_implicit_flow', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "redirectUriSettings": lambda n : setattr(self, 'redirect_uri_settings', n.get_collection_of_object_values(RedirectUriSettings)),
            "redirectUris": lambda n : setattr(self, 'redirect_uris', n.get_collection_of_primitive_values(str)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("homePageUrl", self.home_page_url)
        writer.write_object_value("implicitGrantSettings", self.implicit_grant_settings)
        writer.write_str_value("logoutUrl", self.logout_url)
        writer.write_bool_value("oauth2AllowImplicitFlow", self.oauth2_allow_implicit_flow)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("redirectUriSettings", self.redirect_uri_settings)
        writer.write_collection_of_primitive_values("redirectUris", self.redirect_uris)
        writer.write_additional_data_value(self.additional_data)
    

