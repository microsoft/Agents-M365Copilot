from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .aggregated_environment import AggregatedEnvironment
    from .audit_info import AuditInfo
    from .environment import Environment

from ..entity import Entity

@dataclass
class Zone(Entity, Parsable):
    """
    A security zone grouping cloud environments under a common posture boundary.
    """
    # Environment count summaries by type. Read-only. Supports $filter (eq) on the kind property. For example, $filter=aggregations/any(a: a/kind eq 'azureSubscription').
    aggregations: Optional[list[AggregatedEnvironment]] = None
    # Creation metadata, including user and timestamp. Supports $orderby (dateTime property only). Supports $filter (ge, le, gt, lt) on the dateTime property. For example, $filter=created/dateTime ge 2023-01-01T00:00:00Z.
    created: Optional[AuditInfo] = None
    # Optional description of the zone. Up to 255 characters. Supports $filter (eq, contains). For example, $filter=contains(description, 'production').
    description: Optional[str] = None
    # Human-readable name of the zone. Up to 1,024 characters. Supports $filter (eq, contains), and $orderby. For example, $filter=displayName eq 'Production Zone' or $orderby=displayName asc.
    display_name: Optional[str] = None
    # Collection of attached environments. Supports $expand.
    environments: Optional[list[Environment]] = None
    # Last modification metadata, including user and timestamp. Supports $orderby (dateTime property only). Supports $filter (ge, le, gt, lt) on the dateTime property. For example, $orderby=modified/dateTime desc.
    modified: Optional[AuditInfo] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Zone:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Zone
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Zone()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .aggregated_environment import AggregatedEnvironment
        from .audit_info import AuditInfo
        from .environment import Environment

        from ..entity import Entity
        from .aggregated_environment import AggregatedEnvironment
        from .audit_info import AuditInfo
        from .environment import Environment

        fields: dict[str, Callable[[Any], None]] = {
            "aggregations": lambda n : setattr(self, 'aggregations', n.get_collection_of_object_values(AggregatedEnvironment)),
            "created": lambda n : setattr(self, 'created', n.get_object_value(AuditInfo)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "environments": lambda n : setattr(self, 'environments', n.get_collection_of_object_values(Environment)),
            "modified": lambda n : setattr(self, 'modified', n.get_object_value(AuditInfo)),
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
        writer.write_collection_of_object_values("aggregations", self.aggregations)
        writer.write_object_value("created", self.created)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("environments", self.environments)
        writer.write_object_value("modified", self.modified)
    

