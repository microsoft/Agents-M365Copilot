from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .finding import Finding
    from .permissions_creep_index_distribution import PermissionsCreepIndexDistribution

from .entity import Entity

@dataclass
class PermissionsAnalytics(Entity, Parsable):
    # The output of the permissions usage data analysis performed by Permissions Management to assess risk with identities and resources.
    findings: Optional[list[Finding]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents the Permissions Creep Index (PCI) for the authorization system. PCI distribution chart shows the classification of human and nonhuman identities based on the PCI score in three buckets (low, medium, high).
    permissions_creep_index_distributions: Optional[list[PermissionsCreepIndexDistribution]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PermissionsAnalytics:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PermissionsAnalytics
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PermissionsAnalytics()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .finding import Finding
        from .permissions_creep_index_distribution import PermissionsCreepIndexDistribution

        from .entity import Entity
        from .finding import Finding
        from .permissions_creep_index_distribution import PermissionsCreepIndexDistribution

        fields: dict[str, Callable[[Any], None]] = {
            "findings": lambda n : setattr(self, 'findings', n.get_collection_of_object_values(Finding)),
            "permissionsCreepIndexDistributions": lambda n : setattr(self, 'permissions_creep_index_distributions', n.get_collection_of_object_values(PermissionsCreepIndexDistribution)),
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
        writer.write_collection_of_object_values("findings", self.findings)
        writer.write_collection_of_object_values("permissionsCreepIndexDistributions", self.permissions_creep_index_distributions)
    

