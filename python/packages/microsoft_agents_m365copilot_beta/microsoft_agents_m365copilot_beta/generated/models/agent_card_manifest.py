from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .agent_capabilities import AgentCapabilities
    from .agent_provider import AgentProvider
    from .agent_skill import AgentSkill
    from .entity import Entity
    from .security_requirement import SecurityRequirement
    from .security_schemes import SecuritySchemes

from .entity import Entity

@dataclass
class AgentCardManifest(Entity, Parsable):
    # The capabilities property
    capabilities: Optional[AgentCapabilities] = None
    # Object ID of the user or application that created the agent card manifest. Read-only.
    created_by: Optional[str] = None
    # When this agent card manifest was created.
    created_date_time: Optional[datetime.datetime] = None
    # Default set of supported input MIME types for all skills, which can be overridden on a per-skill basis.
    default_input_modes: Optional[list[str]] = None
    # Default set of supported output MIME types for all skills, which can be overridden on a per-skill basis.
    default_output_modes: Optional[list[str]] = None
    # A human-readable description of the agent.
    description: Optional[str] = None
    # A human-readable display name of the agent.
    display_name: Optional[str] = None
    # URL to agent's documentation.
    documentation_url: Optional[str] = None
    # URL to agent's icon image.
    icon_url: Optional[str] = None
    # When this agent card manifest was last modified.
    last_modified_date_time: Optional[datetime.datetime] = None
    # appId (referred to as Application (client) ID on the Microsoft Entra admin center) of the application managing this agent manifest.
    managed_by: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Name of the store/system where agent originated. For example Copilot Studio.
    originating_store: Optional[str] = None
    # List of object IDs for the owners of the agent card manifest.
    owner_ids: Optional[list[str]] = None
    # Protocol version supported by the agent.
    protocol_version: Optional[str] = None
    # Information about the organization providing the agent.
    provider: Optional[AgentProvider] = None
    # Security requirements - array of security scheme references.
    security: Optional[list[SecurityRequirement]] = None
    # Dictionary of security scheme definitions keyed by scheme name.
    security_schemes: Optional[SecuritySchemes] = None
    # Skills/capabilities that the agent can perform
    skills: Optional[list[AgentSkill]] = None
    # Whether agent supports authenticated extended card retrieval
    supports_authenticated_extended_card: Optional[bool] = None
    # Version of the agent implementation
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AgentCardManifest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AgentCardManifest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AgentCardManifest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .agent_capabilities import AgentCapabilities
        from .agent_provider import AgentProvider
        from .agent_skill import AgentSkill
        from .entity import Entity
        from .security_requirement import SecurityRequirement
        from .security_schemes import SecuritySchemes

        from .agent_capabilities import AgentCapabilities
        from .agent_provider import AgentProvider
        from .agent_skill import AgentSkill
        from .entity import Entity
        from .security_requirement import SecurityRequirement
        from .security_schemes import SecuritySchemes

        fields: dict[str, Callable[[Any], None]] = {
            "capabilities": lambda n : setattr(self, 'capabilities', n.get_object_value(AgentCapabilities)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "defaultInputModes": lambda n : setattr(self, 'default_input_modes', n.get_collection_of_primitive_values(str)),
            "defaultOutputModes": lambda n : setattr(self, 'default_output_modes', n.get_collection_of_primitive_values(str)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "documentationUrl": lambda n : setattr(self, 'documentation_url', n.get_str_value()),
            "iconUrl": lambda n : setattr(self, 'icon_url', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "managedBy": lambda n : setattr(self, 'managed_by', n.get_str_value()),
            "originatingStore": lambda n : setattr(self, 'originating_store', n.get_str_value()),
            "ownerIds": lambda n : setattr(self, 'owner_ids', n.get_collection_of_primitive_values(str)),
            "protocolVersion": lambda n : setattr(self, 'protocol_version', n.get_str_value()),
            "provider": lambda n : setattr(self, 'provider', n.get_object_value(AgentProvider)),
            "security": lambda n : setattr(self, 'security', n.get_collection_of_object_values(SecurityRequirement)),
            "securitySchemes": lambda n : setattr(self, 'security_schemes', n.get_object_value(SecuritySchemes)),
            "skills": lambda n : setattr(self, 'skills', n.get_collection_of_object_values(AgentSkill)),
            "supportsAuthenticatedExtendedCard": lambda n : setattr(self, 'supports_authenticated_extended_card', n.get_bool_value()),
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
        writer.write_object_value("capabilities", self.capabilities)
        writer.write_str_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_collection_of_primitive_values("defaultInputModes", self.default_input_modes)
        writer.write_collection_of_primitive_values("defaultOutputModes", self.default_output_modes)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("documentationUrl", self.documentation_url)
        writer.write_str_value("iconUrl", self.icon_url)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("managedBy", self.managed_by)
        writer.write_str_value("originatingStore", self.originating_store)
        writer.write_collection_of_primitive_values("ownerIds", self.owner_ids)
        writer.write_str_value("protocolVersion", self.protocol_version)
        writer.write_object_value("provider", self.provider)
        writer.write_collection_of_object_values("security", self.security)
        writer.write_object_value("securitySchemes", self.security_schemes)
        writer.write_collection_of_object_values("skills", self.skills)
        writer.write_bool_value("supportsAuthenticatedExtendedCard", self.supports_authenticated_extended_card)
        writer.write_str_value("version", self.version)
    

