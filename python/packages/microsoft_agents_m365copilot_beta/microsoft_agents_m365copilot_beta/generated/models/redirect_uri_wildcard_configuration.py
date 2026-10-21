from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .app_management_policy_actor_exemptions import AppManagementPolicyActorExemptions
    from .app_management_restriction_state import AppManagementRestrictionState
    from .redirect_uri_wildcard_exclude_formats import RedirectUriWildcardExcludeFormats

@dataclass
class RedirectUriWildcardConfiguration(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Applications or service principals that are exempt from this restriction.
    exclude_actors: Optional[AppManagementPolicyActorExemptions] = None
    # Configuration that specifies exceptions to the wildcard restriction, such as allowing wildcards for specific trusted domains.
    exclude_formats: Optional[RedirectUriWildcardExcludeFormats] = None
    # Indicates whether the restriction state was set by Microsoft.
    is_state_set_by_microsoft: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Date and time when this restriction starts applying to newly created applications. Applications created before this date are not affected.
    restrict_for_apps_created_after_date_time: Optional[datetime.datetime] = None
    # The state property
    state: Optional[AppManagementRestrictionState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RedirectUriWildcardConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RedirectUriWildcardConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RedirectUriWildcardConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .app_management_policy_actor_exemptions import AppManagementPolicyActorExemptions
        from .app_management_restriction_state import AppManagementRestrictionState
        from .redirect_uri_wildcard_exclude_formats import RedirectUriWildcardExcludeFormats

        from .app_management_policy_actor_exemptions import AppManagementPolicyActorExemptions
        from .app_management_restriction_state import AppManagementRestrictionState
        from .redirect_uri_wildcard_exclude_formats import RedirectUriWildcardExcludeFormats

        fields: dict[str, Callable[[Any], None]] = {
            "excludeActors": lambda n : setattr(self, 'exclude_actors', n.get_object_value(AppManagementPolicyActorExemptions)),
            "excludeFormats": lambda n : setattr(self, 'exclude_formats', n.get_object_value(RedirectUriWildcardExcludeFormats)),
            "isStateSetByMicrosoft": lambda n : setattr(self, 'is_state_set_by_microsoft', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "restrictForAppsCreatedAfterDateTime": lambda n : setattr(self, 'restrict_for_apps_created_after_date_time', n.get_datetime_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(AppManagementRestrictionState)),
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
        writer.write_object_value("excludeActors", self.exclude_actors)
        writer.write_object_value("excludeFormats", self.exclude_formats)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_datetime_value("restrictForAppsCreatedAfterDateTime", self.restrict_for_apps_created_after_date_time)
        writer.write_enum_value("state", self.state)
        writer.write_additional_data_value(self.additional_data)
    

