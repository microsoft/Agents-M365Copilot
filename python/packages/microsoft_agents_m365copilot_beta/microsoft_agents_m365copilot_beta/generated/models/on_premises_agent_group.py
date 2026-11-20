from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .on_premises_agent import OnPremisesAgent
    from .on_premises_publishing_type import OnPremisesPublishingType
    from .published_resource import PublishedResource

from .entity import Entity

@dataclass
class OnPremisesAgentGroup(Entity, Parsable):
    # List of onPremisesAgent that are assigned to an onPremisesAgentGroup. Read-only. Nullable.
    agents: Optional[list[OnPremisesAgent]] = None
    # Display name of the onPremisesAgentGroup.
    display_name: Optional[str] = None
    # Indicates if the onPremisesAgentGroup is the default agent group. Only a single agent group can be the default onPremisesAgentGroup and is set by the system.
    is_default: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # List of publishedResource that are assigned to an onPremisesAgentGroup. Read-only. Nullable.
    published_resources: Optional[list[PublishedResource]] = None
    # The publishingType property
    publishing_type: Optional[OnPremisesPublishingType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OnPremisesAgentGroup:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OnPremisesAgentGroup
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OnPremisesAgentGroup()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .on_premises_agent import OnPremisesAgent
        from .on_premises_publishing_type import OnPremisesPublishingType
        from .published_resource import PublishedResource

        from .entity import Entity
        from .on_premises_agent import OnPremisesAgent
        from .on_premises_publishing_type import OnPremisesPublishingType
        from .published_resource import PublishedResource

        fields: dict[str, Callable[[Any], None]] = {
            "agents": lambda n : setattr(self, 'agents', n.get_collection_of_object_values(OnPremisesAgent)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isDefault": lambda n : setattr(self, 'is_default', n.get_bool_value()),
            "publishedResources": lambda n : setattr(self, 'published_resources', n.get_collection_of_object_values(PublishedResource)),
            "publishingType": lambda n : setattr(self, 'publishing_type', n.get_enum_value(OnPremisesPublishingType)),
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
        writer.write_collection_of_object_values("agents", self.agents)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isDefault", self.is_default)
        writer.write_collection_of_object_values("publishedResources", self.published_resources)
        writer.write_enum_value("publishingType", self.publishing_type)
    

