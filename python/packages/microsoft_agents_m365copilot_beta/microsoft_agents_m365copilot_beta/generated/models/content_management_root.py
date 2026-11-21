from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .security.content_management.content_management_repository import ContentManagementRepository

from .entity import Entity

@dataclass
class ContentManagementRoot(Entity, Parsable):
    """
    The contentManagement segment under `/security`. Groups the content-management resources(connected repositories) under a single node.
    """
    # The OdataType property
    odata_type: Optional[str] = None
    # Connected source-control repositories that deliver security content as code.
    repositories: Optional[list[ContentManagementRepository]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ContentManagementRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ContentManagementRoot
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ContentManagementRoot()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .security.content_management.content_management_repository import ContentManagementRepository

        from .entity import Entity
        from .security.content_management.content_management_repository import ContentManagementRepository

        fields: dict[str, Callable[[Any], None]] = {
            "repositories": lambda n : setattr(self, 'repositories', n.get_collection_of_object_values(ContentManagementRepository)),
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
        writer.write_collection_of_object_values("repositories", self.repositories)
    

