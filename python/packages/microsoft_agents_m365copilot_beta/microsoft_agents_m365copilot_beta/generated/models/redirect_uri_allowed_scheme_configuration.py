from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .app_management_policy_actor_exemptions import AppManagementPolicyActorExemptions
    from .app_management_restriction_state import AppManagementRestrictionState
    from .redirect_uri_platform_allowed_scheme_configuration import RedirectUriPlatformAllowedSchemeConfiguration

@dataclass
class RedirectUriAllowedSchemeConfiguration(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Collection of URI schemes that are allowed globally across all platforms. Schemes refer to URI schemes as defined in RFC 3986 §3.1. The value '*' can be used to allow any scheme.
    allowed_schemes: Optional[list[str]] = None
    # Applications or service principals that are exempt from this restriction.
    exclude_actors: Optional[AppManagementPolicyActorExemptions] = None
    # Indicates whether the restriction state was set by Microsoft.
    is_state_set_by_microsoft: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Platform-specific allowed scheme configuration for public client applications (native/mobile apps).
    public_client: Optional[RedirectUriPlatformAllowedSchemeConfiguration] = None
    # Date and time when this restriction starts applying to newly created applications. Applications created before this date are not affected.
    restrict_for_apps_created_after_date_time: Optional[datetime.datetime] = None
    # Platform-specific allowed scheme configuration for single-page applications (SPAs).
    spa: Optional[RedirectUriPlatformAllowedSchemeConfiguration] = None
    # The state property
    state: Optional[AppManagementRestrictionState] = None
    # Platform-specific allowed scheme configuration for web applications.
    web: Optional[RedirectUriPlatformAllowedSchemeConfiguration] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RedirectUriAllowedSchemeConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RedirectUriAllowedSchemeConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RedirectUriAllowedSchemeConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .app_management_policy_actor_exemptions import AppManagementPolicyActorExemptions
        from .app_management_restriction_state import AppManagementRestrictionState
        from .redirect_uri_platform_allowed_scheme_configuration import RedirectUriPlatformAllowedSchemeConfiguration

        from .app_management_policy_actor_exemptions import AppManagementPolicyActorExemptions
        from .app_management_restriction_state import AppManagementRestrictionState
        from .redirect_uri_platform_allowed_scheme_configuration import RedirectUriPlatformAllowedSchemeConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "allowedSchemes": lambda n : setattr(self, 'allowed_schemes', n.get_collection_of_primitive_values(str)),
            "excludeActors": lambda n : setattr(self, 'exclude_actors', n.get_object_value(AppManagementPolicyActorExemptions)),
            "isStateSetByMicrosoft": lambda n : setattr(self, 'is_state_set_by_microsoft', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "publicClient": lambda n : setattr(self, 'public_client', n.get_object_value(RedirectUriPlatformAllowedSchemeConfiguration)),
            "restrictForAppsCreatedAfterDateTime": lambda n : setattr(self, 'restrict_for_apps_created_after_date_time', n.get_datetime_value()),
            "spa": lambda n : setattr(self, 'spa', n.get_object_value(RedirectUriPlatformAllowedSchemeConfiguration)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(AppManagementRestrictionState)),
            "web": lambda n : setattr(self, 'web', n.get_object_value(RedirectUriPlatformAllowedSchemeConfiguration)),
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
        writer.write_collection_of_primitive_values("allowedSchemes", self.allowed_schemes)
        writer.write_object_value("excludeActors", self.exclude_actors)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("publicClient", self.public_client)
        writer.write_datetime_value("restrictForAppsCreatedAfterDateTime", self.restrict_for_apps_created_after_date_time)
        writer.write_object_value("spa", self.spa)
        writer.write_enum_value("state", self.state)
        writer.write_object_value("web", self.web)
        writer.write_additional_data_value(self.additional_data)
    

