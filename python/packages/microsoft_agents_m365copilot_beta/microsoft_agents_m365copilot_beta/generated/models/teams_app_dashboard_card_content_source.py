from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .teams_app_dashboard_card_bot_configuration import TeamsAppDashboardCardBotConfiguration
    from .teams_app_dashboard_card_source_type import TeamsAppDashboardCardSourceType

@dataclass
class TeamsAppDashboardCardContentSource(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The configuration for the bot source. Required if sourceType is set to bot.
    bot_configuration: Optional[TeamsAppDashboardCardBotConfiguration] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents the type of source that powers the content of the dashboard card. The possible values are: bot, unknownFutureValue.
    source_type: Optional[TeamsAppDashboardCardSourceType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamsAppDashboardCardContentSource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamsAppDashboardCardContentSource
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TeamsAppDashboardCardContentSource()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .teams_app_dashboard_card_bot_configuration import TeamsAppDashboardCardBotConfiguration
        from .teams_app_dashboard_card_source_type import TeamsAppDashboardCardSourceType

        from .teams_app_dashboard_card_bot_configuration import TeamsAppDashboardCardBotConfiguration
        from .teams_app_dashboard_card_source_type import TeamsAppDashboardCardSourceType

        fields: dict[str, Callable[[Any], None]] = {
            "botConfiguration": lambda n : setattr(self, 'bot_configuration', n.get_object_value(TeamsAppDashboardCardBotConfiguration)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sourceType": lambda n : setattr(self, 'source_type', n.get_enum_value(TeamsAppDashboardCardSourceType)),
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
        writer.write_object_value("botConfiguration", self.bot_configuration)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("sourceType", self.source_type)
        writer.write_additional_data_value(self.additional_data)
    

