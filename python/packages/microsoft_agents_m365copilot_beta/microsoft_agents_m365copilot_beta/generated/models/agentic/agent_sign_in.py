from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .agent_type import AgentType

@dataclass
class AgentSignIn(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The subject's parent object ID. This is either the id of the agentIdentity or agentIdentityBlueprint.
    agent_subject_parent_id: Optional[str] = None
    # The agentSubjectType property
    agent_subject_type: Optional[AgentType] = None
    # The agentType property
    agent_type: Optional[AgentType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The appId of the parent agent where the agentType is agentic.
    parent_app_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AgentSignIn:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AgentSignIn
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AgentSignIn()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .agent_type import AgentType

        from .agent_type import AgentType

        fields: dict[str, Callable[[Any], None]] = {
            "agentSubjectParentId": lambda n : setattr(self, 'agent_subject_parent_id', n.get_str_value()),
            "agentSubjectType": lambda n : setattr(self, 'agent_subject_type', n.get_enum_value(AgentType)),
            "agentType": lambda n : setattr(self, 'agent_type', n.get_enum_value(AgentType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "parentAppId": lambda n : setattr(self, 'parent_app_id', n.get_str_value()),
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
        writer.write_str_value("agentSubjectParentId", self.agent_subject_parent_id)
        writer.write_enum_value("agentSubjectType", self.agent_subject_type)
        writer.write_enum_value("agentType", self.agent_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("parentAppId", self.parent_app_id)
        writer.write_additional_data_value(self.additional_data)
    

