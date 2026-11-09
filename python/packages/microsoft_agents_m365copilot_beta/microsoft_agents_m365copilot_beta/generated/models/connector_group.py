from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .application import Application
    from .connector import Connector
    from .connector_group_region import ConnectorGroupRegion
    from .connector_group_type import ConnectorGroupType
    from .entity import Entity

from .entity import Entity

@dataclass
class ConnectorGroup(Entity, Parsable):
    # The applications property
    applications: Optional[list[Application]] = None
    # The connectorGroupType property
    connector_group_type: Optional[ConnectorGroupType] = None
    # Indicates if the connectorGroup is the default connectorGroup. Only a single connector group can be the default connectorGroup and this is pre-set by the system. Read-only.
    is_default: Optional[bool] = None
    # The members property
    members: Optional[list[Connector]] = None
    # The name associated with the connectorGroup.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The region the connectorGroup is assigned to and will optimize traffic for. This region can only be set if no connectors or applications are assigned to the connectorGroup. The possible values are: nam (for North America), eur (for Europe), aus (for Australia), asia (for Asia), ind (for India), and unknownFutureValue.
    region: Optional[ConnectorGroupRegion] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ConnectorGroup:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConnectorGroup
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ConnectorGroup()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .application import Application
        from .connector import Connector
        from .connector_group_region import ConnectorGroupRegion
        from .connector_group_type import ConnectorGroupType
        from .entity import Entity

        from .application import Application
        from .connector import Connector
        from .connector_group_region import ConnectorGroupRegion
        from .connector_group_type import ConnectorGroupType
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "applications": lambda n : setattr(self, 'applications', n.get_collection_of_object_values(Application)),
            "connectorGroupType": lambda n : setattr(self, 'connector_group_type', n.get_enum_value(ConnectorGroupType)),
            "isDefault": lambda n : setattr(self, 'is_default', n.get_bool_value()),
            "members": lambda n : setattr(self, 'members', n.get_collection_of_object_values(Connector)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "region": lambda n : setattr(self, 'region', n.get_enum_value(ConnectorGroupRegion)),
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
        writer.write_collection_of_object_values("applications", self.applications)
        writer.write_enum_value("connectorGroupType", self.connector_group_type)
        writer.write_bool_value("isDefault", self.is_default)
        writer.write_collection_of_object_values("members", self.members)
        writer.write_str_value("name", self.name)
        writer.write_enum_value("region", self.region)
    

