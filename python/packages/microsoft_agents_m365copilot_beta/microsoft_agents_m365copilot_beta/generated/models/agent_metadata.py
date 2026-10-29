from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class AgentMetadata(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The agentAdministrativeUnitId property
    agent_administrative_unit_id: Optional[str] = None
    # The agentBlueprintId property
    agent_blueprint_id: Optional[str] = None
    # The agentCategory property
    agent_category: Optional[str] = None
    # The agentOwner property
    agent_owner: Optional[str] = None
    # The agentPublisher property
    agent_publisher: Optional[str] = None
    # The altAgentIds property
    alt_agent_ids: Optional[list[str]] = None
    # The isEntraAgentId property
    is_entra_agent_id: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AgentMetadata:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AgentMetadata
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AgentMetadata()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "agentAdministrativeUnitId": lambda n : setattr(self, 'agent_administrative_unit_id', n.get_str_value()),
            "agentBlueprintId": lambda n : setattr(self, 'agent_blueprint_id', n.get_str_value()),
            "agentCategory": lambda n : setattr(self, 'agent_category', n.get_str_value()),
            "agentOwner": lambda n : setattr(self, 'agent_owner', n.get_str_value()),
            "agentPublisher": lambda n : setattr(self, 'agent_publisher', n.get_str_value()),
            "altAgentIds": lambda n : setattr(self, 'alt_agent_ids', n.get_collection_of_primitive_values(str)),
            "isEntraAgentId": lambda n : setattr(self, 'is_entra_agent_id', n.get_bool_value()),
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
        writer.write_str_value("agentAdministrativeUnitId", self.agent_administrative_unit_id)
        writer.write_str_value("agentBlueprintId", self.agent_blueprint_id)
        writer.write_str_value("agentCategory", self.agent_category)
        writer.write_str_value("agentOwner", self.agent_owner)
        writer.write_str_value("agentPublisher", self.agent_publisher)
        writer.write_collection_of_primitive_values("altAgentIds", self.alt_agent_ids)
        writer.write_bool_value("isEntraAgentId", self.is_entra_agent_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

