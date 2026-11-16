from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .applicable_content import ApplicableContent
    from .updatable_asset import UpdatableAsset

from ..entity import Entity

@dataclass
class DeploymentAudience(Entity, Parsable):
    # Content eligible to deploy to devices in the audience. Not nullable. Read-only.
    applicable_content: Optional[list[ApplicableContent]] = None
    # Specifies the assets to exclude from the audience.
    exclusions: Optional[list[UpdatableAsset]] = None
    # Specifies the assets to include in the audience.
    members: Optional[list[UpdatableAsset]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeploymentAudience:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeploymentAudience
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeploymentAudience()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .applicable_content import ApplicableContent
        from .updatable_asset import UpdatableAsset

        from ..entity import Entity
        from .applicable_content import ApplicableContent
        from .updatable_asset import UpdatableAsset

        fields: dict[str, Callable[[Any], None]] = {
            "applicableContent": lambda n : setattr(self, 'applicable_content', n.get_collection_of_object_values(ApplicableContent)),
            "exclusions": lambda n : setattr(self, 'exclusions', n.get_collection_of_object_values(UpdatableAsset)),
            "members": lambda n : setattr(self, 'members', n.get_collection_of_object_values(UpdatableAsset)),
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
        writer.write_collection_of_object_values("applicableContent", self.applicable_content)
        writer.write_collection_of_object_values("exclusions", self.exclusions)
        writer.write_collection_of_object_values("members", self.members)
    

