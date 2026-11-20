from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .connector import Connector
    from .connector_group import ConnectorGroup
    from .entity import Entity
    from .hybrid_agent_updater_configuration import HybridAgentUpdaterConfiguration
    from .ip_application_segment import IpApplicationSegment
    from .on_premises_agent import OnPremisesAgent
    from .on_premises_agent_group import OnPremisesAgentGroup
    from .private_access_sensor import PrivateAccessSensor
    from .published_resource import PublishedResource

from .entity import Entity

@dataclass
class OnPremisesPublishingProfile(Entity, Parsable):
    # List of existing onPremisesAgentGroup objects. Read-only. Nullable.
    agent_groups: Optional[list[OnPremisesAgentGroup]] = None
    # List of existing onPremisesAgent objects. Read-only. Nullable.
    agents: Optional[list[OnPremisesAgent]] = None
    # Represents the segment configurations that are allowed for an on-premises non-web application published through Microsoft Entra application proxy.
    application_segments: Optional[list[IpApplicationSegment]] = None
    # List of existing connectorGroup objects for applications published through Application Proxy. Read-only. Nullable.
    connector_groups: Optional[list[ConnectorGroup]] = None
    # List of existing connector objects for applications published through Application Proxy. Read-only. Nullable.
    connectors: Optional[list[Connector]] = None
    # Represents a hybridAgentUpdaterConfiguration object.
    hybrid_agent_updater_configuration: Optional[HybridAgentUpdaterConfiguration] = None
    # Specifies whether default access for app proxy is enabled or disabled.
    is_default_access_enabled: Optional[bool] = None
    # Represents if Microsoft Entra application proxy is enabled for the tenant.
    is_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # List of existing publishedResource objects. Read-only. Nullable.
    published_resources: Optional[list[PublishedResource]] = None
    # A lightweight agent installed on domain controllers that helps secure access and enforce MFA to on-premise resources.
    sensors: Optional[list[PrivateAccessSensor]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OnPremisesPublishingProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OnPremisesPublishingProfile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OnPremisesPublishingProfile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .connector import Connector
        from .connector_group import ConnectorGroup
        from .entity import Entity
        from .hybrid_agent_updater_configuration import HybridAgentUpdaterConfiguration
        from .ip_application_segment import IpApplicationSegment
        from .on_premises_agent import OnPremisesAgent
        from .on_premises_agent_group import OnPremisesAgentGroup
        from .private_access_sensor import PrivateAccessSensor
        from .published_resource import PublishedResource

        from .connector import Connector
        from .connector_group import ConnectorGroup
        from .entity import Entity
        from .hybrid_agent_updater_configuration import HybridAgentUpdaterConfiguration
        from .ip_application_segment import IpApplicationSegment
        from .on_premises_agent import OnPremisesAgent
        from .on_premises_agent_group import OnPremisesAgentGroup
        from .private_access_sensor import PrivateAccessSensor
        from .published_resource import PublishedResource

        fields: dict[str, Callable[[Any], None]] = {
            "agentGroups": lambda n : setattr(self, 'agent_groups', n.get_collection_of_object_values(OnPremisesAgentGroup)),
            "agents": lambda n : setattr(self, 'agents', n.get_collection_of_object_values(OnPremisesAgent)),
            "applicationSegments": lambda n : setattr(self, 'application_segments', n.get_collection_of_object_values(IpApplicationSegment)),
            "connectorGroups": lambda n : setattr(self, 'connector_groups', n.get_collection_of_object_values(ConnectorGroup)),
            "connectors": lambda n : setattr(self, 'connectors', n.get_collection_of_object_values(Connector)),
            "hybridAgentUpdaterConfiguration": lambda n : setattr(self, 'hybrid_agent_updater_configuration', n.get_object_value(HybridAgentUpdaterConfiguration)),
            "isDefaultAccessEnabled": lambda n : setattr(self, 'is_default_access_enabled', n.get_bool_value()),
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "publishedResources": lambda n : setattr(self, 'published_resources', n.get_collection_of_object_values(PublishedResource)),
            "sensors": lambda n : setattr(self, 'sensors', n.get_collection_of_object_values(PrivateAccessSensor)),
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
        writer.write_collection_of_object_values("agentGroups", self.agent_groups)
        writer.write_collection_of_object_values("agents", self.agents)
        writer.write_collection_of_object_values("applicationSegments", self.application_segments)
        writer.write_collection_of_object_values("connectorGroups", self.connector_groups)
        writer.write_collection_of_object_values("connectors", self.connectors)
        writer.write_object_value("hybridAgentUpdaterConfiguration", self.hybrid_agent_updater_configuration)
        writer.write_bool_value("isDefaultAccessEnabled", self.is_default_access_enabled)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_collection_of_object_values("publishedResources", self.published_resources)
        writer.write_collection_of_object_values("sensors", self.sensors)
    

