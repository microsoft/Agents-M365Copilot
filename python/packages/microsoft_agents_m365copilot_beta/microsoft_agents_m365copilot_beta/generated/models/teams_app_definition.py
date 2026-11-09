from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .identity_set import IdentitySet
    from .teams_app_authorization import TeamsAppAuthorization
    from .teams_app_dashboard_card_definition import TeamsAppDashboardCardDefinition
    from .teams_app_icon import TeamsAppIcon
    from .teams_app_installation_scopes import TeamsAppInstallationScopes
    from .teams_app_publishing_state import TeamsAppPublishingState
    from .teamwork_bot import TeamworkBot

from .entity import Entity

@dataclass
class TeamsAppDefinition(Entity, Parsable):
    # A collection of scopes where the Teams app can be installed. The possible values are:team—Indicates that the Teams app can be installed within a team and is authorized to access that team's data. groupChat—Indicates that the Teams app can be installed within a group chat and is authorized to access that group chat's data. personal—Indicates that the Teams app can be installed in the personal scope of a user and is authorized to access that user's data.
    allowed_installation_scopes: Optional[TeamsAppInstallationScopes] = None
    # Authorization requirements specified in the Teams app manifest.
    authorization: Optional[TeamsAppAuthorization] = None
    # The WebApplicationInfo.Id from the Teams app manifest.
    azure_a_d_app_id: Optional[str] = None
    # The details of the bot specified in the Teams app manifest.
    bot: Optional[TeamworkBot] = None
    # The color version of the Teams app's icon.
    color_icon: Optional[TeamsAppIcon] = None
    # The createdBy property
    created_by: Optional[IdentitySet] = None
    # Dashboard cards specified in the Teams app manifest.
    dashboard_cards: Optional[list[TeamsAppDashboardCardDefinition]] = None
    # The description property
    description: Optional[str] = None
    # The name of the app provided by the app developer.
    display_name: Optional[str] = None
    # The lastModifiedDateTime property
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The outline version of the Teams app's icon.
    outline_icon: Optional[TeamsAppIcon] = None
    # The published status of a specific version of a Teams app. The possible values are:submitted—The specific version of the Teams app has been submitted and is under review. published - The request to publish the specific version of the Teams app has been approved by the admin and the app is published. rejected - The request to publish the specific version of the Teams app was rejected by the admin.
    publishing_state: Optional[TeamsAppPublishingState] = None
    # The shortdescription property
    shortdescription: Optional[str] = None
    # The ID from the Teams app manifest.
    teams_app_id: Optional[str] = None
    # The version number of the application.
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamsAppDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamsAppDefinition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TeamsAppDefinition()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .identity_set import IdentitySet
        from .teams_app_authorization import TeamsAppAuthorization
        from .teams_app_dashboard_card_definition import TeamsAppDashboardCardDefinition
        from .teams_app_icon import TeamsAppIcon
        from .teams_app_installation_scopes import TeamsAppInstallationScopes
        from .teams_app_publishing_state import TeamsAppPublishingState
        from .teamwork_bot import TeamworkBot

        from .entity import Entity
        from .identity_set import IdentitySet
        from .teams_app_authorization import TeamsAppAuthorization
        from .teams_app_dashboard_card_definition import TeamsAppDashboardCardDefinition
        from .teams_app_icon import TeamsAppIcon
        from .teams_app_installation_scopes import TeamsAppInstallationScopes
        from .teams_app_publishing_state import TeamsAppPublishingState
        from .teamwork_bot import TeamworkBot

        fields: dict[str, Callable[[Any], None]] = {
            "allowedInstallationScopes": lambda n : setattr(self, 'allowed_installation_scopes', n.get_collection_of_enum_values(TeamsAppInstallationScopes)),
            "authorization": lambda n : setattr(self, 'authorization', n.get_object_value(TeamsAppAuthorization)),
            "azureADAppId": lambda n : setattr(self, 'azure_a_d_app_id', n.get_str_value()),
            "bot": lambda n : setattr(self, 'bot', n.get_object_value(TeamworkBot)),
            "colorIcon": lambda n : setattr(self, 'color_icon', n.get_object_value(TeamsAppIcon)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "dashboardCards": lambda n : setattr(self, 'dashboard_cards', n.get_collection_of_object_values(TeamsAppDashboardCardDefinition)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "outlineIcon": lambda n : setattr(self, 'outline_icon', n.get_object_value(TeamsAppIcon)),
            "publishingState": lambda n : setattr(self, 'publishing_state', n.get_enum_value(TeamsAppPublishingState)),
            "shortdescription": lambda n : setattr(self, 'shortdescription', n.get_str_value()),
            "teamsAppId": lambda n : setattr(self, 'teams_app_id', n.get_str_value()),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
        writer.write_enum_value("allowedInstallationScopes", self.allowed_installation_scopes)
        writer.write_object_value("authorization", self.authorization)
        writer.write_str_value("azureADAppId", self.azure_a_d_app_id)
        writer.write_object_value("bot", self.bot)
        writer.write_object_value("colorIcon", self.color_icon)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_collection_of_object_values("dashboardCards", self.dashboard_cards)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_object_value("outlineIcon", self.outline_icon)
        writer.write_enum_value("publishingState", self.publishing_state)
        writer.write_str_value("shortdescription", self.shortdescription)
        writer.write_str_value("teamsAppId", self.teams_app_id)
        writer.write_str_value("version", self.version)
    

