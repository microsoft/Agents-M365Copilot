from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .agent_blueprint_api_based_endpoint_configuration_details import AgentBlueprintApiBasedEndpointConfigurationDetails
    from .agent_blueprint_bot_based_endpoint_configuration_details import AgentBlueprintBotBasedEndpointConfigurationDetails
    from .agent_endpoint_configuration_type import AgentEndpointConfigurationType

@dataclass
class AgentEndpointConfiguration(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The API-based endpoint details. Populated when configurationType is apiBased; carries the callback URI that Teams posts to. Must be null when configurationType is botBased.
    api_based: Optional[AgentBlueprintApiBasedEndpointConfigurationDetails] = None
    # The bot-based endpoint details. Populated when configurationType is botBased; carries the bot ID that Teams messages. Must be null when configurationType is apiBased.
    bot_based: Optional[AgentBlueprintBotBasedEndpointConfigurationDetails] = None
    # The configurationType property
    configuration_type: Optional[AgentEndpointConfigurationType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AgentEndpointConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AgentEndpointConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AgentEndpointConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .agent_blueprint_api_based_endpoint_configuration_details import AgentBlueprintApiBasedEndpointConfigurationDetails
        from .agent_blueprint_bot_based_endpoint_configuration_details import AgentBlueprintBotBasedEndpointConfigurationDetails
        from .agent_endpoint_configuration_type import AgentEndpointConfigurationType

        from .agent_blueprint_api_based_endpoint_configuration_details import AgentBlueprintApiBasedEndpointConfigurationDetails
        from .agent_blueprint_bot_based_endpoint_configuration_details import AgentBlueprintBotBasedEndpointConfigurationDetails
        from .agent_endpoint_configuration_type import AgentEndpointConfigurationType

        fields: dict[str, Callable[[Any], None]] = {
            "apiBased": lambda n : setattr(self, 'api_based', n.get_object_value(AgentBlueprintApiBasedEndpointConfigurationDetails)),
            "botBased": lambda n : setattr(self, 'bot_based', n.get_object_value(AgentBlueprintBotBasedEndpointConfigurationDetails)),
            "configurationType": lambda n : setattr(self, 'configuration_type', n.get_enum_value(AgentEndpointConfigurationType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_object_value("apiBased", self.api_based)
        writer.write_object_value("botBased", self.bot_based)
        writer.write_enum_value("configurationType", self.configuration_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

